import json
OUT="/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/vol10/ch-iwakura-1871.json"
LAN="https://ia801300.us.archive.org/31/items/japaneseinameric00lanm/japaneseinameric00lanm_djvu.txt"
UDEL="https://www1.udel.edu/History-old/figal/Hist370/text/er/iwakura.pdf"
MAYO="https://www.cambridge.org/core/journals/journal-of-asian-studies/article/catechism-of-western-diplomacy-the-japanese-and-hamilton-fish-1872/80A3FF41485BCD9961E600084BD95657"
MHS="https://masshist.org/object-of-the-month/february-2014"
SALT="https://explore.saltairecollection.org/files/original/e5e80c580437c03a38470a269564bc95c4282e4f.pdf"
KEIO="https://www.keio.ac.jp/en/about/public-relations/mita-hyoron/koenroku/202402-1"
KREBS="https://www.dijtokyo.org/wp-content/uploads/2016/09/103-124_DIE-IWAKURA-MISSION-IN-PREUSSEN_Mono_32_Krebs-7.pdf"
KOREA="https://koreascience.kr/article/JAKO201323965810532.pdf"
KANSAI="https://kansai-u.repo.nii.ac.jp/record/13074/files/KU-0400-20190401-17.pdf"
DES="https://www.deseret.com/2014/7/13/20544715/drew-clark-samurai-visiting-salt-lake-in-1872-launched-interactions-between-japanese-and-mormons"
GUT="https://gutenberg.org/files/13012/old/13012-h/13012-h.htm"
HABS="https://habsburger.net/en/chapter/logbook-kume-kunitake"
WIKI="https://en.wikipedia.org/wiki/Iwakura_Mission"
NAJ="https://www.digital.archives.go.jp/DAS/pickup/view/print/printArchivesEn/0000000709"
SPEC="https://archive.spectator.co.uk/article/24th-august-1872/3/the-lions-of-loudon-just-now-are-the-japanese-amba"

eyes=[
 dict(id="kume",short="Kume",name="Kume Kunitake",life="1839–1931",
  role="Scholar of the former Saga domain, aged 32; private secretary to Iwakura and the embassy's appointed recorder",
  side="Japan; the Meiji government's embassy",where="With the embassy throughout: America, Britain, the Continent, the voyage home",
  lat=51.507,lon=-0.128,waypoints=[{"lat":35.444,"lon":139.638,"label":"Yokohama, Dec 1871"},{"lat":37.79,"lon":-122.40,"label":"San Francisco, Jan 1872"},{"lat":40.76,"lon":-111.89,"label":"Salt Lake City, Feb 1872"},{"lat":38.90,"lon":-77.04,"label":"Washington, Mar–Jul 1872"},{"lat":51.507,"lon":-0.128,"label":"London and the British tour, Aug–Dec 1872"},{"lat":52.52,"lon":13.40,"label":"Berlin, Mar 1873"}],
  vantage=0,vantage_label="the embassy's official recorder",form="travel journal (official record, compiled from notes and published 1878)",language="Japanese (kanbun-style prose)",
  authenticity="Tokumei Zenken Taishi Bei-Ō Kairan Jikki, 5 volumes, Tokyo 1878, compiled by Kume from his own notes and the embassy's papers after the return; it is a worked-up official account rather than a day-book, and some dates in it disagree with the host press (e.g. a Berlin school visit). English translation: The Iwakura Embassy 1871–73, ed. Graham Healey and Tsuzuki Chūshichi, 5 vols (Japan Documents, 2002); read here only in digest.",
  bio="A Confucian-trained scholar who became, through this book, one of Meiji Japan's founding historians. His account measures everything: mill output, road costs, school hours, the price of granite. He admires and criticises in the same paragraph, and his record is the spine on which the other eyes in this chapter are laid.",
  sources=[{"title":"Kume Kunitake (overview, edition and translation details)","url":"https://en.wikipedia.org/wiki/Kume_Kunitake"},{"title":"From the Logbook of Kume Kunitake (Vienna)","url":HABS}]),
 dict(id="kido",short="Kido",name="Kido Takayoshi",life="1833–1877",
  role="Councillor (sangi) of the Meiji government from Chōshū, aged 38; vice-ambassador",
  side="Japan; the embassy",where="With the embassy in America, Britain and the Continent; left it in spring 1873 and reached Japan in July",
  lat=38.90,lon=-77.04,waypoints=[{"lat":35.444,"lon":139.638,"label":"Yokohama, Dec 1871"},{"lat":38.90,"lon":-77.04,"label":"Washington, 1872"},{"lat":53.835,"lon":-1.79,"label":"Saltaire, Oct 1872"},{"lat":51.507,"lon":-0.128,"label":"London, late 1872"},{"lat":52.52,"lon":13.40,"label":"Berlin, Mar 1873"},{"lat":35.69,"lon":139.69,"label":"Tokyo, Jul 1873"}],
  vantage=0,vantage_label="vice-ambassador keeping a private diary",form="diary",language="Japanese",
  authenticity="Kido's diary survives and was printed in Japanese as Kido Takayoshi nikki (1932–33). English: The Diary of Kido Takayoshi, trans. Sidney DeVere Brown and Akiko Hirota, 3 vols (University of Tokyo Press, 1983–86). Read here only in digest, through the translation and studies that cite it.",
  bio="One of the three great men of the Restoration, older and more cautious than Itō and Ōkubo. His diary is private and often irritable: it records sights, but also friction inside the embassy, and his growing conviction that Japan needed schools and a constitution before it needed wars.",
  sources=[{"title":"The Diary of Kido Takayoshi (CiNii catalogue record)","url":"https://ci.nii.ac.jp/ncid/BA00384223?l=en"}]),
 dict(id="okubo",short="Ōkubo",name="Ōkubo Toshimichi",life="1830–1878",
  role="Finance Minister (Ōkura-kyō) from Satsuma, aged 41; vice-ambassador",
  side="Japan; the embassy",where="America (with a return trip to Japan for credentials, spring–summer 1872), Britain, France, Germany; went home from Europe in spring 1873",
  lat=51.507,lon=-0.128,waypoints=[{"lat":38.90,"lon":-77.04,"label":"Washington, Mar 1872"},{"lat":35.69,"lon":139.69,"label":"Tokyo, for credentials, May 1872"},{"lat":51.507,"lon":-0.128,"label":"London, autumn 1872"},{"lat":52.52,"lon":13.40,"label":"Berlin, Mar 1873"}],
  vantage=0,vantage_label="vice-ambassador writing home",form="dated letters",language="Japanese",
  authenticity="Ōkubo kept no full diary for the journey; his letters home (to Saigō Takamori, Yoshii Tomozane and others) are printed in Ōkubo Toshimichi monjo (1927–29). No complete English translation exists; read here only in digest from studies that cite them, and dated only approximately.",
  bio="The hard-headed Satsuma administrator who would dominate the government after 1873. His letters show a man less interested in parliaments than in factories, and most impressed, in Berlin, by a state that had made itself strong quickly.",
  sources=[{"title":"Ōkubo Toshimichi: his political and economic policies (Journal of Asian Studies)","url":"https://www.cambridge.org/core/journals/journal-of-asian-studies/article/okubo-toshimichi-his-political-and-economic-policies-in-early-meiji-japan/27FFF10E33442589F3E8E6888C10FB37"}]),
 dict(id="ito",short="Itō",name="Itō Hirobumi",life="1841–1909",
  role="Assistant Vice-Minister of Public Works from Chōshū, aged 30; vice-ambassador and the embassy's English speaker",
  side="Japan; the embassy",where="San Francisco, Washington, the return trip for credentials, Britain and the Continent",
  lat=37.79,lon=-122.40,waypoints=[{"lat":37.79,"lon":-122.40,"label":"San Francisco, Jan 1872"},{"lat":38.90,"lon":-77.04,"label":"Washington, 1872"},{"lat":51.507,"lon":-0.128,"label":"London, 1872"}],
  vantage=0,vantage_label="vice-ambassador speaking in English",form="speech (printed in the press)",language="English (delivered in English)",
  authenticity="The 'Hi no maru' (rising sun) speech at the Grand Hotel, San Francisco, was given in English and printed in American newspapers in 1872; it was reprinted by John R. Black in Young Japan, vol. 2 (1881), pp. 358–360, from which modern source-books take it. Some reprints carry the lunar date (Meiji 4, 12th month, 14th day) as if it were Western.",
  bio="The youngest of the leaders and one of the 'Chōshū Five' who had studied in London in 1863. He was the embassy's public voice in America, and the one who pressed hardest for trying to sign a new treaty in Washington, a gamble that failed.",
  sources=[{"title":"Meiji Japan Through Contemporary Sources, vol. 2, excerpt (Itō's speech from Black, Young Japan)","url":UDEL}]),
 dict(id="iwakura",short="Iwakura",name="Iwakura Tomomi",life="1825–1883",
  role="Court noble and Minister of the Right (Udaijin), aged 46; ambassador plenipotentiary and head of the embassy",
  side="Japan; the embassy",where="At the head of the embassy for the whole journey",
  lat=38.90,lon=-77.04,waypoints=[{"lat":37.79,"lon":-122.40,"label":"San Francisco, Jan 1872"},{"lat":38.90,"lon":-77.04,"label":"Washington, Mar–Jul 1872"},{"lat":51.483,"lon":-0.604,"label":"Windsor, 5 Dec 1872"},{"lat":48.857,"lon":2.352,"label":"Paris, Dec 1872"},{"lat":52.52,"lon":13.40,"label":"Berlin, Mar 1873"},{"lat":35.444,"lon":139.638,"label":"Yokohama, 13 Sep 1873"}],
  vantage=0,vantage_label="the ambassador",form="speeches, formal addresses and official letters",language="Japanese (delivered through interpreters)",
  authenticity="Iwakura's formal replies and addresses were delivered in Japanese and printed in English translation in the American and British press and in Lanman's The Japanese in America (1872); his negotiating positions survive in the minutes of the State Department and Foreign Office conferences and in his letters, known here through Mayo (1967).",
  bio="A court aristocrat who had plotted the Restoration and now led the government's most senior members abroad for almost two years. He kept his topknot and court dress at first and changed to Western clothes in America; in the record he is the formal voice, careful and ceremonial.",
  sources=[{"title":"Mayo, 'A Catechism of Western Diplomacy: The Japanese and Hamilton Fish, 1872', JAS 26:3 (1967)","url":MAYO}]),
 dict(id="mori",short="Mori",name="Mori Arinori",life="1847–1889",
  role="Japan's chargé d'affaires in Washington, aged 24",
  side="Japan; the Washington legation",where="Washington",lat=38.90,lon=-77.04,
  vantage=1,vantage_label="Japan's man already in Washington",form="dated letters (official and private)",language="English and Japanese",
  authenticity="Mori's letters of 1871–72 survive in State Department files, in Lanman's The Japanese in America (1872), which prints his letter of 12 January 1872, and in his own collection Education in Japan (1873).",
  bio="A Satsuma man educated in London and America, sent to Washington in 1871 as Japan's first resident diplomat there. He met the embassy as its host and adviser, urged the attempt to sign a treaty, and became the channel for the request that Tokyo send fuller powers.",
  sources=[{"title":"Lanman (ed.), The Japanese in America (1872), full text","url":LAN}]),
 dict(id="tsuda",short="Tsuda Ume",name="Tsuda Umeko (Ume)",life="1864–1929",
  role="Aged 6 at departure (born 31 December 1864, so 7 by Western count within days); the youngest of five girls sent to be educated in America",
  side="Japan; the embassy's students",where="Georgetown, District of Columbia, in the Lanman household, 1872–1882",
  lat=38.909,lon=-77.065,waypoints=[{"lat":35.444,"lon":139.638,"label":"Yokohama, Dec 1871"},{"lat":38.909,"lon":-77.065,"label":"Georgetown, 1872–82"},{"lat":35.444,"lon":139.638,"label":"Yokohama, Nov 1882"}],
  vantage=1,vantage_label="a child left behind in America",form="dated letters (written later, from 1882)",language="English",
  authenticity="No diary from her childhood journey is used here. Her letters to Adeline Lanman, begun on her return to Japan in 1882, were published as The Attic Letters: Ume Tsuda's Correspondence to Her American Mother, ed. Yoshiko Furuki et al. (1991); read in digest only. Her own childhood is known mainly through the Lanmans and later biographies.",
  bio="She went to America knowing no English and came back eleven years later having nearly lost her Japanese. Her later letters look back at the bargain the embassy made with five girls, and she founded what became Tsuda University in 1900. Her gaze in this chapter is the long one: the mission seen from the far end of the decade it set in motion.",
  sources=[{"title":"Tsuda Umeko (overview)","url":"https://en.wikipedia.org/wiki/Tsuda_Umeko"},{"title":"Woods Hole Museum: Umeko Tsuda and Sutematsu Yamakawa","url":"https://woodsholemuseum.org/JapaneseWH/pages/iwakura.html"}]),
 dict(id="lanman",short="Lanman",name="Charles Lanman",life="1819–1895",
  role="American writer and painter, aged 52; American Secretary of the Japanese Legation in Washington",
  side="United States; in Japanese service",where="Washington and Georgetown",lat=38.909,lon=-77.065,
  vantage=1,vantage_label="American host on the Japanese payroll",form="edited book of dated documents and reports (published 1872)",language="English",
  authenticity="The Japanese in America, edited by Charles Lanman (New York: University Publishing Company, 1872), collects reports of the embassy's arrival, speeches and students' essays, printed within the year; it is a host's compilation, not a diary.",
  bio="A prolific travel writer who worked for Mori at the legation and took the young Tsuda Ume into his childless household in Georgetown. His book is the American side's first attempt to explain the visitors to its own readers, earnest and admiring.",
  sources=[{"title":"The Japanese in America (1872), full text","url":LAN}]),
 dict(id="fish",short="Fish",name="Hamilton Fish",life="1808–1893",
  role="US Secretary of State, aged 63",side="United States; the Grant administration",where="Washington, the State Department",lat=38.897,lon=-77.04,
  vantage=1,vantage_label="the negotiator across the table",form="diary",language="English",
  authenticity="Fish's manuscript diary is in the Hamilton Fish Papers, Library of Congress; it is unpublished, and its 1872 entries on the Japanese are known here through Marlene Mayo's study (1967), which cites entries of 18 January, 6 and 12 March and 10 July 1872. Content in digest is drawn from that study and given as approximate.",
  bio="A New York patrician and careful lawyer who ran Grant's foreign policy. Faced with an embassy that wanted to negotiate without full powers and then to move talks to Europe, he held to diplomatic form, and his diary is the hosts' most private record of the failed talks.",
  sources=[{"title":"Mayo (1967), JAS, citing Fish's diary","url":MAYO}]),
 dict(id="grant",short="Grant",name="Ulysses S. Grant",life="1822–1885",
  role="President of the United States, aged 49",side="United States",where="Washington, the White House",lat=38.898,lon=-77.037,
  vantage=1,vantage_label="the head of state receiving them",form="speeches and state papers",language="English",
  authenticity="Grant's remarks at the audience of 4 March 1872 were printed in the press; his Fourth Annual Message (2 December 1872) is printed in Richardson's Compilation of the Messages and Papers of the Presidents, vol. 7, and is US government public domain.",
  bio="The Union general turned president received the first Japanese ambassadors since 1860. His public words are brief and official, but they frame the embassy as the Americans wished to see it: a progressive nation coming to learn.",
  sources=[{"title":"Richardson, Messages and Papers of the Presidents, vol. 7 (Project Gutenberg)","url":GUT}]),
 dict(id="snow",short="Lorenzo Snow",name="Lorenzo Snow",life="1814–1901",
  role="Latter-day Saint apostle, aged 57; President of the Council of the Utah Territorial Legislature",
  side="United States; Utah Territory",where="Salt Lake City",lat=40.76,lon=-111.89,
  vantage=1,vantage_label="host in the snowbound city",form="speech (printed in the local press)",language="English",
  authenticity="Snow's address of 16 February 1872 was printed in Salt Lake City papers at the time; the passage used here is quoted in the Deseret News (2014).",
  bio="A leader of a community that was itself regarded as alien by much of America. His welcome turned the usual direction of the visit around, asking the Japanese for lessons in government.",
  sources=[{"title":"Deseret News, 'Samurai visiting Salt Lake in 1872'","url":DES}]),
 dict(id="holmes",short="Holmes",name="Oliver Wendell Holmes Sr.",life="1809–1894",
  role="Physician, poet and essayist, aged 62",side="United States; Boston",where="Revere House, Boston",lat=42.361,lon=-71.063,
  vantage=1,vantage_label="poet at the farewell banquet",form="occasional poem (read aloud, printed 1872)",language="English",
  authenticity="Holmes's poem for the Boston Board of Trade banquet of 2 August 1872 was printed in the Boston press and in the banquet's published proceedings; the line used here is cited by the Massachusetts Historical Society.",
  bio="Boston's after-dinner laureate. His verse, full of puns about the 1872 presidential race, shows a host city enjoying itself as much as studying its guests.",
  sources=[{"title":"Massachusetts Historical Society, Object of the Month, February 2014","url":MHS}]),
 dict(id="victoria",short="Victoria",name="Queen Victoria",life="1819–1901",
  role="Queen of the United Kingdom, aged 53",side="Britain; the court",where="Windsor Castle",lat=51.483,lon=-0.604,
  vantage=1,vantage_label="the monarch who kept them waiting",form="journal",language="English",
  authenticity="The Queen's journal survives in the Royal Archives, partly in her own hand and partly in Princess Beatrice's later transcript; it is online through the Royal Archives' Queen Victoria's Journals project. Her entry for 5 December 1872 is not quoted here and is given in digest as approximate.",
  bio="The embassy reached Britain in August while she was in Scotland and waited until December for its audience. Her view is a court view: dress, bows, interpreters, the letter from the Emperor.",
  sources=[{"title":"Keio University lecture on the Iwakura Mission in Britain","url":KEIO}]),
 dict(id="britpress",short="British press",name="The British press (The Spectator, The Times, Illustrated London News, Newcastle Daily Chronicle, Bradford Daily Telegraph)",life="newspapers, 1872",
  role="London and provincial newspapers reporting the embassy's tour",side="Britain; the press",where="London, Newcastle, Bradford",lat=51.513,lon=-0.104,
  waypoints=[{"lat":51.513,"lon":-0.104,"label":"London papers"},{"lat":54.973,"lon":-1.614,"label":"Newcastle, Oct 1872"},{"lat":53.795,"lon":-1.759,"label":"Bradford, Oct 1872"}],
  vantage=2,vantage_label="reporters at the factory gate",form="newspaper",language="English",
  authenticity="Dated issues of 1872, cited through the Saltaire Collection, the Spectator Archive and studies of the British tour (Korea Science, Kansai University). Each entry names its paper.",
  bio="A collective eye: the press that followed the Japanese through dockyards, mills and banquets. It moved from curiosity about costume to a recognition that these visitors were measuring Britain.",
  sources=[{"title":"Spectator Archive, 24 August 1872","url":SPEC},{"title":"Saltaire Collection: the Iwakura Mission at Saltaire","url":SALT}]),
]

E=[]
def e(d,disp,prec,eye,place,head,dig,quote,conf,note):
    E.append(dict(date_iso=d,date_display=disp,precision=prec,eye=eye,place=place,headline=head,digest=dig,quote=quote,confidence=conf,source_note=note))

e("1871-12-23","Saturday 23 December 1871 (Meiji 4, 11th month, 12th day)","day","kume","Yokohama, aboard the Pacific Mail steamer America","Embassy sails from Yokohama with its students",
 "The Jikki opens with the embarkation at Yokohama: ambassador, four vice-ambassadors, about fifty officials and secretaries, and some sixty students and attendants, among them five girls. The ship was the American paddle-steamer America, bound for San Francisco. Kume frames the departure as a deliberate act of state, the government sending its own leaders abroad to see for themselves.",
 "","verified","Departure date with lunar equivalent: Keio University lecture; Wikipedia, Iwakura Mission. Content of the Jikki's opening given in general terms.")
e("1871-12-23","23 December 1871 (Meiji 4, 11th month, 12th day)","day","kido","Yokohama harbour","A councillor's diary goes to sea",
 "Kido's diary, still dated by the lunar calendar, records the leave-taking from Yokohama and the start of the Pacific crossing. He was one of the most senior men in the government, now leaving it for what was planned as ten months and became almost two years.",
 "","approx","Kido's diary (Brown and Hirota trans., vol. 2); entry content summarised generally.")
e("1872-01-12","12 January 1872","day","mori","Washington, Japanese legation","Mori tells Washington when to expect the embassy",
 "Writing from the legation, Mori informed the American side that the embassy had sailed and should reach Washington toward the end of the month. Lanman printed the letter within the year. In the event snow in the Rockies delayed the party by weeks.",
 "about the close of the present month","verified","Lanman (ed.), The Japanese in America (1872), Mori's letter of 12 January 1872.")
e("1872-01-15","15 January 1872 (Meiji 4, 12th month, 6th day)","day","lanman","Report of the arrival at San Francisco","The America lands 107 Japanese at San Francisco",
 "Lanman's compilation records the steamer's arrival with its Japanese passengers: forty-nine members of the embassy and, travelling under the care of the American minister Charles DeLong and his family, five young ladies and fifty-three young gentlemen and servants.",
 "one hundred and seven Japanese passengers","verified","Lanman (ed.), The Japanese in America (1872), opening account.")
e("1872-01-15","15 January 1872","day","kume","San Francisco","First sight of an American city",
 "Kume describes San Francisco as a city barely twenty years old, built on gold and trade, with hotels of a size Japan had never seen. The embassy was lodged at the Grand Hotel. He notes gaslight, carriages and crowds in the street come to look at the visitors.",
 "","approx","The Iwakura Embassy 1871–73, vol. 1 (Healey and Tsuzuki), San Francisco chapters; detail summarised.")
e("1872-01-16","16 January 1872","day","iwakura","San Francisco","Formal welcome by the mayor",
 "On the day after landing the embassy was formally received; Mayor William Alvord welcomed it, and Iwakura replied in Japanese through an interpreter. The exchange set the pattern for the American tour: lavish civic hospitality answered by measured ceremonial courtesy.",
 "","verified","Lanman (ed.), The Japanese in America (1872): reception 'the day after' arrival.")
e("1872-01-23","Tuesday 23 January 1872 (Meiji 4, 12th month, 14th day)","day","ito","Grand Hotel, San Francisco","Itō's 'rising sun' speech",
 "At the city's banquet Itō spoke in English. Japan, he said, had abolished the feudal domains without bloodshed, was eager to learn from the West, and meant its flag to stand as the emblem of a nation rising among the enlightened powers rather than a seal on a closed country. The speech was printed across America.",
 "no longer appear like a wafer over a sealed empire","verified","Text in Black, Young Japan II, 358–360, reprinted in Meiji Japan Through Contemporary Sources (udel.edu PDF), where it carries the lunar date '14 December 1871'.")
e("1872-01-23","23 January 1872","day","lanman","Grand Hotel dinner, as reported","Lanman prints the banquet speeches",
 "Lanman's book reproduces the Grand Hotel dinner and the Japanese replies in full, beginning with Itō's courteous opening thanks. For an American reader, this was the first chance to read Japanese statesmen in their own speeches.",
 "","verified","Lanman (ed.), The Japanese in America (1872), dinner of 23 January.")
e("1872-02-03","3 February 1872","day","kume","Ogden and Salt Lake City, Utah Territory","Snow buries the railway in the Rockies",
 "The embassy reached Ogden by the Central Pacific and went on to Salt Lake City, where it was stranded: drifts had closed the Union Pacific line through the mountains. Kume used the delay to describe the Mormon city, its broad streets and its unusual social order.",
 "","verified","Deseret News (2014), citing Kume's account; arrival at Ogden 3 February 1872.")
e("1872-02-16","16 February 1872","day","snow","Salt Lake City","A Utah legislator asks the Japanese for lessons",
 "Welcoming the snowbound visitors, Lorenzo Snow turned the flattery around: the Americans, he said, hoped to learn from Japan about government and law. For a territory whose own institutions were under suspicion in Washington, the compliment had an edge.",
 "We would ask at your hands some lessons in civil polity","verified","Deseret News (2014), quoting Snow's speech of 16 February 1872.")
e("1872-02-22","22 February 1872","day","kume","Leaving Salt Lake City, eastbound","The line opens; on to Chicago",
 "After almost three weeks the track was cleared and the embassy left Utah. Passing through Chicago, still marked by the great fire of October 1871, Kume noted the speed of rebuilding as a sign of American energy.",
 "","approx","Departure date: Deseret News (2014). Chicago observations summarised from the Jikki, vol. 1; precise Chicago dates not confirmed.")
e("1872-02-29","Thursday 29 February 1872 (Meiji 5, 1st month, about the 21st day)","day","kume","Washington","Arrival in the capital",
 "The embassy reached Washington, five weeks later than Mori had forecast, and was lodged at the Arlington Hotel. Kume begins his long description of the American republic: Congress, the departments, and a president chosen by election rather than birth.",
 "","verified","Arrival date: Wikipedia, Iwakura Mission. Hotel and description summarised from the Jikki; lunar equivalent computed.")
e("1872-03-04","Monday 4 March 1872","day","iwakura","The White House","The Emperor's letter presented to Grant",
 "In court dress, Iwakura led the ambassadors to the White House and presented the Emperor's letter of credence, which announced the embassy's friendly purpose and its wish to prepare for treaty revision. His address was read in Japanese and translated.",
 "","verified","Audience date: MHS (early March) and the standard chronology; Emperor's letter in Meiji Japan Through Contemporary Sources. Wording of the address not quoted.")
e("1872-03-04","4 March 1872","day","grant","The White House","Grant welcomes the first ambassadors since 1860",
 "Grant answered with a short formal reply welcoming the embassy, praising Japan's wish to learn and expressing America's interest in closer trade and friendship. An engraving of the scene, with the cabinet ranged behind the president, appeared in the illustrated press the next month.",
 "","approx","Grant's reply printed in the press in March 1872; wording not verified here. Engraving: Bridgeman Images listing (April 1872).")
e("1872-03-04","4 March 1872","day","kume","The White House","A republican audience without ceremony",
 "Kume was struck by how plain the audience was: no guards in ranks, no prostrations, a president in a black coat among his ministers. He reflects on a state where the highest office is held by a citizen who will return to private life.",
 "","approx","Jikki, vol. 1, Washington chapters; summarised.")
e("1872-03-06","6 March 1872","day","fish","State Department, Washington","Fish records the embassy's first approach",
 "Fish noted the embassy's opening approach on business. Mayo's reading of the diary shows him puzzled about what the Japanese actually wanted: they spoke of revising the 1858 treaty but had earlier given out that revision would wait until their return home.",
 "","approx","Fish, Diary, 6 March 1872, cited in Mayo (1967), n. 17; content of entry summarised from Mayo.")
e("1872-03-12","12 March 1872","day","fish","State Department, Washington","Talks begin, and the question of full powers",
 "As formal interviews began, Fish insisted that any treaty be signed only by envoys holding full powers in proper form. The ambassadors' letters authorised them to discuss but not to conclude. Fish, in Mayo's phrase a stickler for tradition, would not bend the rule.",
 "","approx","Fish, Diary, 12 March 1872, cited in Mayo (1967), n. 21–22; minutes of 13 March conference (n. 31).")
e("1872-03-14","14 March 1872","day","mori","Washington","Tokyo is asked for fuller powers",
 "With the embassy's backing, a request went to Tokyo for full powers to conclude a treaty, to be issued to Mori and the ambassadors. A provisional draft treaty followed within days. Mori was among those who had argued that the Americans would sign quickly.",
 "","approx","Mayo (1967), n. 28: telegram of 14 March, draft of 17 March; Mori's role summarised.")
e("1872-03","late March 1872","range","okubo","Washington to Tokyo","Ōkubo and Itō turn back for credentials",
 "Ōkubo and Itō left Washington to fetch the full powers in person, a voyage across the continent and the Pacific and back. Ōkubo's letters show a finance minister suddenly absent from the work of state while the talks waited. The commission was granted in Tokyo in May.",
 "","approx","National Archives of Japan item on Grant (commission dated 14 May 1872); departure date approximate.")
e("1872-03","March–April 1872","range","kido","Washington","Kido fumes at the wasted months",
 "With half the leadership on its way back to Japan, Kido's diary turns sour. He blames the haste of the younger men, Itō above all, for a scheme that had left the embassy waiting, and he fills the time studying American schools and the constitution.",
 "","approx","Kido's diary, Brown and Hirota trans., vol. 2, Washington entries; summarised from secondary studies; exact days not checked.")
e("1872-07-10","10 July 1872","day","fish","State Department, Washington","Fish lets the treaty talks die",
 "Even with Ōkubo and Itō back, the ambassadors now wanted any revision settled at a joint conference in Europe, which Fish would not accept. His diary and letters to Grant record the administration deciding to let the negotiations end politely.",
 "","approx","Fish, Diary, 10 July 1872, pp. 339–40, and letters to Grant, cited in Mayo (1967), n. 43; date verified, content summarised.")
e("1872-07-22","22 July 1872","day","iwakura","State Department, Washington","The last conference with Fish",
 "At the final recorded conference Iwakura confirmed that the embassy would not conclude a treaty in Washington. The months of argument ended in courtesies; the embassy's purpose shifted to study, and treaty revision would wait until 1894.",
 "","approx","Minutes of conference, 22 July 1872, cited in Mayo (1967), n. 45; content summarised.")
e("1872-08-02","Friday 2 August 1872","day","holmes","Revere House, Boston","Holmes's verse for the farewell banquet",
 "At the Boston Board of Trade's dinner for about 150 guests, Holmes read a punning poem about the presidential campaign. He also told the guests, in a line that played on the late hour of Japan's opening, that they had come a little late. Emerson spoke too, praising the Perry expedition for opening Japan.",
 "You are welcome, but oh! You're a little too late!","verified","Massachusetts Historical Society, Object of the Month, February 2014.")
e("1872-08-02","2 August 1872","day","kume","Boston","Boston as the brain of the republic",
 "Kume recorded the Boston welcome with warmth, observing that Americans treated foreigners as family or friends. A Japanese guest at the dinner called Boston the brain of the republic; around the visit the embassy toured the Lowell and Lawrence textile mills.",
 "","verified","MHS, Object of the Month, February 2014, citing Kume.")
e("1872-08-06","6 August 1872","day","kume","Boston harbour, aboard the Cunard steamer Olympus","Sailing for England",
 "After seven months in America the embassy sailed for Liverpool on the Olympus. Kume closed the American volumes of his record with a long assessment of the republic's riches and its youth.",
 "","verified","Date and ship: MHS, Object of the Month.")
e("1872-08-17","17 August 1872","day","kume","Liverpool, then London","Landing at Liverpool",
 "The embassy landed at Liverpool and went straight on to London. The Queen was in Scotland, and the audience the embassy had come for would wait almost four months, time Kume filled with a tour of Britain's industry.",
 "","verified","Date: Wikipedia, Keio lecture, Saltaire Collection.")
e("1872-08-24","24 August 1872","day","britpress","The Spectator, London","The Spectator takes the Japanese seriously",
 "The Spectator set the Japanese envoys against a Burmese mission it thought unimportant: these, it said, represented an independent Asian ruler remaking a nation of thirty million. It found them fluent in English and in Western dress, and judged Iwakura a shrewd diplomat, not anyone's protégé.",
 "worth studying, as well as conciliating","verified","Spectator Archive, 24 August 1872, p. 3.")
e("1872-08-30","30 August 1872","day","britpress","The Times, London","The Times follows them to Portsmouth",
 "The Times reported the embassy's visit to the dockyard at Portsmouth and a Royal Navy gunnery ship, accompanied by Sir Harry Parkes, the British minister to Japan, then home on leave and the embassy's guide in Britain.",
 "","verified","The Times, 30 August 1872, as cited in Kansai University study (KU-0400).")
e("1872-10-07","7 October 1872","day","kume","Manchester","Calico printing and a civic banquet",
 "In Manchester the embassy toured a calico-printing works and was given a civic reception and banquet. Kume tracks the whole cotton chain, from raw bales to printed cloth for Asian markets, and concludes that Britain's wealth rests on coal, iron and machines.",
 "","verified","Date: Wikipedia; Korea Science study of the British industrial cities (calico works, 7 October).")
e("1872-10-12","12 October 1872","day","britpress","Illustrated London News","The Illustrated London News explains the mission",
 "The Illustrated London News reported the embassy's aims to its readers, presenting it as a government sending its chief men to study Western institutions, industry and education before negotiating new treaties.",
 "","approx","ILN, 12 October 1872, cited in Kansai University study; content summarised.")
e("1872-10-17","17 October 1872","day","kido","Manchester district","Kido in the mills",
 "Kido's diary records factory visits in the Manchester district. The scale of the machines impressed him, but his entries return to who worked them and whether they were schooled, the theme that runs through his British pages.",
 "","approx","Keio University lecture (Kido in Manchester factories, 17 October); diary content summarised.")
e("1872-10-23","23 October 1872","day","britpress","Newcastle Daily Chronicle","Newcastle notes their plain clothes",
 "Reporting the visit to Armstrong's works at Elswick the day before, the Newcastle paper described the delegates' dress, noting with evident surprise that it was entirely ordinary.",
 "attired in ordinary morning costume","verified","Newcastle Daily Chronicle, 23 October 1872, quoted in Wikipedia, Iwakura Mission; Armstrong visit 22 October (Korea Science).")
e("1872-10-25","Friday 25 October 1872","day","kume","Saltaire, near Bradford","A model mill town",
 "By special train from Bradford the embassy visited Titus Salt's mill village, where Kume noted that the land had been open moor twenty years before. He studied the school where the village children spent half the day in class and half at work in the mill, and judged the town a deliberate model for promoting industry.",
 "","verified","Saltaire Collection PDF; Keio University lecture.")
e("1872-10-25","25 October 1872","day","kido","Saltaire","Kido admires the setting",
 "Kido's diary praises the scenery around Saltaire and notes, as Kume does, that Titus Salt himself was absent. His entries on the village show more interest in the setting and the school than in the looms.",
 "","verified","Saltaire Collection PDF, citing Kido's diary; quotation not used because the wording is a modern translation.")
e("1872-10-25","25 October 1872","day","britpress","Bradford Daily Telegraph","Bradford reports the visit to Saltaire",
 "The local paper reported the special train, the tour of the mill and the crowd that gathered, noting that few men were there to watch because most were at work.",
 "they being mostly at work in the mill","verified","Bradford Daily Telegraph, 25 October 1872, quoted in Saltaire Collection PDF.")
e("1872-11","November 1872","month","okubo","London","Ōkubo writes home: factories everywhere",
 "In a letter home Ōkubo wrote that wherever the embassy went it saw factories and smoke, and that Britain's power came from industry and trade, not from the soil. The letter is often taken as a seed of his later policy of state-led industry.",
 "","approx","Ōkubo Toshimichi monjo; letter cited in studies of Ōkubo's policies (JAS); exact date and wording not verified.")
e("1872-11-22","22 November 1872","day","iwakura","Foreign Office, London","Talks with Granville",
 "Iwakura met the Foreign Secretary, Lord Granville, and a second session followed on 27 November. The British raised foreigners' rights to travel in Japan's interior; as in Washington, neither side had a basis for a new treaty.",
 "","verified","Keio University lecture; Saltaire Collection PDF.")
e("1872-12","August–December 1872","range","kido","London, East End","Kido and Ōkubo walk the slums incognito",
 "Kido and Ōkubo went into the East End without escort. Kido described what he saw as worse than a slum, a place of thieves beyond description; Ōkubo's comment was that the world had become wretched. The pages record a shock for men who had just toured the mills that paid for London's wealth.",
 "","approx","Keio University lecture, citing Kido and Ōkubo (undated); month approximate.")
e("1872-12-02","Monday 2 December 1872","day","grant","Washington, Fourth Annual Message to Congress","Grant reports the embassy to Congress",
 "In his annual message Grant told Congress that treaty relations with Japan remained unchanged, and that an impressive embassy from Japan had visited during the year. The failed negotiation was passed over in a sentence.",
 "An imposing embassy from that interesting and progressive nation","verified","Richardson, Messages and Papers of the Presidents, vol. 7 (Project Gutenberg 13012), Fourth Annual Message.")
e("1872-12-05","Thursday 5 December 1872 (Meiji 5, 11th month, about the 5th day)","day","victoria","Windsor Castle","The Queen receives the Japanese ambassadors",
 "The Queen's journal records receiving the ambassadors at Windsor, with Lord Granville and Sir Harry Parkes present, and the presentation of the Emperor's letter through an interpreter. She did not attend the luncheon given for them afterward.",
 "","approx","Date: Wikipedia, Keio lecture, Saltaire Collection. Journal content not checked against the manuscript; attendance detail from Keio lecture.")
e("1872-12-05","5 December 1872","day","kume","Windsor Castle","Audience at Windsor at last",
 "After almost four months in Britain the ambassadors went to Windsor by train and presented their letter to the Queen. Kume records the ceremony and the setting; within days the embassy took leave of the Prince of Wales at Sandringham and on 16 December crossed to France.",
 "","verified","Dates: Wikipedia; Saltaire Collection (Sandringham 9 Dec, departure 16 Dec).")
e("1873-03-15","Saturday 15 March 1873","day","kume","Berlin, Bismarck's dinner","Bismarck tells them how small nations survive",
 "At his dinner for the embassy Bismarck spoke of Prussia's own rise from weakness since Napoleon's time. Kume records the advice in summary: the great powers respect international law only when it suits them, so a small nation must build its own strength. He added that Germany, unlike Britain and France, sought no colonies.",
 "","verified","Krebs, 'Die Iwakura-Mission in Preußen' (DIJ Tokyo), on Kume's report of the dinner of 15 March 1873.")
e("1873-03","March 1873","month","okubo","Berlin","Ōkubo's admiration for Bismarck",
 "Ōkubo's letters from Berlin show him impressed by Bismarck and by a state that had made itself strong in a generation. Historians often date from here his view of Prussia, rather than Britain or America, as the closer model for Japan.",
 "","approx","Studies citing Ōkubo's Berlin letters; wording and exact date not verified.")
e("1873-04","April 1873","month","kume","St Petersburg","Russia, the northern giant",
 "From Berlin the embassy went on to St Petersburg. Kume describes the capital's palaces and the poverty of its people, and measures Russia as a vast, backward neighbour whose expansion in the north Pacific concerned Japan.",
 "","approx","Jikki, vol. 4 (Healey and Tsuzuki trans.); dates of the Russian stay not verified here.")
e("1873-06","June 1873","month","kume","Vienna, the World Exhibition","At the Vienna fair",
 "In Vienna the embassy saw the World Exhibition, where Japan was exhibiting officially for the first time. Kume praised the city's well-paved roads and recorded paving costs in detail; he judged Austria's arms and constitutional practice some forty years behind the most advanced states, and noted that the embassy had to pay for its own meals.",
 "","approx","Habsburger.net, 'From the Logbook of Kume Kunitake'; month approximate.")
e("1873-07","July 1873","month","kido","Tokyo","Kido's memorial: a constitution first",
 "Back in Japan ahead of the embassy, Kido submitted a memorial arguing that Japan needed a written constitution to bind rulers and ruled, drawing on what he had seen of Western states. It sets out the lesson he had taken from the journey.",
 "","approx","Kido's memorial of July 1873, excerpted in Meiji Japan Through Contemporary Sources (udel.edu PDF).")
e("1873-09-13","Saturday 13 September 1873 (Meiji 6, 9th month, 13th day: Gregorian)","day","kume","Yokohama","Home after twenty-one months",
 "The embassy returned to Yokohama via Suez, Ceylon, Singapore, Saigon, Hong Kong and Shanghai, after almost two years. It came back into a government now dated by the Gregorian calendar, and divided over whether to send an expedition to Korea.",
 "","verified","Date: Wikipedia; Keio lecture; route: Wikipedia.")
e("1882-11","November 1882","month","tsuda","Yokohama and Tokyo","Ume comes home a stranger",
 "In the first letters to Adeline Lanman after landing, Tsuda describes a homeland she could no longer speak to: a family she knew only from photographs, customs she had to relearn, and few roles for an educated woman. The letters look back on the embassy's promise to the five girls from the other end of a decade.",
 "","approx","The Attic Letters (1991), opening letters; dates and contents summarised from secondary accounts.")

claims=[
 dict(date_iso="1872-01-15",date_display="15 January 1872",eye="lanman",claim="Counts the Japanese passengers and singles out five young ladies travelling under American care",form="other",evidence="Lanman, The Japanese in America (1872)",confidence="verified"),
 dict(date_iso="1872-01-23",date_display="23 January 1872",eye="ito",claim="Tells Americans that Japan's flag will be the emblem of a rising nation, no longer a seal on a closed country",form="speech",evidence="Black, Young Japan II, 358–360",confidence="verified"),
 dict(date_iso="1872-02-16",date_display="16 February 1872",eye="snow",claim="A Utah host asks the Japanese for lessons in government and law",form="speech",evidence="Quoted in Deseret News (2014)",confidence="verified"),
 dict(date_iso="1872-03-04",date_display="4 March 1872",eye="kume",claim="Finds the White House audience strikingly plain for the reception of a head of state",form="travel journal",evidence="Jikki, vol. 1",confidence="approx"),
 dict(date_iso="1872-03-12",date_display="12 March 1872",eye="fish",claim="Holds that envoys without full powers in proper form cannot sign a treaty",form="diary",evidence="Fish, Diary, via Mayo (1967)",confidence="approx"),
 dict(date_iso="1872-03",date_display="March–April 1872",eye="kido",claim="Blames the younger leaders' haste for the credentials fiasco",form="diary",evidence="Kido's diary, Brown and Hirota trans.",confidence="approx"),
 dict(date_iso="1872-08-02",date_display="2 August 1872",eye="kume",claim="Americans treat foreigners like family or friends",form="travel journal",evidence="Jikki, cited by MHS",confidence="verified"),
 dict(date_iso="1872-08-02",date_display="2 August 1872",eye="holmes",claim="Jokes that Japan has arrived a little late to the company of nations",form="poem",evidence="MHS, Object of the Month, Feb 2014",confidence="verified"),
 dict(date_iso="1872-08-24",date_display="24 August 1872",eye="britpress",claim="The Spectator calls the envoys, fluent in English and in Western dress, worth studying as well as conciliating",form="newspaper",evidence="Spectator, 24 Aug 1872",confidence="verified"),
 dict(date_iso="1872-10-07",date_display="7 October 1872",eye="kume",claim="Britain's wealth rests on mineral resources, coal and iron, turned into goods by machines",form="travel journal",evidence="Jikki, cited in Korea Science study",confidence="approx"),
 dict(date_iso="1872-10-23",date_display="23 October 1872",eye="britpress",claim="The Newcastle press is surprised that the delegates wear ordinary morning dress",form="newspaper",evidence="Newcastle Daily Chronicle, 23 Oct 1872",confidence="verified"),
 dict(date_iso="1872-10-25",date_display="25 October 1872",eye="kume",claim="Saltaire's half-time school, children in class half the day and in the mill the other half, is a model of industrial promotion",form="travel journal",evidence="Jikki, cited by Saltaire Collection and Keio",confidence="verified"),
 dict(date_iso="1872-12",date_display="late 1872",eye="kido",claim="London's East End is a den of thieves beyond description",form="diary",evidence="Keio University lecture",confidence="approx"),
 dict(date_iso="1872-12-02",date_display="2 December 1872",eye="grant",claim="Calls Japan an interesting and progressive nation that sent an imposing embassy",form="other",evidence="Fourth Annual Message, Richardson vol. 7",confidence="verified"),
 dict(date_iso="1873-03-15",date_display="15 March 1873",eye="kume",claim="Records Bismarck's advice that international law protects only the strong",form="travel journal",evidence="Jikki, via Krebs (DIJ Tokyo)",confidence="verified"),
 dict(date_iso="1873-06",date_display="June 1873",eye="kume",claim="Judges Austria's arms and constitutionalism forty years behind, while praising Vienna's paving",form="travel journal",evidence="Habsburger.net",confidence="approx"),
]

conv=[
 dict(date="1871-12-23",label="Departure from Yokohama",eyes=["kume","kido"],note="The official recorder frames a state enterprise; the councillor's private diary starts the clock on a long absence. The six-year-old Tsuda Ume left no record of that day."),
 dict(date="1872-01-23",label="The Grand Hotel banquet, San Francisco",eyes=["ito","lanman"],note="Itō speaks to Americans in their own language; Lanman prints the speeches so that Americans can read the visitors in their own words. The banquet date is 14th day of the 12th month in Itō's calendar."),
 dict(date="1872-03-04",label="Audience with President Grant",eyes=["iwakura","grant","kume"],note="The ambassador in court dress presents a letter of credence; the president welcomes a nation coming to learn; the recorder marvels at how little ceremony a republic needs."),
 dict(date="1872-03-12",label="The full-powers impasse (week of 12–14 March)",eyes=["fish","mori","kido","okubo"],note="Fish insists on form; Mori and the younger leaders gamble on speed; Kido's diary records the cost; Ōkubo sets off across the world to fetch a document."),
 dict(date="1872-08-02",label="Boston farewell banquet",eyes=["holmes","kume"],note="The host poet jokes that the guests are late; the guest recorder notes how warmly they are welcomed. Both are pleased; neither mentions the failed treaty."),
 dict(date="1872-10-25",label="Saltaire",eyes=["kume","kido","britpress"],note="Kume studies the half-time school as policy, Kido the landscape, and the Bradford paper the crowd of onlookers, with the men away at work."),
 dict(date="1872-12-05",label="Windsor audience",eyes=["victoria","kume","grant"],note="Three days after Grant tells Congress the embassy has come and gone, the Queen finally receives it. Each host records a courtesy; neither treaty negotiation had produced anything."),
 dict(date="1873-03-15",label="Bismarck's dinner, Berlin",eyes=["kume","okubo"],note="Kume records the lesson in summary; Ōkubo's letters show a man persuaded. The Germans present recorded a dinner; the Japanese recorded a doctrine."),
]

ties=[
 dict(a="kume",b="iwakura",kind="met",note="Kume was Iwakura's private secretary and wrote the embassy's official record under his authority."),
 dict(a="kido",b="ito",kind="met",note="Both from Chōshū; Kido had been Itō's patron, and their relations cooled in Washington over the credentials gamble."),
 dict(a="kido",b="okubo",kind="met",note="Restoration allies and rivals, from Chōshū and Satsuma; in London they walked the East End together, and both left the embassy early in 1873."),
 dict(a="okubo",b="ito",kind="met",note="Travelled together from Washington to Tokyo and back in spring and summer 1872 to fetch full powers."),
 dict(a="mori",b="lanman",kind="met",note="Lanman worked as American secretary at Mori's legation and printed Mori's letters in his 1872 book."),
 dict(a="lanman",b="tsuda",kind="met",note="Tsuda Ume grew up in the Lanman household in Georgetown; her later letters to Adeline Lanman are the source used here."),
 dict(a="fish",b="iwakura",kind="opposite sides",note="Across the table in the 1872 treaty interviews, from March to late July."),
 dict(a="fish",b="mori",kind="opposite sides",note="Mori was the chargé through whom the embassy dealt with the State Department and for whom full powers were requested."),
 dict(a="grant",b="iwakura",kind="met",note="Iwakura presented the Emperor's letter to Grant at the White House on 4 March 1872."),
 dict(a="grant",b="fish",kind="met",note="Fish reported the negotiations to Grant in letters of July 1872 before the talks were dropped."),
 dict(a="victoria",b="iwakura",kind="met",note="Iwakura presented the Emperor's letter to the Queen at Windsor on 5 December 1872."),
 dict(a="holmes",b="kume",kind="met",note="Both were at the Revere House banquet of 2 August 1872, one reading verse and one taking notes."),
 dict(a="snow",b="kume",kind="met",note="Snow and other Utah leaders hosted the snowbound embassy that Kume described, in February 1872."),
]

threads=[
 dict(to="v15:missing-days",note="Japan replaced the lunisolar calendar with the Gregorian while the embassy was in Europe: by a decree of the 9th day of the 11th month of Meiji 5, the 3rd day of the 12th month became 1 January 1873. The last month of the old year was cut to two days, so officials at home lost a month's pay."),
 dict(to="embassy-1860",note="The 1860 embassy came to Washington to ratify the 1858 Harris treaty; the Iwakura embassy came twelve years later hoping to revise that same treaty, and failed."),
 dict(to="v2:black-ships",note="At the Boston banquet of 2 August 1872 Emerson praised the Fillmore administration and the Perry expedition for opening Japan, the event that began the treaty system the embassy wanted to change."),
 dict(to="naser-1873",note="Naser al-Din Shah of Persia toured Europe in 1873, overlapping the Iwakura embassy's months on the Continent; both visited Berlin and the Vienna World Exhibition that year."),
 dict(to="v7:oceans-1869",note="The embassy crossed America by the transcontinental railroad completed in 1869 and came home in 1873 through the Suez Canal opened the same year."),
]

images=[
 dict(url="https://www.bridgemanimages.it/en-US/noartistknown/japanese-diplomatic-delegation-led-by-iwakura-tomomi-presents-their-documents-to-president-grant-and/wood-engraving/asset/7067158",title="Japanese delegation presents its documents to President Grant",caption="A wood engraving of the 4 March 1872 audience, with Iwakura's party before Grant and his cabinet; published in the American illustrated press in April 1872, according to the agency listing.",date="April 1872",credit="Unknown engraver; Bridgeman Images"),
 dict(url=NAJ,title="His Excellency President Grant (draft)",caption="A Japanese drawing of Grant from the Kobun Fuzoku no Zu, the illustrations attached to the Grand Council of State's records. It shows how the government at home pictured the man the embassy met.",date="c. 1872",credit="National Archives of Japan"),
 dict(url=MHS,title="Silk bill of fare, Boston farewell banquet",caption="Printed silk menu for the Revere House dinner of 2 August 1872, opening with a welcome to the Lords of the Land of the Sun. The Massachusetts Historical Society holds three colour variants.",date="2 August 1872",credit="Massachusetts Historical Society"),
 dict(url="https://www.heritage-images.com/preview/sionii-iwakura-the-japanese-special-ambassador-1872-creator-unknown-3046981",title="Iwakura, the Japanese Special Ambassador",caption="An engraved portrait of Iwakura published in Britain in 1872, according to the agency listing, the image through which most British readers met him.",date="1872",credit="Creator unknown; Heritage Images"),
 dict(url="https://www.digital.archives.go.jp/gallery/en/0000000750",title="Overall view of the Vienna World Exposition site",caption="A Japanese illustration of the 1873 exhibition grounds in the Prater, the first world fair at which the Meiji government exhibited officially; the embassy visited it in June 1873.",date="1873",credit="National Archives of Japan, Kobun Fuzoku no Zu"),
]

further=[
 dict(title="Lanman (ed.), The Japanese in America (1872), full text",url=LAN),
 dict(title="Meiji Japan Through Contemporary Sources: the Iwakura Mission (excerpts)",url=UDEL),
 dict(title="Mayo, 'A Catechism of Western Diplomacy: The Japanese and Hamilton Fish, 1872' (JAS 1967)",url=MAYO),
 dict(title="Krebs, 'Die Iwakura-Mission in Preußen' (DIJ Tokyo)",url=KREBS),
 dict(title="The Iwakura Mission at Saltaire (Saltaire Collection)",url=SALT),
 dict(title="The Iwakura Embassy and British Industrial Cities (Korea Science)",url=KOREA),
 dict(title="Keio University: the Iwakura Mission in Britain",url=KEIO),
 dict(title="Massachusetts Historical Society: the Boston banquet of 1872",url=MHS),
]

intro=[
 "On 23 December 1871 a steamer left Yokohama carrying half the government of Japan. Iwakura Tomomi, the ambassador, took with him four vice-ambassadors: Kido Takayoshi, Ōkubo Toshimichi, Itō Hirobumi and Yamaguchi Masuka. With them went some fifty officials and secretaries and about sixty students. The students included five girls, the youngest of them Tsuda Ume, aged six, who would not see Japan again for eleven years. The embassy was meant to last ten months. It took twenty-one, and it went round the world.",
 "It had two purposes, and only one of them succeeded. The leaders hoped to begin revising the unequal treaties of 1858. In Washington, swayed by the warmth of their welcome, they tried to negotiate a new treaty at once, found they lacked full powers, and sent Ōkubo and Itō back across the Pacific to fetch them. When they returned, the moment had passed. The other purpose was to look: at mills, dockyards, schools, prisons, parliaments and slums. That one succeeded beyond anyone's plan.",
 "This chapter sets the travellers' records beside their hosts'. Kume Kunitake's five-volume official account (1878) is the spine. It is a worked-up record compiled after the return, not a day-book. Kido's private diary is the most candid Japanese voice; Ōkubo speaks only through his letters home; Itō's one great public speech was delivered in English. On the hosts' side are Hamilton Fish's diary of the failed talks, Grant's state papers, the welcomes of a Utah legislator and a Boston poet, the Queen's journal, and a string of British newspapers from London to Bradford.",
 "Most Japanese texts here survive only in Japanese or in modern translation, so they appear as digests. Quotations are limited to what was printed in English at the time: Itō's speech, Grant's message, Holmes's verse, the Spectator, the provincial press. Where a date or detail rests on a later study rather than on a fetched text, the entry says so.",
 "The best days are the ones when both sides wrote. On 4 March 1872 Grant welcomed a nation coming to learn, while Kume wondered at a head of state with no guards in ranks. On 25 October 1872 at Saltaire, a Bradford reporter counted the crowd while Kume counted the hours the mill children spent in school. And on 15 March 1873 Bismarck gave his guests a lesson in power, which Kume summarised and Ōkubo seems to have taken home.",
]

cal=("Japan used a lunisolar calendar, dated by era name, until the end of Meiji 5. The embassy left Yokohama on the 12th day of the 11th month of Meiji 4, which was 23 December 1871. It reached San Francisco on the 6th day of the 12th month (15 January 1872), and Itō's speech of the 14th day of that month fell on 23 January 1872; some reprints mislabel it '14 December 1871'. Meiji 5 began on 9 February 1872, so the Washington arrival of 29 February was about the 21st day of the 1st month. "
 "While the embassy was in Britain the government decreed, on the 9th day of the 11th month of Meiji 5 (about 9 December 1872), that the 3rd day of the 12th month would become 1 January 1873 (Meiji 6). The old 12th month thus lasted two days. From 1873 Japanese month and day numbers match the Western ones, so the return of 13 September 1873 is Meiji 6, 9th month, 13th day. "
 "Here date_iso is always Gregorian. Lunar equivalents for 1872 are computed, and those marked 'about' may be off by a day. Kido's diary and the letters home were dated in the old calendar until the change; Kume's printed record and the host papers use Western dates.")

ch=dict(id="iwakura-1871",title="Half a Government Abroad: The Iwakura Embassy",short_title="The Iwakura Embassy",
 subtitle="The Iwakura Mission in America and Europe, December 1871 – September 1873",span="1871–1873",
 intro=intro,calendar_note=cal,eyes=eyes,entries=E,claims=claims,convergences=conv,ties=ties,threads_out=threads,images=images,further=further,
 vantage_key="0 = the embassy's leaders and recorder; 1 = hosts who met them face to face, and the child left in America; 2 = reporters on the spot; 3 = observers elsewhere in the same country; 4 = abroad, news only.")
json.dump(ch,open(OUT,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
ids={x["id"] for x in eyes}
assert all(x["eye"] in ids for x in E+claims)
assert all(set(c["eyes"])<=ids for c in conv)
assert all(t["a"] in ids and t["b"] in ids for t in ties)
assert all(len(x["short"])<=16 for x in eyes)
for x in E:
    if x["quote"]: assert len(x["quote"].split())<=12, x["quote"]
print(len(eyes),len(E),len(claims),len(conv),len(ties),len(threads),len(images),len(further))
