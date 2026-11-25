# Contributing

Thanks for helping keep the numbers accurate. Prices change often, so corrections and new rows are welcome.

## Rules

1. **Every change needs a source URL.** Link the provider's own public pricing page, model page or docs. A screenshot alone is not enough; a social post is not a source.
2. **List price only.** Record what the provider publishes. Do not add negotiated, enterprise, reseller-bundle or "my invoice said" prices.
3. **Never guess.** If the page does not open, is JS-only, or the price is unclear, either set `confidence` to `low` and say why in `assumptions`, or leave the row out.
4. **No vendor favouritism.** Rows for every vendor follow the same rules. Marketing copy does not belong in the data.
5. **One row per model x provider x resolution x audio.** Keep `id` unique and stable (see existing rows).

## How to edit

1. Edit `data/prices.json` (the CSV and README table are generated, do not edit them by hand).
2. Fill every field required by `data/schema.json`:
   - `list_price` is the raw text/number in the provider's own unit.
   - `usd_per_second` is the normalized price. Set `usd_per_5s` = 5 x `usd_per_second` and `usd_per_10s` = 10 x `usd_per_second`.
   - For token-priced models, write the vendor's formula and token rate in `assumptions` (for example: width x height x fps x seconds / 1024).
   - For credit-priced models, write the USD value of one credit and where it comes from.
   - Set `checked_at` to the date you looked at the page (YYYY-MM-DD) and `confidence` to `high`, `medium` or `low`.
   - If a time-limited discount applies, record the price payable on the check date, set `promotion` to `true` and describe the end date in `assumptions`.
3. Run:

   ```
   python scripts/build.py
   python scripts/validate.py
   ```

   Both must pass (Python 3.8+, standard library only).
4. Open a pull request with the source URL in the description.

## Confidence levels

- `high`: the number is read directly from an official page and needs only arithmetic.
- `medium`: official page, but a unit or resolution had to be interpreted (for example a "per count" unit or an inferred credit value).
- `low`: indirect, outdated or partial source. Use sparingly.

## Licenses

By contributing you agree that data contributions are licensed CC BY 4.0 and script contributions MIT.
