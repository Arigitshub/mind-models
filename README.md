# mind-models

> An open standard for documenting psychological models, cognitive frameworks, and behavioral patterns in a structured, machine-readable, human-friendly format.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Models](https://img.shields.io/badge/models-34-blue)](models/)
[![GitHub Pages](https://img.shields.io/badge/docs-live-green)](https://arigitshub.github.io/mind-models/)
[![Validation](https://img.shields.io/github/actions/workflow/status/Arigitshub/mind-models/validate-models.yml?branch=master&label=validation)](https://github.com/Arigitshub/mind-models/actions/workflows/validate-models.yml)

---

## What is mind-models?

A growing library of psychological models written in structured Markdown. Each model is a self-contained file describing:

- What the model is and where it comes from
- How it works (triggers, mechanisms, stages)
- Real-world examples
- How it connects to other models
- How to apply or counter it

Think of it as an RFC for the human mind: a reference spec anyone can use, extend, or implement.

---

## Categories

| Category | Description | Models |
|----------|-------------|--------|
| [cognitive](models/cognitive/) | Mental shortcuts, perception, memory, reasoning | 7 |
| [behavioral](models/behavioral/) | Habits, conditioning, reward systems, motivation | 4 |
| [social](models/social/) | Influence, conformity, group dynamics, trust | 5 |
| [emotional](models/emotional/) | Emotion regulation, affect, mood patterns | 5 |
| [decision](models/decision/) | Decision-making frameworks, heuristics, biases | 7 |
| [developmental](models/developmental/) | Growth stages, learning models, identity | 6 |

---

## Quick Example

```markdown
# Cognitive Dissonance

**Category:** cognitive
**Origin:** Leon Festinger, 1957
**Tags:** belief, conflict, rationalization
```

See [full model](models/cognitive/cognitive-dissonance.md).

---

## Schema

Every model follows the [model schema](spec/schema.md). This makes models consistent, parseable, and interoperable.

## Validation

Run the local validator before opening a pull request:

```bash
python scripts/validate_models.py
```

The same command runs in GitHub Actions on every push and pull request.

To refresh the generated library page and JSON search index after adding or editing models:

```bash
python scripts/build_index.py
```

Generated outputs:

- `library.md` - navigable library page for GitHub Pages
- `search-index.json` - lightweight search document used by the browser UI
- `models.json` - normalized full export with sections and related links

Published docs:

- [Home](index.md)
- [Library](library.md)
- [Search](search.md)
- [Search Index](search-index.json)
- [Models Export](models.json)

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

MIT - free to use, extend, and build on.
