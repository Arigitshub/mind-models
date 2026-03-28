# mind-models

> An open standard for documenting psychological models, cognitive frameworks, and behavioral patterns — in a structured, machine-readable, human-friendly format.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Models](https://img.shields.io/badge/models-30%2B-blue)](models/)
[![GitHub Pages](https://img.shields.io/badge/docs-live-green)](https://arigitshub.github.io/mind-models/)

---

## What is mind-models?

A growing library of psychological models written in structured Markdown. Each model is a self-contained file describing:

- What the model is and where it comes from
- How it works (triggers, mechanisms, stages)
- Real-world examples
- How it connects to other models
- How to apply or counter it

Think of it as an **RFC for the human mind** — a reference spec anyone can use, extend, or implement.

---

## Categories

| Category | Description | Models |
|----------|-------------|--------|
| [cognitive](models/cognitive/) | Mental shortcuts, perception, memory, reasoning | 8 |
| [behavioral](models/behavioral/) | Habits, conditioning, reward systems, motivation | 6 |
| [social](models/social/) | Influence, conformity, group dynamics, trust | 6 |
| [emotional](models/emotional/) | Emotion regulation, affect, mood patterns | 4 |
| [decision](models/decision/) | Decision-making frameworks, heuristics, biases | 6 |
| [developmental](models/developmental/) | Growth stages, learning models, identity | 4 |

---

## Quick Example

```markdown
# Cognitive Dissonance

**Category:** cognitive
**Origin:** Leon Festinger, 1957
**Tags:** belief, conflict, rationalization
```

→ See [full model](models/cognitive/cognitive-dissonance.md)

---

## Schema

Every model follows the [model schema](spec/schema.md). This makes models consistent, parseable, and interoperable.

---

## Use Cases

- Build AI agents that understand human psychology
- Train models on behavioral patterns
- Design better UX, products, or teams
- Study and teach psychology systematically
- Extend with your own models via PR

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). All models must follow the [schema](spec/schema.md).

---

## Roadmap

See [ROADMAP.md](ROADMAP.md).

---

## License

MIT — free to use, extend, and build on.
