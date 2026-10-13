<<<<<<< Updated upstream
# AM4-Tools_Shared_Reources
Shared Resources for our AM4-Tools
=======
# AM4 Tools – Shared Resources

Files shared by the [AM4 Route Calculator](https://github.com/Global-Air-Alliance/AM4_Route_Calculator) and the [AM4 Hub Planner](https://github.com/Global-Air-Alliance/AM4_Hub_Planner). Deployed to `www/tools/shared_resources/` on globalairall.net.

## Contents

| File | Purpose |
| --- | --- |
| `site/tools/shared_resources/am4.js` | `window.AM4`: aircraft list, loading of airports and demand, distance, number formatting (browser locale), texts from `<div id="am4-strings">` |
| `site/tools/shared_resources/am4tools.css` | Shared styles, scoped to `.am4` so they work next to Bootstrap; light/dark via `data-bs-theme` |
| `site/tools/shared_resources/data/airports.json` | 3,907 airports in database order (index 0…3906). Fields: name, fullname, country, iata, icao, lat, lng, rwy (ft) |
| `site/tools/shared_resources/data/demand/<idx>.bin` | Demand from airport `<idx>` to all 3,907 airports: per destination 3 × uint16 little-endian (Y, J, F) = 23,442 bytes per file; value for destination k at byte offset k × 6 |
| `scripts/build_data.py` | Rebuilds `data/` from abc8747/am4 (not deployed) |

Pages load `shared_resources/am4.js` before the tool script. Data files are loaded relative to `am4.js`, so the page location does not matter.

## Rebuild the game data

Requires Python with pandas and pyarrow, and a copy of [abc8747/am4](https://github.com/abc8747/am4):

```
python3 scripts/build_data.py <path-to-am4>/src/am4/utils/data site/tools/shared_resources/data
```

Game data as of August 2026.

## Deployment

Every push to `main` that changes `site/` runs the workflow **Deploy Shared Resources** (`.github/workflows/deploy.yml`): rsync over SSH to `www/tools/shared_resources/` (checksum comparison, so unchanged demand files are not transferred again), then a message per commit in the Discord forum posts of both tools; on failure an e-mail. Variables and secrets are listed at the top of the workflow file.

Game data: AM4 community project [abc8747/am4](https://github.com/abc8747/am4). No guarantee of accuracy. Not affiliated with Trophy Games / Airline Manager.
>>>>>>> Stashed changes
