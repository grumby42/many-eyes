# Volume III chapter spec (Exploration and Encounter) — "Many Eyes"

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
5. threads_out may point to Volume III chapter ids:
   treasure-fleets, embassies-1403, narrow-road, endeavour, humboldt, corps-of-discovery,
   livingstone-1871, nile-source, north-pole, south-pole, fram, everest-1953
   or to Volume I chapter ids with a "v1:" prefix:
   v1:heian, v1:thirty-years, v1:london-1666, v1:french-rev, v1:russia-1812, v1:us-civil-war, v1:ww1,
   v1:russia-1917, v1:nanjing-1937, v1:ww2-europe, v1:japan-1945, v1:long-threads
   or to Volume II chapter ids with a "v2:" prefix:
   v2:merer, v2:babylon-331, v2:vesuvius-79, v2:black-death, v2:constantinople-1453, v2:first-contact,
   v2:imjin-war, v2:ming-qing, v2:vienna-1683, v2:lisbon-1755, v2:tambora-1816, v2:opium-war,
   v2:irish-famine, v2:black-ships, v2:delhi-1857, v2:krakatoa-1883, v2:spain-1936, v2:moscow-1937,
   v2:partition-1947, v2:apollo-11, v2:wall-1989
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

VOLUME III ADDITIONS (exploration and encounter):
- The heart of each chapter is the ENCOUNTER: wherever possible pair the traveller's record with the hosts'
  record of the same meeting (court annals, Indigenous dated chronicles such as Lakota winter counts, local
  officials' reports, letters of the people met). Where the hosts' voice survives only in later oral
  tradition or through the travellers' own pages, say so plainly and flag the form — never invent balance,
  never dismiss it.
- Give every travelling eye a full route as "waypoints" (up to 6, chronological, each {lat, lon, label ≤22
  chars}) — maps are this volume's main extra feature.
- Use respectful, accurate names for peoples and places, with the explorers' period names in brackets
  where useful.
