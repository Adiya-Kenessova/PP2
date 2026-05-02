import json
import os

FILE = "leaderboard.json"


def load_leaderboard():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_score(name, score, distance, coins):
    board = load_leaderboard()

    board.append({
        "name": name,
        "score": score,
        "distance": distance,
        "coins": coins
    })

    board = sorted(board, key=lambda x: x["score"], reverse=True)[:10]

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(board, f, indent=4, ensure_ascii=False)