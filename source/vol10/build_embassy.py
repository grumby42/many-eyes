import json

OUT = "/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/vol10/ch-embassy-1860.json"

LOC_BLOG = "https://blogs.loc.gov/international-collections/2016/06/who-were-the-first-japanese-to-visit-washington/"
FESSLER = "https://library.oapen.org/bitstream/20.500.12657/41573/1/9780472901975.pdf"
AH = "https://www.americanheritage.com/ordeal-kanrin-maru"
NDL = "https://www.ndl.go.jp/nikki/column/01"
ENGELS = "https://engelsbergideas.com/notebook/when-the-samurai-came-to-america/"
CWS = "https://lup.nl/wp-content/uploads/intro-14.pdf"

ch = {
 "id": "embassy-1860",
 "title": "Two-Sworded Princes on Broadway: The First Japanese Embassy to the United States",
 "short_title": "The Japanese Embassy of 1860",
 "subtitle": "Kanrin Maru and USS Powhatan to San Francisco, Washington, Philadelphia and New York, and home by Africa and Java, February–November 1860",
 "span": "1860",
 "intro": [
  "In February 1860 the Tokugawa shogunate sent its first embassy to a Western country. Seventy-seven men under the envoy Shinmi Masaoki, the vice-envoy Muragaki Norimasa and the inspector (metsuke) Oguri Tadamasa sailed from Yokohama in the American steam frigate USS Powhatan, carrying the Japanese text of the 1858 Treaty of Amity and Commerce negotiated by Townsend Harris, to exchange ratifications in Washington. A Japanese-manned escort, the steam corvette Kanrin Maru under Kimura Yoshitake with Katsu Kaishū as captain, crossed separately to San Francisco with the castaway-turned-interpreter Nakahama Manjirō, a young retainer named Fukuzawa Yukichi, and an American naval officer, Lieutenant John Mercer Brooke, who had been shipwrecked in Japan and was going home.",
  "The embassy went by Honolulu, San Francisco and the Panama railway to Washington, landing at the Navy Yard on 14 May. President Buchanan received the envoys in the East Room on 17 May, ratifications were exchanged on 22 May, and the party then toured Baltimore, Philadelphia (where Oguri insisted on a whole-coin assay of Japanese and American gold at the Mint) and New York, where a procession up Broadway on 16 June drew enormous crowds and a poem from Walt Whitman. The envoys sailed home in USS Niagara on 30 June by the Cape Verde Islands, Luanda, Batavia and Hong Kong, reaching Edo in November: the first Japanese official party to go round the world.",
  "The gaze ran hard both ways. The Japanese diarists measured America against Confucian order and found it loud, egalitarian, oddly mixed in its sexes and careless of rank; Muragaki laughed at ballroom dancing, compared the Senate to a fish market, and privately thought samurai could beat these people, while also recording kindness, bouquets thrown from windows and a rooster in Honolulu that crowed just as cocks did at home. American newspapers read the visitors' faces, swords and manners with a physiognomist's eye, praised them as a 'wonderful people', worried that they might colonise, and turned a seventeen-year-old apprentice interpreter, Tateishi Onojirō, into 'Tommy', a celebrity of polkas and love letters. Lieutenant Brooke, aboard the Kanrin Maru, judged the Japanese crew harshly and Manjirō with near reverence.",
  "Most of the Japanese record is diaries kept on the voyage and copied out afterwards for circulation: Muragaki's (published in Japanese in 1918 and 1928; English translations 1920 and 1958), the Sendai retainer Tamamushi Sadayū's seven-volume 'Kōbei nichiroku' (unpublished until 1913), the navigational journal of the Kanrin Maru officer Akamatsu Noriyoshi, and the illustrated diary of Oguri's attendant Satō Tōshichi, a village headman, published only in 2001. Fukuzawa's vivid stories come from his autobiography dictated in 1897–99, nearly forty years on, and are marked as memoir. Brooke's journals stayed in his family until 1960. On the American side the record is newspapers, a lawyer's diary, a naval officer's wife's letters, a president's formal reply and a poem; there is no first-person account by Tommy himself here, only what others wrote about him.",
  "Both sides wrote within prejudices of their own. Muragaki's verse called the Americans barbarians; American papers that praised the Japanese 'fine heads' were the same press that, in San Francisco that very spring, described local Chinese residents as despised and overtaxed, and historians have since shown that African American papers used the embassy to argue against the racial ranking the white press applied. The entries below report these judgements as written, without endorsing any of them. The visit came months before secession: the Niagara reached Boston in April 1861 to find the Civil War begun, and Brooke went south to the Confederate navy."
 ],
 "calendar_note": "Japan in 1860 used the Tenpō lunisolar calendar. The year began as Ansei 7; on the 18th day of the 3rd month (8 April 1860) the era was renamed Man'en, so the embassy's crossing is dated Ansei 7 and its American weeks Man'en 1 (the embassy learned of the new era only later). Months in 1860 began on about 23 January (1st), 22 February (2nd), 22 March (3rd), 21 April (intercalary 3rd), 21 May (4th), 19 June (5th), 18 July (6th), 17 August (7th), 15 September (8th), 14 October (9th) and 13 November (10th); these were checked against fixed points (Kanrin Maru sailing 19th day of 1st month = 10 February; Akamatsu's log, 3rd day of 2nd month = 24 February; Sakuradamon assassination, 3rd day of 3rd month = 24 March). The Japanese travellers kept Japan's day-count across the Pacific, so after crossing the date line their dates run one day ahead of American local dates: the audience with Buchanan on Thursday 17 May in Washington is the 28th day of the intercalary 3rd month, which in Japan was 18 May. date_iso gives the local Gregorian date where the event happened; date_display gives the Japanese date where one applies. Some popular sources convert these dates inconsistently; where a Japanese-calendar date is not printed in an accessible source it is computed here and marked accordingly.",
 "eyes": [
  {"id": "muragaki", "short": "Muragaki", "name": "Muragaki Norimasa (Awaji-no-kami)", "life": "1813–1880",
   "role": "Vice-envoy (fukushi) of the embassy, aged 46; a shogunal official who had served as a commissioner for Hakodate and foreign affairs",
   "side": "Tokugawa shogunate", "where": "USS Powhatan; Honolulu; San Francisco; Washington (Willard's Hotel); Philadelphia; New York; USS Niagara home",
   "lat": 38.8968, "lon": -77.0322,
   "waypoints": [{"lat": 35.44, "lon": 139.64, "label": "Yokohama, sailed 13 Feb"}, {"lat": 21.31, "lon": -157.86, "label": "Honolulu, March"}, {"lat": 37.79, "lon": -122.40, "label": "San Francisco, 29 Mar"}, {"lat": 38.8968, "lon": -77.0322, "label": "Washington, 14 May"}, {"lat": 40.7246, "lon": -73.9973, "label": "New York, 16 June"}, {"lat": 35.62, "lon": 139.74, "label": "Edo, November"}],
   "vantage": 0, "vantage_label": "envoy, keeping the embassy's most personal diary",
   "form": "diary (travel journal kept on the voyage, with waka poems)", "language": "Japanese",
   "authenticity": "Known as 'Kōkai nikki' or 'Kenbeishi nikki'. Printed in Japanese in 1918 and in 'Kengai shisetsu nikki sanshū' 1 (1928). An English version by Shibama Chikakichi (1920) is flawed and drops the poems; Helen M. Uno's 1958 translation ('Kokai Nikki: The Diary of the First Japanese Embassy to the United States of America') is considered faithful. Read here through modern scholarship; digests only.",
   "bio": "A senior bakufu official of the old school, Muragaki wrote poems at every stage of the journey and judged America by the decorum and hierarchy he valued. His diary is unusually frank: by turns homesick, amused, contemptuous and, in places, moved.",
   "sources": [{"title": "Fessler, Musashino in Tuscany (2004), ch. 2 on Muragaki's diary (open access)", "url": FESSLER}, {"title": "Library of Congress, 'Who were the first Japanese to visit Washington?' (2016)", "url": LOC_BLOG}, {"title": "Harding, 'When the Samurai came to America' (Engelsberg Ideas)", "url": ENGELS}]},
  {"id": "tamamushi", "short": "Tamamushi", "name": "Tamamushi Sadayū", "life": "1823–1869",
   "role": "Retainer of the Sendai domain, aged 37, travelling as an attendant to the envoy Shinmi",
   "side": "Tokugawa embassy (Sendai domain)", "where": "USS Powhatan; Honolulu; San Francisco; Washington; Philadelphia; New York",
   "lat": 38.8968, "lon": -77.0322,
   "waypoints": [{"lat": 35.44, "lon": 139.64, "label": "Yokohama"}, {"lat": 21.31, "lon": -157.86, "label": "Honolulu"}, {"lat": 38.8968, "lon": -77.0322, "label": "Washington"}, {"lat": 40.7246, "lon": -73.9973, "label": "New York"}],
   "vantage": 1, "vantage_label": "junior attendant, a domain scholar watching closely",
   "form": "diary ('Kōbei nichiroku', copied in fair form after the return)", "language": "Japanese (with classical Chinese brush-talk)",
   "authenticity": "Seven-volume 'Kōbei nichiroku' (Daily record of the voyage to America) circulated in manuscript copies (one dated 1861 is digitised by the University of Michigan); first printed 1913. Content is summarised here from catalogue descriptions and scholarship.",
   "bio": "A Sendai scholar who had already travelled in Ezo, Tamamushi was alert to how Westerners treated others; in Honolulu he exchanged written Chinese with a Chinese pharmacist about the British war on China. In 1868–69 he helped organise the Northern Alliance against the new imperial government and was executed after its defeat.",
   "sources": [{"title": "ABAA listing: 'Kōbei nichiroku' manuscript, seven volumes", "url": "https://www.abaa.org/book/1609255786"}, {"title": "University of Michigan: manuscript copy of Kōbei Nichiroku, vol. 1 (1861)", "url": "https://quod.lib.umich.edu/j/japanese/japanese.0005.001?view=toc"}]},
  {"id": "fukuzawa", "short": "Fukuzawa", "name": "Fukuzawa Yukichi", "life": "1835–1901",
   "role": "Nakatsu-domain samurai and Dutch-learning teacher, aged 25, who volunteered as personal attendant to Kimura Yoshitake on the Kanrin Maru",
   "side": "Kanrin Maru (Japanese escort ship)", "where": "Kanrin Maru; San Francisco and Mare Island, March–May 1860; Honolulu; home to Uraga",
   "lat": 37.7946, "lon": -122.4,
   "waypoints": [{"lat": 35.24, "lon": 139.72, "label": "Uraga, sailed 10 Feb"}, {"lat": 37.7946, "lon": -122.4, "label": "San Francisco, 17 Mar"}, {"lat": 21.31, "lon": -157.86, "label": "Honolulu, May"}, {"lat": 35.24, "lon": 139.72, "label": "Uraga, June"}],
   "vantage": 1, "vantage_label": "young attendant on the escort ship, remembering decades later",
   "form": "memoir (written later: autobiography dictated 1897–98, published 1899)", "language": "Japanese",
   "authenticity": "'Fukuō jiden' was dictated near the end of his life and is a polished, often comic retelling; dates are rarely given. English translation by Kiyooka Eiichi (1934). Treated here as memoir, not a contemporaneous record.",
   "bio": "Later the most influential popular educator of Meiji Japan and founder of Keiō, Fukuzawa first met the West in San Francisco. His recollections of carpets, dancing, a photograph and a question about George Washington's descendants became the classic Japanese image of that first contact.",
   "sources": [{"title": "Keio University, 'Around Yukichi Fukuzawa' (Kanrin Maru in Hawaii)", "url": "https://www.keio.ac.jp/en/about/public-relations/mita-hyoron/around-yukichi-fukuzawa/201712-1"}, {"title": "Harding, 'When the Samurai came to America'", "url": ENGELS}]},
  {"id": "akamatsu", "short": "Akamatsu", "name": "Akamatsu Noriyoshi (Daizaburō)", "life": "1841–1920",
   "role": "Naval trainee and officer on the Kanrin Maru, aged 19, a graduate of the Nagasaki naval training school",
   "side": "Kanrin Maru (Japanese escort ship)", "where": "Kanrin Maru, North Pacific; San Francisco",
   "lat": 37.7946, "lon": -122.4,
   "waypoints": [{"lat": 35.24, "lon": 139.72, "label": "Uraga"}, {"lat": 40.0, "lon": 175.0, "label": "North Pacific (approx.)"}, {"lat": 37.7946, "lon": -122.4, "label": "San Francisco"}],
   "vantage": 1, "vantage_label": "junior officer keeping the ship's working log",
   "form": "log (navigational diary)", "language": "Japanese, with Japanized Dutch nautical terms",
   "authenticity": "'Amerika-yuki kōkai nikki' survives in the Akamatsu Noriyoshi Papers at the National Diet Library (item 26) and is printed in 'Man'en gannen kenbei shisetsu shiryō shūsei' vol. 4 (1961).",
   "bio": "Akamatsu later studied in the Netherlands and became a vice-admiral in the Meiji navy. His 1860 log is a working record, not a reflective one, which is why it is valuable: it shows the Japanese side of the watch-keeping problems Brooke complained about.",
   "sources": [{"title": "National Diet Library, 'The world of diaries' column 1 (Akamatsu and Brooke)", "url": NDL}]},
  {"id": "brooke", "short": "Brooke", "name": "John Mercer Brooke", "life": "1826–1906",
   "role": "Lieutenant, US Navy, aged 33; surveyor whose schooner Fenimore Cooper had been wrecked near Yokohama in 1859; adviser and passenger on the Kanrin Maru",
   "side": "United States Navy", "where": "Kanrin Maru, Uraga to San Francisco, February–March 1860",
   "lat": 37.7946, "lon": -122.4,
   "waypoints": [{"lat": 35.24, "lon": 139.72, "label": "Uraga, 10 Feb"}, {"lat": 40.0, "lon": 175.0, "label": "North Pacific storms (approx.)"}, {"lat": 37.7946, "lon": -122.4, "label": "San Francisco, 17 Mar"}],
   "vantage": 1, "vantage_label": "American officer aboard the Japanese ship",
   "form": "journal", "language": "English",
   "authenticity": "Private day-to-day journals kept by his family; first published in 1961 (with Japanese translation) as vol. 5 of 'Man'en gannen kenbei shisetsu shiryō shūsei', and in English in George M. Brooke Jr's edition 'John M. Brooke's Pacific Cruise and Japanese Adventure, 1858–1860' (1986). Not quoted here because first published after 1928.",
   "bio": "Brooke had been stranded in Japan and accepted passage on the Kanrin Maru as an adviser. His journal is the sharpest outside view of the crossing: impatient with the crew and officers, admiring of Manjirō. In 1861 he joined the Confederate navy and worked on the armour and guns of the ironclad CSS Virginia.",
   "sources": [{"title": "Warinner, 'The Ordeal of the Kanrin Maru', American Heritage 14:5 (1963)", "url": AH}, {"title": "National Diet Library diary column (Brooke's Kanrin Maru journal)", "url": NDL}]},
  {"id": "alta", "short": "Daily Alta", "name": "Daily Alta California (newspaper)", "life": "1849–1891",
   "role": "San Francisco's leading daily", "side": "United States (California press)", "where": "San Francisco",
   "lat": 37.7946, "lon": -122.4, "vantage": 2, "vantage_label": "harbour-front newspaper",
   "form": "newspaper", "language": "English",
   "authenticity": "Digitised in the California Digital Newspaper Collection; the arrival report is quoted in modern accounts.",
   "bio": "The Alta reported the first Japanese warship to enter San Francisco Bay, with the names of ship and captain rendered as best its reporters could manage.",
   "sources": [{"title": "'The Samurai, the Ship, and the Golden Gate' (quotes the Alta of 18 March 1860)", "url": "https://www.samurai-revolution.com/?p=6019"}]},
  {"id": "dispatch", "short": "Rich. Dispatch", "name": "Richmond Daily Dispatch (newspaper)", "life": "1850–1884",
   "role": "Daily newspaper of Richmond, Virginia", "side": "United States (Southern press, slave state)", "where": "Richmond, Virginia",
   "lat": 37.5407, "lon": -77.436, "vantage": 3, "vantage_label": "Southern paper following the visit at a distance",
   "form": "newspaper", "language": "English",
   "authenticity": "Digitised (University of Richmond); items cited in Natalia Doan's 'Civil War Samurai' introduction.",
   "bio": "A Richmond paper read the embassy through its own racial vocabulary, praising the visitors' heads and bearing, and later followed Tommy's flirtations as he 'went north'.",
   "sources": [{"title": "Doan, Civil War Samurai, introduction (press citations)", "url": CWS}]},
  {"id": "buchanan", "short": "Buchanan", "name": "James Buchanan", "life": "1791–1868",
   "role": "Fifteenth President of the United States, aged 69", "side": "United States government", "where": "The White House, Washington",
   "lat": 38.8977, "lon": -77.0365, "vantage": 0, "vantage_label": "host head of state",
   "form": "speech (formal reply at the audience, printed in the press)", "language": "English",
   "authenticity": "His reply to the envoys on 17 May 1860 was printed in contemporary newspapers and is cited by the US Diplomacy Center; the wording used here is from a secondary quotation.",
   "bio": "A lame-duck president months before secession, Buchanan staged the audience in the East Room before his cabinet and a crowd of onlookers, and sent a gold watch with his portrait to the shogun.",
   "sources": [{"title": "Ghosts of DC, 'First Japanese Embassy in America'", "url": "https://ghostsofdc.org/2012/07/03/japanese-embassy-1860/"}, {"title": "National Museum of American Diplomacy: 1860 Japanese Embassy medal", "url": "https://diplomacy.state.gov/items/1860-japanese-embassy-medal"}]},
  {"id": "sophie", "short": "Sophie Du Pont", "name": "Sophie Madeleine du Pont", "life": "1810–1888",
   "role": "Wife of Captain Samuel Francis Du Pont, one of the three naval officers commissioned to escort the embassy", "side": "United States (naval family, Delaware)", "where": "Louviers, near Wilmington, Delaware",
   "lat": 39.776, "lon": -75.583, "vantage": 3, "vantage_label": "at home, hearing the gossip through her husband's role",
   "form": "dated letters", "language": "English",
   "authenticity": "Manuscript letters in the Du Pont family papers (Hagley Museum and Library); cited in Doan's 'Civil War Samurai'. Not quoted.",
   "bio": "Sophie Du Pont, a lively and devout letter-writer, sat at the edge of the embassy's fame: her husband ran its American escort, and the curious wrote to the family in hope of access to the visitors.",
   "sources": [{"title": "Doan, Civil War Samurai, introduction (Du Pont letters)", "url": CWS}]},
  {"id": "dubois", "short": "P. Du Bois", "name": "Patterson Du Bois", "life": "1847–1917",
   "role": "Philadelphia writer, later author of the fullest account of the Mint's dealings with the embassy", "side": "United States (Philadelphia)", "where": "Philadelphia",
   "lat": 39.9515, "lon": -75.1636, "vantage": 2, "vantage_label": "Mint-side account, written fifty years later",
   "form": "memoir (written later: paper read to the American Philosophical Society, 1910)", "language": "English",
   "authenticity": "'The Great Japanese Embassy of 1860', Proceedings of the American Philosophical Society 49 (1910), 243–266, drawing on Mint records. Whether he witnessed the assay himself is not established here.",
   "bio": "Du Bois's paper preserves the technical side of the visit: the inspector Oguri's demand for a whole-coin assay to fix the true gold value of the Japanese koban against the American dollar, the issue behind Japan's ruinous gold drain.",
   "sources": [{"title": "Du Bois, 'The Great Japanese Embassy of 1860' (1910), BioStor record", "url": "https://biostor.org/reference/203957"}, {"title": "DVIDS, 'Japanese envoy's first visit to U.S. Mint in 1860'", "url": "https://www.dvidshub.net/news/printable/440992"}]},
  {"id": "nyt", "short": "NY Times", "name": "The New York Times (newspaper)", "life": "1851–",
   "role": "New York daily under Henry J. Raymond", "side": "United States (Northern press)", "where": "Park Row, New York",
   "lat": 40.7115, "lon": -74.0063, "vantage": 2, "vantage_label": "metropolitan daily covering the visit day by day",
   "form": "newspaper", "language": "English",
   "authenticity": "Items cited by Stambler (2011) and Doan (2019/2022) from the Times archive.",
   "bio": "The Times followed the embassy from Philadelphia to New York, mixing admiration, rumour and anxiety, and in June printed Whitman's poem on the Broadway procession.",
   "sources": [{"title": "Stambler, 'Ambassadors of Exchange', Education About Asia (2011)", "url": "https://www.asianstudies.org/wp-content/uploads/ambassadors-of-exchange-the-1860-japanese-mission-to-the-us.pdf"}, {"title": "Doan, Civil War Samurai, introduction", "url": CWS}]},
  {"id": "whitman", "short": "Whitman", "name": "Walt Whitman", "life": "1819–1892",
   "role": "Poet and journalist, aged 41, living in Brooklyn and writing for the press", "side": "United States (New York)", "where": "Broadway, Manhattan",
   "lat": 40.7246, "lon": -73.9973, "vantage": 1, "vantage_label": "poet in the Broadway crowd",
   "form": "poem (dated in its title, published in a newspaper)", "language": "English",
   "authenticity": "Published as 'The Errand-Bearers. 16th 6th Month, Year 84 of the States' in the New York Times, 27 June 1860; revised as 'A Broadway Pageant' in Drum-Taps (1865) and Leaves of Grass. Public domain.",
   "bio": "Whitman turned the procession into a vision of Asia arriving at Manhattan, the world's peoples converging on his city. His poem is the most famous American text of the visit and also a period example of how the visitors' skin and swords were made into emblems.",
   "sources": [{"title": "Walt Whitman Archive, 'The Errand-Bearers' (1860)", "url": "https://whitmanarchive.org/item/per.00154"}, {"title": "Pfaff's archive: The Errand-Bearers, New York Times 27 June 1860", "url": "https://pfaffs.web.lehigh.edu/node/60074"}]},
  {"id": "harpers", "short": "Harper's Weekly", "name": "Harper's Weekly (illustrated newspaper)", "life": "1857–1916",
   "role": "New York illustrated weekly", "side": "United States (Northern press)", "where": "Franklin Square, New York",
   "lat": 40.7095, "lon": -74.0005, "vantage": 2, "vantage_label": "picture paper making the visitors visible",
   "form": "newspaper", "language": "English",
   "authenticity": "Original issues survive and are sold and digitised; content cited from an issue description.",
   "bio": "Harper's, like its rival Frank Leslie's, put engravings of the envoys before a national readership, and gave Tommy a column of his own.",
   "sources": [{"title": "Harper's Weekly, 23 June 1860 (issue description)", "url": "https://www.rarenewspapers.com/view/172374"}]},
  {"id": "strong", "short": "G. T. Strong", "name": "George Templeton Strong", "life": "1820–1875",
   "role": "New York lawyer and vestryman of Trinity Church, aged 40", "side": "United States (New York)", "where": "Gramercy Park and lower Manhattan",
   "lat": 40.7368, "lon": -73.9845, "vantage": 2, "vantage_label": "sceptical New York diarist",
   "form": "diary", "language": "English",
   "authenticity": "Manuscript diary at the New-York Historical Society; edited by Allan Nevins and Milton Halsey Thomas (4 vols, 1952). Not quoted, as first published after 1928.",
   "bio": "Strong's diary is the great private chronicle of mid-century New York. He was cool toward the public fuss over the embassy but impressed by what its junior members chose to buy.",
   "sources": [{"title": "Diary of George Templeton Strong, vol. 3, p. 36 (entry of 23 June 1860), excerpted", "url": "https://civilwarnotebook.blogspot.com/2026/04/diary-of-george-templeton-strong-june.html?m=1"}]}
 ],
 "entries": [],
 "claims": [],
 "convergences": [],
 "ties": [],
 "threads_out": [],
 "images": [],
 "further": [],
 "vantage_key": "0 = the envoys and the president who received them; 1 = on the ships or in the street with them; 2 = the host cities' press and diarists; 3 = following the visit from elsewhere in the country; 4 = abroad."
}

E = ch["entries"]
def e(date_iso, date_display, precision, eye, place, headline, digest, quote, confidence, source_note):
    E.append(dict(date_iso=date_iso, date_display=date_display, precision=precision, eye=eye, place=place,
                  headline=headline, digest=digest, quote=quote, confidence=confidence, source_note=source_note))

e("1860-02-13", "Ansei 7, 1st month, days 18–22 (9–13 February 1860)", "range", "muragaki", "Edo and Yokohama, boarding USS Powhatan",
  "Leaving Edo with poems and a brave face",
  "Muragaki opens his diary by setting down the embassy's rank and purpose and describing the American warship that would carry it. He copies in the poems exchanged at his farewell party and admits the leave-taking was heavy: had he not put on a show of courage, he writes, his children would have been in despair. The Powhatan sailed from Yokohama on 13 February.",
  "", "approx", "Fessler, Musashino in Tuscany, ch. 2 (summary of the opening of Muragaki's diary); departure date 13 Feb from Fessler and LOC. Exact day of the farewell entry not established.")
e("1860-02-10", "Friday 10 February 1860 (Ansei 7, 1st month, 19th day)", "day", "brooke", "Kanrin Maru, leaving Uraga",
  "An American passenger on a Japanese warship",
  "Brooke and a handful of his wrecked crew sailed from Uraga in the Kanrin Maru, the shogunate's Dutch-built steam corvette, crewed by about ninety-six Japanese under Kimura Yoshitake and Katsu Kaishū. His journal of the crossing runs from this day to 16 March. He was aboard as an adviser and a guest, a delicate position on a ship whose officers meant the voyage to prove they could cross the Pacific themselves.",
  "", "verified", "NDL diary column (Brooke journal covers 10 Feb–16 Mar 1860); departure date 19th day of 1st month per Wikipedia and Samurai Archives.")
e("1860-02-14", "Tuesday 14 February 1860", "day", "brooke", "Kanrin Maru, off the Japanese coast",
  "No stations, no watches",
  "Four days out, Brooke records that the crew has no assigned stations and that watches have not been properly set. He notes the disorder on deck, with too few men on each watch, and resolves to press the commander for regular arrangements before matters get worse.",
  "", "verified", "NDL column cites Brooke's journal for 14 February 1860; Warinner (American Heritage 1963) on the two-man watches.")
e("1860-02-20", "Monday 20 February 1860", "day", "brooke", "Kanrin Maru, North Pacific",
  "Blaming the commodore for the ship's state",
  "Brooke writes that Kimura, the commodore, has failed to organise stations and watches, and that he means to push for improvement while he is still aboard. Storms had already sent Katsu and Kimura to their bunks with seasickness, and Brooke found himself handling the ship. His judgement of the sailors as incompetent, and of Japanese habits as unsuited to naval discipline, is blunt and one-sided.",
  "", "verified", "NDL column (entry of 20 Feb 1860); Warinner, 'The Ordeal of the Kanrin Maru' for seasickness and Brooke's verdicts.")
e("1860-02-24", "Friday 24 February 1860 (Ansei 7, 2nd month, 3rd day)", "day", "akamatsu", "Kanrin Maru, North Pacific",
  "A working log in Dutch-flavoured sea terms",
  "Akamatsu's entry is a plain navigational record, with courses and sail handling set down partly in Japanized Dutch terms learned at the Nagasaki training school. It also shows, read beside Brooke, that regular watch duties had been assigned only the day before, the fourteenth day of the voyage. The Japanese log confirms the problem the American was complaining of, without his tone.",
  "", "verified", "National Diet Library column 'Nikki no sekai' 1: Akamatsu, 'Amerika-yuki kōkai nikki' 1, entry for the 3rd day of the 2nd month = 24 Feb 1860.")
e("1860-03-01", "Thursday 1 March 1860", "day", "brooke", "Kanrin Maru, North Pacific",
  "Brooke threatens to stop working the ship",
  "After a botched attempt to tack in heavy weather, Brooke sent his own men below and told the captain he would no longer work the ship unless the Japanese officers did their part. The captain lectured his officers and put them under Brooke's orders. Earlier, Manjirō had reported that sailors threatened to hang him from the yardarm for ordering them aloft; Brooke wrote that he would hang mutineers if authorised.",
  "", "verified", "Warinner, American Heritage (1963), giving Brooke's journal for 1 March 1860.")
e("1860-03-07", "c. 7–8 March 1860 (Ansei 7, 2nd month, mid-month)", "range", "muragaki", "Honolulu",
  "Mirrors, fruit, and a familiar rooster",
  "In Honolulu, where the Powhatan put in after storm damage, Muragaki describes a public hall full of mirrors and flowers and the island fruit. The envoys were received by King Kamehameha IV and Queen Emma. Little else pleased him, but a cock crowing at dawn sounded exactly like the one in his home village, and he wrote a poem on the thought that the bird's song is the same in the East.",
  "", "approx", "Fessler, Musashino in Tuscany, ch. 2 (dates the Hawaii passage 7–8 March); Samurai Archives and Wikipedia for the royal audience.")
e("1860-03-10", "March 1860", "month", "tamamushi", "Honolulu",
  "Brush-talk with a Chinese pharmacist",
  "In Honolulu Tamamushi met a Chinese pharmacist and, with no spoken language in common, the two conversed by writing classical Chinese. They talked about the Arrow War, Britain and France's campaign against Qing China, and both criticised the conduct of the Western powers. It is a reminder that the embassy's first conversations abroad were not only with Americans.",
  "", "approx", "ABAA catalogue description of Tamamushi's 'Kōbei nichiroku'. Day not established.")
e("1860-03-15", "February–March 1860", "range", "tamamushi", "USS Powhatan, Pacific crossing",
  "Watching how American officers treat their men",
  "On the Powhatan Tamamushi watched how the ship's officers dealt with their sailors and recorded, with some surprise, the closeness between ranks, including the grief shown when a seaman died. Coming from a world of strict status, he read this as something worth noting about American cohesion rather than as mere disorder.",
  "", "approx", "Widely cited theme of 'Kōbei nichiroku' in scholarship on the embassy; the specific entry and date were not confirmed from an accessible text.")
e("1860-03-17", "Saturday 17 March 1860 (Ansei 7, 2nd month, 26th day by Japan's count)", "day", "brooke", "San Francisco Bay",
  "Thirty-seven days to the Golden Gate",
  "The Kanrin Maru anchored in San Francisco after thirty-seven days at sea, the first Japanese warship to enter the bay. Brooke's account of the passage singles out Manjirō, the former castaway who had grown up in Massachusetts, as one of the most remarkable men he had met, a man who had translated Bowditch's navigator and had done more than anyone to open Japan.",
  "", "verified", "Warinner, American Heritage (1963), from Brooke's journal and official letter; arrival date confirmed by the Daily Alta California, 18 March 1860.")
e("1860-03-17", "Saturday 17 March 1860", "day", "fukuzawa", "San Francisco Bay",
  "Answering the salute gun for gun",
  "Fukuzawa later recalled the argument on deck when the American shore fired a salute: some officers doubted the ship's gunners could answer it properly, but the senior officer insisted that if Americans saluted Japan, Japan must return the honour. The guns were fired and timed with an hourglass, and the reply went off correctly. He told the story as an early point of national pride.",
  "", "approx", "Fukuō jiden (1899), as summarised in 'The Samurai, the Ship, and the Golden Gate'. Memoir written nearly forty years later.")
e("1860-03-18", "Sunday 18 March 1860", "day", "alta", "San Francisco",
  "The 'Candinmarru' arrives off Vallejo Street",
  "The Alta announced that the Japanese steamer had arrived the previous afternoon and anchored off the Vallejo Street wharf. Its reporters, with no standard romanisation to hand, rendered the ship as the 'Candinmarru' and Katsu as 'Kat-sin-tarroh'. The city was soon competing to entertain the visitors.",
  "anchored off Vallejo street wharf, at three o'clock P.M.", "verified", "Daily Alta California, 18 March 1860, quoted in 'The Samurai, the Ship, and the Golden Gate'.")
e("1860-03-23", "Ansei 7, 3rd month, 3rd day (24 March in Japan; 23 March by the ship's local reckoning)", "day", "muragaki", "USS Powhatan, five days out of Honolulu",
  "Gulls at sea on the Doll Festival",
  "Five days after leaving Honolulu Muragaki saw gulls and thought of home, where this was the day of the Doll Festival. He wrote a homesick poem, and the envoy Shinmi answered with one of his own, which Muragaki says consoled him. On that same day in Edo, unknown to anyone aboard, the great councillor Ii Naosuke, the man behind the treaty they carried, was assassinated outside the Sakurada Gate.",
  "", "approx", "Fessler, Musashino in Tuscany, ch. 2 (third day of third month). Gregorian equivalent computed; the Sakuradamon incident is dated 24 March 1860.")
e("1860-03-29", "Late March–April 1860 (from 29 March)", "range", "muragaki", "San Francisco",
  "Butter rice, sugared rice and dancing like mice",
  "In San Francisco Muragaki complained that the rice was cooked in butter or mixed with sugar, a hardship he said no brush could describe. At a reception he watched couples dancing and likened them to mice frolicking, while the women's skirts seemed to swell to enormous size; he did not hide his laughter. The embassy soon obtained permission to cook its own food.",
  "", "approx", "Harding, 'When the Samurai came to America' (Engelsberg Ideas), paraphrasing Muragaki; arrival date 29 March from Fessler and Wikipedia. Exact days not established.")
e("1860-03-25", "March–April 1860", "range", "fukuzawa", "San Francisco",
  "Carpets walked on in shoes",
  "Fukuzawa remembered his astonishment at hotel rooms laid wall to wall with carpet of a kind Japanese would cut into purses and tobacco pouches, which Americans walked over in their street shoes. At dinners he watched men and women hopping about the room together and had to stifle his laughter. He admitted that ordinary American things puzzled the visitors more than machinery, which they had read about.",
  "", "approx", "Fukuō jiden (1899); Harding (Engelsberg Ideas) on the dancing. Memoir; no exact date.")
e("1860-04-10", "Spring 1860", "range", "fukuzawa", "San Francisco",
  "Nobody knows what became of Washington's descendants",
  "Fukuzawa asked his hosts what had become of George Washington's descendants and was struck that no one seemed to know or care. To a man raised under a hereditary shogunate, the founder's family should have been a ruling house; in a republic it was a matter of indifference. He later used the moment to explain how unfamiliar the idea of elected office was.",
  "", "approx", "Fukuō jiden (1899); Beasley, Japan Encounters the Barbarian (1995) p. 61, as cited in Unseen Japan and Engelsberg Ideas. Some retellings misplace it in Washington, where Fukuzawa never went in 1860.")
e("1860-05-01", "April–May 1860", "range", "fukuzawa", "San Francisco",
  "A Webster's dictionary and a photograph",
  "Before the Kanrin Maru left, Fukuzawa bought a copy of Webster's dictionary, which he would use to begin serious English study. He also had himself photographed with the photographer's teenage daughter, Theodora Alice Shaw, and later delighted in showing the picture to his shipmates, who had no idea he had managed it.",
  "", "approx", "Unseen Japan and Wikipedia summaries; Fukuō jiden. Date within the San Francisco stay not established.")
e("1860-05-08", "Early May 1860", "range", "brooke", "San Francisco and Mare Island",
  "The Kanrin Maru repaired and sent home without him",
  "Storm-damaged on the crossing, the Kanrin Maru was refitted at the navy yard on Mare Island and then sailed back toward Japan by way of Honolulu, without going on to Washington. Brooke's part was over; his official praise of Manjirō as a Japanese of singular ability went into his report.",
  "", "approx", "Wikipedia and Warinner on repairs and return; Keio University for the Honolulu arrival on 23 May. Departure day not confirmed here.")
e("1860-04-17", "Tuesday 17 April 1860", "day", "dispatch", "Richmond, Virginia",
  "Reading character in the visitors' faces",
  "The Dispatch, reporting the embassy's progress, admired the Japanese for their heads, intelligent faces and dignified carriage. The praise used the period's physiognomic language of racial ranking, placing the visitors well above the peoples Americans habitually disparaged, and the paper went on calling them 'distinguished strangers' in May.",
  "fine heads, intellectual countenances and dignified bearing", "verified", "Richmond Daily Dispatch, 17 April 1860, cited in Doan, Civil War Samurai, introduction.")
e("1860-05-01", "Late April–12 May 1860", "range", "muragaki", "USS Roanoke, Aspinwall to Hampton Roads",
  "An officer still boasting about Perry",
  "Crossing Panama by railway, the embassy boarded the frigate Roanoke for the Atlantic leg. Muragaki found the ship clean but inconvenient, and was unimpressed by an officer who kept bragging of his part in Perry's expedition to Japan; he suggested drily that this explained why the man was still only a captain.",
  "", "approx", "Gowen, 'The First Japanese Mission to America' (Washington Historical Quarterly, c. 1924), paraphrasing Muragaki. Day not established.")
e("1860-05-14", "Monday 14 May 1860 (Man'en 1, intercalary 3rd month, 25th day by Japan's count)", "day", "muragaki", "Washington Navy Yard and Willard's Hotel",
  "Landing in Washington before thousands",
  "The embassy came up the Potomac by steamer and landed at the Navy Yard, then rode in procession to Willard's Hotel past crowds packed on pavements, in trees and at windows. In his diary Muragaki wrote that the samurai had to hold themselves in check to preserve their dignity as representatives of their country, whatever they felt at the spectacle.",
  "", "approx", "Landing date verified (Library of Congress blog; Ghosts of DC, citing the Baltimore Sun on the crowds). Muragaki's remark on restraint from Samurai Archives, not tied there to a specific day.")
e("1860-05-17", "Thursday 17 May 1860 (Man'en 1, intercalary 3rd month, 28th day by Japan's count)", "day", "muragaki", "East Room, the White House",
  "A silver-haired president without ceremony",
  "The envoys, in full court robes, delivered the shogun's letter to Buchanan before his cabinet and a crowd that included many women, some standing on chairs to see. Muragaki found the president silver-haired and genial yet dignified, but the absence of any formal ceremony, the plain black clothes and the mixed crowd struck him as strange. He marked the day with a waka asking even the 'barbarians' to look up at the light of Japan, the land of the rising sun.",
  "", "approx", "Audience date verified (White House Historical Association; House Divided; Frank Leslie's 2 June 1860). Muragaki's description via White House Historical Association as quoted in Ghosts of DC; the waka is widely attributed to this day but was not checked in an accessible edition.")
e("1860-05-17", "Thursday 17 May 1860", "day", "buchanan", "East Room, the White House",
  "A president's welcome before secession",
  "Replying to the envoys' address, Buchanan welcomed the first embassy Japan had sent to any Western nation and said he trusted the treaty would be the forerunner of lasting friendship between the two countries. A gold watch with his likeness was later sent to the shogun, and Secretary of State Cass gave commemorative medals to the embassy's members.",
  "perpetual peace and friendship between the two countries", "approx", "Buchanan's reply as quoted by the US Diplomacy Center via Ghosts of DC; wording not checked against a contemporary printing. Medals: National Museum of American Diplomacy.")
e("1860-05-17", "Thursday 17 May 1860", "day", "sophie", "Louviers, Delaware",
  "A dentist who wanted to see Japanese teeth",
  "Writing to her husband, who was escorting the embassy, Sophie Du Pont joked that a dentist had sent the family strawberries in the hope of being allowed to inspect the Japanese visitors' teeth. The anecdote catches the mixture of hospitality and specimen-hunting curiosity that followed the envoys everywhere.",
  "", "verified", "Sophie Madeleine Du Pont to Samuel Francis Du Pont, 17 May 1860 (Hagley), cited in Doan, Civil War Samurai, introduction.")
e("1860-05-22", "Tuesday 22 May 1860 (Man'en 1, 4th month, 3rd day by Japan's count)", "day", "muragaki", "Department of State, Washington",
  "Ratifications exchanged",
  "Six days after a first reception by Secretary of State Lewis Cass, the envoys formally exchanged the ratified copies of the 1858 treaty at the State Department, completing the embassy's official purpose. Buchanan and others urged them to tour the country at length; the envoys preferred to finish quickly and report home.",
  "", "approx", "Exchange date as given in treaty records and standard accounts; Cass reception on 16 May from House Divided (Vincent's Register, 1860). Japanese date computed.")
e("1860-05-25", "c. 24–25 May 1860", "range", "muragaki", "Washington Navy Yard",
  "The blast furnace at the Navy Yard",
  "The envoys were invited back to the Navy Yard to see its foundry, blast furnace and workshops, where a group photograph of the embassy with American officers was probably taken. Muragaki's diary is the source that fixes the visit to these days rather than to the landing on 14 May.",
  "", "verified", "Library of Congress blog (2016): Muragaki's journal, published 1918, dates the Navy Yard visit to 24 or 25 May.")
e("1860-05-26", "Late May 1860", "range", "muragaki", "The Capitol, Washington",
  "Congress like the fish market at Nihonbashi",
  "Taken to see Congress in session, the envoys watched members shout and gesture while the presiding officer sat on a raised platform. To Muragaki the scene resembled the fish market at Nihonbashi in Edo, all noise and no visible order. The embassy declined to ask questions about the debate, judging it presumptuous to inquire into another nation's affairs.",
  "", "approx", "Harding (Engelsberg Ideas) and Stambler (2011) on the fish-market comparison; attribution to Muragaki follows common citation of his diary. Day not established.")
e("1860-05-27", "Late May 1860", "range", "muragaki", "Mount Vernon, Virginia",
  "Hats off at Washington's tomb",
  "At George Washington's grave Muragaki noted that music was played and every American removed his hat, a gesture of reverence he could recognise. It was one of the few American rituals he recorded with respect rather than amusement.",
  "", "approx", "Fessler, Musashino in Tuscany, ch. 2. Date of the Mount Vernon visit not established.")
e("1860-05-30", "May 1860", "month", "muragaki", "Washington",
  "Admiring an army of hirelings, privately scornful",
  "Muragaki admired how easily the American military hired and dismissed men as needed, a flexibility unknown to a hereditary warrior class. At the same time he confided that the samurai could easily overcome such a country. Admiration and contempt sit side by side in the same pages.",
  "", "approx", "Harding, 'When the Samurai came to America' (Engelsberg Ideas). Not tied to a day.")
e("1860-06-11", "Monday 11 June 1860", "day", "dispatch", "Richmond, Virginia",
  "'A Japanese Gone North': Tommy's flirtations",
  "Under the headline 'A Japanese Gone North', the Dispatch followed the young interpreter Tateishi Onojirō as the embassy moved toward Philadelphia, retailing his flirting with American women. The papers had renamed him Tommy, and his easy manners made him the embassy's most reported member.",
  "", "verified", "Richmond Daily Dispatch, 11 June 1860, cited in Doan, Civil War Samurai, introduction.")
e("1860-06-12", "Tuesday 12 June 1860", "day", "nyt", "New York (reporting from Philadelphia)",
  "Rumours of a dead Tycoon and fears of colonists",
  "The Times reported the embassy's arrival in Philadelphia together with a rumour that the 'Tycoon' had died, a garbled echo of the assassination of Ii Naosuke that had reached America by sea, telegraph and Pony Express. Another item voiced the fear that the Japanese, having seen America, might make up their minds to colonise it. The same day the Tribune was teasing Tommy about a 'little maid in blue' in Washington.",
  "make up their minds to colonize", "verified", "New York Times, 11–12 June 1860, as cited by Stambler (2011) and Doan, Civil War Samurai, introduction.")
e("1860-06-13", "Wednesday–Thursday 13–14 June 1860", "range", "dubois", "United States Mint, Philadelphia",
  "Oguri's whole-coin assay at the Mint",
  "Under Director James Ross Snowden, the Mint showed the envoys its machinery. The inspector Oguri had come for one thing: to settle the true gold content of the Japanese koban against the American dollar. Refusing samples, he had whole coins assayed, checking weights with his own ivory steelyard and an abacus. Du Bois called the Japanese method crude and antiquated but the results exceedingly satisfactory; the envoys took home a written account to use in exchange negotiations.",
  "exceedingly satisfactory", "verified", "Du Bois, 'The Great Japanese Embassy of 1860', Proc. APS 49 (1910), as summarised by DVIDS and Stack's Bowers (citing Pacific Northwest Quarterly, April 1941). Written fifty years later.")
e("1860-06-16", "Saturday 16 June 1860 ('16th 6th Month, Year 84 of the States')", "day", "whitman", "Broadway, Manhattan",
  "Asia arrives on Broadway",
  "The embassy landed at the Battery and rode up Broadway in open carriages past crowds estimated in the hundreds of thousands, with flags on every building. Whitman dated his poem to this day in the American revolutionary style. He pictured the envoys as courteous princes of Asia leaning back in their carriages, bringing the East to meet the West at Manhattan, and described their dark cheeks and two swords as emblems of a whole continent.",
  "First-comers, guests, two-sworded princes", "verified", "Walt Whitman Archive, 'The Errand-Bearers', dated in its title 16 June 1860.")
e("1860-06-16", "May–June 1860 (Man'en 1, intercalary 3rd–4th months)", "range", "muragaki", "Processions in Washington, Philadelphia and New York",
  "Bouquets from the windows, and women introduced",
  "Muragaki explained to his readers that the women and children throwing bouquets from windows as the carriages passed meant it as congratulation, not insult. He found the American habit of formally introducing wives and daughters to the envoys awkward at first, but came to accept it as the custom of the country. He still left a ballroom early, shocked by the dancing.",
  "", "approx", "Fessler, Musashino in Tuscany, ch. 2. The diary passage is not tied here to a specific city or day.")
e("1860-06-23", "Saturday 23 June 1860", "day", "harpers", "New York",
  "A page of envoys and a column for Tommy",
  "Harper's ran a full-page engraving of the embassy and its attendants and a separate item on Tommy, by now the best-known Japanese person in America. Papers reported women sending him portraits and love letters, and a 'Tommy Polka' was published in his honour.",
  "", "verified", "Harper's Weekly, 23 June 1860 (issue description, Rare Newspapers); Tommy Polka by Charles Grobe per Stambler (2011).")
e("1860-06-23", "Saturday 23 June 1860", "day", "strong", "New York",
  "The attachés buying children's books at Appleton's",
  "Strong noted that members of the embassy had twice visited Appleton's new bookstore and bought heavily: works on the industrial arts, geography, atlases and children's books, which he judged a sensible way to learn a new language. He thought them intelligent and observant. Of the grand ball for the embassy on Monday he wrote that he and his wife had no wish to go, tickets or no.",
  "", "verified", "Diary of George Templeton Strong, ed. Nevins and Thomas (1952), vol. 3, p. 36, entry of 23 June 1860.")
e("1860-06-23", "c. Man'en 1, 5th month, 5th day (23 June 1860)", "day", "fukuzawa", "Uraga",
  "Home again, and guessing the news",
  "When the Kanrin Maru reached Uraga, Fukuzawa recalled, he teased the official who came aboard by guessing that something dramatic had happened in their absence, and learned that Ii Naosuke had been cut down by Mito rōnin in March. The embassy's patron was dead before the envoys reached Washington, and the political ground had shifted under them.",
  "", "approx", "Fukuō jiden (1899), memoir; return date commonly given as the 5th day of the 5th month, not checked in a primary source.")
e("1860-06-27", "Wednesday 27 June 1860", "day", "whitman", "New York Times, New York",
  "'The Errand-Bearers' in the Times",
  "Whitman's poem appeared in the New York Times eleven days after the procession and was reprinted in the Saturday Press three days later. In 1865 he revised it as 'A Broadway Pageant' for Drum-Taps, where the visiting Japanese became a prelude to his vision of America's future across the Pacific.",
  "", "verified", "Pfaff's archive (Lehigh): New York Times 27 June 1860; Saturday Press 30 June 1860; Whitman Archive notes on revision.")
e("1860-08-20", "Monday 20 August 1860", "day", "nyt", "New York",
  "Tommy wants West Point and a Yankee wife",
  "Weeks after the embassy had gone, the Times reported that Tommy had hoped to stay on, improve his English, attend the Naval Academy or West Point, and marry an American. The story, true or embroidered, shows how fully the press had adopted him.",
  "Yankee wife", "verified", "New York Times, 20 August 1860, cited in Doan, Civil War Samurai, introduction.")
e("1860-11-09", "8–10 November 1860 (Man'en 1, 9th month, 26th–28th days)", "range", "muragaki", "Edo Bay and Shinagawa",
  "Home round the world to a changed Edo",
  "The Niagara entered Edo Bay and landed the embassy after a voyage of about nine months, the first Japanese official party to circle the globe. Muragaki and his colleagues returned to a capital where the treaty party had lost its leader and anti-foreign anger was rising; the knowledge the envoys brought home had to make its way in a far more dangerous political climate than the one they had left.",
  "", "approx", "DANFS (entered Tokyo Bay 8 Nov); Harper's engraving caption (10 Nov); House Divided (9 Nov). Japanese date computed.")
e("1865", "1865", "year", "whitman", "Brooklyn and Washington",
  "Revised as 'A Broadway Pageant'",
  "Whitman reworked the 1860 newspaper poem for Drum-Taps, his book of the Civil War, retitling it 'A Broadway Pageant'. The Japanese procession, seen five years and a war later, became the poem's opening image of Asia and America facing each other across the Pacific.",
  "", "verified", "Walt Whitman Archive, note to 'The Errand-Bearers'.")
e("1899", "1899", "year", "fukuzawa", "Tokyo",
  "Fukuō jiden published",
  "Fukuzawa's autobiography, dictated in his last years, was published in 1899. Its chapter on the Kanrin Maru fixed the image of the 1860 voyage in Japanese memory: Japanese sailors crossing the Pacific by themselves, a young man laughing at ballroom dancing and puzzling over Washington's forgotten heirs. Brooke's journal, unpublished until 1961, would complicate that picture.",
  "", "verified", "Standard bibliographic date of 'Fukuō jiden' (1899).")

C = ch["claims"]
def c(date_iso, date_display, eye, claim, form, evidence, confidence):
    C.append(dict(date_iso=date_iso, date_display=date_display, eye=eye, claim=claim, form=form, evidence=evidence, confidence=confidence))

c("1860-02-20", "20 February 1860", "brooke", "Judges the Japanese crew incompetent and Japanese habits unsuited to naval discipline; blames the commodore for the ship's disorder", "travel journal", "Brooke's Kanrin Maru journal (pub. 1961, 1986); NDL column; American Heritage 1963", "verified")
c("1860-03-07", "c. 7–8 March 1860", "muragaki", "Finds little to like in Honolulu, but hears a rooster crow exactly as at home: the bird's song is the same in the East", "travel journal", "Muragaki's diary, via Fessler ch. 2", "approx")
c("1860-03-17", "17 March 1860", "brooke", "Calls Manjirō one of the most remarkable men he has met, the man who did most to open Japan", "travel journal", "Brooke's journal and official letter, via American Heritage 1963", "verified")
c("1860-03-18", "18 March 1860", "alta", "Reports the Japanese warship as the 'Candinmarru' commanded by 'Kat-sin-tarroh'", "newspaper", "Daily Alta California, 18 March 1860", "verified")
c("1860-03-29", "Late March–April 1860", "muragaki", "Likens American ballroom dancing to mice frolicking and laughs openly at the women's swelling skirts", "travel journal", "Muragaki's diary, via Harding (Engelsberg Ideas)", "approx")
c("1860-04-10", "Spring 1860", "fukuzawa", "Is astonished that no American knows or cares what became of George Washington's descendants", "other", "Fukuō jiden (1899), memoir", "approx")
c("1860-04-17", "17 April 1860", "dispatch", "Praises the envoys' 'fine heads, intellectual countenances and dignified bearing'", "newspaper", "Richmond Daily Dispatch, 17 April 1860", "verified")
c("1860-05-17", "17 May 1860", "muragaki", "Finds Buchanan silver-haired, genial and dignified, but the audience strangely lacking in ceremony; calls Americans barbarians in a commemorative waka", "travel journal", "Muragaki's diary, via White House Historical Association; waka widely attributed", "approx")
c("1860-05-17", "17 May 1860", "sophie", "Jokes that a dentist sent strawberries hoping to inspect the Japanese visitors' teeth", "letter", "Sophie Du Pont to S. F. Du Pont, 17 May 1860 (Hagley)", "verified")
c("1860-05-17", "17 May 1860", "buchanan", "Hopes the treaty will bring perpetual peace and friendship between the two countries", "speech", "Buchanan's reply at the audience, as quoted by the US Diplomacy Center", "approx")
c("1860-05-26", "Late May 1860", "muragaki", "Compares the US Congress in session to the fish market at Nihonbashi", "travel journal", "Muragaki's diary, via Harding and Stambler", "approx")
c("1860-05-30", "May 1860", "muragaki", "Privately thinks the samurai could easily defeat America, while admiring its flexible hiring of soldiers", "travel journal", "Muragaki's diary, via Harding (Engelsberg Ideas)", "approx")
c("1860-06-12", "12 June 1860", "nyt", "Voices fear that the Japanese might 'make up their minds to colonize'", "newspaper", "New York Times, 12 June 1860", "verified")
c("1860-06-13", "13–14 June 1860", "dubois", "Calls Oguri's assay method crude and antiquated but its results 'exceedingly satisfactory'", "other", "Du Bois, Proc. APS 49 (1910)", "verified")
c("1860-06-16", "16 June 1860", "whitman", "Hails the envoys as courteous, 'two-sworded', lesson-giving princes of Asia, marking their dark cheeks", "poem", "'The Errand-Bearers', New York Times, 27 June 1860", "verified")
c("1860-06-23", "23 June 1860", "strong", "Finds the embassy's attachés intelligent and observant buyers of technical and children's books", "diary", "Diary of George Templeton Strong, vol. 3, p. 36", "verified")

ch["convergences"] = [
 {"date": "1860-02-24", "label": "The Kanrin Maru's crossing: who keeps the watch?", "eyes": ["brooke", "akamatsu"],
  "note": "Brooke's journal (14 and 20 February) complains that no watches are set; Akamatsu's log for 24 February records, without complaint, that watches were assigned only the day before. The same problem, seen by a frustrated guest and a junior officer of the ship."},
 {"date": "1860-03-17", "label": "The Kanrin Maru reaches San Francisco", "eyes": ["brooke", "fukuzawa", "alta"],
  "note": "Brooke's journal dwells on his own handling of the ship and on Manjirō's help; Fukuzawa remembers it as a Japanese triumph, salute answered gun for gun; the Alta reports a 'Candinmarru' at the Vallejo Street wharf. Three different ships arrive in the same harbour."},
 {"date": "1860-03-10", "label": "Honolulu: the first foreign stop", "eyes": ["muragaki", "tamamushi"],
  "note": "Muragaki finds Honolulu tiresome except for a rooster that sounds like home; his junior Tamamushi spends the time writing classical Chinese with a Chinese pharmacist about Western aggression in China."},
 {"date": "1860-05-17", "label": "The audience in the East Room", "eyes": ["muragaki", "buchanan", "sophie"],
  "note": "Buchanan speaks of perpetual friendship; Muragaki sees a pleasant old man in plain clothes and writes a poem calling his hosts barbarians; in Delaware, Sophie Du Pont laughs at a dentist who wants to examine the guests' teeth."},
 {"date": "1860-06-12", "label": "The Philadelphia week", "eyes": ["dispatch", "nyt", "dubois"],
  "note": "While the Dispatch and the Times trade in Tommy's romances, rumours from Edo and fears of colonisation, Oguri spends two days at the Mint on the dull, decisive question of how much gold is in a koban."},
 {"date": "1860-06-16", "label": "Broadway", "eyes": ["whitman", "muragaki", "harpers"],
  "note": "Whitman sees Asia arriving at Manhattan; Muragaki has to explain to his readers that the flowers thrown from windows are meant kindly; within a week Harper's has put the attendants and Tommy on its pages."},
 {"date": "1860-06-23", "label": "Saturday 23 June: bookshop and homecoming", "eyes": ["strong", "harpers", "fukuzawa"],
  "note": "On the same date Strong records the attachés buying children's books in New York and Harper's prints Tommy, while on the other side of the world the Kanrin Maru reaches Uraga and Fukuzawa learns that Ii Naosuke has been assassinated."}
]

ch["ties"] = [
 {"a": "brooke", "b": "akamatsu", "kind": "same street", "note": "Shipmates on the Kanrin Maru; their journals describe the same watches from opposite sides."},
 {"a": "brooke", "b": "fukuzawa", "kind": "same street", "note": "Both crossed in the Kanrin Maru; Fukuzawa's memoir leaves the American adviser almost out of the story Brooke's journal puts him at the centre of."},
 {"a": "brooke", "b": "alta", "kind": "mentioned", "note": "The Alta reported the arrival of the ship Brooke had helped bring across."},
 {"a": "muragaki", "b": "tamamushi", "kind": "met", "note": "Vice-envoy and attendant in the same embassy, writing separate diaries of the same journey."},
 {"a": "muragaki", "b": "buchanan", "kind": "met", "note": "Muragaki was received by Buchanan in the East Room on 17 May 1860 and described him in his diary."},
 {"a": "sophie", "b": "muragaki", "kind": "mentioned", "note": "Sophie Du Pont's husband, Captain Samuel F. Du Pont, commanded the American escort of the envoys and was later presented with a sword by them."},
 {"a": "dubois", "b": "muragaki", "kind": "met", "note": "The three envoys, Muragaki among them, attended the Mint assay that Du Bois described."},
 {"a": "whitman", "b": "nyt", "kind": "read each other", "note": "The Times published Whitman's poem on the procession on 27 June 1860."},
 {"a": "whitman", "b": "muragaki", "kind": "same street", "note": "Whitman's Broadway procession carried Muragaki and the other envoys in open carriages."},
 {"a": "dispatch", "b": "nyt", "kind": "opposite sides", "note": "Southern and Northern papers covered the same visitors months before secession, with the same appetite for Tommy."},
 {"a": "strong", "b": "harpers", "kind": "same street", "note": "Both in New York writing on 23 June 1860, one privately, one for a national readership."}
]

ch["threads_out"] = [
 {"to": "iwakura-1871", "note": "Eleven years later the Iwakura Embassy retraced the route to San Francisco and Washington with a far larger party and a new government, seeking treaty revision rather than ratification; scholars routinely compare the two missions."},
 {"to": "v2:black-ships", "note": "The embassy was the diplomatic sequel to Perry's 1853–54 expedition and Harris's 1858 treaty; in New York the envoys called on Perry's widow, and on the Roanoke Muragaki met an officer still boasting of the Perry voyage."},
 {"to": "v1:us-civil-war", "note": "The visit came months before secession: the Niagara returned to Boston in April 1861 to find the war begun, and Lieutenant Brooke joined the Confederate navy and worked on the ironclad CSS Virginia."},
 {"to": "v14:california-1848", "note": "Both ships landed first in gold-rush San Francisco, and the embassy's purpose included settling the gold value of Japanese coin against the dollar, which Oguri tested at the Philadelphia Mint."}
]

ch["images"] = [
 {"url": "https://rp-digitalcollections.nypl.org/items/510d47dd-f6a6-a3d9-e040-e00a18064a99", "title": "Reception of the Japanese Ambassadors by the President of the United States, in the East Room of the White House, May 17", "caption": "Wood engraving from Frank Leslie's Illustrated Newspaper of 2 June 1860 showing Buchanan receiving the envoys, with many women among the onlookers; an artist's reconstruction for the press, not a photograph.", "date": "2 June 1860", "credit": "Frank Leslie's Illustrated Newspaper; New York Public Library, Wallach Division of Art, Prints and Photographs"},
 {"url": "http://www.loc.gov/item/2017645256/", "title": "Reception of the Japanese Embassy, New-York, June 16, 1860. Broadway looking up", "caption": "One of a series of contemporary views of the Broadway procession of 16 June 1860, the day Whitman dated his poem.", "date": "1860", "credit": "Library of Congress, Prints and Photographs (associated name: George Stacy)"},
 {"url": "http://www.loc.gov/item/2011648395/", "title": "The Japanese Embassy in New York--scenes and incidents", "caption": "Stereograph published by Edward Anthony of the embassy's reception in New York, catalogued with Battery Park, where the envoys landed; stereographs let Americans look at the visitors at home in three dimensions.", "date": "1860", "credit": "Edward Anthony; Library of Congress, Prints and Photographs"},
 {"url": "https://quod.lib.umich.edu/j/japanese/japanese.0005.001?view=toc", "title": "Manuscript copy of Kōbei nichiroku by Tamamushi Sadayū, volume one", "caption": "A manuscript copy, made in Edo in 1861, of Tamamushi's diary of the embassy, showing how such journals circulated in handwritten copies long before they were printed in 1913.", "date": "1861", "credit": "University of Michigan Library"},
 {"url": "https://diplomacy.state.gov/items/1860-japanese-embassy-medal", "title": "1860 Japanese Embassy medal", "caption": "Silver example of the medal bearing Buchanan's portrait that Secretary of State Cass presented to members of the embassy, struck in gold, silver or bronze according to rank.", "date": "1860", "credit": "National Museum of American Diplomacy, US Department of State, 2011.0003.05.01"},
 {"url": "https://ibiblio.org/hyperwar/OnlineLibrary/photos/images/h59000/h59571c.htm", "title": "USS Niagara arriving at Yeddo with the Japanese Embassy, November 1860", "caption": "Line engraving published in Harper's Weekly in 1861 showing the Niagara bringing the envoys home to Edo after their voyage round the world.", "date": "1861 (event November 1860)", "credit": "Harper's Weekly; US Naval History and Heritage Command, NH 59571"}
]

ch["further"] = [
 {"title": "Library of Congress, 'Who were the first Japanese to visit Washington?' (2016)", "url": LOC_BLOG},
 {"title": "Warinner, 'The Ordeal of the Kanrin Maru', American Heritage (1963)", "url": AH},
 {"title": "Fessler, Musashino in Tuscany: Japanese Overseas Travel Literature, 1860–1912 (open access)", "url": FESSLER},
 {"title": "Doan, 'The 1860 Japanese Embassy and the Antebellum African American Press', Historical Journal (2019)", "url": "https://cambridge.org/core/journals/historical-journal/article/1860-japanese-embassy-and-the-antebellum-african-american-press/C63068580AFB0BC8D20FE551D36C959E"},
 {"title": "Stambler, 'Ambassadors of Exchange: The 1860 Japanese Mission to the US', Education About Asia (2011)", "url": "https://www.asianstudies.org/eaa/ambassadors-of-exchange-the-1860-japanese-mission-to-the-us/"},
 {"title": "Walt Whitman Archive: 'The Errand-Bearers' (1860)", "url": "https://whitmanarchive.org/item/per.00154"},
 {"title": "National Diet Library, 'Nikki no sekai': Akamatsu and Brooke on the Kanrin Maru", "url": NDL},
 {"title": "Du Bois, 'The Great Japanese Embassy of 1860', Proc. American Philosophical Society 49 (1910)", "url": "https://biostor.org/reference/203957"}
]

ch["entries"].sort(key=lambda x: x["date_iso"])
ch["claims"].sort(key=lambda x: x["date_iso"])
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(ch, f, ensure_ascii=False, indent=1)
print(len(ch["eyes"]), len(ch["entries"]), len(ch["claims"]), len(ch["convergences"]), len(ch["ties"]))
