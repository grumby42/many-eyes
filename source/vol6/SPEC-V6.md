# Volume VI chapter spec (Meetings of minds: The Room) — "Many Eyes"

Read and follow /tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/SPEC.md
(the Volume I rules: authentic only, verify dates, paraphrase digests in your own words, quotes ≤12 words
and only from English originals published before 1929 or famous phrases, real URLs only, form tags honest,
calendar honesty with date_iso as the sortable date). These additions and overrides apply:

1. SEARCH BUDGET: web searches are shared across many agents running at once. Use AT MOST the number of
   WebSearch calls in your task. Many sites are blocked (Wikimedia, archive.org, some national libraries):
   if a fetch fails, move on immediately; do not retry the same host.
2. ANCIENT / PRE-1582 DATES: date_iso uses the proleptic Julian calendar as historians cite it; for BC
   years use astronomical numbering with a leading minus (e.g. 331 BC = "-0330"; 2560 BC = "-2559") and put
   the conventional BC form in date_display. If only a year or reign-year is known, set precision "year".
3. Each eye MUST also carry "lat", "lon" (decimal degrees, where they mainly stood) and optional
   "waypoints": [{"lat":..,"lon":..,"label":".."}] (≤6, chronological) for eyes who travelled.
4. Each eye MUST carry "short": a display name of ≤16 characters (e.g. "Barbaro", "Yi Sun-sin").
5. threads_out may point to Volume VI chapter ids:
   worms-1521, fatehpur-sikri, philadelphia-1787, vienna-1815, seneca-falls, paris-1919, yalta, bandung
   or to earlier volumes with a prefix: "v1:" (heian, thirty-years, london-1666, french-rev, russia-1812,
   us-civil-war, ww1, russia-1917, nanjing-1937, ww2-europe, japan-1945, long-threads), "v2:" (merer,
   babylon-331, vesuvius-79, black-death, constantinople-1453, first-contact, imjin-war, ming-qing,
   vienna-1683, lisbon-1755, tambora-1816, opium-war, irish-famine, black-ships, delhi-1857, krakatoa-1883,
   spain-1936, moscow-1937, partition-1947, apollo-11, wall-1989), "v3:" (treasure-fleets, embassies-1403,
   narrow-road, endeavour, humboldt, corps-of-discovery, nile-source, livingstone-1871, fram, north-pole,
   south-pole, everest-1953), "v4:" (telescope-1609, transits-of-venus, edo-dissection, darwin-wallace,
   curies, fission, double-helix), "v5:" (florence-1504, grasmere, ninth-1824, impressionists-1874,
   vienna-1900, rite-1913, bauhaus, harlem)
   Real, specific links only (people, places, consequences, ideas, institutions, the epidemic/disaster threads).
6. Treat violence (sieges, sacks, massacres, invasions) with sobriety: what the diarists recorded, the scale,
   their reactions — no graphic detail.
7. Where the honest record is mostly letters, chronicles, logs or administrative documents rather than
   diaries, include them with correct form tags; say so plainly in the intro.

Also give the chapter a top-level "short_title" (≤34 chars) if the title is long.

Write the chapter JSON (same shape as SPEC.md) to the path in your task, validate it with
python3 -c "import json;json.load(open(PATH))", and reply with a 3-line summary: eyes, entries, what you
could not verify.

TWENTIETH-CENTURY ADDITIONS (spain-1936, moscow-1937, partition-1947, apollo-11, wall-1989):
- Copyright: these diaries are modern publications, so NO quotes except a handful of world-famous phrases
  (e.g. Armstrong's first words from the NASA transcript, which is US-government public domain). Digests only.
- Privacy: use only diarists whose diaries are published under their own names or who were public figures;
  for archive collections (Mass Observation, Tagebucharchiv, Prozhito) cite the published edition or the
  archive's own public excerpt, never identify private living people beyond what the publication states.
- Political evenhandedness: describe what each side recorded; add no verdicts of your own on contested questions.

VOLUME VI ADDITIONS (meetings of minds over critical issues):
- The heart of each chapter is the ROOM: a diet, a debate hall, a convention, a congress, a conference. Lay the
  official record (minutes, protocols, journals of proceedings) beside the private notes of people in the room,
  the dispatches sent out of it, the spies and police reports on it, and the people kept outside it (petitioners,
  the press, the excluded). The convergences are the sessions several eyes recorded.
- Add a top-level "claims" list — the DECISION LEDGER (same field name as before):
  [{"date_iso": "", "date_display": "", "eye": "eye-id", "claim": "what was proposed, debated, decided, voted,
    signed or refused, one line (e.g. 'Moves that the executive be a single person')",
    "form": "proposed | debated | voted | decided | signed | refused | petitioned | reported | other",
    "evidence": "where it is recorded", "confidence": "verified | approx"}]
  8–16 items, chronological. Record votes with their counts where the record gives them.
- Evenhandedness is essential: religious, political and national positions are reported as what each side said
  and did, with the evidence; no verdicts on who was right. Where the record is one-sided (one side's minutes,
  a hostile chronicler), say so in the eye's authenticity note.
- Interpreters, secretaries, daughters, doctors, servants and petitioners whose notes survive get eyes.
- Twentieth-century material (anything first published after 1928, including diaries published later):
  copyright rules apply — no quotes except world-famous phrases; digests only. Official US-government records
  (e.g. FRUS) may be quoted within the ≤12-word rule.
- Sobriety: executions, massacres and wars mentioned in passing are stated plainly, without graphic detail.
