# Second-edition patch spec — "Many Eyes"

You are improving ONE existing chapter of an offline HTML book that lays real diaries side by side.
First read the rules in /tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/SPEC.md
(authentic only, verify dates, paraphrase digests in your own words, quotes ≤12 words and only from
pre-1929 English originals or famous phrases, real URLs only, New Style date_iso). Then read the chapter
file named in your task to see what already exists (eye ids, entries, their 0-based indices).

SEARCH BUDGET: web searches are shared across many agents. Use AT MOST the number of WebSearch calls
given in your task. WebFetch calls are not limited the same way but many sites are blocked (Wikimedia,
archive.org); move on quickly when a page fails.

DO NOT edit the chapter file. Write a PATCH file (path given in your task), exactly this JSON shape:
```json
{
  "chapter": "chapter-id",
  "add_eyes": [ { ...same fields as SPEC eyes..., "lat": 0.0, "lon": 0.0 } ],
  "add_entries": [ { ...same fields as SPEC entries... } ],
  "add_convergences": [ { "date": "", "label": "", "eyes": [], "note": "" } ],
  "add_ties": [ { "a": "", "b": "", "kind": "", "note": "" } ],
  "add_images": [ { "url": "", "title": "", "caption": "", "date": "", "credit": "" } ],
  "add_further": [ { "title": "", "url": "" } ],
  "add_claims": [ { ...same fields as the volume's ledger items... } ],
  "add_threads_out": [ { "to": "", "note": "" } ],
  "updates": [ { "where": "entry:<0-based index in the ORIGINAL file> | eye:<id> | convergence:<n>", "fix": { "field": "new value" }, "why": "what you verified" } ]
}
```
- New entries may reference new or existing eye ids. Existing-eye entries are welcome (e.g. a missing entry for an existing diarist).
- Use `updates` to upgrade `confidence` to "verified" ONLY when you actually confirmed the date and
  content, or to correct a wrong date / fact. Include the fields you change.
- Give every NEW eye approximate `lat`/`lon` (decimal degrees) of where they stood during the event.
- Validate with python3 -c "import json;json.load(open(PATH))" and reply with a 3-line summary.
