---
title: mind-models
---

<section class="hero">
  <p class="eyebrow">Open Standard</p>
  <h1>mind-models</h1>
  <p class="hero-copy">A structured library of psychological models designed to be readable by humans, parseable by tools, and reliable enough to build on.</p>
  <div class="hero-actions">
    <a class="button button-primary" href="{{ '/library' | relative_url }}">Browse Library</a>
    <a class="button button-secondary" href="{{ '/search' | relative_url }}">Search Models</a>
    <a class="button button-secondary" href="{{ '/models.json' | relative_url }}">Download models.json</a>
  </div>
</section>

<section class="stats-grid">
  <article class="stat-card">
    <p class="stat-value">34</p>
    <p class="stat-label">Total Models</p>
  </article>
  <article class="stat-card">
    <p class="stat-value">6</p>
    <p class="stat-label">Categories</p>
  </article>
  <article class="stat-card">
    <p class="stat-value">3</p>
    <p class="stat-label">Generated Artifacts</p>
  </article>
  <article class="stat-card">
    <p class="stat-value">1</p>
    <p class="stat-label">Validation Workflow</p>
  </article>
</section>

## Start Here

<div class="card-grid">
  <article class="surface-card">
    <h3><a href="{{ '/library' | relative_url }}">Library</a></h3>
    <p>Browse the full categorized catalog with summaries, origins, tags, and related-model links.</p>
  </article>
  <article class="surface-card">
    <h3><a href="{{ '/search' | relative_url }}">Search</a></h3>
    <p>Filter the library quickly by model name, tags, category, or core concept using the generated index.</p>
  </article>
  <article class="surface-card">
    <h3><a href="{{ '/models.json' | relative_url }}">models.json</a></h3>
    <p>Use the normalized export for agents, scripts, embeddings, indexing, or downstream tooling.</p>
  </article>
  <article class="surface-card">
    <h3><a href="{{ '/spec/schema.md' | relative_url }}">Schema</a></h3>
    <p>See the markdown contract that every model file follows across the repository.</p>
  </article>
</div>

## Coverage

<p class="lede">The library now spans cognitive biases, conditioning loops, social influence, affective dynamics, decision frameworks, and developmental models. It is intentionally broad enough to support research, teaching, product work, and agent-oriented reasoning.</p>

## Maintenance

```bash
python scripts/validate_models.py
python scripts/build_index.py
```

The GitHub Actions workflow validates model structure and confirms generated artifacts are committed.
