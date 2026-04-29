from __future__ import annotations

import re
from collections import defaultdict

from scripts.shared import DATA_DIR, read_jsonl, stable_id, top_tokens, write_json

TRIVIAL_ACK_RE = re.compile(
    r"^(thank you|thanks|you're welcome|you are welcome|yes sir|no sir|right sir|very good|bye|goodbye|hello)\b",
    re.IGNORECASE,
)


def score_query(candidate: dict, response: dict) -> int:
    score = 0
    gap = response["line_num"] - candidate["line_num"]
    if gap <= 2:
        score += 2
    elif gap <= 4:
        score += 1
    if candidate["scene"] == response["scene"]:
        score += 1
    lower_text = candidate["text"].lower()
    if "computer" in lower_text:
        score += 3
    if candidate["question"]:
        score += 1
    if TRIVIAL_ACK_RE.match(candidate["text"]):
        score -= 4
    return score


def main() -> None:
    dialogue = read_jsonl(DATA_DIR / "dialogue.jsonl")
    episodes: dict[str, list[dict]] = defaultdict(list)
    for row in dialogue:
        episodes[row["episode"]].append(row)

    interactions: list[dict] = []

    for episode, rows in episodes.items():
        rows.sort(key=lambda row: row["line_num"])
        index = 0
        while index < len(rows):
            row = rows[index]
            if not row["is_computer"]:
                index += 1
                continue

            cluster = [row]
            next_index = index + 1
            while next_index < len(rows) and rows[next_index]["is_computer"] and rows[next_index]["line_num"] - cluster[-1]["line_num"] <= 2:
                cluster.append(rows[next_index])
                next_index += 1

            query = None
            best_score = -999
            for candidate in reversed(rows[:index]):
                if candidate["is_computer"]:
                    break
                if row["line_num"] - candidate["line_num"] > 4:
                    break
                candidate_score = score_query(candidate, row)
                if candidate_score > best_score:
                    best_score = candidate_score
                    query = candidate
            if best_score < 0:
                query = None

            context_start = max(0, index - 2)
            context_end = min(len(rows), next_index + 1)
            context = rows[context_start:context_end]

            interaction = {
                "id": stable_id(episode, row["line_num"], cluster[0]["text"]),
                "episode": episode,
                "episode_number": row["episode_number"],
                "season": row["season"],
                "stardate": row["stardate"],
                "scene": row["scene"],
                "query_speaker": query["speaker"] if query else "",
                "query_text": query["text"] if query else "",
                "response_text": " ".join(item["text"] for item in cluster),
                "response_lines": [item["line_num"] for item in cluster],
                "response_count": len(cluster),
                "context": [
                    {
                        "speaker": item["speaker"],
                        "text": item["text"],
                        "line_num": item["line_num"],
                        "is_computer": item["is_computer"],
                    }
                    for item in context
                ],
            }
            interaction["response_keywords"] = top_tokens([interaction["response_text"]], limit=6)
            interactions.append(interaction)
            index = next_index

    interactions.sort(key=lambda row: (row["season"], row["episode_number"], row["response_lines"][0]))
    write_json(DATA_DIR / "computer_interactions.json", interactions)

    with_query = sum(1 for row in interactions if row["query_text"])
    print(f"Wrote {len(interactions)} computer interactions")
    print(f"Interactions with paired query: {with_query}")


if __name__ == "__main__":
    main()
