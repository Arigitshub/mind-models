# AGENTS.md — mind-models integration contract

Use this file when connecting **mind-models** to ChatGPT, Claude, Gemini, a coding agent, a retrieval pipeline, or another AI system.

## What this repository is

mind-models is a structured reference library for psychological models, cognitive frameworks, and behavioral patterns.

Treat it as a **portable reasoning vocabulary**: a way for an AI system to name relevant models, retrieve mechanisms and examples, connect related models, and point back to sources.

It is not a diagnostic engine, personality classifier, or substitute for clinical judgment.

## Canonical data surfaces

| Need | Use |
|---|---|
| Read one model deeply | `models/<category>/<model>.md` |
| Load complete structured records | `models.json` |
| Retrieval / embeddings / RAG | `model-chunks.jsonl` |
| Lightweight browser search | `search-index.json` |
| Spreadsheet / notebook ingestion | `exports/*.csv` |
| Human browsing | `library.md`, category pages, GitHub Pages |

Generated model records use a stable non-empty `id`, canonical `name`, `category`, `origin`, `tags`, `summary`, source `path`, related-model links, and section content.

## Retrieval protocol

When a user asks about a situation, decision, behavior, or pattern:

1. Describe the situation before labeling it.
2. Retrieve candidate models from `summary`, `tags`, `category`, and chunk text.
3. Prefer **2–4 relevant models** over dumping a long list.
4. Explain why each model fits and what evidence in the user's description supports that fit.
5. Follow `related` links when models interact or compete.
6. Separate **observation**, **model interpretation**, and **uncertainty**.
7. When factual rigor matters, point back to the model `path` and its `References` section.

Do not present a model match as proof that a person has a diagnosis, trait, motive, or disorder.

## Minimal system prompt

```text
Use the mind-models library as a structured reasoning reference.

When analyzing a situation:
- retrieve only the most relevant models;
- distinguish observed facts from interpretation;
- explain why each model fits;
- note competing explanations and uncertainty;
- follow related-model links when useful;
- cite the source model path and use its References section for provenance;
- never turn a model match into a mental-health diagnosis or a claim about hidden motives.

Prefer a small convergent set of models over a long list.
```

## Example tool flow

```text
query -> retrieve top chunks from model-chunks.jsonl
      -> group chunks by model_id
      -> load full records from models.json
      -> compare mechanisms / triggers / counters
      -> answer with source paths + uncertainty
```

## Maintainer rules

- `models/*.md` are the human-authored source of truth.
- Generated artifacts must be rebuilt after model edits.
- Every generated model `id` must be non-empty and unique.
- The validation workflow must stay green.
- References are required provenance. They are **not yet** a standardized evidence-strength score.
- New integrations should depend on the public schema/exports, not on private maintainer systems.
