# Volume XIV chapter spec (The Assay: precious metals, gems and elements) — "Many Eyes"

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
5. threads_out may point to Volume XIV chapter ids:
   potosi-1545, davy-1807, kohinoor-1849, california-1848, kimberley-1867, mendeleev-1869, witwatersrand-1886,
   argon-1894, klondike-1896, cullinan-1905
   or to Volume IX with "v9:" (tenochtitlan-1520, boston-1721, philadelphia-1793, balmis-1803, cholera-1832,
   broad-street-1854, scutari-1854, bombay-1896, influenza-1918, polio-1954), to Volume XIII with "v13:" (chappe-1794, morse-1844, cables-1858, telephone-1876, wireless-1901, titanic-1912,
   zimmermann-1917, midway-1942, arpanet-1969), Volume XV with "v15:" (clean-slates, dream-books, hildegard-1141,
   missing-days, diodati-1816, darwin-1837, hidden-christians-1865, waking-ideas, inflation-1923, jerusalem-1948,
   everett-1957, berlin-1961, gold-1971, private-books), or to earlier volumes with a prefix: "v1:" (heian, thirty-years, london-1666, french-rev, russia-1812,
   us-civil-war, ww1, russia-1917, nanjing-1937, ww2-europe, japan-1945, long-threads), "v2:" (merer,
   babylon-331, vesuvius-79, black-death, constantinople-1453, first-contact, imjin-war, ming-qing,
   vienna-1683, lisbon-1755, tambora-1816, opium-war, irish-famine, black-ships, delhi-1857, krakatoa-1883,
   spain-1936, moscow-1937, partition-1947, apollo-11, wall-1989), "v3:" (treasure-fleets, embassies-1403,
   narrow-road, endeavour, humboldt, corps-of-discovery, nile-source, livingstone-1871, fram, north-pole,
   south-pole, everest-1953), "v4:" (telescope-1609, transits-of-venus, edo-dissection, darwin-wallace,
   curies, fission, double-helix), "v5:" (florence-1504, jahangir-1615, grasmere, ninth-1824, impressionists-1874, exposition-1889,
   benin-1897, vienna-1900, gitanjali-1912, rite-1913, bauhaus, harlem, murals-1922, mei-lanfang-1935), "v6:" (worms-1521, fatehpur-sikri, philadelphia-1787, vienna-1815,
   seneca-falls, paris-1919, yalta, bandung), "v7:" (balloons-1783, steam-water, rainhill-1830, oceans-1869, the-road,
   kitty-hawk, channel-atlantic, airships, rockets, jet-age, shinkansen), "v8:" (supernova-1054, halley-1066,
   eclipse-1715, leonids-1833, carrington-1859, tunguska-1908, halley-1910, eclipse-1919)
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

VOLUME XIV ADDITIONS (The Assay: precious metals, gems and elements — the strike, the rush, the stone and the laboratory):
- Lay side by side the finders and the prospectors, the labourers who dug (Indigenous, enslaved, conscripted and
  migrant workers — Andean mita labourers, Chinese and Californio miners, African mineworkers), the owners and
  officials, the chemists and assayers, the rulers who lost or gained the treasure, and the press that spread the
  news. Workers and dispossessed peoples get eyes of their own wherever the record allows; when only others wrote
  about them, say so ("No surviving firsthand account found.").
- Add a top-level "claims" list — the ASSAY LEDGER (same field name as before):
  [{"date_iso": "", "date_display": "", "eye": "eye-id",
    "claim": "what was found, assayed, weighed, valued, claimed or announced (one line), with the figure where the
      record gives one (ounces, carats, atomic weight, price, number of workers)",
    "form": "notebook | letter | diary | assay | claim register | official report | paper | newspaper | treaty | other",
    "evidence": "where it is recorded", "confidence": "verified | approx"}]
  8–16 items, chronological. Priority disputes (who found it first, whose table came first) and ownership disputes
  (whose land, whose stone) are positions with evidence; no verdicts.
- Treat forced labour, dispossession, violence and deaths in the mines soberly and plainly, without euphemism and
  without graphic detail. Give the claims of the people whose land it was in their own records where they exist.
- Twentieth-century material first published after 1928: digests only, except world-famous phrases and
  US-government records (e.g. US Geological Survey, US Mint) quoted ≤12 words. Most of this volume is pre-1929 and
  quotable within the ≤12-word rule.
