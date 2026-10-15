#!/usr/bin/env python3
"""Shallow-clone (or update) every GitHub repo linked in README.md tables into repos/,
then write repos/INDEX.tsv listing their skills, agents, commands and plugins.

Agent instruction files (CLAUDE.md, AGENTS.md, .claude/, .cursor/, ...) are never
checked out, so cloned repos can't inject instructions into sessions in this project.

Usage: python3 scripts/sync_repos.py [--selftest]
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPOS = ROOT / "repos"
SPARSE = [
    "/*",
    "!CLAUDE.md", "!**/CLAUDE.md", "!**/CLAUDE.local.md", "!**/AGENTS.md",
    "!**/.claude/", "!**/.cursor/", "!**/.cursorrules", "!**/.codex/",
]
LINK = re.compile(r"^\| \[[^\]]+\]\(https://github\.com/([\w.-]+/[\w.-]+)\)")


def git(*args, cwd=None):
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True)


def repos_from_readme():
    lines = (ROOT / "README.md").read_text().splitlines()
    return sorted({m.group(1) for line in lines if (m := LINK.match(line))})


def sync(repo):
    path = REPOS / repo
    if path.exists():
        git("fetch", "--depth", "1", "origin", cwd=path)
        git("reset", "--hard", "FETCH_HEAD", cwd=path)
    else:
        git("clone", "--depth", "1", "--no-checkout", f"https://github.com/{repo}.git", str(path))
        git("sparse-checkout", "set", "--no-cone", *SPARSE, cwd=path)
        git("checkout", cwd=path)


def frontmatter(text):
    """name/description from a markdown file's YAML frontmatter (single-line or folded values)."""
    if not text.startswith("---"):
        return {}
    block = text.split("---", 2)[1] if text.count("---") >= 2 else ""
    out, key = {}, None
    for line in block.splitlines():
        m = re.match(r"^(name|description):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            out[key] = "" if val in (">", "|", ">-", "|-") else val.strip("'\"")
        elif key and line.startswith((" ", "\t")):
            out[key] = (out[key] + " " + line.strip()).strip()
        else:
            key = None
    return out


def kind(rel):
    parts = rel.parts
    if rel.name == "SKILL.md":
        return "skill"
    if rel.name == "plugin.json":
        return "plugin"
    for k in ("agents", "commands"):
        if k in parts[:-1] and rel.suffix == ".md":
            return k[:-1]
    return None


def index():
    rows = {}  # repos often ship the same skill again inside plugin folders: keep the shortest path
    for repo in repos_from_readme():
        base = REPOS / repo
        for f in base.rglob("*"):
            rel = f.relative_to(base)
            k = kind(rel)
            if not k or ".git" in rel.parts or not f.is_file():
                continue
            text = f.read_text(errors="ignore")
            if k == "plugin":
                try:
                    meta = json.loads(text)
                except ValueError:
                    continue
            else:
                meta = frontmatter(text)
            name, desc = meta.get("name") or f.parent.name, meta.get("description") or ""
            if k != "plugin" and not desc:
                continue  # agents/commands dirs hold plenty of non-definition markdown
            clean = lambda s: re.sub(r"\s+", " ", str(s))[:300]
            key, path = (repo, k, clean(name), clean(desc)), str(f.relative_to(ROOT))
            if key not in rows or len(path) < len(rows[key]):
                rows[key] = path
    (REPOS / "INDEX.tsv").write_text("repo\tkind\tname\tdescription\tpath\n" + "\n".join("\t".join([*k, p]) for k, p in sorted(rows.items())) + "\n")
    return len(rows)


def selftest():
    assert frontmatter("---\nname: a\ndescription: b c\n---\nx") == {"name": "a", "description": "b c"}
    assert frontmatter("---\nname: 'a'\ndescription: >\n  b\n  c\nlicense: MIT\n---") == {"name": "a", "description": "b c"}
    assert frontmatter("no frontmatter") == {}
    assert kind(Path("skills/x/SKILL.md")) == "skill"
    assert kind(Path("plugins/p/agents/rev.md")) == "agent"
    assert kind(Path(".claude-plugin/plugin.json")) == "plugin"
    assert kind(Path("docs/agents.md")) is None
    assert LINK.match("| [x](https://github.com/a-b/c.d) | y | z |").group(1) == "a-b/c.d"
    print("ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    failed = []
    for repo in repos_from_readme():
        print(f"sync {repo}", flush=True)
        try:
            sync(repo)
        except subprocess.CalledProcessError as e:
            print(f"  FAILED: {e.stderr.strip()}", file=sys.stderr)
            failed.append(repo)
    print(f"indexed {index()} entries -> repos/INDEX.tsv")
    if failed:
        sys.exit(f"failed: {', '.join(failed)}")
