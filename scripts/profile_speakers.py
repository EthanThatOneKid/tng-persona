from __future__ import annotations

from collections import Counter, defaultdict

from scripts.shared import DATA_DIR, read_jsonl, top_tokens, write_json


def main() -> None:
    dialogue = read_jsonl(DATA_DIR / "dialogue.jsonl")
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in dialogue:
        grouped[row["speaker"]].append(row)

    profiles: list[dict] = []
    for speaker, rows in grouped.items():
        texts = [row["text"] for row in rows]
        openers = Counter(" ".join(text.split()[:3]).strip() for text in texts if text.strip())
        profile = {
            "speaker": speaker,
            "is_computer": any(row["is_computer"] for row in rows),
            "line_count": len(rows),
            "episode_count": len({row["episode"] for row in rows}),
            "question_rate": round(sum(1 for row in rows if row["question"]) / len(rows), 3),
            "avg_word_count": round(sum(row["word_count"] for row in rows) / len(rows), 2),
            "top_tokens": top_tokens(texts, limit=12),
            "common_openers": [phrase for phrase, _ in openers.most_common(8) if phrase],
            "sample_lines": texts[:5],
        }
        profiles.append(profile)

    profiles.sort(key=lambda row: (-row["line_count"], row["speaker"]))
    write_json(DATA_DIR / "speaker_profiles.json", profiles)
    print(f"Wrote {len(profiles)} speaker profiles")


if __name__ == "__main__":
    main()
