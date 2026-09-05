#!/usr/bin/env bash
# @spec docs/AUTOMATION.md#local-guards

readonly FACTORY_WORKER_BRANCH="main"
readonly FACTORY_WORKER_REMOTE="origin"

FACTORY_GIT_NAME=""
FACTORY_GIT_EMAIL=""
FACTORY_GIT_IDENTITY=""

factory_error() {
  printf 'ERREUR: %s\n' "$*" >&2
}

factory_die() {
  factory_error "$*"
  exit 1
}

factory_repo_root() {
  git rev-parse --show-toplevel 2>/dev/null ||
    factory_die "cette commande doit être exécutée dans un dépôt Git"
}

factory_hooks_mode() {
  git config --local --get factory.hooks.mode 2>/dev/null || printf 'standard\n'
}

factory_is_worker_mode() {
  [[ "$(factory_hooks_mode)" == "worker" ]]
}

factory_check_local_identity() {
  FACTORY_GIT_NAME="$(git config --local --get user.name 2>/dev/null || true)"
  FACTORY_GIT_EMAIL="$(git config --local --get user.email 2>/dev/null || true)"

  [[ -n "$FACTORY_GIT_NAME" ]] ||
    factory_die "user.name local est absent ; pose l'identité du responsable avec : git config --local user.name \"<nom>\""
  [[ -n "$FACTORY_GIT_EMAIL" ]] ||
    factory_die "user.email local est absent ; pose l'identité du responsable avec : git config --local user.email \"<adresse>\""

  FACTORY_GIT_IDENTITY="$FACTORY_GIT_NAME <$FACTORY_GIT_EMAIL>"
}

factory_check_effective_identity() {
  local variable label identity expected_prefix

  factory_check_local_identity
  expected_prefix="$FACTORY_GIT_IDENTITY "

  for variable in GIT_AUTHOR_IDENT GIT_COMMITTER_IDENT; do
    case "$variable" in
      GIT_AUTHOR_IDENT) label="auteur" ;;
      GIT_COMMITTER_IDENT) label="committer" ;;
    esac
    identity="$(git var "$variable" 2>/dev/null || true)"
    [[ "$identity" == "$expected_prefix"* ]] ||
      factory_die "l'identité effective de l'$label est '${identity:-<absente>}' ; valeur attendue : '$FACTORY_GIT_IDENTITY' ; une variable d'environnement ou --author surcharge peut-être la configuration locale"
  done
}

factory_require_worker_branch() {
  local branch
  branch="$(git symbolic-ref --quiet --short HEAD 2>/dev/null || true)"
  [[ "$branch" == "$FACTORY_WORKER_BRANCH" ]] ||
    factory_die "le mode worker exige HEAD attaché à '$FACTORY_WORKER_BRANCH' ; état courant : '${branch:-HEAD détaché}'"
}

factory_forbidden_message_match() {
  local input_file="$1"

  LC_ALL=C grep -Ein -m 1 \
    '^[[:space:]]*co-authored-by[[:space:]]*:|generated[[:space:]-]+(with|by)[[:space:]-]+(claude|codex|chatgpt|openai|copilot|gemini|an?[[:space:]]+ai)|ai[[:space:]-]+generated[[:space:]]+(commit|change|code)|claude\.ai/code' \
    "$input_file" 2>/dev/null || true
}

factory_check_message_file() {
  local input_file="$1" context="${2:-message de commit}" match

  [[ -r "$input_file" ]] || factory_die "message de commit illisible : $input_file"
  match="$(factory_forbidden_message_match "$input_file")"
  [[ -z "$match" ]] ||
    factory_die "$context contient une attribution ou signature interdite : $match"
}

factory_check_message_text() {
  local message="$1" context="${2:-message de commit}" match

  match="$(printf '%s\n' "$message" | LC_ALL=C grep -Ein -m 1 \
    '^[[:space:]]*co-authored-by[[:space:]]*:|generated[[:space:]-]+(with|by)[[:space:]-]+(claude|codex|chatgpt|openai|copilot|gemini|an?[[:space:]]+ai)|ai[[:space:]-]+generated[[:space:]]+(commit|change|code)|claude\.ai/code' || true)"
  [[ -z "$match" ]] ||
    factory_die "$context contient une attribution ou signature interdite : $match"
}

factory_check_commit() {
  local commit="$1" short author committer message

  factory_check_local_identity
  short="$(git rev-parse --short "$commit")"
  author="$(git show -s --format='%an <%ae>' "$commit")"
  committer="$(git show -s --format='%cn <%ce>' "$commit")"

  [[ "$author" == "$FACTORY_GIT_IDENTITY" ]] ||
    factory_die "le commit $short a pour auteur '$author' ; valeur attendue : '$FACTORY_GIT_IDENTITY'"
  [[ "$committer" == "$FACTORY_GIT_IDENTITY" ]] ||
    factory_die "le commit $short a pour committer '$committer' ; valeur attendue : '$FACTORY_GIT_IDENTITY'"

  message="$(git show -s --format='%B' "$commit")"
  factory_check_message_text "$message" "le commit $short"
}

factory_is_code_path() {
  local path="$1" basename extension
  basename="${path##*/}"
  extension="${basename##*.}"

  case "$path" in
    .githooks/*) return 0 ;;
    scripts/*|tests/*)
      [[ "$basename" == *.* ]] || return 0
      ;;
  esac

  case "$basename" in
    Makefile|GNUmakefile|Dockerfile|Dockerfile.*) return 0 ;;
  esac

  case "$extension" in
    bash|c|cc|cjs|cpp|css|cs|cxx|go|h|hpp|html|java|js|jsx|kt|kts|less|lua|mjs|php|py|rb|rs|sass|scala|scss|sh|sql|svelte|swift|toml|ts|tsx|vue|yaml|yml|zsh)
      return 0
      ;;
  esac

  return 1
}

factory_is_test_path() {
  local path="$1" basename
  basename="${path##*/}"

  case "/$path/" in
    */test/*|*/tests/*|*/__tests__/*) return 0 ;;
  esac

  case "$basename" in
    test_*|*_test.*|*.test.*|*.spec.*|verify-*) return 0 ;;
  esac

  return 1
}

factory_is_forbidden_env_path() {
  local basename="${1##*/}"

  case "$basename" in
    .env.example|.env.sample|.env.template) return 1 ;;
    .env|.env.*) return 0 ;;
  esac

  return 1
}

factory_added_line_contains_secret() {
  local line="$1"

  [[ "$line" =~ -----BEGIN[[:space:]]+(RSA[[:space:]]+|EC[[:space:]]+|DSA[[:space:]]+|OPENSSH[[:space:]]+)?PRIVATE[[:space:]]+KEY----- ]] ||
    [[ "$line" =~ (^|[^A-Z0-9])AKIA[0-9A-Z]{16}([^A-Z0-9]|$) ]] ||
    [[ "$line" =~ (^|[^[:alnum:]_])gh[pousr]_[[:alnum:]]{32,}([^[:alnum:]_]|$) ]] ||
    [[ "$line" =~ (^|[^[:alnum:]_-])xox[baprs]-[[:alnum:]-]{20,}([^[:alnum:]-]|$) ]]
}
