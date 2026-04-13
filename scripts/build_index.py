from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = ROOT / "models"
LIBRARY_PAGE = ROOT / "library.md"
SEARCH_INDEX = ROOT / "search-index.json"
MODELS_JSON = ROOT / "models.json"
CATEGORIES_DIR = ROOT / "categories"
CHUNKS_JSON = ROOT / "model-chunks.json"
CHUNKS_JSONL = ROOT / "model-chunks.jsonl"

FIELD_PATTERN = re.compile(r"^\*\*(Category|Origin|Tags):\*\*\s*(.+?)\s*$", re.MULTILINE)
SECTION_PATTERN = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

CATEGORY_DESCRIPTIONS = {
    "behavioral": "Habits, conditioning, reinforcement, motivation, and learned behavior.",
    "cognitive": "Biases, perception, memory, reasoning, and self-monitoring.",
    "decision": "Choice under uncertainty, framing, loss, and forecasting.",
    "developmental": "How the mind changes over time through stages, learning, and identity development.",
    "emotional": "Emotion regulation, affective learning, and self-evaluative states.",
    "social": "Influence, conformity, authority, and group-driven behavior.",
}
CATEGORY_ORDER = [
    "cognitive",
    "behavioral",
    "social",
    "emotional",
    "decision",
    "developmental",
]


def slugify(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return normalized


def split_sections(text: str) -> dict[str, str]:
    matches = list(SECTION_PATTERN.finditer(text))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        if body.endswith("---"):
            body = body[:-3].rstrip()
        sections[match.group(1).strip()] = body
    return sections


def parse_model(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    fields = {name: value.strip() for name, value in FIELD_PATTERN.findall(text)}
    title = text.splitlines()[0].lstrip("# ").strip()
    sections = split_sections(text)
    category = fields.get("Category", path.parent.name)
    relative_path = path.relative_to(ROOT).as_posix()
    tags = [tag.strip() for tag in fields.get("Tags", "").split(",") if tag.strip()]

    related = []
    related_body = sections.get("Related Models", "")
    for label, href in LINK_PATTERN.findall(related_body):
        resolved = (path.parent / href).resolve().relative_to(ROOT).as_posix()
        related.append({"name": label, "path": resolved})

    normalized = {
        "id": slugify(title),
        "name": title,
        "category": category,
        "origin": fields.get("Origin", ""),
        "tags": tags,
        "summary": " ".join(sections.get("Summary", "").split()),
        "path": relative_path,
        "related": related,
        "sections": {name: body for name, body in sections.items() if name != "Related Models"},
        "section_names": list(sections.keys()),
    }
    return normalized


def build_search_index(models: list[dict]) -> list[dict]:
    search_entries = []
    for model in models:
        search_entries.append(
            {
                "id": model["id"],
                "name": model["name"],
                "category": model["category"],
                "origin": model["origin"],
                "tags": model["tags"],
                "summary": model["summary"],
                "path": model["path"],
                "related": model["related"],
                "keywords": sorted({model["category"], *model["tags"], *model["name"].lower().split()}),
            }
        )
    return search_entries


def build_chunks(models: list[dict]) -> list[dict]:
    chunks = []
    for model in models:
        chunks.append(
            {
                "chunk_id": f"{model['id']}::summary",
                "model_id": model["id"],
                "name": model["name"],
                "category": model["category"],
                "path": model["path"],
                "section": "Summary",
                "text": model["summary"],
                "tags": model["tags"],
            }
        )
        for section_name, body in model["sections"].items():
            normalized_text = " ".join(body.split())
            if not normalized_text or section_name == "Summary":
                continue
            chunks.append(
                {
                    "chunk_id": f"{model['id']}::{slugify(section_name)}",
                    "model_id": model["id"],
                    "name": model["name"],
                    "category": model["category"],
                    "path": model["path"],
                    "section": section_name,
                    "text": normalized_text,
                    "tags": model["tags"],
                }
            )
    return chunks


def build_library_page(models: list[dict]) -> str:
    category_counts = Counter(model["category"] for model in models)
    lines = [
        "---",
        "title: Model Library",
        "---",
        "",
        "<section class=\"hero hero-compact\">",
        "  <p class=\"eyebrow\">Generated Library</p>",
        "  <h1>Model Library</h1>",
        f"  <p class=\"hero-copy\">A validated catalog of <strong>{len(models)} models</strong> spanning cognitive, behavioral, social, emotional, decision, and developmental frameworks.</p>",
        "  <div class=\"hero-actions\">",
        "    <a class=\"button button-primary\" href=\"{{ '/search' | relative_url }}\">Search Models</a>",
        "    <a class=\"button button-secondary\" href=\"{{ '/models.json' | relative_url }}\">Download models.json</a>",
        "    <a class=\"button button-secondary\" href=\"{{ '/model-chunks.json' | relative_url }}\">Chunk Export</a>",
        "  </div>",
        "</section>",
        "",
        "<section class=\"stats-grid\">",
    ]

    for category in CATEGORY_ORDER:
        lines.extend(
            [
                "  <article class=\"stat-card\">",
                f"    <p class=\"stat-value\">{category_counts.get(category, 0)}</p>",
                f"    <p class=\"stat-label\">{category.title()}</p>",
                "  </article>",
            ]
        )
    lines.extend(["</section>", ""])

    grouped = {category: [] for category in CATEGORY_ORDER}
    for model in models:
        grouped.setdefault(model["category"], []).append(model)

    for category in CATEGORY_ORDER:
        entries = sorted(grouped.get(category, []), key=lambda item: item["name"])
        lines.extend(
            [
                f"## {category.title()} ({len(entries)})",
                "",
                CATEGORY_DESCRIPTIONS.get(category, ""),
                "",
                f"[Open category page]({{{{ '/categories/{category}' | relative_url }}}})",
                "",
                "<div class=\"card-grid\">",
            ]
        )
        for model in entries:
            tags = " ".join(f"<span class=\"tag\">{tag}</span>" for tag in model["tags"])
            related = ", ".join(
                f"<a href=\"{{{{ '/{item['path']}' | relative_url }}}}\">{item['name']}</a>"
                for item in model["related"][:3]
            )
            lines.extend(
                [
                    "  <article class=\"model-card\">",
                    f"    <p class=\"model-card-category\">{model['category']}</p>",
                    f"    <h3><a href=\"{{{{ '/{model['path']}' | relative_url }}}}\">{model['name']}</a></h3>",
                    f"    <p>{model['summary']}</p>",
                    f"    <p class=\"meta-line\"><strong>Origin:</strong> {model['origin']}</p>",
                    f"    <div class=\"tag-row\">{tags}</div>",
                    f"    <p class=\"meta-line\"><strong>Related:</strong> {related if related else 'None yet'}</p>",
                    "  </article>",
                ]
            )
        lines.extend(["</div>", ""])

    return "\n".join(lines).rstrip() + "\n"


def build_category_page(category: str, models: list[dict]) -> str:
    lines = [
        "---",
        f"title: {category.title()} Models",
        "---",
        "",
        "<section class=\"hero hero-compact\">",
        "  <p class=\"eyebrow\">Category View</p>",
        f"  <h1>{category.title()}</h1>",
        f"  <p class=\"hero-copy\">{CATEGORY_DESCRIPTIONS.get(category, '')} This page currently lists <strong>{len(models)} models</strong>.</p>",
        "  <div class=\"hero-actions\">",
        "    <a class=\"button button-primary\" href=\"{{ '/library' | relative_url }}\">Back to Library</a>",
        "    <a class=\"button button-secondary\" href=\"{{ '/search' | relative_url }}\">Search</a>",
        "  </div>",
        "</section>",
        "",
        "<div class=\"card-grid\">",
    ]
    for model in models:
        tags = " ".join(f"<span class=\"tag\">{tag}</span>" for tag in model["tags"])
        lines.extend(
            [
                "  <article class=\"model-card\">",
                f"    <h3><a href=\"{{{{ '/{model['path']}' | relative_url }}}}\">{model['name']}</a></h3>",
                f"    <p>{model['summary']}</p>",
                f"    <p class=\"meta-line\"><strong>Origin:</strong> {model['origin']}</p>",
                f"    <div class=\"tag-row\">{tags}</div>",
                "  </article>",
            ]
        )
    lines.extend(["</div>", ""])
    return "\n".join(lines).rstrip() + "\n"


def build_categories_index(models: list[dict]) -> str:
    category_counts = Counter(model["category"] for model in models)
    lines = [
        "---",
        "title: Categories",
        "---",
        "",
        "<section class=\"hero hero-compact\">",
        "  <p class=\"eyebrow\">Browse by Category</p>",
        "  <h1>Categories</h1>",
        "  <p class=\"hero-copy\">Use category landing pages when you want a tighter slice of the library before dropping into the full catalog.</p>",
        "</section>",
        "",
        "<div class=\"card-grid\">",
    ]
    for category in CATEGORY_ORDER:
        lines.extend(
            [
                "  <article class=\"surface-card\">",
                f"    <p class=\"model-card-category\">{category}</p>",
                f"    <h3><a href=\"{{{{ '/categories/{category}' | relative_url }}}}\">{category.title()}</a></h3>",
                f"    <p>{CATEGORY_DESCRIPTIONS.get(category, '')}</p>",
                f"    <p class=\"meta-line\"><strong>Models:</strong> {category_counts.get(category, 0)}</p>",
                "  </article>",
            ]
        )
    lines.extend(["</div>", ""])
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    models = sorted(
        [parse_model(path) for path in MODELS_DIR.rglob("*.md")],
        key=lambda item: (CATEGORY_ORDER.index(item["category"]), item["name"]),
    )
    search_index = build_search_index(models)
    chunks = build_chunks(models)
    CATEGORIES_DIR.mkdir(exist_ok=True)

    LIBRARY_PAGE.write_text(build_library_page(models), encoding="utf-8")
    SEARCH_INDEX.write_text(json.dumps(search_index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    MODELS_JSON.write_text(json.dumps(models, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    CHUNKS_JSON.write_text(json.dumps(chunks, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    CHUNKS_JSONL.write_text(
        "".join(json.dumps(chunk, ensure_ascii=False) + "\n" for chunk in chunks),
        encoding="utf-8",
    )
    for category in CATEGORY_ORDER:
        category_models = [model for model in models if model["category"] == category]
        (CATEGORIES_DIR / f"{category}.md").write_text(
            build_category_page(category, category_models),
            encoding="utf-8",
        )
    (CATEGORIES_DIR / "index.md").write_text(build_categories_index(models), encoding="utf-8")

    print(f"Wrote {LIBRARY_PAGE.relative_to(ROOT)}")
    print(f"Wrote {SEARCH_INDEX.relative_to(ROOT)}")
    print(f"Wrote {MODELS_JSON.relative_to(ROOT)}")
    print(f"Wrote {CHUNKS_JSON.relative_to(ROOT)}")
    print(f"Wrote {CHUNKS_JSONL.relative_to(ROOT)}")
    print(f"Wrote {CATEGORIES_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
