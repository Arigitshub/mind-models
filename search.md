---
title: Search
---

# Search

Search the published model library using the generated JSON index.

<input id="search-box" type="search" placeholder="Search by model, tag, category, or concept" style="width: 100%; max-width: 48rem; padding: 0.75rem 1rem; font-size: 1rem; border: 1px solid #c7d2da; border-radius: 0.5rem; margin: 1rem 0;" />

<p id="search-status">Loading search index...</p>
<div id="search-results"></div>

<script>
const input = document.getElementById("search-box");
const status = document.getElementById("search-status");
const results = document.getElementById("search-results");
const baseUrl = "{{ '/' | relative_url }}";

function scoreEntry(entry, query) {
  const haystack = [
    entry.name,
    entry.category,
    entry.origin,
    entry.summary,
    ...(entry.tags || []),
  ].join(" ").toLowerCase();

  if (!query) return 0;
  if (entry.name.toLowerCase() === query) return 100;
  if (entry.name.toLowerCase().includes(query)) return 80;
  if ((entry.tags || []).some(tag => tag.toLowerCase() === query)) return 70;
  if (haystack.includes(query)) return 50;
  return 0;
}

function render(entries, query) {
  results.innerHTML = "";

  if (!query) {
    status.textContent = `Loaded ${entries.length} models. Start typing to filter them.`;
    return;
  }

  const ranked = entries
    .map(entry => ({ entry, score: scoreEntry(entry, query) }))
    .filter(item => item.score > 0)
    .sort((a, b) => b.score - a.score || a.entry.name.localeCompare(b.entry.name))
    .slice(0, 30);

  status.textContent = `${ranked.length} result(s) for "${query}".`;

  if (!ranked.length) {
    results.innerHTML = "<p>No matches found.</p>";
    return;
  }

  for (const { entry } of ranked) {
    const article = document.createElement("article");
    article.style.padding = "1rem 0";
    article.style.borderTop = "1px solid #e5ebef";

    const tags = (entry.tags || []).map(tag => `<code>${tag}</code>`).join(" ");
    const related = (entry.related || []).slice(0, 3).map(item => item.name).join(", ");
    const href = `${baseUrl}${entry.path}`.replace(/([^:]\/)\/+/g, "$1");

    article.innerHTML = `
      <h3 style="margin-bottom: 0.25rem;"><a href="${href}">${entry.name}</a></h3>
      <p style="margin: 0.25rem 0;"><strong>${entry.category}</strong> - ${entry.origin}</p>
      <p style="margin: 0.5rem 0;">${entry.summary}</p>
      <p style="margin: 0.5rem 0;">${tags}</p>
      ${related ? `<p style="margin: 0.5rem 0;"><strong>Related:</strong> ${related}</p>` : ""}
    `;
    results.appendChild(article);
  }
}

fetch("{{ '/search-index.json' | relative_url }}")
  .then(response => response.json())
  .then(entries => {
    render(entries, "");
    input.addEventListener("input", () => render(entries, input.value.trim().toLowerCase()));
  })
  .catch(() => {
    status.textContent = "Failed to load search index.";
  });
</script>
