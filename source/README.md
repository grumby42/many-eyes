# Source data for Many Eyes

Everything needed to rebuild the volumes, apart from the raw image files (already embedded in each built HTML file).

- `build/` — `build.py` (VOL=1..9, 13, 15), `template.html`, `series.json`, `geo.py`, the companion and site generators, and `check4.py` (Playwright test).
- `volN/` — chapter JSON (`ch-*.json`), second-edition patches (`patch-*.json`), fact-check audits (`audit-*.json`, `audit2-*.json` for patches), map coordinates, image manifests and reject lists, and the specs and briefs the researchers and fact-checkers followed. Volume I lives in `vol1/`.
- `pron/` — the pronunciation respellings per volume.
- `review/` — the subject-matter reviews behind the expansion plan.

The scripts expect this tree at the session's scratchpad path (`SP` in `build.py`); point `SP` here to rebuild elsewhere.
