---
type: github_repo
repo: claude-code-working
file: knip.json
---

# knip.json

```json
{
	"$schema": "https://unpkg.com/knip@6/schema.json",
	"entry": ["src/entrypoints/cli.tsx"],
	"project": ["src/**/*.{ts,tsx}"],
	"ignore": ["src/types/**", "src/**/*.d.ts"],
	"ignoreDependencies": [
		"@ant/*",
		"react-compiler-runtime",
		"@anthropic-ai/mcpb",
		"@anthropic-ai/sandbox-runtime"
	],
	"ignoreBinaries": ["bun"],
	"workspaces": {
		"packages/*": {
			"entry": ["src/index.ts"],
			"project": ["src/**/*.ts"]
		},
		"packages/@ant/*": {
			"ignore": ["**"]
		}
	}
}
```
