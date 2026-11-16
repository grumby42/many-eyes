# Volume XVI chapter spec (Voices and Visions: djinn, spirits, angels and demons, and messages taken as from God that started movements, ended states, or raised or removed leaders) — "Many Eyes"

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
5. threads_out may point to Volume XVI chapter ids:
   constantine-312, joan-1429, loudun-1632, djinn-1640, sabbatai-1665, handsome-lake-1799, smith-1820, hong-1837,
   bab-1844, nongqawuse-1856, mahdi-1881, wovoka-1889, fatima-1917
   or to Volume XII with "v12:" (lancaster-1744, greenville-1795, dancing-rabbit-1830, batman-1835, waitangi-1840,
   fort-laramie-1851, medicine-lodge-1867, treaty-six-1876, berlin-1884, rudd-1888), or to Volume XI with "v11:" (galileo-1633, charles-1649, salem-1692, hastings-1788, caroline-1820, amistad-1839,
   john-brown-1859, dreyfus-1894, nuremberg-1945, tokyo-1946), or to Volume X with "v10:" (siam-1686, mehmed-1720, mai-1774, abutaleb-1799, tahtawi-1826, embassy-1860, iwakura-1871, naser-1873,
   guo-1877, vivekananda-1893)
   or to Volume XIV with "v14:" (potosi-1545, davy-1807, kohinoor-1849, california-1848, kimberley-1867,
   mendeleev-1869, witwatersrand-1886, argon-1894, klondike-1896, cullinan-1905), to Volume IX with "v9:" (tenochtitlan-1520, boston-1721, philadelphia-1793, balmis-1803, cholera-1832,
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

VOLUME XVI ADDITIONS (Voices and Visions):
- Each chapter follows one vision, voice, apparition, possession or prophecy that the people of the time took to come
  from beyond, and what it did in the world: a movement begun, a state ended, a leader raised or removed. Lay the
  visionary's own words (where they survive) beside believers, opponents, officials, physicians, missionaries,
  journalists and later investigators, on one timeline.
- NO VERDICT on whether anything supernatural happened, and every faith is treated the same way: Christian, Jewish,
  Muslim, Bábí, Haudenosaunee, Xhosa, Paiute, Latter-day Saint, Taiping, Catholic and folk belief alike. Report what
  each witness said they saw or heard, what believers concluded, what sceptics and authorities concluded, and the
  consequences, in the same neutral voice. Use each tradition's own respectful terms (e.g. "the Báb", "Prophet
  Joseph Smith" only inside believers' quotations; neutral names elsewhere). No mockery and no endorsement.
- Each entry carries "source_kind": one of "firsthand" (written or dictated by the witness at the time), "later
  firsthand" (the witness's own account written down later — give the gap), "secondhand" (someone reporting what
  the witness said or did), "official record" (court, church, state or mission record), or "legend" (a story first
  written long after, or of unknown origin). Many famous visions survive only in later or secondhand tellings
  (Constantine's sign; Joseph Smith's 1820 vision told in 1832, 1835, 1838 and 1842 accounts): set the versions side by
  side by date, as positions, and say which is earliest.
- Add a top-level "claims" list — the WITNESS LEDGER (same field name as before):
  [{"date_iso": "", "date_display": "", "eye": "eye-id",
    "claim": "what was seen, heard, foretold, believed, denied or done because of it (one line)",
    "form": "vision account | letter | diary | sermon | scripture | court record | church record | report | newspaper | oral history | other",
    "evidence": "where it is recorded", "confidence": "verified | approx"}]
  8–16 items, chronological, mixing believers, opponents and officials. Where an event happened long before it was
  written down, put the gap in the claim text (e.g. "seen in 312; first written c. 315").
- Prophecies that failed (Nongqawuse's appointed day; Sabbatai Zevi's year; the Ghost Dance) are reported as dated
  facts with what believers and others said afterwards, never with mockery. Deaths, famine and massacre (the
  cattle-killing famine, Wounded Knee, the Taiping war, Loudun's burning) are told soberly, with scale, no graphic detail.
- Mental-health language: do not diagnose historical people. If physicians or later scholars offered medical
  explanations, report them as their positions with dates.
- Quotes: scripture and religious texts, letters, trial records and books published before 1929 in English or in
  English translations published before 1929 are quotable (≤12 words). Modern translations and post-1928 material →
  digests only.
- Calendars: Julian for Constantine and Joan of Arc (as historians cite them); Hijri dates for the Báb, the Mahdi and
  Evliya Çelebi, and Chinese reign years for Hong Xiuquan, converted and explained in calendar_note; Hebrew dates for
  Sabbatai Zevi converted and explained.
