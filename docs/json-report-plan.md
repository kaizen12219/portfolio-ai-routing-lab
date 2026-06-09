# JSON Route Report Plan

This change plans a JSON export mode for route reports so screenshots and portfolio fixtures can be generated from the same deterministic data.

## Proposed Shape

```json
{
  "summary": {
    "algorithm": "a-star",
    "found": true,
    "score": 88
  },
  "path": [
    { "x": 0, "y": 0 }
  ]
}
```

## Acceptance Notes

- Add a `--output` CLI option.
- Keep stdout behavior when `--output` is omitted.
- Add tests for found and not-found route exports.
