from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = ROOT / "models"
FIELD_PATTERN = re.compile(r"^\*\*(Category|Origin|Tags):\*\*\s*(.+?)\s*$", re.MULTILINE)
SUMMARY_PATTERN = re.compile(r"## Summary\s+(.+?)(?:\n---|\Z)", re.DOTALL)


def parse_fields(text: str) -> tuple[str, str, list[str], str]:
    fields = {name: value.strip() for name, value in FIELD_PATTERN.findall(text)}
    title = text.splitlines()[0].lstrip("# ").strip()
    tags = [tag.strip() for tag in fields.get("Tags", "").split(",") if tag.strip()]
    summary_match = SUMMARY_PATTERN.search(text)
    summary = " ".join(summary_match.group(1).strip().split()) if summary_match else ""
    return title, fields.get("Category", ""), tags, fields.get("Origin", ""), summary


def strip_existing_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        parts = text.split("---\n", 2)
        if len(parts) == 3:
            return parts[2].lstrip("\n")
    return text


def format_front_matter(title: str, category: str, tags: list[str], origin: str, summary: str) -> str:
    yaml_tags = "[" + ", ".join(tags) + "]"
    lines = [
        "---",
        "layout: model",
        f'title: "{title.replace(chr(34), chr(92) + chr(34))}"',
        f"category: {category}",
        f"model_tags: {yaml_tags}",
        f'origin: "{origin.replace(chr(34), chr(92) + chr(34))}"',
        f'summary: "{summary.replace(chr(34), chr(92) + chr(34))}"',
        "---",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    updated = 0
    for path in sorted(MODELS_DIR.rglob("*.md")):
        original = path.read_text(encoding="utf-8")
        body = strip_existing_front_matter(original)
        title, category, tags, origin, summary = parse_fields(body)
        front_matter = format_front_matter(title, category, tags, origin, summary)
        new_text = front_matter + body.lstrip("\n")
        if new_text != original:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
    print(f"Updated {updated} model files.")


if __name__ == "__main__":
    main()
