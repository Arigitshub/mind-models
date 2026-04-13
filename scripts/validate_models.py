from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = ROOT / "models"
ALLOWED_CATEGORIES = {
    "behavioral",
    "cognitive",
    "decision",
    "developmental",
    "emotional",
    "social",
}
REQUIRED_FIELDS = ("Category", "Origin", "Tags")
REQUIRED_SECTIONS = (
    "Summary",
    "Mechanism",
    "Triggers",
    "Effects",
    "Examples",
    "Related Models",
    "References",
)
OPTIONAL_SECTION_PREFIXES = ("Counters",)
FIELD_PATTERN = re.compile(r"^\*\*(Category|Origin|Tags):\*\*\s*(.+?)\s*$", re.MULTILINE)
SECTION_PATTERN = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
RELATED_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")
EXAMPLE_PATTERN = re.compile(r"^\*\*Example\s+\d+\b", re.MULTILINE)
KEBAB_CASE_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
LOWERCASE_TAG_PATTERN = re.compile(r"^[a-z0-9-]+$")


@dataclass
class ValidationResult:
    path: Path
    errors: list[str] = field(default_factory=list)

    def add(self, message: str) -> None:
        self.errors.append(message)


def collect_fields(text: str) -> dict[str, str]:
    return {name: value.strip() for name, value in FIELD_PATTERN.findall(text)}


def collect_sections(text: str) -> list[str]:
    return [heading.strip() for heading in SECTION_PATTERN.findall(text)]


def validate_file(path: Path, all_model_paths: set[Path]) -> ValidationResult:
    result = ValidationResult(path=path)
    text = path.read_text(encoding="utf-8")
    relative_path = path.relative_to(ROOT)

    if not KEBAB_CASE_PATTERN.match(path.name):
        result.add("filename must be kebab-case")

    category_from_folder = path.parent.name
    if category_from_folder not in ALLOWED_CATEGORIES:
        result.add(f"folder category '{category_from_folder}' is invalid")

    fields = collect_fields(text)
    for field_name in REQUIRED_FIELDS:
        if field_name not in fields:
            result.add(f"missing required field '{field_name}'")

    category = fields.get("Category")
    if category:
        if category not in ALLOWED_CATEGORIES:
            result.add(f"category '{category}' is invalid")
        if category != category_from_folder:
            result.add(
                f"category '{category}' does not match containing folder '{category_from_folder}'"
            )

    tags_value = fields.get("Tags")
    if tags_value:
        tags = [tag.strip() for tag in tags_value.split(",") if tag.strip()]
        if not 3 <= len(tags) <= 6:
            result.add("tags must contain between 3 and 6 entries")
        invalid_tags = [tag for tag in tags if not LOWERCASE_TAG_PATTERN.match(tag)]
        if invalid_tags:
            result.add(f"tags must be lowercase kebab-case keywords: {', '.join(invalid_tags)}")

    sections = collect_sections(text)
    for section in REQUIRED_SECTIONS:
        if section not in sections:
            result.add(f"missing required section '{section}'")

    if not any(section.startswith(prefix) for prefix in OPTIONAL_SECTION_PREFIXES for section in sections):
        result.add("missing counters section")

    if len(EXAMPLE_PATTERN.findall(text)) < 2:
        result.add("must include at least 2 examples")

    for related_link in RELATED_LINK_PATTERN.findall(text):
        target = (path.parent / related_link).resolve()
        if target not in all_model_paths:
            result.add(f"related model link does not exist: {related_link}")

    if not text.endswith("\n"):
        result.add("file must end with a trailing newline")

    if result.errors:
        result.path = relative_path
    else:
        result.path = relative_path

    return result


def main() -> int:
    model_paths = sorted(MODELS_DIR.rglob("*.md"))
    all_model_paths = {path.resolve() for path in model_paths}
    results = [validate_file(path, all_model_paths) for path in model_paths]
    failures = [result for result in results if result.errors]

    print(f"Validated {len(model_paths)} model files.")
    if not failures:
        print("All models passed.")
        return 0

    for failure in failures:
        print()
        print(f"{failure.path}:")
        for error in failure.errors:
            print(f"  - {error}")

    print()
    print(f"{len(failures)} file(s) failed validation.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
