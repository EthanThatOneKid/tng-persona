from __future__ import annotations

from scripts.shared import DATA_DIR, iter_episode_paths, parse_episode, write_json, write_jsonl


def main() -> None:
    dialogue_rows: list[dict] = []
    episode_rows: list[dict] = []

    for path in iter_episode_paths():
        records, summary = parse_episode(path)
        dialogue_rows.extend(records)
        episode_rows.append(summary)
        print(f"{path.name}: {len(records)} dialogue lines, {summary['computer_lines']} computer lines")

    write_jsonl(DATA_DIR / "dialogue.jsonl", dialogue_rows)
    write_json(DATA_DIR / "episode_index.json", episode_rows)

    print(f"\nWrote {len(dialogue_rows)} dialogue rows")
    print(f"Wrote {len(episode_rows)} episode summaries")


if __name__ == "__main__":
    main()
