# Patches

Custom patches to clawdbot plugins that need reapplying after updates.

## memory-lancedb-index.ts

Patched version of the LanceDB memory plugin. Changes from upstream:

| Setting | Upstream | Patched |
|---|---|---|
| Auto-recall limit | 3 | 8 |
| Auto-recall similarity threshold | 0.3 | 0.15 |
| Auto-capture limit | 3 per conversation | 8 per conversation |
| shouldCapture max text length | 500 chars | 1000 chars |
| Emoji filter | >3 emojis = skip | >8 emojis = skip |
| Markdown filter (`**` + `\n-`) | Active | Removed |
| Memory trigger patterns | 9 | 19 |

New trigger patterns added:
- Project: `decided`, `agreed`, `plan is`, `strategy`, `goal`, `deadline`, `set up`, `configured`, `installed`, `created`, `built`
- Family: `family`, `kids`, `children`, `wife`, `husband`, `son`, `daughter`, `birthday`, `anniversary`
- Health: `health`, `bloodwork`, `supplement`, `medication`, `exercise`
- Learning: `learned`, `mastered`, `struggling`, `progress`, `lesson`
- Feedback: `don't`, `stop`, `change`, `fix`, `adjust`, `instead`

### Reapply after update

```bash
bash ~/clawd/patches/apply-memory-patches.sh
npx clawdbot gateway restart
```
