# Profile projects

`profile_projects.py` writes the "What I'm Building" section of the profile README
(between the `PROJECTS` markers) and the SVGs in `assets/projects/`. The
`Update projects` workflow runs it daily, so changes on a repo reach the profile
within a day. Run it by hand with `python scripts/profile_projects.py`.

## Adding or changing a project

Everything is decided by topics on the repo itself:

| Topic | Effect |
| :--- | :--- |
| `live-demo` | A poster under "Try it live", linking to the repo's website (homepage) |
| `featured` | A row under "In progress", linking to the repo |
| `status-alpha`, `status-beta`, `status-prerelease`, `status-learning`, `status-stable` | The stage pill on a row (no topic shows `ACTIVE`) |

Remove the topic and the project leaves the profile. Forks and archived repos are ignored.

Text comes from the repo's description. To replace it, or anything else the repo
can't say, add an entry to `overrides.json`:

```json
{ "nl2sql": { "title": "nl2sql", "demo": "https://…", "tagline": "…", "cta": "Ask your database" } }
```

Poster taglines fit about 100 characters and row taglines about 66; longer text is cut with `…`.

## Poster diagrams

`viz/<repo>.svg` is an optional hand-drawn diagram for a poster, in a 228 × 90 box.
Write colours as `{{amber}}`, `{{border}}`, `{{muted}}`, `{{bg}}`, `{{live}}` or
`{{amber_soft}}` so one drawing works in both light and dark themes. Without one,
the poster shows the header's node-graph motif.

## Tests

```
python -m unittest discover -s scripts -p "test_*.py"
```
