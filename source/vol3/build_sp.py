import json
OUT = "/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/vol3/ch-south-pole.json"

BLOG = "https://scottvsamundsen.blogspot.com/"
B14D = "https://scottvsamundsen.blogspot.com/2011/12/thursday-14-december-1911.html"
B17J = "https://scottvsamundsen.blogspot.com/2012/01/wednesday-17-january-1912.html"
B18J = "https://scottvsamundsen.blogspot.com/2012/01/thursday-18-january-1912.html"
B8M = "https://scottvsamundsen.blogspot.com/2012/03/friday-8-march-1912.html"
B17M = "https://scottvsamundsen.blogspot.com/2012/03/sunday-17-march-1912.html"
B12N = "https://scottvsamundsen.blogspot.com/2012/11/tuesday-12-november-1912.html"
BFEB13 = "https://scottvsamundsen.blogspot.com/2013/02"

POLE = {"lat": -89.99, "lon": 0.0, "label": "South Pole"}
CAPE_EVANS = {"lat": -77.64, "lon": 166.40, "label": "Cape Evans hut"}
LAST_CAMP = {"lat": -79.67, "lon": 169.38, "label": "Last camp, Mar 1912"}
FRAMHEIM = {"lat": -78.55, "lon": -163.7, "label": "Framheim"}

eyes = [
 {
  "id": "scott", "name": "Robert Falcon Scott", "short": "Scott", "life": "1868–1912",
  "role": "Captain RN, aged 43, leader of the British Antarctic (Terra Nova) Expedition and of its five-man polar party",
  "side": "British (British Antarctic Expedition 1910–13)",
  "where": "Cape Evans, Ross Island; the Barrier, the Beardmore Glacier and the polar plateau",
  "lat": -89.99, "lon": 0.0,
  "waypoints": [
   {"lat": -77.64, "lon": 166.40, "label": "Cape Evans, 1 Nov 1911"},
   {"lat": -83.6, "lon": 170.5, "label": "Foot of Beardmore"},
   {"lat": -87.53, "lon": 160.0, "label": "Last support, 4 Jan"},
   {"lat": -89.99, "lon": 0.0, "label": "Pole, 17 Jan 1912"},
   {"lat": -83.6, "lon": 170.5, "label": "Evans dies, 17 Feb"},
   {"lat": -79.67, "lon": 169.38, "label": "Last camp, Mar 1912"}
  ],
  "vantage": 0, "vantage_label": "leader of the British polar party; died on the return",
  "form": "journal (sledging diaries)", "language": "English",
  "authenticity": "Holograph sledging journals found in the tent on 12 November 1912, now in the British Library (Add MS 51024–51035). Published in edited form in 'Scott's Last Expedition' (1913, arranged by Leonard Huxley); the printed text softened a few remarks about companions and the Norwegians, which later facsimile and scholarly editions restore.",
  "bio": "A career naval officer who had led the Discovery expedition of 1901–04, Scott planned a combined scientific programme and polar journey relying on ponies, motor sledges and man-hauling. His journal, kept to the last days in the tent, became the founding text of the British memory of the race. It is the record of a man who understood, earlier than his companions said aloud, that they were unlikely to get home.",
  "sources": [
   {"title": "Scott vs Amundsen day-by-day (quotes Scott's journal via 'Scott's Last Expedition')", "url": BLOG},
   {"title": "University of Cambridge: final letters mark centenary of Scott's last march", "url": "https://www.cam.ac.uk/research/news/final-letters-mark-centenary-of-scotts-last-march"}
  ]
 },
 {
  "id": "wilson", "name": "Edward Adrian Wilson", "short": "Wilson", "life": "1872–1912",
  "role": "Physician, zoologist and artist, aged 39; chief of scientific staff; member of the polar party",
  "side": "British (British Antarctic Expedition)",
  "where": "With Scott on the polar journey; died in the last tent",
  "lat": -79.67, "lon": 169.38,
  "waypoints": [
   {"lat": -77.64, "lon": 166.40, "label": "Cape Evans, Nov 1911"},
   {"lat": -83.6, "lon": 170.5, "label": "Beardmore Glacier"},
   {"lat": -89.99, "lon": 0.0, "label": "Pole, 17 Jan 1912"},
   {"lat": -79.67, "lon": 169.38, "label": "Last camp, Mar 1912"}
  ],
  "vantage": 0, "vantage_label": "polar party; doctor and naturalist",
  "form": "diary (sledging diary) and dated last letters", "language": "English",
  "authenticity": "Wilson's sledging diary was recovered from the tent; passages were printed by Cherry-Garrard in 'The Worst Journey in the World' (1922) and the whole by H. G. R. King (1972). His last letters, to his wife Oriana and to the families of others, are largely held by the Scott Polar Research Institute.",
  "bio": "Scott's closest confidant, a devout Christian and a gifted painter of Antarctic light, Wilson kept a naturalist's diary even on the plateau: temperatures, haze, the gear the Norwegians left behind. He carried the party's geological specimens to the end at his own insistence. His tone is quieter than Scott's and his grief harder to see.",
  "sources": [
   {"title": "Scott vs Amundsen: 17 January 1912 (Wilson's diary via 'The Worst Journey')", "url": B17J},
   {"title": "Scott vs Amundsen: 18 January 1912", "url": B18J}
  ]
 },
 {
  "id": "bowers", "name": "Henry Robertson 'Birdie' Bowers", "short": "Bowers", "life": "1883–1912",
  "role": "Lieutenant, Royal Indian Marine, aged 28; in charge of stores; added to the polar party as the fifth man",
  "side": "British (British Antarctic Expedition)",
  "where": "Polar journey; died in the last tent beside Scott and Wilson",
  "lat": -79.67, "lon": 169.38,
  "waypoints": [
   {"lat": -77.64, "lon": 166.40, "label": "Cape Evans, Nov 1911"},
   {"lat": -87.53, "lon": 160.0, "label": "Made fifth man, 4 Jan"},
   {"lat": -89.99, "lon": 0.0, "label": "Pole, 17 Jan 1912"},
   {"lat": -79.67, "lon": 169.38, "label": "Last camp, Mar 1912"}
  ],
  "vantage": 0, "vantage_label": "polar party; navigator and photographer",
  "form": "diary and dated letters to his mother", "language": "English",
  "authenticity": "Bowers's diaries and letters to his mother Emily are held at the Scott Polar Research Institute; extracts quoted by Huntford (1980) and Crane (2005). His Pole photographs, taken with a string release, survived in the tent.",
  "bio": "Short, red-nosed and famously tough, Bowers had ordered his skis left at a depot before Scott chose him as a fifth man, so he walked the plateau on foot beside four skiers. He was the party's meticulous navigator and photographer; he took the picture of the five at the Pole. His letters home are cheerful almost to the end.",
  "sources": [
   {"title": "Scott vs Amundsen: 14 December 1911 (Bowers via Huntford)", "url": B14D},
   {"title": "Isobel Williams: notes on Bowers and the Pole photographs", "url": "https://isobelpwilliams.com/tag/birdie-bowers/"}
  ]
 },
 {
  "id": "cherry", "name": "Apsley Cherry-Garrard", "short": "Cherry-Garrard", "life": "1886–1959",
  "role": "Assistant zoologist, aged 25; member of the first supporting party; later the dog-team relief to One Ton Depot and a member of the search party",
  "side": "British (British Antarctic Expedition)",
  "where": "Beardmore Glacier (to Dec 1911), One Ton Depot (Mar 1912), Hut Point, Cape Evans, the tent (Nov 1912)",
  "lat": -79.48, "lon": 169.0,
  "waypoints": [
   {"lat": -77.64, "lon": 166.40, "label": "Cape Evans, Nov 1911"},
   {"lat": -85.1, "lon": 163.0, "label": "Turned back, 22 Dec"},
   {"lat": -77.85, "lon": 166.64, "label": "Hut Point, Feb 1912"},
   {"lat": -79.48, "lon": 169.0, "label": "One Ton, 4–10 Mar"},
   {"lat": -79.67, "lon": 169.38, "label": "Tent found, 12 Nov"}
  ],
  "vantage": 1, "vantage_label": "supporting party; waited at One Ton Depot; found the tent",
  "form": "diary; memoir (written later)", "language": "English",
  "authenticity": "His expedition diaries are at the Scott Polar Research Institute; 'The Worst Journey in the World' (1922) is a later memoir that quotes his own and Wilson's diaries at length and is clearly marked as such here.",
  "bio": "The youngest of the scientific staff, short-sighted and untrained, Cherry-Garrard had survived the midwinter journey to the Emperor penguins with Wilson and Bowers. In March 1912 he waited at One Ton Depot with the dogs, less than seventy miles from the party he could not know was struggling towards him. He spent the rest of his life asking whether he should have gone on.",
  "sources": [
   {"title": "The Worst Journey in the World (1922), Standard Ebooks", "url": "https://standardebooks.org/ebooks/apsley-cherry-garrard/the-worst-journey-in-the-world/text/chapter-18"},
   {"title": "Scott vs Amundsen: 8 March 1912 (Cherry-Garrard diary)", "url": B8M}
  ]
 },
 {
  "id": "gran", "name": "Tryggve Gran", "short": "Gran", "life": "1888–1980",
  "role": "Norwegian ski expert, aged 22, recruited on Nansen's advice; member of the Western geological party and of the search party",
  "side": "Norwegian serving with the British expedition",
  "where": "Cape Evans; Granite Harbour (Western party, Nov 1911–Feb 1912); the Barrier search, Nov 1912",
  "lat": -77.64, "lon": 166.40,
  "waypoints": [
   {"lat": -77.64, "lon": 166.40, "label": "Cape Evans"},
   {"lat": -76.9, "lon": 162.7, "label": "Granite Harbour, 1911"},
   {"lat": -77.64, "lon": 166.40, "label": "Cape Evans, 2nd winter"},
   {"lat": -79.67, "lon": 169.38, "label": "Tent found, 12 Nov"},
   {"lat": -43.6, "lon": 172.72, "label": "Lyttelton, 12 Feb 1913"}
  ],
  "vantage": 1, "vantage_label": "a Norwegian in the British camp; found the tent",
  "form": "diary", "language": "Norwegian and English",
  "authenticity": "Gran kept a Norwegian diary (7 Nov 1911–25 Feb 1912) and an English one (to Feb 1913), both bought by Canterbury Museum, Christchurch, in 2018; these are less edited than the versions he later revised and published, including 'The Norwegian with Scott' (English, 1984). Treat his later published text as partly reworked.",
  "bio": "A young Norwegian naval cadet and football international, Gran found himself the only Norwegian in a British camp racing a Norwegian expedition. He taught the British to ski, and on the search journey he wore Scott's skis back so that, as he put it, they would finish the journey. In 1914 he made the first flight across the North Sea and then served as a pilot in the First World War.",
  "sources": [
   {"title": "Canterbury Museum: museum acquires two more diaries by Scott's ski expert", "url": "https://www.canterburymuseum.com/explore/latest-news/museum-acquires-two-more-diaries-by-scotts-ski-expert"},
   {"title": "Canterbury Museum collection: Tryggve Gran's journal", "url": "https://collection.canterburymuseum.com/objects/959961"},
   {"title": "Scott vs Amundsen: 12 November 1912", "url": B12N}
  ]
 },
 {
  "id": "amundsen", "name": "Roald Amundsen", "short": "Amundsen", "life": "1872–1928",
  "role": "Leader of the Norwegian expedition in the Fram, aged 39; leader of the five-man polar party",
  "side": "Norwegian (Fram expedition 1910–12)",
  "where": "Framheim, Bay of Whales; the Barrier, Axel Heiberg Glacier and plateau; later Hobart and an American lecture tour",
  "lat": -89.99, "lon": 0.0,
  "waypoints": [
   {"lat": -78.55, "lon": -163.7, "label": "Framheim, 19 Oct 1911"},
   {"lat": -85.4, "lon": -165.0, "label": "Axel Heiberg Glacier"},
   {"lat": -89.99, "lon": 0.0, "label": "Polheim, 14 Dec 1911"},
   {"lat": -78.55, "lon": -163.7, "label": "Framheim, 25 Jan 1912"},
   {"lat": -42.88, "lon": 147.33, "label": "Hobart, 7 Mar 1912"},
   {"lat": 43.07, "lon": -89.40, "label": "Madison, Feb 1913"}
  ],
  "vantage": 0, "vantage_label": "leader of the first party to reach the Pole",
  "form": "diary; published narrative (written soon after)", "language": "Norwegian",
  "authenticity": "Amundsen's original diaries are in the National Library of Norway; the Norwegian Polar Institute has published transcripts. 'Sydpolen' (1912) was translated into English by A. G. Chater as 'The South Pole' (1912): that English text is a translation, so it is paraphrased here, not quoted. His diary ran one day ahead on the polar journey (the Pole entry is headed 15 December).",
  "bio": "The Norwegian who first sailed the North-West Passage had planned to drift across the Arctic in Nansen's Fram; when Cook and Peary claimed the North Pole in 1909 he turned south secretly, revealing his aim only at Madeira. He relied on skis, dogs and the deliberate slaughter of dogs for food along the route. His diary is terse and practical; his book is triumphant and careful; neither hides that he regarded the Pole itself as a second prize to his boyhood dream of the north.",
  "sources": [
   {"title": "The South Pole, vols 1–2 (tr. A. G. Chater, 1912), Project Gutenberg", "url": "https://gutenberg.org/files/4229/4229-h/4229-h.htm"},
   {"title": "Amundsen, 'The First Account' (Hobart, March 1912), Cool Antarctica", "url": "https://www.coolantarctica.com/Antarctica%20fact%20file/History/The_South_Pole/amundsen_the_first_account.php"},
   {"title": "Fram Museum: the third Fram expedition 1910–1914", "url": "https://frammuseum.no/polar-history/expeditions/the-third-fram-expedition-1910-1914/"},
   {"title": "Diaries of Note: Amundsen's Pole entry (transcript via Norwegian Polar Institute)", "url": "https://diariesofnote.com/2023/12/14/thanks-be-to-god/"}
  ]
 },
 {
  "id": "bjaaland", "name": "Olav Bjaaland", "short": "Bjaaland", "life": "1873–1961",
  "role": "Champion skier and ski-maker from Morgedal, Telemark, aged 38; dog-driver and photographer of the polar party",
  "side": "Norwegian (Fram expedition)",
  "where": "Framheim and the polar journey",
  "lat": -89.99, "lon": 0.0,
  "waypoints": [
   {"lat": -78.55, "lon": -163.7, "label": "Framheim, Oct 1911"},
   {"lat": -85.4, "lon": -165.0, "label": "Axel Heiberg Glacier"},
   {"lat": -89.99, "lon": 0.0, "label": "Polheim, Dec 1911"},
   {"lat": -78.55, "lon": -163.7, "label": "Framheim, Jan 1912"}
  ],
  "vantage": 0, "vantage_label": "polar party; a farmer-craftsman's eye",
  "form": "diary", "language": "Norwegian (Telemark dialect)",
  "authenticity": "Bjaaland's diaries of the third Fram voyage were first published as a book by the Ishavsmuseet Aarvak (Brandal); individual entries are best known in English through Roland Huntford's quotations in 'Scott and Amundsen' (1980). Paraphrased here from those quotations.",
  "bio": "A Telemark farmer and the finest skier of the party, Bjaaland built the light sledges and took most of the usable photographs of the Norwegian journey. His diary is blunter than his leader's: hungry, competitive, sometimes sour, often funny. Fifty years later he inscribed a photograph of himself at the Pole with a greeting to the new American station there.",
  "sources": [
   {"title": "Ishavsmuseet: Olav Bjaaland's diaries, The South Pole Expedition 1910–14", "url": "https://www.ishavsmuseet.no/en/produkt/olav-bjaalands-dagboker-sydpolekspedisjonen-1910-14/"},
   {"title": "Fram Museum: Olav Olavsen Bjaaland", "url": "https://frammuseum.no/polar-history/explorers/olav-olavsen-bjaaland-1873-1961/"},
   {"title": "Norwegian Polar Institute centenary diary, 19 Oct 2011 (quotes Bjaaland)", "url": "https://sorpolen2011.npolar.no/en/diary/south-pole/2011-10-19-the-day-we-should-have-set-off.html"}
  ]
 },
 {
  "id": "prestrud", "name": "Kristian Prestrud", "short": "Prestrud", "life": "1881–1927",
  "role": "First lieutenant, Royal Norwegian Navy, aged 30; leader of the Eastern sledge party and in charge at Framheim while Amundsen was away",
  "side": "Norwegian (Fram expedition)",
  "where": "Framheim; King Edward VII Land (Nov–Dec 1911); the Bay of Whales",
  "lat": -78.55, "lon": -163.7,
  "waypoints": [
   {"lat": -78.55, "lon": -163.7, "label": "Framheim, 8 Nov 1911"},
   {"lat": -77.2, "lon": -154.5, "label": "King Edward VII Land"},
   {"lat": -78.55, "lon": -163.7, "label": "Framheim"},
   {"lat": -78.5, "lon": -164.2, "label": "Kainan Maru, 17 Jan"}
  ],
  "vantage": 1, "vantage_label": "left behind at the base; met the Japanese",
  "form": "sledging report (dated, printed in 'The South Pole')", "language": "Norwegian",
  "authenticity": "Prestrud's day-by-day report of the Eastern journey is printed as a chapter of Amundsen's 'The South Pole' (English tr. 1912). His visit to the Kainan Maru on 17 January 1912 is recorded in the Japanese expedition's own report, not in a surviving Prestrud diary consulted here.",
  "bio": "Prestrud had been demoted from the Pole party in the quarrel after the failed September start, and was given the Eastern journey with Johansen and Stubberud instead. His party were the first people to set foot on King Edward VII Land. In January 1912, with the polar party still out, he and Fram's captain Thorvald Nilsen were the Norwegians who climbed aboard the Japanese ship.",
  "sources": [
   {"title": "Prestrud, 'The Eastern Sledge Journey' (The South Pole, ch. 15), Cool Antarctica", "url": "https://coolantarctica.com/Antarctica%20fact%20file/History/The_South_Pole/south_pole_amundsen_chapter15.php"}
  ]
 },
 {
  "id": "shirase", "name": "Shirase Nobu", "short": "Shirase", "life": "1861–1946",
  "role": "Army lieutenant (retired), aged 50, leader of the Japanese Antarctic Expedition in the Kainan Maru and of its 'Dash Patrol'",
  "side": "Japanese (Japanese Antarctic Expedition 1910–12)",
  "where": "Kainan Maru; Sydney (1911); Kainan Bay and the Bay of Whales; the Ross Ice Shelf to 80°5'S",
  "lat": -80.08, "lon": -156.62,
  "waypoints": [
   {"lat": 35.68, "lon": 139.77, "label": "Tokyo, 29 Nov 1910"},
   {"lat": -41.29, "lon": 174.78, "label": "Wellington, Feb 1911"},
   {"lat": -33.87, "lon": 151.21, "label": "Sydney, May–Nov 1911"},
   {"lat": -78.28, "lon": -161.83, "label": "Kainan Bay, 16 Jan"},
   {"lat": -78.5, "lon": -164.2, "label": "Bay of Whales, 17 Jan"},
   {"lat": -80.08, "lon": -156.62, "label": "80°5'S, 28 Jan 1912"}
  ],
  "vantage": 1, "vantage_label": "a third expedition on the Ross Ice Shelf; met the Fram",
  "form": "expedition record compiled from members' journals ('Nankyoku-ki', 1913)", "language": "Japanese",
  "authenticity": "'Nankyoku-ki' (1913), the official account compiled by the Shirase Antarctic Expedition Supporters' Association from the journals of Shirase, the scientist Takeda Terutarō and others; English translation by Lara Dagnell and Hilary Shibata (2011). Its scientific appendix was translated in the Antarctic Record (1957). It is an edited record rather than a single person's diary; dates are given in the Gregorian calendar, which Japan had used since 1873.",
  "bio": "A soldier from Akita who had served in the Kuril Islands, Shirase raised money from the public and the statesman Ōkuma Shigenobu for a small converted fishing schooner. Mocked in the Sydney press while he waited out the winter of 1911, he returned with a scientific aim once the Pole was clearly out of reach. His record is the only non-European voice in this chapter, and its account of meeting the Norwegians is the encounter at the heart of it.",
  "sources": [
   {"title": "NIPR: English translation of the Nankyoku-ki scientific appendix (Antarctic Record, 1957)", "url": "https://nipr.repo.nii.ac.jp/record/6803/files/KJ00002475816.pdf"},
   {"title": "Cool Antarctica: Shirase Nobu and the Kainan Maru", "url": "https://coolantarctica.com/Antarctica%20fact%20file/History/antarctic_whos_who_shirase_nobu_kainan_maru.php"},
   {"title": "Polar Journal: the odd bird on the fringe of history", "url": "https://polarjournal.net/the-odd-bird-on-the-fringe-of-history/"},
   {"title": "National Diet Library: portrait of Shirase Nobu", "url": "https://www.ndl.go.jp/portrait/e/datas/281.html"}
  ]
 },
 {
  "id": "filchner", "name": "Wilhelm Filchner", "short": "Filchner", "life": "1877–1957",
  "role": "Bavarian army officer and surveyor, aged 34; leader of the Second German Antarctic Expedition in the Deutschland",
  "side": "German (Second German Antarctic Expedition 1911–12)",
  "where": "Weddell Sea: South Georgia, the Luitpold Coast, Vahsel Bay, then beset and drifting",
  "lat": -77.8, "lon": -35.1,
  "waypoints": [
   {"lat": 53.54, "lon": 8.58, "label": "Bremerhaven, May 1911"},
   {"lat": -34.6, "lon": -58.38, "label": "Buenos Aires, Sep 1911"},
   {"lat": -54.28, "lon": -36.51, "label": "Grytviken, 11 Dec 1911"},
   {"lat": -77.8, "lon": -35.1, "label": "Vahsel Bay, Feb 1912"},
   {"lat": -70.0, "lon": -42.0, "label": "Beset, drifting 1912"},
   {"lat": -54.28, "lon": -36.51, "label": "Grytviken, 19 Dec 1912"}
  ],
  "vantage": 2, "vantage_label": "the other side of the continent; a rival plan for a crossing",
  "form": "expedition narrative from his journal ('Zum sechsten Erdteil', 1922); exposé written later", "language": "German",
  "authenticity": "Filchner's official narrative 'Zum sechsten Erdteil' (1922) is based on the expedition journals but was written after the war and after bitter quarrels on board; a franker account he wrote shortly before his death was published only in 1985. Treat the narrative as an edited record, not a raw diary.",
  "bio": "Filchner, who had surveyed in Tibet, wanted to test whether the Weddell and Ross Seas were joined by a channel and to cross the continent. He found a new coast and a bay at the head of the Weddell Sea, lost his planned base when the iceberg it stood on broke away, and spent the winter of 1912 beset in a ship riven by feuds. His expedition shows the same season from the Atlantic side, far from the Pole race but inside the same scramble for the continent.",
  "sources": [
   {"title": "Second German Antarctic Expedition (encyclopedia mirror)", "url": "https://en.wikipedia.org/wiki/Second_German_Antarctic_Expedition"},
   {"title": "Falklands Biographies: Wilhelm Filchner", "url": "https://falklandsbiographies.org/biographies/184"},
   {"title": "South-pole.com: Wilhelm Filchner", "url": "https://www.south-pole.com/p0000103.htm"}
  ]
 },
 {
  "id": "mawson", "name": "Douglas Mawson", "short": "Mawson", "life": "1882–1958",
  "role": "Geologist, University of Adelaide, aged 29; leader of the Australasian Antarctic Expedition and of its Far Eastern sledging party",
  "side": "Australian / New Zealand (Australasian Antarctic Expedition 1911–14)",
  "where": "Cape Denison, Commonwealth Bay (George V Land) and the Far Eastern journey",
  "lat": -67.01, "lon": 142.66,
  "waypoints": [
   {"lat": -42.88, "lon": 147.33, "label": "Hobart, 2 Dec 1911"},
   {"lat": -54.5, "lon": 158.94, "label": "Macquarie Island"},
   {"lat": -67.01, "lon": 142.66, "label": "Cape Denison, Jan 1912"},
   {"lat": -68.6, "lon": 151.4, "label": "Ninnis lost, 14 Dec"},
   {"lat": -67.9, "lon": 145.5, "label": "Mertz dies, 8 Jan 1913"},
   {"lat": -67.01, "lon": 142.66, "label": "Hut, 8 Feb 1913"}
  ],
  "vantage": 2, "vantage_label": "a third coast; science rather than the Pole",
  "form": "diary; published narrative ('The Home of the Blizzard', 1915)", "language": "English",
  "authenticity": "Mawson's diaries are held at the South Australian Museum and were published as 'Mawson's Antarctic Diaries' (1988); 'The Home of the Blizzard' (1915) is his edited public account. Xavier Mertz's German diary, kept to the end, independently records the day Ninnis died.",
  "bio": "Mawson had been with Shackleton's men to the South Magnetic Pole and turned down Scott's invitation to join the Terra Nova in order to explore the coast south of Australia. His base at Cape Denison proved to be one of the windiest places on earth. His Far Eastern journey of 1912–13, on which both his companions died, is the third tragedy of this season and the one he survived alone.",
  "sources": [
   {"title": "Mawson's Huts: catastrophe (Ninnis, 14 Dec 1912)", "url": "https://mawsonshuts.antarctica.gov.au/cape-denison/mawsons-fatal-journey/catastrophe/"},
   {"title": "Mawson's Huts: bad news and a breakthrough (wireless, Feb 1913)", "url": "https://mawsonshuts.antarctica.gov.au/macquarie-island/the-wireless-relay/bad-news-and-a-breakthrough/"},
   {"title": "Australian Antarctic Division: 'The Home of the Blizzard', ch. 27", "url": "https://www.antarctica.gov.au/about-antarctica/history/exploration-and-expeditions/australasian-antarctic-expedition/home-of-the-blizzard-book/chapter27/"}
  ]
 },
 {
  "id": "kathleen", "name": "Kathleen Scott", "short": "Kathleen Scott", "life": "1878–1947",
  "role": "Sculptor, aged 34, Scott's wife and mother of their son Peter",
  "side": "British (at home and at sea)",
  "where": "London; aboard the liner Aorangi in the Pacific, bound for New Zealand to meet her husband",
  "lat": -10.0, "lon": -150.0,
  "waypoints": [
   {"lat": 51.51, "lon": -0.13, "label": "London"},
   {"lat": 37.77, "lon": -122.42, "label": "San Francisco"},
   {"lat": -10.0, "lon": -150.0, "label": "Aorangi, at sea"},
   {"lat": -41.29, "lon": 174.78, "label": "Wellington, 1913"}
  ],
  "vantage": 4, "vantage_label": "the family, hearing the news at sea",
  "form": "diary", "language": "English",
  "authenticity": "Kathleen Scott's diaries are held at Cambridge University Library; extracts were published in her autobiography 'Self-Portrait of an Artist' (1949). The day she was told is reported differently: a 1913 New Zealand press account says the Aorangi's captain heard by wireless around midnight on 16 February and told her the next morning; other accounts put it about nine days after the 10 February announcement.",
  "bio": "A sculptor who had studied in Paris and known Rodin, Kathleen married Scott in 1908 and sailed to meet him in New Zealand at the end of the expedition. She learned at sea, days after the world knew, that she had been a widow for nearly a year. She went on to make the statue of Scott that stands in Waterloo Place.",
  "sources": [
   {"title": "Dominion, 1 March 1913: how the news reached Lady Scott on the Aorangi (Papers Past)", "url": "https://dynamic-rsnz.natlib.govt.nz/newspapers/DOM19130301.2.74"},
   {"title": "History Hit: the widows of Captain Scott's expedition", "url": "https://www.historyhit.com/the-widows-of-captain-scotts-doomed-antarctic-expedition/"}
  ]
 }
]

E = []
def e(date, disp, prec, eye, place, head, dig, quote="", conf="verified", note=""):
    E.append({"date_iso": date, "date_display": disp, "precision": prec, "eye": eye, "place": place,
              "headline": head, "digest": dig, "quote": quote, "confidence": conf, "source_note": note})

# ---- 1910–1911 prelude
e("1910-11-29", "Tuesday 29 November 1910", "day", "shirase", "Shibaura, Tokyo",
  "The Kainan Maru leaves Tokyo for the far south",
  "The expedition's record opens with the small schooner leaving Japan with 27 men and a pack of sled dogs, cheered off by crowds but thinly funded. Shirase has no illusions about the size of his ship against the British and Norwegian expeditions already in the south; his backers want a Japanese flag in Antarctica.",
  conf="approx", note="NIPR translation of the Nankyoku-ki appendix gives 29 Nov 1910; south-pole.com gives 1 Dec 1910. Shown as approx.")
e("1911-03-12", "Sunday 12 March 1911", "day", "shirase", "Ross Sea, 74°16'S",
  "Pack ice turns the Japanese back for the winter",
  "Having reached the Ross Sea too late in the season, the Kainan Maru meets closing pack ice and turns north from 74°16'S before she is trapped. Most of the dogs have already died. Shirase decides to winter in Sydney and try again, a humiliation the Australian press does not let him forget.",
  note="NIPR, Antarctic Record no. 1 (1957), translation of the Nankyoku-ki appendix.")
e("1911-09-08", "Friday 8 September 1911", "day", "amundsen", "Framheim, Bay of Whales",
  "A premature start for the Pole ends in frostbite",
  "Impatient to beat the British, Amundsen takes eight men south as soon as the temperature rises. Within days it falls to about −55°C; the party caches its loads at the 80° depot and runs back in disorder, with frostbitten heels. On the return Johansen and Prestrud are left behind, and Johansen's public anger leads Amundsen to strike him and Prestrud from the Pole party.",
  note="Fram Museum, 'The third Fram expedition 1910–1914'.")
e("1911-10-19", "Thursday 19 October 1911", "day", "amundsen", "Framheim, Bay of Whales",
  "Five men, four sledges and 52 dogs set off at last",
  "After weeks of waiting for steady weather Amundsen asks his men whether they should go, and they leave: five on skis with four sledges of thirteen dogs each, Prestrud filming them away. His diary records the relief of finally getting off. (His Hobart account gives 20 October.)",
  note="Norwegian Polar Institute centenary diary for 19 Oct 2011, linking Amundsen's diary of 19 Oct 1911; The South Pole vol. 2 ('At last we got away, on October 19'). Fram Museum gives 20 Oct.")
e("1911-10-19", "c. 19 October 1911", "range", "bjaaland", "Framheim, Bay of Whales",
  "Bjaaland hopes this start will not be another fiasco",
  "Remembering the September retreat, Bjaaland writes that he hopes this attempt will not end the same way. He also makes himself a promise that, if he comes home alive, he will keep away from polar exploration for good.",
  conf="approx", note="Bjaaland's diary as quoted in the Norwegian Polar Institute centenary diary entry for 19 October; exact day of his entry not stated.")
e("1911-11-01", "Wednesday 1 November 1911", "day", "scott", "Cape Evans, Ross Island",
  "Scott leaves Cape Evans with the ponies",
  "With the motor sledges already ahead (they will soon break down), Scott leads the pony parties out from the hut. His plan stakes everything on ponies across the Barrier and men hauling up the Beardmore Glacier and over the plateau; he knows Amundsen is somewhere to the east with dogs, starting nearer the Pole.",
  conf="approx", note="Standard chronology of the Terra Nova expedition; Scott's journal in 'Scott's Last Expedition' (1913).")
e("1911-11-08", "Wednesday 8 November 1911", "day", "prestrud", "Framheim",
  "The Eastern party leaves for King Edward VII Land",
  "With Johansen and Stubberud, Prestrud sets out east to explore the land Scott had glimpsed in 1902. His report admits that, seeing a distant figure on the ice a few days later, the three had half-believed they had met Japanese or Englishmen before it resolved into something ordinary.",
  note="Prestrud, 'The Eastern Sledge Journey', The South Pole ch. 15: 'On November 8 we left Framheim'; 11 Nov mention of 'Japanese, Englishmen'.")
e("1911-11-19", "Sunday 19 November 1911", "day", "shirase", "Sydney Harbour",
  "Second departure from Sydney, now with science in view",
  "After six months camped at Parramatta, re-provisioned and with a scientist, Takeda Terutarō, the Kainan Maru sails again. The record frames the second voyage as research and exploration: the Pole has become unrealistic, but landing on the Barrier and going as far south as possible has not.",
  note="south-pole.com Shirase page; Polar Journal; Nankyoku-ki appendix (NIPR).")
e("1911-12-02", "Saturday 2 December 1911", "day", "mawson", "Hobart",
  "The Aurora sails from Hobart for the unknown coast",
  "Mawson's Australasian expedition leaves Hobart, heavily loaded, for Macquarie Island and then the coast due south of Australia. His aim is not the Pole but a long stretch of coastline no one has seen, with wireless and a chain of bases.",
  conf="approx", note="Standard AAE chronology; 'The Home of the Blizzard' (1915).")
e("1911-12-03", "c. 3 December 1911", "range", "prestrud", "King Edward VII Land",
  "Bare rock: the first land touched in King Edward VII Land",
  "After a blizzard, the Eastern party sights dark rock showing through the snow on the side of a hill and reaches it, the first positive proof of land in this quarter. They celebrate with an outsize meal of pemmican and chocolate and are then pinned in the tent by a gale for days, with dog food running short.",
  conf="approx", note="Prestrud, The South Pole ch. 15; the day is inferred from his dated entries of 1–7 December.")
e("1911-12-11", "Monday 11 December 1911", "day", "filchner", "Grytviken, South Georgia",
  "The Deutschland leaves South Georgia for the Weddell Sea",
  "After seven weeks at the whaling station, Filchner's ship heads south into the Weddell Sea. His plan is to land a base at its head and test whether the continent is split by a channel to the Ross Sea.",
  note="Second German Antarctic Expedition article (summarising Filchner, 'Zum sechsten Erdteil').")

# ---- 14 December 1911
e("1911-12-14", "Thursday 14 December 1911 (Amundsen's diary heads it Friday 15 December)", "day", "amundsen", "Polheim, 90°S",
  "Three in the afternoon: the Norwegians at the Pole",
  "Amundsen's entry is short: a fine morning clouding over, a flat plateau without sastrugi, three sledges and seventeen dogs left. At three o'clock they halt at the Pole by their reckoning, plant the flag with all five hands on it, and give thanks. A small piece of seal meat each serves as celebration; next day they will ski out in three directions to box in the spot.",
  note="Amundsen diary, quoted in Huntford, 'The Amundsen Photographs' (1987), via scottvsamundsen 14 Dec 1911; Diaries of Note (NPI transcript).")
e("1911-12-14", "Thursday 14 December 1911", "day", "bjaaland", "Polheim, 90°S",
  "No English flag here, only a Norwegian one",
  "Bjaaland's diary records the goal reached and the pride of being first, noting with satisfaction that there is no English flag at the Pole. Then the food: seal steak, biscuits, pemmican and chocolate, as much as they can eat and drink.",
  note="Bjaaland diary, quoted in Huntford, 'Scott and Amundsen' (1980) p. 487, via scottvsamundsen 14 Dec 1911.")
e("1911-12-14", "Thursday 14 December 1911", "day", "scott", "Beardmore Glacier, c. 84°8'S",
  "Same day, 360 miles away: hauling up the glacier",
  "Scott's day is indigestion, wet clothes, cramp and raw blistered lips. The man-hauling parties climb eleven or twelve miles up the Beardmore to about 2,500 feet; swapping sledges, his team finds Bowers's easier to pull. He began the march with little hope and ends it slightly cheered.",
  note="Scott's journal, 'Scott's Last Expedition' vol. 1, via scottvsamundsen 14 Dec 1911.")
e("1911-12-14", "Thursday 14 December 1911", "day", "bowers", "Beardmore Glacier",
  "Ten to fifteen jerks to start the sledge",
  "Bowers describes man-hauling on the glacier as hard, back-breaking work: it takes ten or fifteen violent heaves on the harness simply to get the sledge moving. He does not complain, but the arithmetic of effort is all there.",
  note="Bowers diary, quoted in Huntford, 'Scott and Amundsen' (1980) p. 466, via scottvsamundsen 14 Dec 1911.")
e("1911-12-22", "Friday 22 December 1911", "day", "cherry", "Upper Glacier Depot, c. 85°S",
  "Sent back from the top of the Beardmore",
  "Scott sends the first supporting party (Atkinson, Wright, Cherry-Garrard and Keohane) home from the head of the glacier. Cherry-Garrard records the disappointment and the handshake; in 'The Worst Journey' he later writes that he had no idea it was the last time he would see Wilson and Bowers.",
  conf="approx", note="Standard chronology; Cherry-Garrard, 'The Worst Journey in the World' (1922).")

# ---- January 1912
e("1912-01-04", "Thursday 4 January 1912", "day", "scott", "Polar plateau, c. 87°32'S",
  "The last supporting party turns back; the party becomes five",
  "Scott sends Teddy Evans, Lashly and Crean back and keeps Wilson, Bowers, Oates and Edgar Evans: five men for a tent and rations planned for four, and Bowers without skis. He records the parting as emotional and his confidence high.",
  conf="approx", note="Scott's journal, 'Scott's Last Expedition' vol. 1; standard chronology.")
e("1912-01-16", "Tuesday 16 January 1912", "day", "shirase", "Kainan Bay, Ross Ice Shelf, 78°17'S",
  "A first landing on the Barrier, and a bay named",
  "Four men land at a small inlet on the ice front at 78°17'S and name it Kainan Bay after the ship. Their report is grim: crevasses everywhere and a surface nearly impossible to travel. The ship sails on west towards the Bay of Whales.",
  note="Japanese Antarctic Expedition article (from Nankyoku-ki via Dagnell & Shibata 2011); Polar Journal; south-pole.com.")
e("1912-01-16", "16 January 1912 (as recorded in 'The South Pole')", "day", "amundsen", "Bay of Whales (reported; Amundsen himself on the Barrier homeward)",
  "Norwegian record: the Japanese arrive near our winter quarters",
  "Amundsen's book gives the Norwegian side in a single sentence: on 16 January the Japanese expedition arrived at the Bay of Whales and landed on the Barrier near Framheim. He was still 400 miles south at the time and is relaying what Fram's men told him; elsewhere the Norwegians wrote that they admired how far the Japanese had come in so small and poorly equipped a ship.",
  conf="approx", note="Amundsen, 'The First Account' / The South Pole (tr. Chater 1912). The Japanese record places Kainan Bay on 16 Jan and the Bay of Whales visit on 17 Jan; the Norwegian date may compress the two.")
e("1912-01-17", "Wednesday 17 January 1912", "day", "scott", "South Pole",
  "At the Pole, forestalled: 'an awful place'",
  "Little sleep after yesterday's sight of a black flag; they follow Norwegian ski and dog tracks, then set their own course in a bitter wind at −22°. Evans's hands are badly frostbitten. Scott calls the day horrible and the place dismal, and the bitterness of arriving without priority runs through the entry, softened at the end by hot food, an extra stick of chocolate and a cigarette from Wilson.",
  quote="Great God! this is an awful place",
  note="Scott's journal, 'Scott's Last Expedition' (1913), via scottvsamundsen 17 Jan 1912.")
e("1912-01-17", "Wednesday 17 January 1912", "day", "wilson", "South Pole",
  "The coldest march Wilson can remember",
  "Wilson notes a very bitter day, the sun showing now and then, ice crystals greying the horizon. No cairn or flag in sight; from the direction of the tracks he reckons Amundsen's camp about three miles off. The party agrees the Norwegians have prior claim, since they had made it a race.",
  note="Wilson's diary, quoted in Cherry-Garrard, 'The Worst Journey', ch. 13, via scottvsamundsen 17 Jan 1912.")
e("1912-01-17", "Wednesday 17 January 1912", "day", "bowers", "South Pole",
  "Sad to be forestalled, proud of man-hauling",
  "Bowers writes that it is sad to have been beaten by the Norwegians, but he takes comfort that the British have reached the Pole by their own hauling, without dogs.",
  note="Bowers, 17 Jan 1912, quoted in Crane, 'Scott of the Antarctic' (2005) p. 487, via scottvsamundsen 17 Jan 1912.")
e("1912-01-17", "Wednesday 17 January 1912", "day", "shirase", "Bay of Whales, aboard the Kainan Maru",
  "Two Norwegian officers come aboard the Japanese ship",
  "Moored away from the ice edge near the Fram, the Japanese receive Fram's captain Thorvald Nilsen and Lieutenant Prestrud, entertaining them with wine and cigars. Neither side shares a language, and talk is largely gesture. Shirase, who has turned in, does not meet them; the record notes that the strange ship had first been taken for something hostile.",
  note="Japanese Antarctic Expedition article (Nankyoku-ki via Dagnell & Shibata 2011); Polar Journal on gestures and initial suspicion.")
e("1912-01-17", "Wednesday 17 January 1912", "day", "amundsen", "The Barrier, 81°30'S",
  "Homeward: brilliant skiing, thirty miles a day",
  "On the same day the British stand at the Pole, Amundsen's diary is all speed: grainy snow with a crust the skis glide over, heavy only for the dogs. His packing-case markers stand out clearly. They camp at 81°30'S after thirty nautical miles.",
  conf="approx", note="Amundsen diary via Huntford, 'Race for the South Pole' p. 248; scottvsamundsen notes the entry is headed 18 January and adjusts it to 17 January for his day-ahead error.")
e("1912-01-18", "Thursday 18 January 1912", "day", "scott", "Polheim, the Norwegian tent",
  "Amundsen's tent, his note, and a Union Jack",
  "Bowers spots the Norwegian tent. Inside are the five names and a note from Amundsen asking Scott to forward a letter to King Haakon, which puzzles him. They photograph, build a cairn, raise their own flag in the cold, and Scott ends facing 800 miles of hauling home and the end of their daydreams.",
  note="Scott's journal, 'Scott's Last Expedition', and Huntford (edited-out remark), via scottvsamundsen 18 Jan 1912.")
e("1912-01-18", "Thursday 18 January 1912", "day", "wilson", "Polheim",
  "An inventory of what the Norwegians left",
  "Wilson lists the abandoned gear: reindeer sleeping bags and trousers, a sextant, a hypsometer with broken thermometers. He takes the spirit lamp for sterilising and sketches one of the black marker flags. He also releases the shutter for one of the group photographs.",
  note="Wilson's diary via 'The Worst Journey'; scottvsamundsen 18 Jan 1912.")
e("1912-01-19", "Friday 19 January 1912", "day", "bjaaland", "The Barrier, homeward",
  "Mountains on the first clear day",
  "On the first clear day for a while Bjaaland notes a line of mountains about thirty miles off, running north-east. The Norwegians are well fed, well ahead of schedule, and look about them like tourists.",
  note="Bjaaland diary for 19 Jan 1912, quoted in Huntford, via scottvsamundsen 18 Jan 1912.")
e("1912-01-19", "Friday 19 January 1912", "day", "shirase", "Bay of Whales",
  "Captain Nomura visits the Fram; landing on the ice cliff",
  "The ice shifts and the dangerous landing begins, up a path cut into the Barrier cliff. Captain Nomura Naokichi returns the visit aboard the Fram and is deeply impressed by the ship. The record also notes the Norwegians' disapproval of the rough way the Japanese crew had been catching and killing wildlife.",
  note="Japanese Antarctic Expedition article (Nankyoku-ki via Dagnell & Shibata 2011).")
e("1912-01-20", "Saturday 20 January 1912", "day", "shirase", "Ross Ice Shelf, south-east of the Bay of Whales",
  "The 'Dash Patrol' sets out at noon",
  "Shirase, Takeda, Miisho and the two Ainu dog-drivers leave with twenty days' food, choosing a south-easterly line to keep clear of Amundsen's tracks. Weather stops them almost at once and confines them to the tents the next day; dogs go lame and frostbitten.",
  note="Japanese Antarctic Expedition article (Nankyoku-ki via Dagnell & Shibata 2011); Cool Antarctica.")
e("1912-01-25", "Thursday 25 January 1912", "day", "amundsen", "Framheim",
  "Back at Framheim on the day planned two years earlier",
  "After 99 days and about 3,000 km, the five return with two sledges and eleven dogs. Amundsen notes with satisfaction that his plan of September 1909 had named this very date for the return.",
  note="The South Pole: 'It was on January 25, 1912, that we came into Framheim'. Fram Museum gives 26 Jan.")
e("1912-01-28", "Sunday 28 January 1912", "day", "shirase", "80°5'S, 156°37'W, Ross Ice Shelf",
  "Flag on the snow plain: Yamato Yukihara",
  "With food for only a day or two left, the Dash Patrol stops at 80°5'S. They raise the Japanese flag, salute the Emperor, bury a canister with their names and name the plain Yamato Yukihara. They have not reached the continent proper, and know it, but they have travelled farther south than any Asian expedition before them.",
  note="NIPR translation of Nankyoku-ki appendix (28 Jan, 80°05'S 156°37'W); Polar Journal caption gives 29 Jan.")
e("1912-01-30", "Tuesday 30 January 1912", "day", "filchner", "Weddell Sea, c. 77°S",
  "New land at the head of the Weddell Sea",
  "On 30 January the Deutschland sights an ice-covered coast where charts showed open sea. Filchner names it the Luitpold Coast after the Bavarian Prince Regent, the first proof that the Weddell Sea has a southern shore.",
  note="Second German Antarctic Expedition article (land sighted 30 Jan 1912).")
e("1912-02-04", "Sunday 4 February 1912", "day", "shirase", "Bay of Whales",
  "Leaving in haste, the dogs left behind",
  "With weather closing and ice threatening to trap the ship, everyone is got aboard and the Kainan Maru leaves. Much equipment and all the remaining dogs are abandoned on the ice, a loss the record does not hide.",
  note="Japanese Antarctic Expedition article; Cool Antarctica gives 3 Feb for all aboard.")

# ---- Feb–Mar 1912
e("1912-02-17", "Saturday 17 February 1912", "day", "scott", "Foot of the Beardmore Glacier",
  "'A very terrible day': Edgar Evans dies",
  "Evans, the strongest man in the party in October, has been failing for weeks after a fall and frostbite. He drops behind, is found on his knees with his clothing disarranged and half-conscious, and dies that night in the tent. Scott records it plainly and adds that the party's position is now desperate.",
  note="Scott's journal, 'Scott's Last Expedition' (1913), entry for 17 Feb 1912.")
e("1912-02-18", "Sunday 18 February 1912", "day", "filchner", "Vahsel Bay",
  "The base hut floats away on its iceberg",
  "The hut has just been built on what Filchner took for grounded ice when, on the spring tide, the berg calves and drifts off with it. Men and most of the stores are rescued, but the plan to winter ashore is finished.",
  note="Second German Antarctic Expedition article (hut erected by 17 Feb; calving 18 Feb 1912).")
e("1912-02-27", "Late February 1912", "month", "wilson", "The Barrier, south of the Southern Barrier Depot",
  "Wilson's sledging diary falls silent",
  "Wilson's diary entries thin to lines on temperatures and miles and then stop in late February, as the party crawls across the Barrier short of fuel. He goes on doctoring the others, and carries the geological specimens to the end.",
  conf="approx", note="Wilson's diary (King ed., 1972); exact last date not checked here.")
e("1912-03-07", "c. 7–8 March 1912", "range", "amundsen", "Hobart, Tasmania",
  "Hobart: the news goes out by cable",
  "The Fram anchors at Hobart on 7 March and Amundsen, telling the crowd nothing, cables his brother Leon in Kristiania; the next day the world's papers carry the news. In London The Times sniffs at a mere dash for the Pole; Norwegian papers celebrate.",
  conf="approx", note="Fram Museum (Hobart 7 Mar 1912); 'First Account' dated Hobart 8 March; press reactions via scottvsamundsen 8 Mar 1912.")
e("1912-03-08", "Friday 8 March 1912", "day", "cherry", "One Ton Depot, 79°29'S",
  "Waiting at One Ton, sure he saw them",
  "With Dimitri and two dog teams, Cherry-Garrard waits in winds and −28°F to −40°F. The night before he was so sure he saw the returning party on the horizon that he almost walked out to meet them. He has orders not to risk the dogs and no instruction to go further south.",
  note="Cherry-Garrard diary, 8 Mar 1912, via scottvsamundsen 8 Mar 1912.")
e("1912-03-08", "Friday 8 March 1912", "day", "scott", "The Barrier, c. 70 miles south of One Ton",
  "'In a very bad way': Oates's foot",
  "Scott fears Oates's left foot cannot last and that the time lost on footgear each morning is ruinous. They do 4½ miles. He worries about what fuel and food they will find at the next depot and whether the dogs have reached it.",
  note="Scott's journal, 8 Mar 1912, via scottvsamundsen 8 Mar 1912.")
e("1912-03-15", "Friday 15 March 1912", "day", "filchner", "Weddell Sea",
  "Beset: the Deutschland frozen in for the winter",
  "Failing to get north before the sea freezes, the ship is caught in the pack and begins a drift that will last until late November. Quarrels between Filchner and the ship's officers, already bitter, worsen in the dark months.",
  note="Second German Antarctic Expedition article (beset 15 March 1912).")
e("1912-03-16", "'Friday March 16 or Saturday 17' 1912 (Scott: 'lost track of dates')", "range", "scott", "The Barrier, c. 26 miles south of One Ton",
  "Oates walks out into the blizzard",
  "Scott records that Oates asked to be left in his sleeping bag, marched once more, and the next morning said he was going outside and might be some time, and went into the blizzard. They knew he was walking to his death and did not stop him. Scott writes that Oates's last thoughts were of his mother and calls it the act of a brave soul and an English gentleman. It was Oates's 32nd birthday.",
  quote="I am just going outside and may be some time.",
  note="Scott's journal, 'Scott's Last Expedition' (1913), via scottvsamundsen 17 Mar 1912; Gilbert White's House & the Oates Collections.")
e("1912-03-17", "Sunday 17 March 1912", "day", "cherry", "Hut Point",
  "Back at Hut Point, near breaking",
  "Returned from One Ton, Cherry-Garrard is close to a breakdown with worry. He writes bitterly that Dimitri, ill on the march, recovered as soon as they reached the hut. He does not yet know that the polar party is a few days' march from where he waited.",
  note="Cherry-Garrard diary, 17 Mar 1912 (SPRI), via scottvsamundsen 17 Mar 1912.")
e("1912-03-25", "Late March 1912", "month", "bowers", "The last tent, 11 miles south of One Ton",
  "A last letter to his mother",
  "Pinned by the blizzard, Bowers writes to Emily Bowers. He tells her that the party has done all it could, that he is not afraid, and that he trusts in God; he hopes she will be comforted that he died doing his duty with good companions.",
  conf="approx", note="Bowers's last letter (SPRI); see 'The Last Letters' (SPRI) noted in the Cambridge centenary article. Paraphrase of its widely reported gist; day unknown.")
e("1912-03-29", "Headed 'Thursday, March 29' 1912 (29 March 1912 fell on a Friday)", "day", "scott", "The last tent, 11 miles south of One Ton",
  "Last entry",
  "Scott writes that the gale has blown since the 21st, that they had fuel for two cups of tea a man and food for two days, and that every morning they meant to start for the depot. They will stick it out to the end, but they are weaker and it cannot be far. He signs it and adds a final line.",
  quote="For God's sake look after our people.",
  note="Scott's journal, 'Scott's Last Expedition' (1913), last entry; BL Add MS 51024–51035.")
e("1912-06-20", "Thursday 20 June 1912", "day", "shirase", "Tokyo",
  "Home to crowds, and to debt",
  "The Kainan Maru reaches Yokohama on 19 June and Tokyo the next day, where tens of thousands welcome Shirase as a hero. The expedition's debts follow him for decades; he spends years lecturing to repay them.",
  note="Japanese Antarctic Expedition article; NIPR (19 June); Polar Journal (20 June; debts).")
e("1912-08-08", "Thursday 8 August 1912", "day", "filchner", "Deutschland, beset in the Weddell Sea",
  "Captain Vahsel dies in the ice",
  "Richard Vahsel, the ship's captain, dies of illness during the drift and is buried in the sea two days later. Filchner's narrative records the death soberly; his later private account is franker about how poisoned relations on board had become.",
  note="Second German Antarctic Expedition article (death 8 Aug 1912, buried two days later).")

# ---- Nov 1912 – Feb 1913
e("1912-11-12", "Tuesday 12 November 1912", "day", "gran", "The Barrier, 11 miles south of One Ton",
  "The tent: Scott between his companions",
  "Gran describes Scott in the middle, half out of his bag, Bowers to his right and Wilson to his left; Scott seems to have struggled to the last, the others to have died in their sleep. The tent is collapsed over them, a snow cairn raised, and Gran's skis tied into a cross on top. Atkinson reads the service, and they sing hymns bareheaded as the snow covers the dead.",
  note="Gran diary, 12 Nov 1912, quoted in 'The Norwegian with Scott' (1984) pp. 216–17, via scottvsamundsen 12 Nov 1912; Canterbury Museum on the English diary.")
e("1912-11-12", "Tuesday 12 November 1912", "day", "cherry", "The Barrier, the tent",
  "Everything tidy; the letters and the lamp",
  "Cherry-Garrard notes how orderly the tent was: well pitched, door facing down the sastrugi, no snow inside the lining. Personal things, letters and records lay where they had been left, with a makeshift lamp by Scott that he thinks Scott wrote by to the end. The bodies are not moved; a chapter of Corinthians is read at midnight.",
  note="'The Worst Journey in the World' (1922), ch. 14 (memoir written later from his diary), via scottvsamundsen 12 Nov 1912.")
e("1912-11-13", "Mid-November 1912", "range", "gran", "The Barrier, homeward",
  "Wearing Scott's skis back to the hut",
  "Gran takes Scott's skis for the return to Cape Evans, writing that they must finish the journey, and that they will. The search party also looks for Oates's body to the south without success and raises a memorial cairn near where he was lost.",
  conf="approx", note="Canterbury Museum, on Gran's English diary; Gilbert White's House (cairn inscription).")
e("1912-11-10", "Sunday 10 November 1912", "day", "mawson", "Cape Denison",
  "The Far Eastern party sets out",
  "Mawson, the British soldier Belgrave Ninnis and the Swiss skier and lawyer Xavier Mertz leave the hut with dogs to survey far to the east. They expect to be back in mid-January for the ship.",
  conf="approx", note="Standard AAE chronology; 'The Home of the Blizzard' (1915).")
e("1912-12-14", "Saturday 14 December 1912", "day", "mawson", "Far Eastern journey, c. 480 km east of Cape Denison",
  "Ninnis gone into a crevasse",
  "Soon after his noon latitude, Mawson crosses a snow bridge and calls back a warning; when Mertz stops and looks round there is only a gaping hole. Ninnis, his sledge, the best dogs and most of the food have gone. They call for three hours, read the burial service, and turn for home with almost nothing, ending the entry with a prayer.",
  quote="May God Help us.",
  note="Mawson diary, 14 Dec 1912 (via Mawson's Huts Foundation, 'Catastrophe'); Mertz's diary records the same day. Diary published 1988; quote is his own short phrase.")
e("1913-01-08", "c. 7–8 January 1913", "range", "mawson", "George V Land, homeward",
  "Mertz dies; Mawson alone",
  "Weakened by starvation (later thought to have been worsened by eating the dogs' livers), Mertz becomes delirious and dies in the night. Mawson buries him in his sleeping bag and goes on alone, cutting his sledge in half, more than 150 km from the hut.",
  conf="approx", note="Standard AAE chronology; Mawson's Huts Foundation pages on 'Mawson's fatal journey'.")
e("1913-02-08", "Saturday 8 February 1913", "day", "mawson", "Cape Denison",
  "The ship's smoke on the horizon, hours too late",
  "Mawson reaches the hut to see the Aurora steaming away; six men have stayed behind to look for him. Recalled by wireless, the ship cannot return through the weather, and Mawson faces a second winter. That same day Macquarie Island intercepts the message; the next, they hear of Scott's death.",
  note="Mawson's Huts Foundation, 'Bad news and a breakthrough' (8 Feb interception; Scott news the day after).")
e("1913-02-10", "Monday 10 February 1913", "day", "cherry", "Off Oamaru, New Zealand",
  "Terra Nova at Oamaru, flag at half-mast",
  "The ship arrives off Oamaru at 2.30 in the morning but stays at sea because of the press contract, while Pennell and Atkinson are rowed ashore to send the cable. The crew are ordered to answer no questions. That night the news is in the world's papers.",
  note="'The Worst Journey', ch. 19; Wellington Evening Post 10 Feb 1913, via scottvsamundsen Feb 1913.")
e("1913-02-11", "Tuesday 11 February 1913 (press report)", "day", "amundsen", "Madison, Wisconsin, on a lecture tour",
  "Amundsen hears of Scott's death",
  "On tour in the American Midwest, Amundsen is reported pacing his hotel rooms in dejection and saying he cannot read Scott's last message without emotion. This is a newspaper report, not his diary. His brother Leon writes the condolence letter to the Royal Geographical Society that Amundsen cannot bring himself to write.",
  conf="verified", note="New York Times, 11 Feb 1913, and Leon Amundsen's letter (Huntford p. 562), via scottvsamundsen Feb 1913.")
e("1913-02-12", "Wednesday 12 February 1913", "day", "gran", "Lyttelton, New Zealand",
  "Lyttelton: flags at half-mast",
  "The Terra Nova comes into Lyttelton to find flags lowered everywhere. Gran writes that Scott is dead and the adventure is over, a short entry closing two and a half years of his life.",
  note="Gran diary, 12 Feb 1913, in 'The Norwegian with Scott' p. 237, via scottvsamundsen Feb 1913.")
e("1913-02-17", "c. 17–19 February 1913", "range", "kathleen", "Aboard the Aorangi, Pacific Ocean",
  "Told at sea, a week after the world",
  "On her way to meet her husband in New Zealand, Kathleen Scott is called to the captain, who has received the news by wireless and waited until morning to tell her. Her diary records her keeping her composure in public and the effort it cost. She has been a widow for almost eleven months without knowing.",
  conf="approx", note="Dominion (Wellington), 1 Mar 1913: Captain Stevens of the Aorangi received the news c. midnight 16 Feb and told her after breakfast 17 Feb; other accounts give c. 19 Feb. Diary extracts in 'Self-Portrait of an Artist' (1949).")
e("1912-11-26", "Tuesday 26 November 1912", "day", "filchner", "Weddell Sea",
  "The Deutschland breaks free",
  "After more than eight months in the pack, the ship is released and heads for South Georgia, reaching Grytviken on 19 December. Filchner's plan for a crossing is abandoned; the coast he found keeps his and Luitpold's names.",
  note="Second German Antarctic Expedition article (release 26 Nov; Grytviken 19 Dec 1912).")

DROP={("scott","1911-11-01"),("mawson","1911-12-02"),("mawson","1912-11-10"),("shirase","1911-11-19"),("filchner","1912-11-26"),("shirase","1910-11-29")}
E[:]=[x for x in E if (x["eye"],x["date_iso"]) not in DROP]
E.sort(key=lambda x: (x["date_iso"], x["eye"]))

ch = {
 "id": "south-pole",
 "title": "Five Flags on the Ice: The Race to the South Pole",
 "short_title": "The Race to the South Pole",
 "subtitle": "Norwegian, British, Japanese, German and Australasian expeditions in Antarctica, 1910–1913",
 "span": "1910–1913",
 "intro": [
  "In the southern summer of 1911–12 five national expeditions were at work on one continent that had no human inhabitants at all. The Norwegians under Roald Amundsen were camped at the Bay of Whales on the Ross Ice Shelf; Robert Falcon Scott's British expedition was 400 miles west at Cape Evans on Ross Island; Shirase Nobu's Japanese ship was coming south from Sydney; Wilhelm Filchner's Germans were pushing into the Weddell Sea on the far side; and Douglas Mawson's Australasians were landing on the coast south of Australia. This chapter sets their records side by side.",
  "Antarctica has no Indigenous people, so the encounters here are between the expeditions themselves and with the port towns that fed and reported them: Hobart, Sydney, Wellington, Lyttelton, Buenos Aires and Grytviken. The heart of the chapter is two meetings. On 17 January 1912, the day Scott's party reached the Pole and found Amundsen's tracks, two Norwegian officers were drinking wine aboard the Japanese ship at the Bay of Whales, talking mostly by gesture. The next day the British reached the Norwegian tent and read Amundsen's note. Both meetings are told from both sides where the record allows: the Japanese account survives as a compiled expedition record, the Norwegian one mostly as a sentence in Amundsen's book.",
  "The forms are mixed and are labelled. Scott, Wilson, Bowers, Amundsen, Bjaaland, Gran, Cherry-Garrard, Mawson and Kathleen Scott kept diaries; Prestrud's report and Filchner's narrative are dated accounts written up from journals; Shirase's 'Nankyoku-ki' (1913) is an official record compiled from members' journals; Cherry-Garrard's 'The Worst Journey in the World' (1922) is a later memoir. Scott's published journal (1913) was lightly edited, and Gran revised his diaries for publication decades later. Amundsen's book reached English readers in a 1912 translation and is paraphrased here, not quoted.",
  "The deaths are told as the diarists recorded them, without embellishment: Edgar Evans on 17 February 1912, Lawrence Oates about 16–17 March, and Scott, Wilson and Bowers in their tent at the end of March, eleven miles from a depot; then, on Mawson's journey that December and January, Belgrave Ninnis and Xavier Mertz. The tent was found on 12 November 1912, and the world learned the news on 10–11 February 1913, almost a year after the deaths and eleven months after the cable from Hobart that announced Amundsen's success.",
  "Read together, the pages show how differently the same weeks felt. On 14 December 1911 Bjaaland is eating seal steak at the Pole while Bowers needs fifteen jerks to start his sledge on the Beardmore. On 17 January Amundsen is skiing thirty miles a day homeward on a perfect crust while Scott writes the most famous sentence of the race. In March, Cherry-Garrard waits at One Ton with the dogs and the polar party struggles towards a depot it never reaches."
 ],
 "calendar_note": "All dates are Gregorian (Japan had used the Gregorian calendar since 1873). The Ross Sea region straddles the 180° meridian, and the expeditions kept their own dates: Amundsen's diary on the polar journey ran one day ahead (his Pole entry is headed Friday 15 December for Thursday 14 December), and some quotations of his diary are re-dated by one day by modern editors; Scott wrote in mid-March that he had lost track of dates, so the Oates entry is 'March 16 or 17', and his last entry is headed 'Thursday, March 29' though 29 March 1912 fell on a Friday. Dates are given as each diarist recorded them, with the conventional dates of the main events.",
 "eyes": eyes,
 "entries": E,
 "convergences": [
  {"date": "1911-12-14", "label": "Amundsen's party reaches the Pole", "eyes": ["amundsen", "bjaaland", "scott", "bowers"],
   "note": "At Polheim the Norwegians feast and thank God; Bjaaland savours the absence of an English flag. The same day, some 360 miles north, Scott's diary is blisters and cramp and Bowers's is the brute work of starting a sledge on the Beardmore. None of the British knows."},
  {"date": "1912-01-17", "label": "Scott at the Pole; the Norwegians aboard the Kainan Maru", "eyes": ["scott", "wilson", "bowers", "shirase", "prestrud", "amundsen"],
   "note": "Scott calls the Pole an awful place and Wilson concedes the Norwegian claim, while at the Bay of Whales Nilsen and Prestrud accept wine and cigars from Japanese hosts with whom they share no language, and Amundsen, homeward on the Barrier, records only perfect snow. Three expeditions, three moods on one calendar day."},
  {"date": "1912-01-18", "label": "The British at the Norwegian tent", "eyes": ["scott", "wilson", "bjaaland"],
   "note": "Scott reads Amundsen's note and is puzzled by being asked to carry a letter to a king; Wilson calmly lists and borrows the Norwegians' gear. Bjaaland's next entry is about mountains seen on a clear day."},
  {"date": "1912-01-28", "label": "Furthest south for the Japanese; the Deutschland nears new land", "eyes": ["shirase", "filchner", "amundsen"],
   "note": "Shirase plants a flag at 80°5'S on the Ross Ice Shelf two days before Filchner sights the Luitpold Coast on the far side of the continent; Amundsen is already back at Framheim."},
  {"date": "1912-03-08", "label": "The news from Hobart; waiting at One Ton", "eyes": ["amundsen", "cherry", "scott"],
   "note": "As Amundsen's cable becomes world news, Cherry-Garrard waits at One Ton Depot and Scott records that Oates's foot cannot last. The world now knows who won; it will not know for eleven months what that meant for the losers."},
  {"date": "1912-03-16", "label": "Oates walks out; Cherry-Garrard back at Hut Point; the Deutschland beset", "eyes": ["scott", "cherry", "filchner"],
   "note": "Within the same few days the polar party loses Oates, Cherry-Garrard returns from One Ton half-broken by worry, and Filchner's ship is frozen in for a winter of drift on the other side of the continent."},
  {"date": "1912-11-12", "label": "The tent found", "eyes": ["gran", "cherry"],
   "note": "Gran, the Norwegian, records the positions of the bodies and his skis made into a cross; Cherry-Garrard records the tidiness and the lamp. Mawson, far to the west, is two days into the journey that will kill both his companions."},
  {"date": "1913-02-10", "label": "The world learns", "eyes": ["cherry", "amundsen", "gran", "mawson", "kathleen"],
   "note": "In one week the Terra Nova lands its cable at Oamaru, Amundsen hears the news in Wisconsin, Gran sees half-masted flags at Lyttelton, Mawson's men on Macquarie Island hear it the day after they learn their own leader is stranded, and Kathleen Scott is told at sea."}
 ],
 "ties": [
  {"a": "scott", "b": "amundsen", "kind": "opposite sides", "note": "Amundsen's telegram reached Scott in Melbourne in October 1910; Scott read Amundsen's note in the tent at the Pole on 18 January 1912 and carried the letter for King Haakon, which was found with his body."},
  {"a": "prestrud", "b": "shirase", "kind": "met", "note": "On 17 January 1912 Prestrud and Fram's captain Nilsen visited the Kainan Maru at the Bay of Whales; Shirase had turned in and did not meet them, though his record describes the visit."},
  {"a": "scott", "b": "wilson", "kind": "met", "note": "Close friends since the Discovery expedition; they died in the same tent, and Wilson's last letters include one to Scott's family."},
  {"a": "wilson", "b": "cherry", "kind": "influenced", "note": "Wilson chose Cherry-Garrard for the expedition and the winter journey; 'The Worst Journey' is in part a memorial to him and prints his diary."},
  {"a": "bowers", "b": "cherry", "kind": "met", "note": "Companions on the midwinter Emperor penguin journey of 1911; Cherry-Garrard later found Bowers in the tent."},
  {"a": "gran", "b": "scott", "kind": "met", "note": "Recruited by Scott on Nansen's advice to teach skiing; Gran found Scott's body and wore his skis back to the hut."},
  {"a": "gran", "b": "amundsen", "kind": "opposite sides", "note": "A Norwegian in the British camp while his countryman raced it; his diary records the double loyalty."},
  {"a": "amundsen", "b": "bjaaland", "kind": "met", "note": "Shared the tent and sledges of the Norwegian polar party; Bjaaland photographed the party at the Pole."},
  {"a": "amundsen", "b": "prestrud", "kind": "met", "note": "Amundsen removed Prestrud from the Pole party after the failed September start and gave him the Eastern journey instead."},
  {"a": "mawson", "b": "scott", "kind": "met", "note": "Mawson declined Scott's invitation to join the Terra Nova so that he could lead his own expedition to the coast south of Australia."},
  {"a": "kathleen", "b": "scott", "kind": "relative", "note": "Husband and wife; Scott's last letters include one to her, beginning 'To my widow'."},
  {"a": "filchner", "b": "amundsen", "kind": "same street", "note": "The Deutschland and the Fram were both in Buenos Aires in September–October 1911, the Fram having landed Amundsen's party in Antarctica; no meeting of their records is claimed here."},
  {"a": "shirase", "b": "mawson", "kind": "mentioned", "note": "Both expeditions depended on Sydney and its scientists; Mawson's mentor Edgeworth David befriended the Japanese while they wintered there in 1911."}
 ],
 "threads_out": [
  {"to": "fram", "note": "Amundsen's South Pole expedition was the Fram's third voyage (1910–14), in the ship built for Nansen's Arctic drift; Fram's captain Nilsen and Prestrud are the Norwegians who met the Japanese at the Bay of Whales."},
  {"to": "north-pole", "note": "Amundsen turned south only after Cook (1908) and Peary (1909) claimed the North Pole, which wrecked the financing of his planned Arctic drift; he later flew over the North Pole in the airship Norge (1926)."},
  {"to": "everest-1953", "note": "Edmund Hillary of the 1953 Everest climb led the New Zealand party of the Commonwealth Trans-Antarctic Expedition to the South Pole in January 1958, the first party to reach it overland since Scott's."},
  {"to": "v1:ww1", "note": "Many of these men went straight into the First World War: Gran as a pilot after making the first flight across the North Sea in July 1914, Cherry-Garrard with armoured cars in Flanders, Filchner in the German army, and Teddy Evans, leader of Scott's last supporting party, as a destroyer captain."},
  {"to": "endeavour", "note": "Cook sailed in 1768 under secret orders to look for a southern continent; this chapter is that continent finally reached at its centre, 143 years later."}
 ],
 "images": [
  {"url": "https://collections.sea.museum/objects/192567/the-polar-party-at-the-south-pole", "title": "The Polar Party at the South Pole", "caption": "Scott, Bowers, Wilson, Oates and Evans at the Pole on 18 January 1912, taken by Bowers with a string to the shutter; the plates were found in the tent.", "date": "18 January 1912", "credit": "Henry Bowers; Australian National Maritime Museum"},
  {"url": "https://teara.govt.nz/en/photograph/37192/scotts-party-at-the-norwegian-tent", "title": "Scott's party at the Norwegian tent", "caption": "The British polar party beside Amundsen's tent Polheim, where Scott found Amundsen's note.", "date": "January 1912", "credit": "Te Ara – The Encyclopedia of New Zealand"},
  {"url": "https://col.rct.uk/collection/2580039/at-the-south-pole", "title": "At the South Pole", "caption": "Print of the British party at the Pole in the Royal Collection, part of the memorial culture that grew around the expedition after 1913.", "date": "1912 (print 1913)", "credit": "Royal Collection Trust"},
  {"url": "https://nettarkiv.npolar.no/www.nansenamundsen.no/en/galleries/amundsen/south-pole-1911/index.html", "title": "Amundsen's South Pole expedition, 1911 (gallery)", "caption": "Norwegian Polar Institute gallery of the Norwegian journey, including the party at Polheim with the Norwegian flag, mostly photographed by Bjaaland.", "date": "1911", "credit": "Norwegian Polar Institute"},
  {"url": "https://southpolestation.com/trivia/igy1/olav.html", "title": "Bjaaland at the Pole, inscribed 1961", "caption": "Bjaaland's photograph of himself and Wisting taking observations at the Pole, December 1911, which he inscribed fifty years later with a greeting to the American station.", "date": "December 1911 / 1961", "credit": "Olav Bjaaland; southpolestation.com"},
  {"url": "https://teara.govt.nz/mi/photograph/36228/members-of-the-japanese-antarctic-expedition-1911", "title": "Members of the Japanese Antarctic Expedition, 1911", "caption": "Shirase's men photographed in New Zealand on their first voyage south, before wintering in Sydney.", "date": "1911", "credit": "Te Ara – The Encyclopedia of New Zealand"},
  {"url": "https://www.ndl.go.jp/portrait/e/datas/281.html", "title": "Shirase Nobu", "caption": "Portrait of the leader of the Japanese expedition, from the National Diet Library's portraits of modern Japanese historical figures.", "date": "early 20th century", "credit": "National Diet Library, Japan"}
 ],
 "further": [
  {"title": "Amundsen, The South Pole, vol. 2 (tr. Chater, 1912), Project Gutenberg", "url": "https://www.gutenberg.org/cache/epub/3415/pg3415.html"},
  {"title": "Cherry-Garrard, The Worst Journey in the World (Standard Ebooks)", "url": "https://standardebooks.org/ebooks/apsley-cherry-garrard/the-worst-journey-in-the-world/text/chapter-18"},
  {"title": "Scott vs Amundsen: a day-by-day blog of both expeditions' diaries", "url": "https://scottvsamundsen.blogspot.com/"},
  {"title": "Mawson's Huts Foundation: Mawson's fatal journey", "url": "https://mawsonshuts.antarctica.gov.au/cape-denison/mawsons-fatal-journey/"},
  {"title": "Mawson, The Home of the Blizzard (Australian Antarctic Division)", "url": "https://www.antarctica.gov.au/about-antarctica/history/exploration-and-expeditions/australasian-antarctic-expedition/home-of-the-blizzard-book/chapter27/"},
  {"title": "Archives Hub: Lawrence Oates collection (SPRI)", "url": "https://archiveshub.ac.uk/search/archives/9a999d72-cade-3a48-816c-caab1a90900f"},
  {"title": "Archives Hub: Tryggve Gran collection (SPRI)", "url": "https://archiveshub.ac.uk/search/archives/3bd36e1c-7795-302e-a675-d50f8bad4d76"},
  {"title": "NIPR: Nankyoku-ki appendix in English (Antarctic Record 1957)", "url": "https://nipr.repo.nii.ac.jp/record/6803/files/KJ00002475816.pdf"}
 ],
 "vantage_key": "0 = in a polar party at or near the Pole; 1 = on the Ross Ice Shelf in support, at the bases, or meeting the other expeditions; 2 = elsewhere on the continent on another expedition; 3 = in the home countries; 4 = abroad or at sea, hearing the news."
}
json.dump(ch, open(OUT, "w"), ensure_ascii=False, indent=1)
print(len(eyes), len(E))
