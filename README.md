# P2Enjoy Software Factory Base

Reusable engineering baseline for P2Enjoy software projects.

This repository is not an application starter and does not impose a product architecture. It provides the global engineering rules, documentation contracts, UI conventions, scheduled worker workflow, executable Git safeguards, bounded subagent roles and multi stack repository defaults used to bootstrap a reproducible software project.

The factory is built around a strict separation:

1. **Global rules** are reusable across projects and must remain independent of any product.
2. **Project rules** live in companion files inside the target repository and contain the local architecture, terminology, commands, constraints, evidence and exceptions.

## Repository contents

```text
.
├── .codex/
│   ├── agents/
│   │   ├── factory-explorer.toml
│   │   ├── factory-reviewer.toml
│   │   └── factory-verifier.toml
│   └── config.toml
├── .githooks/
│   ├── commit-msg
│   ├── pre-commit
│   └── pre-push
├── .gitignore
├── AGENTS.md
├── CHANGELOG.md
├── CLAUDE.md
├── LICENSE
├── README.md
├── docs/
│   ├── .routine
│   ├── AUTOMATION.md
│   ├── CloudWorker.md
│   ├── DESIGN_SYSTEM.md
│   └── JOURNAL.md
├── scripts/git-hooks/
│   ├── check-message
│   ├── check-push
│   ├── check-session
│   ├── check-staged
│   ├── install
│   └── lib.sh
└── tests/git-hooks/
    └── test-hooks
```

This base intentionally contains policy and orchestration documentation plus small portable enforcement scripts rather than application source code.

## Core files

### `CLAUDE.md`

Global engineering contract for AI assisted development sessions.

It defines reusable rules for:

- repository analysis before modification;
- single-writer ownership and bounded subagent delegation;
- architecture and maintainability;
- documentation and specification traceability;
- Git discipline;
- testing and E2E validation;
- visual verification;
- security and production safeguards;
- deterministic development data;
- deployment documentation;
- observability and performance;
- Definition of Done.

`CLAUDE.md` must remain project agnostic.

Any instruction that requires knowledge of the current repository belongs in the local companion:

```text
CLAUDE_PROJECT.md
```

### `AGENTS.md` and `.codex/agents/`

`AGENTS.md` is the compact Codex adapter for the global method. It tells the primary agent to read the normative contracts and defines when the project-scoped custom agents are useful.

The three custom agents have deliberately narrow roles:

- `factory_explorer` maps contracts, dependencies and execution paths in read-only mode;
- `factory_reviewer` reviews a stabilized change in read-only mode;
- `factory_verifier` executes one documented, targeted proof and may write only its expected temporary artifacts.

The primary agent remains the sole source editor, decision maker and operator of Git mutations. Subagents may inspect Git in read-only mode. They are optional and never become a completion dependency.

### `docs/AUTOMATION.md`, `.githooks/` and `scripts/git-hooks/`

`docs/AUTOMATION.md` is the contract for deterministic safeguards. The hooks are thin adapters over versioned scripts so the same checks can be reused by humans, scheduled workers and CI.

Hooks are not activated automatically by Git. Enable the standard policy explicitly:

```bash
scripts/git-hooks/install
```

The scheduled worker uses:

```bash
scripts/git-hooks/install --worker
```

Worker mode additionally restricts branch and push operations to `origin/main`. Neither mode changes Git identity or performs automatic stash, rebase, commit or push operations.

### `docs/DESIGN_SYSTEM.md`

Global P2Enjoy UI and UX reference.

It defines reusable conventions for design tokens, typography, spacing, components, navigation, responsive behavior, accessibility, forms, tables, interaction states, focus management and visual verification.

It must never contain product names, business entities, local screen structures, ticket identifiers, project measurements, local evidence or application specific exceptions.

Projects with an interface create the companion:

```text
docs/DESIGN_SYSTEM_APP.md
```

That file contains the UI decisions that only make sense for the current product.

### `docs/CloudWorker.md`

Execution contract for a scheduled worker operating on an ephemeral checkout.

It defines the lifecycle of a work session, including:

- Git recovery and synchronization;
- continuous persistence through commits and pushes;
- environment initialization;
- project stack startup and seed application;
- selection of one coherent backlog unit;
- specification before implementation;
- targeted proofs during development;
- end of session verification;
- documentation and backlog synchronization;
- final Git state checks.

The worker method is global. Application commands are not.

Exact commands for installation, startup, seed, tests and build must come from the target project's `README.md`, build files or scripts.

### `docs/.routine`

Small scheduled task entrypoint.

It directs the worker to load `docs/CloudWorker.md` and `CLAUDE.md` before starting project work. This keeps the scheduled prompt small while the full contract remains version controlled.

### `.gitignore`

Generic ignore baseline for common generated artifacts from:

- Python;
- C and C++;
- Node.js;
- Deno;
- CMake, Ninja and Meson;
- test and coverage tooling;
- local environments and secrets;
- editors, operating systems and runtime temporary files.

Important source configuration and lockfiles remain versionable.

## Global versus project specific files

| Global reference | Local companion | Responsibility |
| --- | --- | --- |
| `CLAUDE.md` | `CLAUDE_PROJECT.md` | Global engineering rules versus repository specific instructions |
| `docs/DESIGN_SYSTEM.md` | `docs/DESIGN_SYSTEM_APP.md` | Shared UI system versus product specific UI decisions |
| `docs/CloudWorker.md` | `README.md`, build files, scripts | Scheduled worker cycle versus executable project commands |
| `docs/AUTOMATION.md` | project hooks and CI commands | Generic deterministic safeguards versus stack-specific checks |

A rule belongs in a global file only when it can be understood and reused without knowing the current product.

Project specific information includes, for example:

- product or service names;
- business terminology;
- repository specific commands and paths;
- service names and deployment topology;
- screen or route structures;
- seed data and demonstration accounts;
- backlog or ticket identifiers;
- environment specific constraints;
- measured values and local evidence;
- justified exceptions to a global rule.

## Starting a project

Use this repository as the baseline for a new project, then add the specification and execution layer for the actual product.

```bash
git clone https://github.com/P2Enjoy/software-factory-base.git my-project
cd my-project
git config --local user.name "<maintainer name>"
git config --local user.email "<maintainer email>"
scripts/git-hooks/install
```

The project should then establish its own operational documentation.

A typical structure is:

```text
README.md
CHANGELOG.md
CLAUDE_PROJECT.md                 # when local agent rules exist

docs/
├── DAT.md                        # technical architecture
├── BACKLOG.md                    # executable work units and status
├── JOURNAL.md                    # investigations and decisions
├── DESIGN_SYSTEM.md              # global P2Enjoy UI reference, when UI exists
├── DESIGN_SYSTEM_APP.md          # local UI extension, when UI exists
└── manual.md or manuals/         # when user documentation is required
```

Additional documents such as `docs/SCHEMA.md`, deployment procedures or inconsistency reports are added when the project requires them.

## Project README contract

The downstream `README.md` is operational documentation.

It should document at least:

- project purpose;
- actual technology stack;
- prerequisites;
- installation and bootstrap;
- development startup;
- deterministic seed or fixture procedure;
- test commands;
- build command;
- shutdown and reset procedures;
- environment variables;
- important repository structure;
- known limitations.

Humans, CI and scheduled workers should use documented commands rather than infer them from conventions.

## Documentation driven workflow

Documentation is part of the implementation contract.

A validated decision is persisted before implementation. When the implementation changes reality, the corresponding documentation changes in the same work unit.

```text
specification
    ↓
backlog unit
    ↓
implementation
    ↓
tests and verification
    ↓
user and operational documentation
```

Implementation should remain traceable to the specification and backlog unit that justify it. Tests should identify the contract they verify rather than only the source file they execute.

## Development workflow

Work is organized into small, coherent and verifiable units.

```text
understand
    ↓
specify
    ↓
persist specification (commit and push)
    ↓
implement
    ↓
run deterministic local guards
    ↓
persist a coherent checkpoint
    ↓
run targeted proofs and verify real behavior
    ↓
correct and persist as needed
    ↓
run the final campaign
    ↓
update documentation and backlog
    ↓
final commit, push and session guard
```

For scheduled ephemeral workers, `docs/CloudWorker.md` adds repository recovery, environment bootstrap, end of session verification and mandatory persistence through Git.

The hooks and their tests require Bash, Git and the usual Unix tools (`grep`,
`sed`, `mktemp`, `cp`). No package installation is needed. The harness creates
and removes its own temporary repositories; test pushes stay on the local
filesystem.

Run the portable safeguard harness with:

```bash
tests/git-hooks/test-hooks
```

## Verification model

A task is not complete merely because code was generated or a build succeeded.

Depending on the project, verification may include:

- unit tests;
- database tests;
- API and integration tests;
- E2E tests;
- type checking;
- production builds;
- authorization checks that bypass the UI;
- deterministic seed validation;
- visual inspection of the running interface;
- responsive and accessibility checks;
- deployment validation.

For UI work, automated tests do not replace observation of the real application through its canonical user journey.

## Technology scope

This base does not force one application stack.

Its generic conventions support projects using combinations of:

- Python;
- C;
- C++;
- Node.js;
- Deno;
- React and Vite when appropriate;
- containerized local environments when appropriate.

The target project remains authoritative for actual language versions, package managers, databases, services and build tools.

## What does not belong in this repository

The global base should not accumulate product implementation details.

Do not add application source code, domain models, project routes, screen structures, seed data, demonstration users, local environment variables, deployment topology, backlog items or application specific design exceptions merely because one project needs them.

Before promoting a new rule into the base, use this test:

> Can this rule be understood, applied and reused without knowing which product caused us to discover it?

If not, keep it in the project companion documentation.

If a project reveals a genuinely reusable principle, extract the abstract principle, remove all product context and only then promote it to the global base.

## License

This repository is distributed under the Mozilla Public License 2.0. See [`LICENSE`](LICENSE) for the complete terms.
