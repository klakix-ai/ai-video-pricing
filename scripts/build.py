#!/usr/bin/env python3
"""Build data/prices.csv from data/prices.json and refresh the README table.

Standard library only. The README table lives between
<!-- TABLE:START --> and <!-- TABLE:END -->; it is grouped by model family
and sorted by usd_per_second ascending.
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIELDS = ["id", "model_family", "model", "version", "vendor", "provider", "provider_url", "mode", "resolution",
          "audio", "billing_unit", "list_price", "usd_per_second", "usd_per_5s", "usd_per_10s", "assumptions",
          "source_url", "checked_at", "confidence", "status", "promotion"]
START, END = "<!-- TABLE:START -->", "<!-- TABLE:END -->"


def money(x):
    if x >= 1:
        return f"${x:.2f}"
    s = f"{x:.4f}".rstrip("0")
    if len(s.split(".")[1]) < 3:
        s = f"{x:.3f}"
    return "$" + s


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


def short_provider(p):
    return p.split(" (")[0]


def write_csv(rows):
    with open(ROOT / "data" / "prices.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            out = dict(r)
            out["mode"] = "|".join(r["mode"])
            if isinstance(r["audio"], bool):
                out["audio"] = str(r["audio"]).lower()
            out["promotion"] = str(r["promotion"]).lower()
            w.writerow({k: out[k] for k in FIELDS})


def table(rows):
    fams = defaultdict(list)
    for r in rows:
        fams[r["model_family"]].append(r)
    providers = {r["provider"] for r in rows}
    lines = [f"{len(rows)} rows, {len(fams)} model families, {len(providers)} providers. "
             f"Last checked {max(r['checked_at'] for r in rows)}.\n",
             "| Model family | Rows | Cheapest (USD/s) | Most expensive (USD/s) |",
             "|---|---:|---|---|"]
    for fam in sorted(fams):
        rs = sorted(fams[fam], key=lambda r: r["usd_per_second"])
        lo, hi = rs[0], rs[-1]
        lines.append(f"| {fam} | {len(rs)} | {money(lo['usd_per_second'])} ({cell(lo['model'])}, {cell(short_provider(lo['provider']))}, {lo['resolution']}) "
                     f"| {money(hi['usd_per_second'])} ({cell(hi['model'])}, {cell(short_provider(hi['provider']))}, {hi['resolution']}) |")
    lines.append("")
    for fam in sorted(fams):
        rs = sorted(fams[fam], key=lambda r: (r["usd_per_second"], r["model"], r["provider"]))
        lines.append(f"<details>\n<summary><b>{fam}</b> ({len(rs)} rows, sorted by USD/s)</summary>\n")
        lines.append("| Model | Provider | Res | Audio | USD/s | USD/5s | USD/10s | Conf | Source | Notes |")
        lines.append("|---|---|---|---|---:|---:|---:|---|---|---|")
        for r in rs:
            audio = {True: "yes", False: "no", "n/a": "n/a"}[r["audio"]]
            notes = []
            if r["status"] == "discontinued":
                notes.append("discontinued")
            if r["promotion"]:
                notes.append("promo")
            lines.append(f"| {cell(r['model'])} | {cell(short_provider(r['provider']))} | {r['resolution']} | {audio} | "
                         f"{money(r['usd_per_second'])} | {money(r['usd_per_5s'])} | {money(r['usd_per_10s'])} | "
                         f"{r['confidence']} | [link]({r['source_url']}) | {'; '.join(notes)} |")
        lines.append("\n</details>\n")
    return "\n".join(lines)


def main():
    rows = json.loads((ROOT / "data" / "prices.json").read_text(encoding="utf-8"))
    write_csv(rows)
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    a, b = text.index(START), text.index(END)
    new = text[:a + len(START)] + "\n" + table(rows) + "\n" + text[b:]
    readme.write_text(new, encoding="utf-8", newline="\n")
    print(f"wrote data/prices.csv ({len(rows)} rows) and README table")


if __name__ == "__main__":
    main()
