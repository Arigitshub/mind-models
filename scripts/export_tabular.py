from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODELS_JSON = ROOT / "models.json"
CHUNKS_JSON = ROOT / "model-chunks.json"
EXPORTS_DIR = ROOT / "exports"


def load_json(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def flatten_models(models: list[dict]) -> pd.DataFrame:
    rows = []
    for model in models:
        rows.append(
            {
                "id": model["id"],
                "name": model["name"],
                "category": model["category"],
                "origin": model["origin"],
                "summary": model["summary"],
                "path": model["path"],
                "tags": "|".join(model["tags"]),
                "related_names": "|".join(item["name"] for item in model["related"]),
                "related_paths": "|".join(item["path"] for item in model["related"]),
                "section_names": "|".join(model["section_names"]),
            }
        )
    return pd.DataFrame(rows)


def flatten_chunks(chunks: list[dict]) -> pd.DataFrame:
    rows = []
    for chunk in chunks:
        rows.append(
            {
                "chunk_id": chunk["chunk_id"],
                "model_id": chunk["model_id"],
                "name": chunk["name"],
                "category": chunk["category"],
                "path": chunk["path"],
                "section": chunk["section"],
                "text": chunk["text"],
                "tags": "|".join(chunk["tags"]),
            }
        )
    return pd.DataFrame(rows)


def write_parquet_if_possible(frame: pd.DataFrame, path: Path) -> str:
    try:
        frame.to_parquet(path, index=False)
        return "wrote"
    except Exception as exc:  # pragma: no cover - dependency-specific
        return f"skipped ({exc.__class__.__name__})"


def main() -> None:
    EXPORTS_DIR.mkdir(exist_ok=True)

    models = load_json(MODELS_JSON)
    chunks = load_json(CHUNKS_JSON)

    model_frame = flatten_models(models)
    chunk_frame = flatten_chunks(chunks)

    models_csv = EXPORTS_DIR / "models.csv"
    chunks_csv = EXPORTS_DIR / "model-chunks.csv"
    models_parquet = EXPORTS_DIR / "models.parquet"
    chunks_parquet = EXPORTS_DIR / "model-chunks.parquet"

    model_frame.to_csv(models_csv, index=False)
    chunk_frame.to_csv(chunks_csv, index=False)

    print(f"Wrote {models_csv.relative_to(ROOT)}")
    print(f"Wrote {chunks_csv.relative_to(ROOT)}")
    print(f"Parquet models: {write_parquet_if_possible(model_frame, models_parquet)}")
    print(f"Parquet chunks: {write_parquet_if_possible(chunk_frame, chunks_parquet)}")


if __name__ == "__main__":
    main()
