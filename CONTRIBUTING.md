# Contributing to mind-models

## How to Add a Model

1. Find an existing model file to use as a reference
2. Copy the [template](templates/model-template.md)
3. Fill in all required fields (see [CODEX](CODEX.md) for field definitions)
4. Place the file in the correct category folder
5. Add cross-references to related models
6. Run `python scripts/validate_models.py`
7. Open a PR

## Rules

- One model per file
- All required fields must be present
- File name must be `kebab-case.md`
- Minimum 2 real-world examples
- Origin must be traceable (researcher + year)
- Related models must link to files that exist in this repo
- Category must match the folder the file lives in

## What Makes a Good Model

- Backed by research (not just pop-psychology)
- Distinct from existing models (check before adding)
- Concrete - abstract theories without behavioral predictions do not qualify
- Useful - someone should be able to apply or counter it

## PR Template

```
## Model Name
**Category:**
**Why it belongs here:**
**Sources:**
```

## Questions?

Open a GitHub Discussion.
