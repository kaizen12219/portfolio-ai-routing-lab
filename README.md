# Portfolio AI Routing Lab

Python project for AI/data resumes. It demonstrates pathfinding, route scoring, deterministic tests, and a small CLI that can explain why a route was chosen.

## Series Coverage

- AI/data: graph search, scoring, explainable decision output.
- Backend/platform: deterministic algorithm boundaries suitable for an API.
- Mobile/game-adjacent: pathfinding behavior that can be shown visually in portfolio screenshots.

## Run

```powershell
$env:PYTHONPATH='src'
python -m portfolio_ai_routing.cli --width 6 --height 5 --start 0,0 --goal 5,4 --blocked 2,1 2,2 2,3
```

## Test

```powershell
python -m unittest discover -s tests
```

## Honest Development Plan

Use the included issue and PR templates for real follow-up work after the repo is pushed. Do not backdate commits or create fake historical issues.
