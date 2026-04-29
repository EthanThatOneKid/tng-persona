from __future__ import annotations

import subprocess
import sys

STEPS = [
    ("export_dialogue", "Parse all TNG dialogue"),
    ("extract_computer_interactions", "Build Enterprise computer interaction dataset"),
    ("profile_speakers", "Aggregate speaker profiles"),
    ("build_training_jsonl", "Write training JSONL files"),
    ("analyze", "Generate dataset report"),
]


def main() -> None:
    for module_name, label in STEPS:
        print(f"\n{'=' * 60}\n{label}\n{'=' * 60}")
        result = subprocess.run([sys.executable, "-m", f"scripts.{module_name}"])
        if result.returncode != 0:
            raise SystemExit(result.returncode)
    print("\nPipeline complete.")


if __name__ == "__main__":
    main()
