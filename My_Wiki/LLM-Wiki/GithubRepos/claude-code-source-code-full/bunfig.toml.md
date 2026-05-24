---
type: github_repo
repo: claude-code-source-code-full
file: bunfig.toml
---

# bunfig.toml

```
# bunfig.toml — Bun configuration for development mode
# The plugin intercepts `bun:bundle` imports → src/shims/bun-bundle.ts

preload = ["./scripts/bun-plugin-shims.ts"]
```
