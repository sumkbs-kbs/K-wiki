---
type: github_repo
repo: obsidian-code
file: conductor.json
---

# conductor.json

```json
{
    "scripts": {
        "run": "cd $CONDUCTOR_ROOT_PATH && git checkout $(git rev-parse --abbrev-ref HEAD) -- . && npm run build; git reset --hard HEAD"
    }
}
```
