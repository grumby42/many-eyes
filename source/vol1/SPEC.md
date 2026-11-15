# Research spec — "Many Eyes" diary book (one chapter per agent)

You are researching ONE chapter of an offline HTML "book" that sets real, authentic diaries / journals
side by side so a reader sees the SAME event through many eyes (different nations, sides, ranks,
genders, distances from the event). The reader wants as many distinct vantage points as the record
honestly supports (aim 8–14 eyes, minimum 6), and dated entries laid on a shared timeline so that
same-day and same-week entries line up.

## Absolute rules
1. AUTHENTIC ONLY. Every eye must be a real person whose diary/journal/notebook/log/dated letters
   actually exist. No fiction, no composites, no invented entries. If a source is a later memoir,
   a chronicle, or dated letters rather than a diary, still allowed but set `form` honestly
   ("diary", "journal", "notebook", "log", "dated letters", "chronicle", "memoir (written later)",
   "sketchbook (dated drawings)"). Flag disputed / revised / forged material in `authenticity`.
2. VERIFY dates with web searches (WebSearch / WebFetch). Use as many searches as you need (15–40 is
   normal). If you cannot pin an exact day, give the month or range and set confidence "approx".
   Never guess a precise date and present it as exact. Prefer fewer, solid entries over many shaky ones.
3. NO LONG QUOTATION. Write every entry as a paraphrase digest in your own words (2–5 sentences, vivid,
   concrete, specific: what they saw, did, felt, got wrong). You MAY add ONE short quote per entry
   (max 12 words) ONLY if the original was written in English and published before 1929, or is the
   diarist's own famous phrase widely quoted (e.g. a 1–6 word phrase). Never quote modern translations
   at length. Most entries should have no quote.
4. LINKS: only real URLs you actually saw in search results or fetched (no constructed or guessed URLs).
   Prefer free full texts (Project Gutenberg, Internet Archive, HathiTrust, Wikisource, national
   libraries, digitised archives) and Wikimedia Commons FILE pages for period images
   (paintings, engravings, photos, maps, dated sketches, manuscript pages). 3–8 images per chapter.
5. Calendar honesty: if Julian / Gregorian / lunisolar / Russian Old Style dates are involved, give the
   sortable ISO date in the Gregorian (New Style) calendar in `date_iso` (for pre-1582 use proleptic
   Julian as historians usually cite, and say so) and show the original-calendar date in `date_display`.

## Output — write ONE JSON file (UTF-8) to the path given in your task, exactly this shape:
```json
{
  "id": "chapter-id",
  "title": "Evocative chapter title",
  "subtitle": "Event, place, years",
  "span": "e.g. 1665–1666",
  "intro": ["3–6 paragraphs of your own prose setting the scene and explaining why these eyes matter together"],
  "calendar_note": "one paragraph or empty string",
  "eyes": [
    {
      "id": "short-slug",
      "name": "Full name",
      "life": "1633–1703",
      "role": "who they were at the time (age, job, rank, status)",
      "side": "nation / faction / community",
      "where": "where they stood during the event",
      "vantage": 0,
      "vantage_label": "e.g. 'inside the burning city', 'commander', 'victim', 'abroad, hearing news'",
      "form": "diary",
      "language": "original language",
      "authenticity": "short note: manuscript history, editions, any revisions / disputes",
      "bio": "2–4 sentences on the person and why their angle is distinctive",
      "sources": [{"title": "Edition / archive / text", "url": "real url or empty"}]
    }
  ],
  "entries": [
    {
      "date_iso": "1666-09-02",
      "date_display": "Sunday 2 September 1666 (O.S.)",
      "precision": "day | month | range | year",
      "eye": "eye-id",
      "place": "where written / where they were",
      "headline": "6–12 word headline",
      "digest": "2–5 sentence paraphrase in your own words",
      "quote": "optional ≤12-word quote under rule 3, else empty",
      "confidence": "verified | approx",
      "source_note": "which edition / entry / page or URL supported this"
    }
  ],
  "convergences": [
    {"date": "1666-09-02", "label": "what happened that day", "eyes": ["eye-a","eye-b"], "note": "how their views differ / clash / rhyme"}
  ],
  "ties": [
    {"a": "eye-id", "b": "eye-id", "kind": "met | mentioned | opposite sides | same street | relative | read each other | influenced", "note": "1–2 sentences"}
  ],
  "threads_out": [
    {"to": "other-chapter-id", "note": "a real historical link from this chapter to another chapter (people, places, consequences, ideas, technologies, institutions) — 1–3 sentences"}
  ],
  "images": [
    {"url": "real Wikimedia Commons file page or museum/library page", "title": "", "caption": "what it shows and why it matters", "date": "", "credit": "artist / photographer / holder"}
  ],
  "further": [{"title": "", "url": ""}],
  "vantage_key": "one sentence explaining what vantage 0..4 mean in this chapter"
}
```
Vantage scale: 0 = at the very centre / a principal actor or direct victim; 1 = on the scene,
eyewitness; 2 = same city / near the front; 3 = same country, at a distance; 4 = abroad / news only.

Aim for 25–45 entries spread across the eyes and the timeline, with deliberate clusters where 3+ eyes
write about the same day or week (these clusters are the heart of the book). Include a few quieter
"ordinary day" entries too — they make the drama legible.

Chapter ids in the book (use these in threads_out):
heian, thirty-years, london-1666, french-rev, russia-1812, us-civil-war, ww1, russia-1917,
nanjing-1937, ww2-europe, japan-1945, long-threads

When done, validate the JSON (python3 -c "import json;json.load(open(PATH))") and reply with a
3-line summary: number of eyes, number of entries, anything you could not verify.
