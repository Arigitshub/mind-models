# Model Schema

Every model in mind-models follows this exact structure.

---

## Template

```markdown
# [Model Name]

**Category:** [cognitive | behavioral | social | emotional | decision | developmental]
**Origin:** [Researcher/Theorist, Year]
**Tags:** [tag1, tag2, tag3]

---

## Summary

One sentence: what this model describes and why it matters.

---

## Mechanism

How the model works - steps, stages, or loop.

1. Step one
2. Step two
3. Step three

---

## Triggers

What conditions activate this model:

- Trigger A
- Trigger B
- Trigger C

---

## Effects

What this model produces:

- Effect A
- Effect B

---

## Examples

**Example 1 - [Context]:**
Description of example.

**Example 2 - [Context]:**
Description of example.

**Example 3 - [Context]:**
Description of example.

---

## Counters

*(Optional)* How to reduce, override, or work with this model:

- Counter A
- Counter B

---

## Related Models

- [Model Name](../category/model-name.md) - why related
- [Model Name](../category/model-name.md) - why related

---

## References

- Author, A. (Year). *Title*. Publisher.
- Author, B. (Year). *Title*. Journal, Volume(Issue), Pages.
```

---

## Validation Rules

1. All required fields must be present
2. Category must be one of the 6 defined categories
3. Category must match the folder the file lives in
4. Tags: minimum 3, maximum 6, all lowercase kebab-case keywords
5. Examples: minimum 2
6. File name must be kebab-case
7. Related model links must point to existing files
8. Run `python scripts/validate_models.py` before opening a PR
