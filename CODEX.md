# CODEX — mind-models Standard

> The rules, definitions, and philosophy behind the mind-models open standard.

---

## 1. Purpose

mind-models exists to create a **shared, structured language** for psychological models. Not academic papers. Not pop-psychology listicles. A precise, consistent, extensible format.

---

## 2. Core Principles

| Principle | Meaning |
|-----------|---------|
| **Structured** | Every model follows the same schema — no exceptions |
| **Evidence-grounded** | Models trace to a named origin (researcher, theory, experiment) |
| **Neutral** | Models describe, not prescribe — no moral judgements |
| **Interconnected** | Models reference each other — the mind is not modular |
| **Minimal** | Each file is one model, one concept, done thoroughly |

---

## 3. Model Categories

### cognitive
How the mind processes, stores, and interprets information. Includes shortcuts, biases, and perception patterns.

### behavioral
How behavior is formed, reinforced, and changed. Includes conditioning, habits, and motivation systems.

### social
How people influence and are influenced by others. Includes conformity, authority, trust, and group dynamics.

### emotional
How emotions arise, are regulated, and affect behavior. Includes affect theory and mood models.

### decision
How choices are made under uncertainty or complexity. Includes heuristics, frameworks, and biases.

### developmental
How the mind changes over time. Includes learning models, identity formation, and growth stages.

---

## 4. Field Definitions

| Field | Required | Description |
|-------|----------|-------------|
| `name` | ✅ | Full name of the model |
| `category` | ✅ | One of the 6 categories |
| `origin` | ✅ | Researcher/theorist + year |
| `tags` | ✅ | 3–6 lowercase keywords |
| `summary` | ✅ | One sentence — what is this model |
| `mechanism` | ✅ | How it works — steps or stages |
| `triggers` | ✅ | What activates this model |
| `examples` | ✅ | 2–3 concrete real-world examples |
| `effects` | ✅ | What outcomes does this model produce |
| `counters` | ⬜ | How to reduce or override this model |
| `related` | ⬜ | Links to other models in this repo |
| `references` | ⬜ | Academic or primary sources |

---

## 5. Naming Conventions

- File names: `kebab-case.md` (e.g., `cognitive-dissonance.md`)
- Model names: Title Case (e.g., `Cognitive Dissonance`)
- Tags: all lowercase, no spaces (e.g., `belief`, `conflict`)

---

## 6. Version History

| Version | What changed |
|---------|-------------|
| v0.1 | Initial schema + 6 cognitive models |
| v0.2 | Behavioral + social categories |
| v0.3 | Emotional + decision + developmental |
| v1.0 | Full 30+ model library, spec complete |
