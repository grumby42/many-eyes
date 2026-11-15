# Volume VIII chapter spec (The Same Sky) — "Many Eyes"

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
5. threads_out may point to Volume VIII chapter ids:
   supernova-1054, halley-1066, eclipse-1715, leonids-1833, carrington-1859, tunguska-1908, halley-1910, eclipse-1919
   or to earlier volumes with a prefix: "v1:" (heian, thirty-years, london-1666, french-rev, russia-1812,
   us-civil-war, ww1, russia-1917, nanjing-1937, ww2-europe, japan-1945, long-threads), "v2:" (merer,
   babylon-331, vesuvius-79, black-death, constantinople-1453, first-contact, imjin-war, ming-qing,
   vienna-1683, lisbon-1755, tambora-1816, opium-war, irish-famine, black-ships, delhi-1857, krakatoa-1883,
   spain-1936, moscow-1937, partition-1947, apollo-11, wall-1989), "v3:" (treasure-fleets, embassies-1403,
   narrow-road, endeavour, humboldt, corps-of-discovery, nile-source, livingstone-1871, fram, north-pole,
   south-pole, everest-1953), "v4:" (telescope-1609, transits-of-venus, edo-dissection, darwin-wallace,
   curies, fission, double-helix), "v5:" (florence-1504, grasmere, ninth-1824, impressionists-1874,
   vienna-1900, rite-1913, bauhaus, harlem), "v6:" (worms-1521, fatehpur-sikri, philadelphia-1787, vienna-1815,
   seneca-falls, paris-1919, yalta, bandung), "v7:" (balloons-1783, steam-water, rainhill-1830, oceans-1869, the-road,
   kitty-hawk, channel-atlantic, airships, rockets, jet-age, shinkansen)
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

VOLUME VIII ADDITIONS (The Same Sky: one sky event, seen and dated on several continents):
- The heart of each chapter is the SAME NIGHT (or day) recorded by people far apart who did not know of each other:
  court astronomers, monks, farmers, sailors' logs, telegraph operators, newspapers, scientists, diarists. Convergences
  are the nights several of them recorded; lay them in order of longitude/local time where the record allows.
- Add a top-level "claims" list — the OBSERVING LEDGER (same field name as before):
  [{"date_iso": "", "date_display": "", "eye": "eye-id", "claim": "what was seen or measured, where, one line, with
    the figures the record gives (time, altitude, duration, magnitude, deflection, latitude of aurora)",
    "form": "seen | measured | predicted | recorded | reported | explained | disputed | other",
    "evidence": "where it is recorded", "confidence": "verified | approx"}]
  8–16 items, chronological. Rival interpretations (omen vs. phenomenon; competing explanations) as positions.
- Every eye's "where" and lat/lon must be the observing place; the map matters more here than anywhere else.
- Calendars: Chinese lunisolar, Japanese era dates, Islamic Hijri, Julian/Gregorian: give the original date in
  date_display and the converted proleptic date in date_iso, and explain conversions in calendar_note.
- Twentieth-century material (anything first published after 1928): copyright rules apply — digests only except
  world-famous phrases; US-government records may be quoted within the ≤12-word rule. Pre-1929 English originals
  (Halley 1715, Olmsted 1833, Carrington 1859, the 1910 press, Eddington's 1919–20 papers) may be quoted within the rule.
