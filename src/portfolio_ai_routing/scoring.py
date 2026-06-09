from .router import RouteResult


def score_route(result: RouteResult) -> dict[str, int | str | bool]:
    if not result.found:
        return {
            "algorithm": result.algorithm,
            "found": False,
            "score": 0,
            "reason": "No path reached the goal.",
        }

    exploration_penalty = max(0, result.visited_count - result.steps)
    score = max(1, 100 - result.steps * 4 - exploration_penalty)
    return {
        "algorithm": result.algorithm,
        "found": True,
        "score": score,
        "reason": f"{result.algorithm} reached the goal in {result.steps} steps after visiting {result.visited_count} nodes.",
    }
