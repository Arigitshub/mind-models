---
title: mind-models
---

<section class="hero">
  <p class="eyebrow">Open Standard</p>
  <h1>mind-models</h1>
  <p class="hero-copy">A structured library of psychological models designed to be readable by humans, parseable by tools, and reliable enough to build on. Use it as a research reference, a teaching surface, a product thinking toolkit, or a machine-readable foundation for agents and search.</p>
  <div class="hero-actions">
    <a class="button button-primary" href="{{ '/library' | relative_url }}">Browse Library</a>
    <a class="button button-secondary" href="{{ '/search' | relative_url }}">Search Models</a>
    <a class="button button-secondary" href="{{ '/models.json' | relative_url }}">Download models.json</a>
  </div>
  <div class="hero-trust">
    <span>Human-readable markdown</span>
    <span>Generated JSON artifacts</span>
    <span>Category landing pages</span>
    <span>Validation workflow</span>
  </div>
</section>

<section class="stats-grid">
  <article class="stat-card">
    <p class="stat-value">40</p>
    <p class="stat-label">Total Models</p>
  </article>
  <article class="stat-card">
    <p class="stat-value">6</p>
    <p class="stat-label">Categories</p>
  </article>
  <article class="stat-card">
    <p class="stat-value">5</p>
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
    <h3><a href="{{ '/model-chunks.json' | relative_url }}">Chunk Export</a></h3>
    <p>Use chunk-level records when you need embeddings-ready text units instead of whole-model documents.</p>
  </article>
  <article class="surface-card">
    <h3><a href="{{ '/spec/schema.md' | relative_url }}">Schema</a></h3>
    <p>See the markdown contract that every model file follows across the repository.</p>
  </article>
  <article class="surface-card">
    <h3><a href="{{ '/categories/cognitive' | relative_url }}">Category Pages</a></h3>
    <p>Browse each category as its own landing page with focused summaries and direct links.</p>
  </article>
  <article class="surface-card">
    <h3><a href="{{ '/exports/models.csv' | relative_url }}">Tabular Exports</a></h3>
    <p>Pull the library into spreadsheets, notebooks, or bulk ingestion flows using generated CSV outputs.</p>
  </article>
</div>

## Explore by Category

<div class="category-grid">
  <article class="category-card">
    <p class="category-kicker">Cognitive</p>
    <h3><a href="{{ '/categories/cognitive' | relative_url }}">Biases, heuristics, and metacognition</a></h3>
    <p>Anchoring, confirmation bias, availability, dissonance, halo effects, and other models that shape perception and reasoning.</p>
  </article>
  <article class="category-card">
    <p class="category-kicker">Behavioral</p>
    <h3><a href="{{ '/categories/behavioral' | relative_url }}">Habits, rewards, and motivation loops</a></h3>
    <p>Conditioning, motivation, self-perception, and repeatable behavior change frameworks that show up in learning and product design.</p>
  </article>
  <article class="category-card">
    <p class="category-kicker">Decision</p>
    <h3><a href="{{ '/categories/decision' | relative_url }}">Judgment under uncertainty</a></h3>
    <p>Loss aversion, framing, recency, status quo bias, and the shortcuts people use when making choices with incomplete information.</p>
  </article>
  <article class="category-card">
    <p class="category-kicker">Social</p>
    <h3><a href="{{ '/categories/social' | relative_url }}">Influence, conformity, and group dynamics</a></h3>
    <p>Authority, social proof, reciprocity, groupthink, in-group bias, and the forces that spread beliefs and behaviors through groups.</p>
  </article>
  <article class="category-card">
    <p class="category-kicker">Emotional</p>
    <h3><a href="{{ '/categories/emotional' | relative_url }}">Affect, identity, and emotional adaptation</a></h3>
    <p>Imposter syndrome, hedonic adaptation, emotional contagion, attribution, and other models that shape felt experience.</p>
  </article>
  <article class="category-card">
    <p class="category-kicker">Developmental</p>
    <h3><a href="{{ '/categories/developmental' | relative_url }}">Learning and growth across stages</a></h3>
    <p>Attachment theory, growth mindset, theory of mind, social learning, and stage-based models of development and skill acquisition.</p>
  </article>
</div>

## Coverage

<p class="lede">The library now spans cognitive biases, conditioning loops, social influence, affective dynamics, decision frameworks, and developmental models. It is intentionally broad enough to support research, teaching, product work, and agent-oriented reasoning.</p>

## What You Can Do With It

<div class="card-grid">
  <article class="surface-card">
    <h3>Teach faster</h3>
    <p>Use compact model pages as lecture prompts, handouts, reading lists, or discussion starters for psychology, design, and decision-making courses.</p>
  </article>
  <article class="surface-card">
    <h3>Design better systems</h3>
    <p>Map product decisions against motivation, social influence, habit formation, and bias to spot likely user failure modes earlier.</p>
  </article>
  <article class="surface-card">
    <h3>Power search and agents</h3>
    <p>Use the normalized exports, chunk files, and search index to support retrieval, embeddings, tagging, and structured downstream workflows.</p>
  </article>
</div>

## Maintenance

```bash
python scripts/sync_front_matter.py
python scripts/validate_models.py
python scripts/build_index.py
python scripts/export_tabular.py
```

The GitHub Actions workflow validates model structure and confirms generated artifacts are committed.
