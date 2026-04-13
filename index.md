---
title: mind-models
---

# mind-models

An open standard for documenting psychological models, cognitive frameworks, and behavioral patterns in a structured, machine-readable, human-friendly format.

## Start Here

- [Model Library]({{ '/library' | relative_url }})
- [Search]({{ '/search' | relative_url }})
- [Schema]({{ '/spec/schema.md' | relative_url }})
- [Contributing]({{ '/CONTRIBUTING.md' | relative_url }})
- [GitHub Repository](https://github.com/Arigitshub/mind-models)

## What This Repo Contains

- Structured markdown model files under `models/`
- A validation script for keeping the standard consistent
- A generated library page and JSON search index for GitHub Pages

## Category Coverage

- Cognitive: biases, reasoning, perception, and self-monitoring
- Behavioral: habits, conditioning, reinforcement, and action loops
- Social: influence, conformity, authority, and group effects
- Emotional: affect, self-evaluation, and reward learning
- Decision: framing, loss, risk, and forecasting
- Developmental: learning stages, identity formation, and growth over time

## Maintenance

```bash
python scripts/validate_models.py
python scripts/build_index.py
```

The GitHub Actions workflow checks both validation and generated artifacts on every push and pull request.
