"""Generate the "What I'm Building" section of the profile README.

Which repos appear is decided on the repos themselves, through topics:
  live-demo            -> a poster, linking to the repo's homepage (the demo)
  featured             -> a status row, linking to the repo
  status-<stage>       -> the stage pill on a row (alpha, beta, prerelease, learning, stable)

scripts/overrides.json can replace a repo's title, demo URL, tagline or call to action.
scripts/viz/<repo>.svg is an optional hand-drawn diagram for that repo's poster.
"""

import json
import os
import re
import sys
import urllib.request
from html import escape
from pathlib import Path
from urllib.parse import urlparse

USER = "nadeem4"
ROOT = Path(__file__).resolve().parent.parent
HERE = Path(__file__).resolve().parent
OUT = ROOT / "assets" / "projects"
START, END = "<!-- PROJECTS:START -->", "<!-- PROJECTS:END -->"

PALETTES = {
    "light": {
        "card": "#F6F8FA", "bg": "#FFFFFF", "fg": "#1F2328", "muted": "#59636E",
        "border": "#D1D9E0", "amber": "#9A6700", "amber_soft": "#FFF8E5", "live": "#1A7F37",
    },
    "dark": {
        "card": "#151B23", "bg": "#0D1117", "fg": "#E6EDF3", "muted": "#9198A1",
        "border": "#3D444D", "amber": "#E3B341", "amber_soft": "#2B2111", "live": "#3FB950",
    },
}
STATUS = {"alpha": "ALPHA", "beta": "BETA", "prerelease": "PRE-RELEASE",
          "learning": "LEARNING", "stable": "STABLE", "active": "ACTIVE"}
HIGHLIGHT = {"alpha", "beta"}
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace"

# Generic diagram for a poster with no hand-drawn one: the header's node motif.
DEFAULT_VIZ = """
<g stroke="{{border}}" stroke-width="1.5" fill="none"><path d="M20 44 L80 20 M20 44 L80 68 M80 20 L150 44 M80 68 L150 44 M150 44 L214 44"/></g>
<g stroke="{{border}}" stroke-width="1.5" fill="{{bg}}"><circle cx="20" cy="44" r="7"/><circle cx="80" cy="20" r="7"/><circle cx="80" cy="68" r="7"/><circle cx="150" cy="44" r="7"/></g>
<circle cx="214" cy="44" r="8" fill="{{amber}}"/>
"""


def wrap(text, width, max_lines):
    lines, line = [], ""
    for word in text.split():
        candidate = f"{line} {word}".strip()
        if len(candidate) <= width:
            line = candidate
            continue
        lines.append(line)
        line = word
    if line:
        lines.append(line)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        lines[-1] = (last if len(last) < width else last.rsplit(" ", 1)[0]) + "…"
    return lines


def host_label(url):
    host = urlparse(url).hostname or url
    if host.endswith("hf.space") or host == "huggingface.co":
        return "Hugging Face"
    return host


def select(repos, overrides):
    live, building = [], []
    for r in sorted(repos, key=lambda r: (-r["stargazers_count"], r["name"])):
        if r["fork"] or r["archived"]:
            continue
        topics = set(r["topics"])
        o = overrides.get(r["name"], {})
        project = {
            "name": r["name"],
            "title": o.get("title", r["name"]),
            "url": r["html_url"],
            "tagline": o.get("tagline") or r["description"] or "",
        }
        if "live-demo" in topics:
            demo = o.get("demo") or r["homepage"]
            if demo:
                live.append({**project, "demo": demo, "cta": o.get("cta", "Try the demo")})
        elif "featured" in topics:
            stage = next((t[len("status-"):] for t in topics if t.startswith("status-")), "active")
            building.append({**project, "status": stage if stage in STATUS else "active"})
    return live, building


def _fill(fragment, palette):
    return re.sub(r"\{\{(\w+)\}\}", lambda m: palette[m.group(1)], fragment)


def render_poster(p, c, viz):
    lines = wrap(p["tagline"], 36, 3)
    tagline = "".join(
        f'<text x="20" y="{206 + i * 18}" font-size="13" fill="{c["muted"]}">{escape(t)}</text>'
        for i, t in enumerate(lines)
    )
    tag = escape(f"● LIVE · {host_label(p['demo'])}".upper())
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 272 300" width="272" height="300" role="img" aria-label="{escape(p['title'])}: {escape(p['tagline'])}">
  <rect x="0.5" y="0.5" width="271" height="299" rx="12" fill="{c['card']}" stroke="{c['border']}"/>
  <g font-family="{SANS}">
    <text x="20" y="32" font-family="{MONO}" font-size="10" font-weight="600" letter-spacing="1.4" fill="{c['live']}">{tag}</text>
    <text x="20" y="62" font-size="22" font-weight="700" fill="{c['fg']}">{escape(p['title'])}</text>
    <rect x="16.5" y="78.5" width="239" height="103" rx="8" fill="{c['bg']}" stroke="{c['border']}"/>
    <g transform="translate(22 86)" font-family="{MONO}">{_fill(viz or DEFAULT_VIZ, c)}</g>
    {tagline}
    <text x="20" y="278" font-size="14" font-weight="600" fill="{c['amber']}">{escape(p['cta'])} →</text>
  </g>
</svg>
"""


def render_row(p, c):
    stage = p["status"]
    hot = stage in HIGHLIGHT
    pill_fg, pill_bg, pill_stroke = (
        (c["amber"], c["amber_soft"], c["amber"]) if hot else (c["muted"], c["bg"], c["border"])
    )
    label = STATUS[stage]
    name_x, desc_x = 136, 312  # fixed columns so separate row images line up
    name = p["name"] if len(p["name"]) <= 18 else p["name"][:17] + "…"
    desc = wrap(p["tagline"], 66, 1)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 52" width="880" height="52" role="img" aria-label="{escape(p['name'])} ({label.lower()}): {escape(p['tagline'])}">
  <rect x="0.5" y="0.5" width="879" height="51" rx="8" fill="{c['bg']}" stroke="{c['border']}"/>
  <rect x="16.5" y="14.5" width="100" height="23" rx="4" fill="{pill_bg}" stroke="{pill_stroke}"/>
  <text x="66.5" y="30" text-anchor="middle" font-family="{MONO}" font-size="10" font-weight="600" letter-spacing="1.2" fill="{pill_fg}">{label}</text>
  <text x="{name_x}" y="31" font-family="{MONO}" font-size="14" font-weight="600" fill="{c['fg']}">{escape(name)}</text>
  <text x="{desc_x}" y="31" font-family="{SANS}" font-size="14" fill="{c['muted']}">{escape(desc[0] if desc else '')}</text>
  <text x="864" y="31" text-anchor="end" font-family="{SANS}" font-size="13" font-weight="600" fill="{c['amber']}">repo →</text>
</svg>
"""


def _picture(stem, alt, width):
    return (
        f'<picture><source media="(prefers-color-scheme: dark)" srcset="assets/projects/{stem}-dark.svg">'
        f'<img alt="{escape(alt)}" src="assets/projects/{stem}-light.svg" width="{width}"></picture>'
    )


def render_block(live, building):
    parts = []
    if live:
        cards = "\n".join(
            f'<a href="{escape(p["demo"])}">{_picture(p["name"], p.get("title", p["name"]) + ": " + p["tagline"], 272)}</a>'
            for p in live
        )
        parts.append(f"**▶ Try it live**\n\n<p>\n{cards}\n</p>")
    if building:
        rows = "<br>\n".join(
            f'<a href="{escape(p["url"])}">{_picture("row-" + p["name"], p["name"] + ": " + p["tagline"], "100%")}</a>'
            for p in building
        )
        parts.append(f"**In progress**\n\n<p>\n{rows}\n</p>")
    return "\n\n".join(parts)


def replace_block(readme, block):
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(readme):
        raise ValueError("README is missing the PROJECTS markers")
    return pattern.sub(lambda _: f"{START}\n{block}\n{END}", readme)


def fetch_repos():
    req = urllib.request.Request(
        f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner",
        headers={"Accept": "application/vnd.github+json"},
    )
    if os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", f"Bearer {os.environ['GITHUB_TOKEN']}")
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def main():
    overrides_path = HERE / "overrides.json"
    overrides = json.loads(overrides_path.read_text(encoding="utf-8")) if overrides_path.exists() else {}
    live, building = select(fetch_repos(), overrides)

    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.svg"):
        old.unlink()
    for p in live:
        viz_file = HERE / "viz" / f"{p['name']}.svg"
        viz = viz_file.read_text(encoding="utf-8") if viz_file.exists() else ""
        for mode, palette in PALETTES.items():
            (OUT / f"{p['name']}-{mode}.svg").write_text(render_poster(p, palette, viz), encoding="utf-8")
    for p in building:
        for mode, palette in PALETTES.items():
            (OUT / f"row-{p['name']}-{mode}.svg").write_text(render_row(p, palette), encoding="utf-8")

    readme = ROOT / "README.md"
    readme.write_text(replace_block(readme.read_text(encoding="utf-8"), render_block(live, building)),
                      encoding="utf-8", newline="\n")
    print(f"{len(live)} posters, {len(building)} rows")


if __name__ == "__main__":
    sys.exit(main())
