from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = ROOT / "models"
LIBRARY_PAGE = ROOT / "library.md"
SEARCH_INDEX = ROOT / "search-index.json"

FIELD_PATTERN = re.compile(r"^\*\*(Category|Origin|Tags):\*\*\s*(.+?)\s*$", re.MULTILINE)
SUMMARY_PATTERN = re.compile(r"## Summary\s+(.+?)(?:\n---|\Z)", re.DOTALL)
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


def parse_model(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    fields = {name: value.strip() for name, value in FIELD_PATTERN.findall(text)}
    title = text.splitlines()[0].lstrip("# ").strip()
    summary_match = SUMMARY_PATTERN.search(text)
    summary = " ".join(summary_match.group(1).strip().split()) if summary_match else ""
    sections = [section.strip() for section in SECTION_PATTERN.findall(text)]

    related = []
    if "## Related Models" in text:
        related_block = text.split("## Related Models", 1)[1]
        related_block = related_block.split("\n---", 1)[0]
        for label, href in LINK_PATTERN.findall(related_block):
            resolved = (path.parent / href).resolve().relative_to(ROOT).as_posix()
            related.append({"name": label, "path": resolved})

    tags = [tag.strip() for tag in fields.get("Tags", "").split(",") if tag.strip()]
    relative_path = path.relative_to(ROOT).as_posix()

    return {
        "name": title,
        "category": fields.get("Category", path.parent.name),
        "origin": fields.get("Origin", ""),
        "tags": tags,
        "summary": summary,
        "path": relative_path,
        "related": related,
        "sections": sections,
    }


def build_library_page(models: list[dict]) -> str:
    lines = [
        "---",
        "title: Model Library",
        "---",
        "",
        "# Model Library",
        "",
        f"This page is generated from the validated model files in `models/`. It currently indexes **{len(models)}** models.",
        "",
        "## Quick Links",
        "",
        "- [Search]({{ '/search' | relative_url }})",
        "- [Machine-readable index]({{ '/search-index.json' | relative_url }})",
        "",
    ]

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
            ]
        )
        if not entries:
            lines.extend(["No models published in this category yet.", ""])
            continue

        for model in entries:
            tags = ", ".join(f"`{tag}`" for tag in model["tags"])
            related = ", ".join(f"[{item['name']}]({item['path']})" for item in model["related"][:3])
            lines.append(f"### [{model['name']}]({model['path']})")
            lines.append("")
            lines.append(f"{model['summary']}")
            lines.append("")
            lines.append(f"- Origin: {model['origin']}")
            lines.append(f"- Tags: {tags}")
            if related:
                lines.append(f"- Related: {related}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    models = sorted(
        [parse_model(path) for path in MODELS_DIR.rglob("*.md")],
        key=lambda item: (CATEGORY_ORDER.index(item["category"]), item["name"]),
    )

    LIBRARY_PAGE.write_text(build_library_page(models), encoding="utf-8")
    SEARCH_INDEX.write_text(json.dumps(models, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Wrote {LIBRARY_PAGE.relative_to(ROOT)}")
    print(f"Wrote {SEARCH_INDEX.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
