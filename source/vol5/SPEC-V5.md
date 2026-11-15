# Volume V chapter spec (The Arts: The Studio) — "Many Eyes"

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
5. threads_out may point to Volume V chapter ids:
   florence-1504, jahangir-1615, grasmere, ninth-1824, impressionists-1874, exposition-1889, benin-1897,
   vienna-1900, gitanjali-1912, rite-1913, bauhaus, harlem, murals-1922, mei-lanfang-1935
   (and "v6:", "v7:", "v8:" prefixes for later volumes; v8 ids: supernova-1054, halley-1066, eclipse-1715,
   leonids-1833, carrington-1859, tunguska-1908, halley-1910, eclipse-1919)
   or to earlier volumes with a prefix: "v1:" (heian, thirty-years, london-1666, french-rev, russia-1812,
   us-civil-war, ww1, russia-1917, nanjing-1937, ww2-europe, japan-1945, long-threads), "v2:" (merer,
   babylon-331, vesuvius-79, black-death, constantinople-1453, first-contact, imjin-war, ming-qing,
   vienna-1683, lisbon-1755, tambora-1816, opium-war, irish-famine, black-ships, delhi-1857, krakatoa-1883,
   spain-1936, moscow-1937, partition-1947, apollo-11, wall-1989), "v3:" (treasure-fleets, embassies-1403,
   narrow-road, endeavour, humboldt, corps-of-discovery, nile-source, livingstone-1871, fram, north-pole,
   south-pole, everest-1953), "v4:" (telescope-1609, transits-of-venus, edo-dissection, darwin-wallace,
   curies, fission, double-helix)
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

VOLUME V ADDITIONS (the arts):
- The heart of each chapter is the STUDIO and the ROOM: artists, writers, musicians, patrons, critics, friends,
  servants and audiences recording the same works being made, shown, performed and judged. The convergences are
  the days when several of them were in the same room (a premiere, an opening, a committee, a walk, a salon).
- Lay the making of the work beside its reception: the diary entry that became a poem, the conversation-book
  page from the rehearsal, the review the next morning, the letter home afterwards.
- Add a top-level "claims" list to the chapter JSON — the WORK LEDGER (the same field name as Volume IV's ledger):
  [{"date_iso": "", "date_display": "", "eye": "eye-id", "claim": "the work and what happened to it (one line,
    e.g. 'Begins the marble block that becomes David')",
    "form": "begun | completed | shown | performed | published | reviewed | commissioned | decided | other",
    "evidence": "where it is recorded", "confidence": "verified | approx"}]
  8–16 items, chronological. Contested judgements (who influenced whom, who wrote what, whether a riot was staged)
  are reported as positions with evidence, never as the book's verdict.
- Women, collaborators, copyists, servants, models and performers whose part is visible in the record
  (e.g. Dorothy Wordsworth, Berthe Morisot, Alma Schindler, Alice Dunbar-Nelson, the dancers of 1913) get their
  own eyes wherever the record allows.
- Forgeries and later inventions (Schindler's conversation-book entries, legends about premieres) must be flagged
  in the entry and the ledger, never presented as genuine.
- Twentieth-century material (anything first published after 1928, including diaries published later):
  copyright rules apply — no quotes except world-famous phrases; digests only.
- Works of art themselves: describe them; never reproduce poems, lyrics or texts beyond the quote rule.
