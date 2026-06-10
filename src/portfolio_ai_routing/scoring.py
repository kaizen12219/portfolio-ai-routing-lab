from .router import RouteResult


def score_route(result: RouteResult) -> dict[str, int | str | bool]:
    if not result.found:
        return {
            "algorithm": result.algorithm,
            "found": False,
            "score": 0,
            "reason": "No path reached the goal.",
            "portfolio_signal": "edge-case handling",
        }

    exploration_penalty = max(0, result.visited_count - result.steps)
    score = max(1, 100 - result.steps * 4 - exploration_penalty)
    return {
        "algorithm": result.algorithm,
        "found": True,
        "score": score,
        "reason": f"{result.algorithm} reached the goal in {result.steps} steps after visiting {result.visited_count} nodes.",
        "portfolio_signal": _portfolio_signal(score),
    }


def _portfolio_signal(score: int) -> str:
    if score >= 80:
        return "strong AI/data evidence"
    if score >= 50:
        return "usable algorithmic evidence"
    return "needs optimization notes"
