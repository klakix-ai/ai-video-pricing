#!/usr/bin/env python3
"""Validate data/prices.json against data/schema.json plus logic checks.

Standard library only. Exit code 1 when any error is found.
"""
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOL = 0.001


def check(value, schema, path, errors):
    t = schema.get("type")
    if "enum" in schema:
        if not any(value == e and type(value) is type(e) for e in schema["enum"]):
            errors.append(f"{path}: {value!r} not in {schema['enum']}")
        return
    if t == "object":
        if not isinstance(value, dict):
            errors.append(f"{path}: expected object")
            return
        for k in schema.get("required", []):
            if k not in value:
                errors.append(f"{path}: missing '{k}'")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for k in value:
                if k not in props:
                    errors.append(f"{path}: unexpected field '{k}'")
        for k, sub in props.items():
            if k in value:
                check(value[k], sub, f"{path}.{k}", errors)
    elif t == "array":
        if not isinstance(value, list):
            errors.append(f"{path}: expected array")
            return
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: too few items")
        if schema.get("uniqueItems") and len(set(map(str, value))) != len(value):
            errors.append(f"{path}: items not unique")
        for i, v in enumerate(value):
            check(v, schema.get("items", {}), f"{path}[{i}]", errors)
    elif t == "string":
        if not isinstance(value, str):
            errors.append(f"{path}: expected string")
            return
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: too short")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path}: {value!r} does not match {schema['pattern']}")
    elif t == "number":
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            errors.append(f"{path}: expected number")
            return
        if "exclusiveMinimum" in schema and not value > schema["exclusiveMinimum"]:
            errors.append(f"{path}: must be > {schema['exclusiveMinimum']}")
    elif t == "boolean":
        if not isinstance(value, bool):
            errors.append(f"{path}: expected boolean")


def main():
    errors = []
    schema = json.loads((ROOT / "data" / "schema.json").read_text(encoding="utf-8"))
    rows = json.loads((ROOT / "data" / "prices.json").read_text(encoding="utf-8"))
    check(rows, schema, "$", errors)

    seen = set()
    for i, r in enumerate(rows):
        if not isinstance(r, dict):
            continue
        tag = f"row {i} ({r.get('id')})"
        if r.get("id") in seen:
            errors.append(f"{tag}: duplicate id")
        seen.add(r.get("id"))
        try:
            ups = float(r["usd_per_second"])
            if abs(float(r["usd_per_5s"]) - 5 * ups) > TOL:
                errors.append(f"{tag}: usd_per_5s != 5 * usd_per_second")
            if abs(float(r["usd_per_10s"]) - 10 * ups) > TOL:
                errors.append(f"{tag}: usd_per_10s != 10 * usd_per_second")
        except (KeyError, TypeError, ValueError):
            pass
        try:
            datetime.date.fromisoformat(r["checked_at"])
        except (KeyError, ValueError, TypeError):
            errors.append(f"{tag}: checked_at is not a valid date")
        for k in ("source_url", "provider_url"):
            if not str(r.get(k, "")).startswith("https://"):
                errors.append(f"{tag}: {k} must be https")
        unit = str(r.get("billing_unit", ""))
        text = (str(r.get("assumptions", "")) + " " + str(r.get("list_price", ""))).lower()
        if unit == "per_million_tokens" and "token" not in text:
            errors.append(f"{tag}: token-billed row needs the token rate or formula in assumptions")
        if unit.startswith("credits") and "credit" not in text:
            errors.append(f"{tag}: credit-billed row needs the credit value in assumptions")
        low = (str(r.get("vendor", "")) + str(r.get("model", "")) + str(r.get("provider", ""))).lower()
        if "klakix" in low or "ai video yap" in low:
            errors.append(f"{tag}: dataset must stay vendor neutral")

    if errors:
        print(f"{len(errors)} error(s):")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print(f"OK: {len(rows)} rows valid")


if __name__ == "__main__":
    main()
