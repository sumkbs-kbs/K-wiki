---
type: github_repo
repo: claude_agent_teams_ui
file: tsconfig.json
---

# tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2023",
    "module": "ESNext",
    "lib": ["ES2023", "DOM", "DOM.Iterable"],
    "jsx": "react-jsx",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "baseUrl": ".",
    "paths": {
      "@main/*": ["./src/main/*"],
      "@renderer/*": ["./src/renderer/*"],
      "@preload/*": ["./src/preload/*"],
      "@shared/*": ["./src/shared/*"]
    },
    "types": ["node", "vitest/globals"]
  },
  "include": ["src/**/*", "test/**/*"],
  "exclude": ["node_modules", "dist", "dist-electron"]
}
```
