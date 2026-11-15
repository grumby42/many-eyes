import json

OUT = "/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/vol7/ch-the-road.json"

WIKI_BB = "https://en.wikipedia.org/wiki/Bertha_Benz"
DPMA = "https://www.dpma.de/english/our_office/publications/ingeniouswomen/berthabenz/index.html"
MB_GROUP = "https://group.mercedes-benz.com/unternehmen/tradition/gruender-wegbereiter/bertha-benz.html"
MB_PATENT = "https://mercedes-benz.com/en/innovation/milestones/benz-patent-motor-car"
GHDI = "https://germanhistorydocs.org/en/forging-an-empire-bismarckian-germany-1866-1890/carl-friedrich-benz-a-new-bicycle-1867.pdf"
DUNLOP = "https://en.wikipedia.org/wiki/John_Boyd_Dunlop"
WILLARD = "https://www.gutenberg.org/files/60356/60356-h/60356-h.htm"
LONDONDERRY = "https://en.wikipedia.org/wiki/Annie_Londonderry"
JWA = "https://jwa.org/thisweek/jun/25/1894/annie-cohen-kopchovsky"
BLY = "https://medium.com/the-hairpin/let-me-tell-you-what-i-think-of-bicycling-nellie-bly-interviews-susan-b-anthony-1896-c2b15900a5a8"
BLY2 = "https://blog.rarenewspapers.com/nellie-bly-an-interview-with-susan-b-anthony/"
PR = "https://en.wikipedia.org/wiki/Paris%E2%80%93Rouen_(motor_race)"
PBP = "https://en.wikipedia.org/wiki/Paris%E2%80%93Bordeaux%E2%80%93Paris"
CHI = "https://en.wikipedia.org/wiki/Chicago_Times-Herald_race"
DRISCOLL = "https://en.wikipedia.org/wiki/Death_of_Bridget_Driscoll"
BRIGHTON = "https://en.wikipedia.org/wiki/London_to_Brighton_Veteran_Car_Run"
GRACES = "https://gracesguide.co.uk/Emancipation_Run"
P2P = "https://en.wikipedia.org/wiki/Peking_to_Paris"
BARZ_PDF = "https://ia600203.us.archive.org/2/items/pekintoparisacco00barz/pekintoparisacco00barz.pdf"
BARZ_OL = "https://openlibrary.org/books/OL24590543M/Pekin_to_Paris"
BARZ_IT = "https://it.wikisource.org/wiki/La_met%C3%A0_del_mondo_vista_da_un%27automobile/I"
BARZ_DE = "https://gutenberg.org/ebooks/47798"
LOUWMAN = "https://www.louwmanmuseum.nl/en/news/the-peking-paris-automobile-race-in-1907"
MOTORSPORT = "https://www.motorsportmagazine.com/archive/article/september-1997/57/1907-a-race-odyssey"
HISTTODAY = "https://www.historytoday.com/node/52338"
SMITH = "https://www.smithsonianmag.com/history/paris-or-bust-the-great-new-york-to-paris-auto-race-of-1908-116784616/"
SCHUSTER = "https://en.wikipedia.org/wiki/George_Schuster_(driver)"
SPECTATOR = "https://archive.spectator.co.uk/article/25th-april-1908/9/pekin-to-paris-in-a-motorcar"

ch = {
 "id": "the-road",
 "title": "The Road: Bicycles and Motorcars, 1888–1908",
 "short_title": "The Road, 1888–1908",
 "subtitle": "From Bertha Benz's drive to Pforzheim to the Peking–Paris and New York–Paris races",
 "span": "1886–1908",
 "intro": [
  "In August 1888 a woman of thirty-nine took her husband's three-wheeled motor carriage out of a Mannheim workshop before dawn, put her two teenage sons aboard, and drove roughly a hundred kilometres to her mother's house in Pforzheim. That same summer a Belfast veterinary surgeon was patenting an air-filled tyre he had first fitted to his small son's tricycle. Twenty years later, cars were being driven from Peking to Paris and from New York to Paris, with newspapers paying for the petrol and selling the story by telegraph. This chapter follows the ordinary road through those two decades, when the bicycle and the motorcar arrived together and the open highway became a place for trials, wagers, races and the first deaths.",
  "The record is uneven, and the chapter says so. Bertha Benz left no diary; her drive is known from what her husband wrote in his 1925 memoir and from later family retellings, so even the day is disputed. Dunlop told his own story late in life. Frances Willard wrote a short, cheerful book about learning to ride at fifty-three. Annie Londonderry's round-the-world ride survives mostly in newspaper interviews she gave as she went, and she was a gifted and unreliable self-promoter. The early races are known from the newspapers that organised them, whose figures (distances, times, prize decisions) are the closest thing to a test log, and from participants' later books such as H. O. Duncan's.",
  "The motor age's first deaths reached the record through inquests. When Bridget Driscoll was struck by a demonstration car in the grounds of the Crystal Palace in August 1896, the coroner's court heard six hours of evidence about speed, a restricted engine, and a driver who may or may not have rung his bell. The jury's finding, and the coroner's hope that it would not happen again, are reported here as the court recorded them.",
  "The Peking–Paris race of 1907 is the best-documented journey in the chapter, because it was made for the newspapers. Luigi Barzini rode in Prince Scipione Borghese's Itala and wired dispatches to the Corriere della Sera and the Daily Telegraph, then turned them into a book that was in English within months. Jean du Taillis did the same for Le Matin from the Spyker of Charles Godard, a penniless adventurer who borrowed the car and was arrested before the finish. Ettore Guizzardi, the Itala's mechanic, who did much of the driving, left no writing of his own; he survives in Barzini's pages. The New York–Paris race of 1908 closes the chapter, with George Schuster's Thomas Flyer arriving after more than five months.",
  "Read together, these eyes show the road being re-invented from below: a housewife testing an invention, a vet testing a tyre, a temperance leader and a working mother turning the bicycle into a public argument about women's freedom, editors staging races to sell papers, and an inquest jury trying to decide who was responsible when a machine killed a pedestrian."
 ],
 "calendar_note": "All dates are Gregorian. In 1907 and 1908 the Russian Empire still used the Julian calendar, thirteen days behind; the Peking–Paris and New York–Paris crews and the Western press dated their dispatches in the Gregorian calendar, which is used here. Several famous dates in this chapter are disputed (Bertha Benz's departure; Annie Londonderry's start from Boston) and are shown with confidence 'approx' and the competing positions.",
 "eyes": [],
 "entries": [],
 "claims": [],
 "convergences": [],
 "ties": [],
 "threads_out": [],
 "images": [],
 "further": [],
 "vantage_key": "0 = the driver, rider or inventor at the centre of the trial; 1 = riding along or on the course as passenger, reporter or official; 2 = in the same city, organising or judging; 3 = in the same country at a distance; 4 = abroad or reading the news."
}

def eye(**k):
    ch["eyes"].append(k)

eye(id="bertha", short="Bertha Benz", name="Bertha Benz (née Ringer)", life="1849–1944",
    role="Wife and business partner of Karl Benz, aged 39 in August 1888; mother of five; her dowry had funded his workshop",
    side="Germany (Grand Duchy of Baden); the Benz household and firm",
    where="Mannheim, then on the road to Pforzheim and back",
    lat=49.488, lon=8.466,
    waypoints=[{"lat":49.488,"lon":8.466,"label":"Mannheim, dawn departure"},
               {"lat":49.398,"lon":8.672,"label":"Heidelberg"},
               {"lat":49.294,"lon":8.698,"label":"Wiesloch pharmacy, ligroin"},
               {"lat":49.124,"lon":8.598,"label":"Bruchsal"},
               {"lat":48.892,"lon":8.694,"label":"Pforzheim, arrival after dusk"}],
    vantage=0, vantage_label="the driver",
    form="later accounts (husband's memoir 1925; family and company retellings)",
    language="German",
    authenticity="No diary or letter of hers about the drive is known. The story rests on Karl Benz's memoir Lebensfahrt eines deutschen Erfinders (Leipzig, 1925) and on later retellings attributed to the family, notably the sons, which were shaped by Benz company publicity. Details such as the hatpin, the garter and the cobbler's leather are traditional and cannot be checked against a contemporary record; the date itself is disputed (most often 5 August 1888, sometimes 12 August or simply 'early August').",
    bio="Born in Pforzheim to a well-off carpenter's family, she put her inheritance into Benz's firm before their marriage in 1872. The 1888 drive, made without her husband's knowledge, was the first journey of real length in a petrol car and a demonstration that the machine could be used by someone other than its inventor. She lived to 95 and died two days after her birthday in 1944.",
    sources=[{"title":"DPMA (German Patent and Trade Mark Office): 'First car ride in the world'","url":DPMA},
             {"title":"Mercedes-Benz Group: Bertha Benz, founder and pioneer","url":MB_GROUP},
             {"title":"Wikipedia: Bertha Benz","url":WIKI_BB}])

eye(id="karl", short="Karl Benz", name="Karl Friedrich Benz (Carl Benz)", life="1844–1929",
    role="Engineer and owner of Benz & Cie., Mannheim; patentee of the Benz Patent-Motorwagen (1886)",
    side="Germany (Baden); Benz & Cie.",
    where="Mannheim workshop",
    lat=49.488, lon=8.466,
    vantage=2, vantage_label="the inventor left at home",
    form="patent specification (1886) and memoir (written later, 1925)",
    language="German",
    authenticity="German Reich patent DRP 37435 (filed 29 January 1886, granted 2 November 1886) survives and is on UNESCO's Memory of the World register. His memoir, Lebensfahrt eines deutschen Erfinders: Erinnerungen eines Achtzigjährigen (Leipzig, 1925), was written at eighty and is affectionate and selective; an English translation of its bicycle passage is published by German History in Documents and Images.",
    bio="A locksmith's son trained as an engineer, Benz had ridden a crude velocipede in the 1860s and wanted a horseless carriage as comfortable as a coach. His three-wheeled Motorwagen ran publicly in Mannheim in 1886, but sales were nil until his wife's drive showed what it could do. His memoir is the main written witness to her journey.",
    sources=[{"title":"GHDI: Carl Friedrich Benz, 'A New Bicycle (1867)', from Lebensfahrt eines deutschen Erfinders","url":GHDI},
             {"title":"Mercedes-Benz: Benz Patent Motor Car milestone","url":MB_PATENT},
             {"title":"DPMA: patent DE 37435 and Bertha Benz","url":DPMA}])

eye(id="dunlop", short="Dunlop", name="John Boyd Dunlop", life="1840–1921",
    role="Scottish-born veterinary surgeon with a large practice in May Street, Belfast; aged 47 in 1887",
    side="United Kingdom (Belfast, Ireland)",
    where="Belfast; later Dublin",
    lat=54.597, lon=-5.930,
    waypoints=[{"lat":54.597,"lon":-5.930,"label":"Belfast, yard tests 1887"},
               {"lat":53.330,"lon":-6.230,"label":"Dublin, from 1892"}],
    vantage=0, vantage_label="the inventor in his own yard",
    form="patent (1888) and memoir (written later)",
    language="English",
    authenticity="The 1888 British patent survives. Dunlop's own account, The History of the Pneumatic Tyre, was published in Dublin in 1924, after his death, and was written partly to defend his priority; it was not consulted directly for this chapter. His priority was in any case undone in 1890 when Robert William Thomson's 1840s patents for an air-filled tyre were found.",
    bio="Dunlop made an air-filled tyre of rubber sheet and canvas for his son's tricycle to soften Belfast's cobbles, and patented it in 1888. He had little share in the fortune the Dunlop company made. His story shows how an idea already invented once could become new when the bicycle boom gave it a market.",
    sources=[{"title":"Wikipedia: John Boyd Dunlop","url":DUNLOP}])

eye(id="willard", short="Willard", name="Frances Elizabeth Caroline Willard", life="1839–1898",
    role="President of the Woman's Christian Temperance Union, aged 53 when she learned to ride; staying with Lady Henry Somerset in England",
    side="United States; temperance and women's suffrage movements",
    where="Reigate, Surrey (learning), and Evanston, Illinois",
    lat=51.237, lon=-0.206,
    waypoints=[{"lat":51.237,"lon":-0.206,"label":"Reigate, learning to ride"},
               {"lat":42.045,"lon":-87.688,"label":"Evanston, Illinois"}],
    vantage=0, vantage_label="the learner",
    form="memoir (written soon after)",
    language="English",
    authenticity="A Wheel Within a Wheel: How I Learned to Ride the Bicycle (New York and Chicago: Fleming H. Revell, 1895) is her own account, written soon after the lessons; the text is on Project Gutenberg. The year of the lessons is inferred from her stated age and stays in England; the book gives days and months but rarely years.",
    bio="The most famous woman reformer in America in the 1880s and 1890s, Willard took up the bicycle after illness and grief over her mother's death. She named the machine Gladys and turned the lessons into a parable about will, balance and women's independence. A national leader learning in public gave the bicycle a respectability that ordinary riders lacked.",
    sources=[{"title":"A Wheel Within a Wheel (1895), Project Gutenberg","url":WILLARD}])

eye(id="londonderry", short="Londonderry", name="Annie Cohen Kopchovsky ('Annie Londonderry')", life="c. 1870–1947",
    role="Latvian-born Jewish mother of three from Boston, aged about 24; rode as 'Annie Londonderry' for a spring-water sponsor",
    side="United States (Boston)",
    where="Round the world by bicycle and steamer",
    lat=42.358, lon=-71.064,
    waypoints=[{"lat":42.358,"lon":-71.064,"label":"Boston, June 1894"},
               {"lat":41.880,"lon":-87.630,"label":"Chicago, Sept 1894"},
               {"lat":49.490,"lon":0.110,"label":"Le Havre, Dec 1894"},
               {"lat":43.300,"lon":5.370,"label":"Marseille, by ship east"},
               {"lat":35.440,"lon":139.640,"label":"Yokohama, March 1895"},
               {"lat":37.770,"lon":-122.420,"label":"San Francisco, March 1895"}],
    vantage=0, vantage_label="the rider and her own publicist",
    form="newspaper interviews and a signed newspaper article",
    language="English",
    authenticity="No diary is known. She is known from dozens of press interviews along the route and from her own article in the New York World (20 October 1895). Contemporary papers and her later biographer, her great-grand-nephew Peter Zheutlin, show that many of her tales (tiger hunts in India, a Japanese war wound, a hospital stay contradicted by a lecture she gave the same evening) were invented, and the wager that supposedly launched the trip may never have existed. Much of the Asian leg was by steamer.",
    bio="Married with three small children, she left Boston with a placard for Londonderry Lithia spring water on a heavy Columbia bicycle, swapped it in Chicago for a lighter Sterling, crossed to France and went east largely by ship before riding back across the American West. She is both a real long-distance rider and a pioneer of selling a journey to the press.",
    sources=[{"title":"Wikipedia: Annie Londonderry","url":LONDONDERRY},
             {"title":"Jewish Women's Archive: 'First woman to cycle the globe begins journey'","url":JWA}])

eye(id="anthony", short="S. B. Anthony", name="Susan Brownell Anthony", life="1820–1906",
    role="Suffrage leader, aged 75, interviewed by Nellie Bly",
    side="United States; National American Woman Suffrage Association",
    where="Interviewed for the New York World",
    lat=43.156, lon=-77.610,
    vantage=3, vantage_label="the veteran reformer watching the craze",
    form="newspaper interview",
    language="English",
    authenticity="Nellie Bly's long interview, 'Champion of Her Sex: Miss Susan B. Anthony', appeared in Joseph Pulitzer's New York World on 2 February 1896. Anthony's words are as Bly reported them; the bicycle passage has been reprinted many times since.",
    bio="Anthony had worked beside Elizabeth Cady Stanton since 1851 and did not ride herself. Her verdict on the bicycle, given to the most famous woman journalist in America, became the craze's best-known slogan.",
    sources=[{"title":"The Hairpin: Nellie Bly interviews Susan B. Anthony, 1896","url":BLY},
             {"title":"Rare Newspapers: the New York World, 2 February 1896","url":BLY2}])

eye(id="petitjournal", short="Petit Journal", name="Le Petit Journal (editor Pierre Giffard)", life="Giffard 1853–1922",
    role="Mass-circulation Paris daily and its editor, organiser of the first motor competition",
    side="France; the Paris press",
    where="Paris (Porte Maillot) to Rouen",
    lat=48.878, lon=2.283,
    waypoints=[{"lat":48.878,"lon":2.283,"label":"Paris, Porte Maillot"},
               {"lat":48.990,"lon":1.720,"label":"Mantes, lunch halt"},
               {"lat":49.443,"lon":1.099,"label":"Rouen, finish"}],
    vantage=2, vantage_label="the organising newspaper",
    form="newspaper reports and published judges' decision",
    language="French",
    authenticity="The paper's reports and the judges' award are the primary record; figures are as published and repeated in standard histories.",
    bio="Giffard, a cycling enthusiast who had already staged a Paris–Brest–Paris bicycle race in 1891, framed the 1894 event as a 'concours' for horseless carriages judged on safety, ease of driving and cost, not a race. The rules shaped the result as much as the machines did.",
    sources=[{"title":"Wikipedia: Paris–Rouen (motor race)","url":PR}])

eye(id="duncan", short="H. O. Duncan", name="Herbert Osbaldeston Duncan", life="fl. 1880s–1920s",
    role="English racing cyclist turned motoring promoter and journalist, based largely in Paris",
    side="Britain and France; the early motor trade",
    where="Paris (1895) and the London–Brighton road (1896)",
    lat=51.507, lon=-0.125,
    waypoints=[{"lat":48.866,"lon":2.333,"label":"Paris, 1895"},
               {"lat":51.507,"lon":-0.125,"label":"London, Metropole Hotel"},
               {"lat":50.822,"lon":-0.137,"label":"Brighton"}],
    vantage=1, vantage_label="insider on the course",
    form="memoir (written later)",
    language="English",
    authenticity="His The World on Wheels (Paris, 1926) is a participant's history written thirty years on; it is the source of the best-known doubts about which Emancipation Run cars really drove to Brighton. Treated here as a later witness, not a log.",
    bio="Duncan knew the French racing world and Harry Lawson's British syndicate from the inside. His scepticism about the 1896 results, voiced long after, is the main counterweight to the celebratory press accounts.",
    sources=[{"title":"Wikipedia: London to Brighton Veteran Car Run (citing Duncan)","url":BRIGHTON},
             {"title":"Wikipedia: Paris–Bordeaux–Paris","url":PBP}])

eye(id="timesherald", short="Times-Herald", name="Chicago Times-Herald (proprietor H. H. Kohlsaat)", life="Kohlsaat 1853–1924",
    role="Chicago daily that organised and judged the first American motor race",
    side="United States (Chicago)",
    where="Jackson Park, Chicago, to Evanston and back",
    lat=41.790, lon=-87.580,
    waypoints=[{"lat":41.790,"lon":-87.580,"label":"Jackson Park start/finish"},
               {"lat":42.045,"lon":-87.688,"label":"Evanston turn"}],
    vantage=2, vantage_label="organiser and judge",
    form="newspaper reports and judges' official results",
    language="English",
    authenticity="Times, distances and prize awards are those announced by the judges on 5 December 1895 and printed by the paper, which also invented the word 'motocycle' for the cars.",
    bio="Kohlsaat put up $5,000 in prizes to encourage an American industry and sell newspapers, explicitly following the French example. His paper's reporting fixed the numbers that all later accounts repeat.",
    sources=[{"title":"Wikipedia: Chicago Times-Herald race","url":CHI}])

eye(id="inquest", short="Inquest", name="Croydon inquest on Bridget Driscoll (coroner Percy Morrison)", life="held August 1896",
    role="Coroner's court and jury; witnesses included the driver Arthur Edsall, passenger Alice Standing and the victim's daughter",
    side="England (Surrey)",
    where="Croydon, near the Crystal Palace grounds",
    lat=51.376, lon=-0.098,
    vantage=1, vantage_label="the court hearing eyewitnesses",
    form="inquest proceedings as reported in the press",
    language="English",
    authenticity="The inquest record is known through newspaper reports of the evidence and verdict; the court's own papers were not consulted. Evidence about the car's speed conflicted and is reported as conflicting.",
    bio="Bridget Driscoll, a 44-year-old mother from Croydon, was crossing a terrace in the Crystal Palace grounds with her teenage daughter and a friend when a demonstration car hit her on 17 August 1896. The inquest is the first sustained attempt in Britain to judge a motorcar death.",
    sources=[{"title":"Wikipedia: Death of Bridget Driscoll","url":DRISCOLL}])

eye(id="barzini", short="Barzini", name="Luigi Barzini (the elder)", life="1874–1947",
    role="Star correspondent of the Corriere della Sera, also writing for the Daily Telegraph; passenger in the Itala",
    side="Italy; the Itala crew",
    where="In the Itala from Peking to Paris",
    lat=39.904, lon=116.407,
    waypoints=[{"lat":39.904,"lon":116.407,"label":"Peking, 10 June"},
               {"lat":40.810,"lon":114.880,"label":"Kalgan"},
               {"lat":47.920,"lon":106.920,"label":"Urga"},
               {"lat":52.290,"lon":104.280,"label":"Irkutsk"},
               {"lat":55.750,"lon":37.620,"label":"Moscow"},
               {"lat":48.866,"lon":2.333,"label":"Paris, 10 August"}],
    vantage=1, vantage_label="the reporter in the back seat",
    form="telegraphed dispatches and a book written from them (1907)",
    language="Italian (English translation 1907)",
    authenticity="His dispatches ran in the Corriere della Sera and the Daily Telegraph during the race; the book La metà del mondo vista da un'automobile appeared in 1907, with Borghese's preface, and in English the same year as Pekin to Paris (London: E. Grant Richards; translated by L. P. de Castelvecchio). Italian text on Wikisource; German and Dutch translations on Project Gutenberg. Written to be read, with the polish of a professional.",
    bio="Barzini had covered the Boxer aftermath and the Russo-Japanese War; the Corriere sent him to Peking at a day's notice. His book is the race's principal eyewitness narrative and the only place Ettore Guizzardi, the mechanic, speaks at length.",
    sources=[{"title":"La metà del mondo vista da un'automobile, chapter I (Wikisource)","url":BARZ_IT},
             {"title":"Pekin to Paris (1907 English translation), scanned PDF","url":BARZ_PDF},
             {"title":"Open Library: Pekin to Paris (1907)","url":BARZ_OL}])

eye(id="borghese", short="Borghese", name="Prince Scipione Borghese, Prince of Sulmona", life="1871–1927",
    role="Roman aristocrat, traveller and deputy, aged 35; entrant and leader of the Itala crew",
    side="Italy; the Itala crew",
    where="In the Itala from Peking to Paris",
    lat=39.904, lon=116.407,
    waypoints=[{"lat":39.904,"lon":116.407,"label":"Peking"},
               {"lat":47.920,"lon":106.920,"label":"Urga"},
               {"lat":52.290,"lon":104.280,"label":"Irkutsk"},
               {"lat":55.750,"lon":37.620,"label":"Moscow"},
               {"lat":59.940,"lon":30.310,"label":"St Petersburg detour"},
               {"lat":48.866,"lon":2.333,"label":"Paris"}],
    vantage=0, vantage_label="the entrant and leader",
    form="preface and reported telegrams",
    language="Italian",
    authenticity="Borghese wrote no narrative of his own; his voice survives in his preface to Barzini's book and in telegrams and statements reported by Barzini and the press. He had surveyed parts of the route on horseback in advance.",
    bio="An experienced Asian traveller, Borghese planned the run as an expedition, sending scouts and fuel ahead and choosing a powerful 7-litre Itala. His detour to St Petersburg for a dinner in his honour, made while still far ahead, shows how little the others threatened him.",
    sources=[{"title":"Wikipedia: Peking to Paris","url":P2P},
             {"title":"Peking-Paris im Automobil (German translation with Borghese's introduction), Project Gutenberg","url":BARZ_DE}])

eye(id="dutaillis", short="du Taillis", name="Jean du Taillis (for Le Matin)", life="fl. 1907",
    role="Le Matin correspondent riding as Charles Godard's only companion in the Spyker",
    side="France; Le Matin, organiser of the race",
    where="In the Spyker from Peking toward Paris",
    lat=39.904, lon=116.407,
    waypoints=[{"lat":39.904,"lon":116.407,"label":"Peking"},
               {"lat":47.920,"lon":106.920,"label":"Urga"},
               {"lat":56.490,"lon":84.950,"label":"Tomsk, 20 July"},
               {"lat":55.790,"lon":49.120,"label":"Kazan, 8 August"},
               {"lat":52.520,"lon":13.400,"label":"near Berlin, Godard arrested"},
               {"lat":48.866,"lon":2.333,"label":"Paris, 30 August"}],
    vantage=1, vantage_label="the organising paper's man in a rival car",
    form="newspaper dispatches",
    language="French",
    authenticity="His telegraphed reports ran in Le Matin, the paper that issued the challenge (31 January 1907) and later co-organised the 1908 New York–Paris race. Under questioning after Godard's arrest he stated that Godard had acted honestly. A book under his name followed; it was not consulted here.",
    bio="Du Taillis travelled with the most colourful driver in the race: Godard had no money, borrowed fuel and the car, and was arrested for fraud near the German border. His reports are the best view from inside a struggling car rather than the leader.",
    sources=[{"title":"Louwman Museum: The Peking–Paris automobile race in 1907","url":LOUWMAN},
             {"title":"Motor Sport, September 1997: '1907 — a race odyssey'","url":MOTORSPORT}])

eye(id="schuster", short="Schuster", name="George Schuster", life="1873–1972",
    role="Mechanic and road tester at the E. R. Thomas Motor Company, Buffalo; driver of the Thomas Flyer",
    side="United States; the Thomas team",
    where="New York to Paris via the United States, Alaska, Japan and Siberia",
    lat=40.758, lon=-73.985,
    waypoints=[{"lat":40.758,"lon":-73.985,"label":"Times Square, 12 Feb 1908"},
               {"lat":37.770,"lon":-122.420,"label":"San Francisco, March"},
               {"lat":61.130,"lon":-146.350,"label":"Valdez, Alaska, 8 April"},
               {"lat":43.120,"lon":131.890,"label":"Vladivostok"},
               {"lat":55.750,"lon":37.620,"label":"Moscow"},
               {"lat":48.866,"lon":2.333,"label":"Paris, 30 July"}],
    vantage=0, vantage_label="the mechanic who drove most of the way",
    form="memoir (written later)",
    language="English",
    authenticity="Schuster's account, The Longest Auto Race (written with Tom Mahoney, 1966), was published nearly sixty years later; under the chapter's rules it is digested, never quoted. Dates and figures are cross-checked against the New York Times coverage as summarised by the Smithsonian.",
    bio="Schuster joined the Thomas car as mechanic and ended as its driver and the only American aboard from start to finish. His account is the working man's view of the race: repairs, fuel, and the long Siberian mud.",
    sources=[{"title":"Smithsonian: 'Paris or Bust'","url":SMITH},
             {"title":"Wikipedia: George Schuster (driver)","url":SCHUSTER}])

E = ch["entries"]
def en(date_iso, date_display, precision, eye_, place, headline, digest, quote="", confidence="verified", source_note=""):
    E.append(dict(date_iso=date_iso, date_display=date_display, precision=precision, eye=eye_, place=place,
                  headline=headline, digest=digest, quote=quote, confidence=confidence, source_note=source_note))

en("1867","1867","year","karl","Mannheim and Pforzheim",
   "A borrowed velocipede plants the idea of horseless travel",
   "Recalling his twenties, Benz described taking over a friend's racing velocipede that its owner found too hard to ride. After about two weeks he could balance it on Mannheim's cobbles and ride it out to Pforzheim, to laughter and admiration. The wooden wheels and iron hoops rattled him, and he concluded that what was wanted was a vehicle as comfortable as a coach, driven by a machine instead of legs.",
   confidence="approx", source_note="Lebensfahrt eines deutschen Erfinders (1925), pp. 25ff., English translation at GHDI. Written nearly sixty years after the event.")
en("1886-01-29","Friday 29 January 1886","day","karl","Mannheim (filed with the Imperial Patent Office, Berlin)",
   "Patent for a 'vehicle with gas-engine drive'",
   "Benz applied for a patent on a light three-wheeled carriage driven by a single-cylinder petrol engine. The engine gave well under one horsepower and the car could manage about 16 km/h. The patent, numbered 37435, was granted on 2 November 1886 and backdated to the filing day.",
   source_note="DPMA page on Bertha Benz and DE 37435; Mercedes-Benz milestone page.")
en("1887-10","October 1887","month","dunlop","Belfast, his home yard",
   "An air tyre for a small boy's tricycle",
   "Dunlop wrapped an inflated tube of thin rubber in canvas around a wooden disc and fitted it to the back of his young son's tricycle to soften the jolting of Belfast's streets. He tried it in the yard of his house and found it rolled farther and more easily than a solid tyre. He went on to test larger versions for bicycles at the Cherryvale sports ground.",
   confidence="approx", source_note="Wikipedia: John Boyd Dunlop (October 1887); details of construction from Dunlop's later account as commonly summarised.")
en("1888-08-05","early August 1888 (most often Sunday 5 August; some accounts Sunday 12 August)","day","bertha","Mannheim, before dawn",
   "Leaving at first light without telling her husband",
   "Bertha Benz rolled the Model III motor carriage out of the workshop with her sons Eugen (15) and Richard (13) and set off for her mother's house in Pforzheim, leaving Karl asleep and the authorities unasked. She followed cart tracks and roads she knew from coach travel. On the hills the boys got out and pushed.",
   confidence="approx", source_note="DPMA gives 5 August 1888; Mercedes-Benz Group gives only 'August 1888'; a Wired 'This Day in Tech' piece uses 12 August. All details from later accounts, not a contemporary record.")
en("1888-08-05","early August 1888 (same day)","day","bertha","Wiesloch and the road south",
   "Ligroin from a pharmacy, a hatpin and a blacksmith",
   "At Wiesloch she bought ligroin, a cleaning solvent, at the town pharmacy because no one sold fuel, and the shop is now celebrated as the first filling station. On the road she is said to have cleared a blocked fuel line with a hatpin, used a garter to insulate a wire, had a blacksmith repair the chain and a cobbler nail leather onto the wooden brake blocks. Water for the cooling system had to be found at every stop.",
   confidence="approx", source_note="Wikipedia: Bertha Benz, from family tradition and the Memorial Route literature. The hatpin and garter are traditional details without contemporary documentation.")
en("1888-08-05","early August 1888, evening","day","bertha","Pforzheim",
   "Arriving after dusk and wiring Mannheim",
   "After a day of about twelve hours on roughly 106 km of unpaved roads, she reached Pforzheim somewhat after dark and telegraphed her husband that the journey had succeeded. It was the first trip of real length in a petrol car, and it had been made by someone who was not its inventor.",
   confidence="approx", source_note="Mercedes-Benz Group ('more than twelve hours', 'over 100 km'); Wikipedia: Bertha Benz (106 km; telegram).")
en("1888-08","August 1888, several days later","range","bertha","Pforzheim to Mannheim",
   "Driving home with advice for the engineer",
   "Some days later she drove back to Mannheim by another route. She told Karl the car could not climb hills unaided and needed a lower gear, and that the brakes needed lining; he added an extra gear, and she was proud ever after of having prompted it. The drive also gave the firm a story to sell.",
   confidence="approx", source_note="DPMA (third gear suggestion); Wikipedia: Bertha Benz (return several days later). Return date not recorded.")
en("1888-08","August 1888","month","karl","Mannheim",
   "Waking to find car and family gone",
   "In later accounts Karl learned of the trip only when the telegram arrived from Pforzheim. In his memoir he wrote that his wife had been the one person who stood by him when the business was failing and others had given up on the machine.",
   confidence="approx", source_note="DPMA summary of the memoir's statement about Bertha; telegram from Wikipedia: Bertha Benz.")
en("1888-12-07","Friday 7 December 1888","day","dunlop","Belfast",
   "The pneumatic-tyre patent is granted",
   "Dunlop's British patent for an air-filled tyre for cycles and other vehicles was granted, after an application made that summer. He believed the idea was his alone; within two years he was told it was not.",
   source_note="Wikipedia: John Boyd Dunlop (grant date). The application date of July 1888 is widely given but was not checked here.")
en("1889-05-18","Saturday 18 May 1889","day","dunlop","Queen's College sports ground, Belfast",
   "A local racer wins everything on air tyres",
   "Willie Hume, riding a bicycle fitted with Dunlop's tyres, won all four cycling events at the Queen's College Sports in Belfast, and soon after won nearly every event at a meeting in Liverpool. Riders who had laughed at the fat tyres began to order them, which was the start of the tyre business.",
   source_note="Wikipedia: John Boyd Dunlop.")
en("1890","1890","year","dunlop","Belfast",
   "Told the patent is void",
   "About two years after the grant, Dunlop was informed that his patent was invalid because Robert William Thomson had patented an air-filled tyre in the 1840s. The company built on his name survived on later improvements such as detachable tyres and valves, not on his original claim.",
   confidence="approx", source_note="Wikipedia: John Boyd Dunlop ('about two years after').")
en("1893-01-20","20 January (year inferred as 1893)","day","willard","Reigate, Surrey, at Lady Henry Somerset's home",
   "Mounting Gladys alone for the first time",
   "Willard had begun lessons with three young men holding the machine and two women steadying the bar, and practised about fifteen minutes a day. On 20 January she mounted without help, a day she marked as a red-letter day. She was fifty-three, wore long skirts, and had come to the bicycle partly to recover from illness and grief.",
   confidence="approx", source_note="A Wheel Within a Wheel (1895), Project Gutenberg. The book gives the day and month; the year is inferred from her age (53, born September 1839).")
en("1894-06-25","June 1894 (Monday 25 June or Wednesday 27 June)","day","londonderry","Massachusetts State House, Boston",
   "Leaving Boston with a sponsor's placard",
   "Before a crowd at the State House, Annie Kopchovsky set off on a 42-pound Columbia bicycle carrying an advertising placard for Londonderry Lithia spring water, whose $100 bought the name she rode under. She said two Boston men had bet that no woman could circle the globe by bicycle in fifteen months while earning $5,000 on the way. The bettors were never named.",
   confidence="approx", source_note="Wikipedia: Annie Londonderry gives 27 June (about 11 a.m.) in the text and 25 June in its timeline; the Jewish Women's Archive uses 25 June. Wager doubted by her biographer Peter Zheutlin.")
en("1894-07-22","Sunday 22 July 1894","day","petitjournal","Porte Maillot, Paris, to Rouen",
   "The first motor competition on the open road",
   "Twenty-one machines, steam and petrol, left Paris for Rouen, 126 km away, after qualifying trials, with a halt for lunch at Mantes from noon to half past one. Count Jules-Albert de Dion's steam tractor reached Rouen first in 6 hours 48 minutes, averaging about 19 km/h. Because it needed a stoker it was judged not 'easy to drive', and the 5,000-franc first prize was split between Panhard et Levassor and Peugeot.",
   source_note="Wikipedia: Paris–Rouen (motor race). 102 entry fees were paid; four starters stopped on the way.")
en("1894-09-24","Monday 24 September 1894","day","londonderry","Chicago",
   "Twenty pounds lighter, turning back east",
   "She reached Chicago having lost about twenty pounds. With winter coming she gave up crossing the Rockies to San Francisco that year, traded the Columbia for a lighter Sterling Roadster under a new sponsorship, and changed into men's riding clothes before heading back east to sail for France.",
   source_note="Wikipedia: Annie Londonderry.")
en("1894-12-03","Monday 3 December 1894","day","londonderry","Le Havre",
   "French customs take the bicycle",
   "After crossing on La Touraine she landed at Le Havre, where officials impounded her bicycle and took her money. She made her way to Paris and then to Marseille in about two weeks, partly by train, with a bandaged foot, telling French reporters she was an orphan, an heiress and a medical student.",
   source_note="Wikipedia: Annie Londonderry.")
en("1895-03-23","Saturday 23 March 1895","day","londonderry","San Francisco",
   "Back in America with stories from the East",
   "Having gone east from Marseille mostly by steamship, with day rides at ports from Colombo to Nagasaki, she sailed from Yokohama on 9 March and landed in San Francisco. She now told audiences of hunting tigers in India and of being wounded and jailed in the war between Japan and China; her biographer finds no support for either.",
   confidence="verified", source_note="Wikipedia: Annie Londonderry (dates); tales flagged as invented there and by Zheutlin.")
en("1895-06-11","Tuesday 11 June to Thursday 13 June 1895","range","duncan","Paris to Bordeaux and back",
   "Levassor drives 1,178 km almost alone",
   "Émile Levassor's two-seat Panhard covered the 1,178 km to Bordeaux and back in 48 hours 48 minutes, about 24.5 km/h. His relief driver at Bordeaux was asleep in an unknown hotel, so Levassor turned round and drove the return himself. Because the rules were written for four-seat cars, the official victory went to Paul Koechlin's Peugeot, nearly eleven hours slower. The Michelin brothers' car on pneumatic tyres dropped out over the time limit after punctures.",
   source_note="Wikipedia: Paris–Bordeaux–Paris. Duncan's own later account was not consulted for this entry.")
en("1895-10-20","Sunday 20 October 1895","day","londonderry","New York (New York World)",
   "Telling her own story to Pulitzer's paper",
   "Back home after returning to Chicago on 12 September and then Boston, she published a long first-person account in the New York World, billed as the most extraordinary journey ever undertaken by a woman. It mixed real hardship on Western roads with the tall tales she had been telling for months, and it argued that a woman could do anything a man could.",
   confidence="verified", source_note="Wikipedia: Annie Londonderry (date and headline).")
en("1895-11-02","Saturday 2 November 1895","day","timesherald","Chicago to Waukegan and back",
   "A trial run that only two cars start",
   "The Times-Herald's planned race had to be postponed, so a 100-mile exhibition run to Waukegan was held instead with a $500 purse for any car finishing within thirteen hours. Only Oscar Mueller's Benz and Frank Duryea's motor wagon started, and Mueller took the whole purse.",
   confidence="approx", source_note="Wikipedia: Chicago Times-Herald race (dated there as the day after 1 November 1895).")
en("1895-11-28","Thursday 28 November 1895 (Thanksgiving)","day","timesherald","Jackson Park, Chicago, to Evanston and back",
   "Snow, mud and the first American motor race",
   "Six cars started in snow at about 38°F: three Benz cars, the Duryea wagon and two electrics. Frank Duryea finished the 54-mile course in 10 hours 23 minutes, with two breakdowns including a stop at a forge. Oscar Mueller's Benz came second, though Mueller passed out from cold and the umpire, Charles Brady King, drove the last part. The paper called the cars 'motocycles', a word that did not last.",
   source_note="Wikipedia: Chicago Times-Herald race.")
en("1895-12-05","Thursday 5 December 1895","day","timesherald","Chicago",
   "Judges award the prizes",
   "The judges announced that Duryea had won $2,000 and Mueller $1,500, while the gold medal for design went to the Morris & Salom Electrobat, largely on the strength of its tests. As in France, the newspaper's rules, not only the order of finish, decided who counted as the winner.",
   source_note="Wikipedia: Chicago Times-Herald race.")
en("1895","1895","year","willard","Chicago and New York (publication)",
   "Turning the lessons into a public parable",
   "Willard published her account of learning to ride, dedicated to Lady Henry Somerset, who had given her the bicycle. She drew homely lessons from it: that failure came from a wavering will more than a wobbling wheel, that one should look ahead rather than down, and that teachers should hold on only as long as needed. Her trainers' command became her motto.",
   quote="Let go, but stand by.", source_note="A Wheel Within a Wheel (1895), Project Gutenberg.")
en("1896-02-02","Sunday 2 February 1896","day","anthony","New York World",
   "The bicycle as a freer of women",
   "Asked by Nellie Bly about the bicycle craze, Anthony said she rejoiced whenever she saw a woman riding, because it gave her a feeling of freedom and self-reliance. She endorsed bloomers or very short skirts for riding, as long skirts were dangerous in the wheel, and said women dressed foolishly mainly to please men.",
   quote="done more to emancipate women than anything else in the world",
   source_note="Nellie Bly, 'Champion of Her Sex', New York World, 2 February 1896, as reprinted by The Hairpin; date confirmed by Rare Newspapers.")
en("1896-08-17","Monday 17 August 1896","day","inquest","Dolphin Terrace, Crystal Palace grounds, London",
   "A demonstration car strikes a pedestrian",
   "Bridget Driscoll, 44, of Croydon, was crossing a terrace in the Crystal Palace grounds with her daughter May and a friend when a car giving demonstration rides for the Anglo-French Motor Carriage Company struck her; she died of a head injury. The driver, Arthur Edsall, said he had been doing about 4 mph and had rung his bell. One witness said the car came at a reckless pace, like a fire engine.",
   source_note="Wikipedia: Death of Bridget Driscoll, from press reports of the inquest evidence.")
en("1896-08","late August 1896","range","inquest","Croydon",
   "Six hours of evidence and a verdict of accident",
   "The inquest heard conflicting evidence: the car was said to be limited to 4 mph, a passenger, Alice Standing, claimed the engine had been altered to go faster, and a cab driver who examined it said it could not exceed about 4.5 mph. After some six hours the jury returned a verdict of accidental death, and no one was prosecuted. The coroner, Percy Morrison, expressed the hope that it would be the last such death.",
   quote="such a thing would never happen again", confidence="approx",
   source_note="Wikipedia: Death of Bridget Driscoll. Exact day of the inquest not confirmed; coroner's words as reported in the press.")
en("1896-11-14","Saturday 14 November 1896","day","duncan","Metropole Hotel, London, to Brighton",
   "Emancipation Day and a doubtful finish",
   "The Locomotives on Highways Act came into force, raising the limit for light motor vehicles to 14 mph and ending the need for a man walking ahead. Harry Lawson's Motor Car Club celebrated with a run to Brighton: at breakfast Lord Winchilsea tore a red flag in two, and 33 vehicles set off at 10.30 in wind and rain. About 17 reached Brighton; Léon Bollée was placed first in about 3 hours 45 minutes, while the two Duryeas were left off the official result. Duncan later wrote that some electric cars probably went by train and that no one knew how the Duryeas got there.",
   source_note="Wikipedia: London to Brighton Veteran Car Run (citing Duncan); Grace's Guide gives 32 starters and about 20 finishers, and the figures differ by source.")
en("1907-01-31","Thursday 31 January 1907","day","dutaillis","Paris (Le Matin)",
   "Le Matin's challenge: Peking to Paris by car",
   "Le Matin's front page asked whether anyone would drive from Peking to Paris that summer, arguing that a man with a car could go anywhere. About forty entries came in, but by spring only five cars were shipped from Marseille. The race committee later withdrew its sponsorship, and the remaining crews went anyway, with a magnum of champagne as the only prize.",
   source_note="Louwman Museum (date, front page); Wikipedia: Peking to Paris (entries, prize).")
en("1907-03-18","Monday 18 March 1907","day","barzini","Paris",
   "An editor's call: be in Peking",
   "Barzini was summoned by the Corriere della Sera's editor, Luigi Albertini, and told to join the race; within days he was sailing from Cherbourg for New York to cross America and the Pacific. His orders were simply to be at Peking station on a given day.",
   source_note="Barzini, La metà del mondo vista da un'automobile, ch. I (Wikisource).")
en("1907-06-04","Tuesday 4 June 1907","day","barzini","Peking",
   "Fuel caravans ahead, passports withheld",
   "Barzini, who had arrived at Peking station on the evening of 1 June, recorded news that camel caravans with petrol and oil were on their way into Mongolia, and that the French and Dutch cars had come up from Tientsin, one railway wagon lost on the way. The Chinese foreign board at first refused passports and then issued them for Mongolia without mentioning automobiles. Of 25 entrants, five machines had appeared.",
   source_note="Barzini, ch. I (Wikisource).")
en("1907-06-10","Monday 10 June 1907","day","barzini","French legation, Peking",
   "Five cars leave Peking",
   "The five cars left from the French legation: Borghese's 40-hp Itala, the 15-hp Spyker, two 10-hp De Dion-Boutons and Auguste Pons's three-wheeled Contal. Barzini noted that the Itala outweighed the 1,400 kg Spyker by some 600 kg, a burden in the steep, stony Nankou pass north of the city.",
   source_note="Wikipedia: Peking to Paris; Barzini ch. I for the power and weight figures.")
en("1907-06-10","Monday 10 June 1907","day","dutaillis","Peking",
   "A borrowed car and an empty wallet",
   "Du Taillis set out beside Charles Godard, who had reached China in May with the Spyker and almost no money, and who depended on others for petrol. Godard helped the struggling Contal crew by carrying some of their baggage and spare tyres.",
   source_note="Motor Sport, September 1997; Louwman Museum.")
en("1907-06-10","Monday 10 June 1907","day","borghese","Peking",
   "Starting an expedition, not a race",
   "Borghese had prepared the route like a traveller: he had ridden sections on horseback, measured the passes and arranged fuel ahead. His car was heavier and more powerful than any rival, and within days it was running alone at the front.",
   confidence="approx", source_note="Wikipedia: Peking to Paris; Borghese's preface to Barzini's book.")
en("1907-06-18","about 18 June 1907","range","dutaillis","Gobi Desert",
   "The Contal is left behind in the desert",
   "Eight days out, Pons's three-wheeled Contal stalled in the Gobi and could not go on; its crew was found alive by nomads, and the machine was never recovered. Soon afterwards the Spyker ran short of fuel, and Godard, once supplied, drove some 23 hours without stopping from Udde to Urga, about 385 miles, to catch the De Dions.",
   confidence="approx", source_note="Motor Sport, September 1997 (date reckoned from 'eight days after leaving Peking'; mileage as given there).")
en("1907-07","July 1907","month","barzini","Siberia, east of Lake Baikal",
   "Through a bridge and along the railway",
   "Barzini described the Itala breaking through the planks of a wooden bridge and dropping toward the ravine, with the crew thrown clear; Guizzardi and local helpers hauled it out and repaired it. Where roads failed around Lake Baikal the car was driven along the Trans-Siberian line itself, bumping over the sleepers with permission from the railway.",
   confidence="approx", source_note="History Today (bridge); Barzini, Pekin to Paris (1907), Siberian chapters. Exact day not checked.")
en("1907-07-20","Saturday 20 July 1907","day","dutaillis","Tomsk",
   "A postcard as proof of passage",
   "Godard posted a stamped card from Tomsk to prove he had been there. The Spyker was badly worn; it stopped at Tcheremkhovo, and Godard went west by train to meet a mechanic sent from the factory, while the De Dion crews telegraphed Le Matin demanding his disqualification.",
   confidence="verified", source_note="Louwman Museum (Tomsk card, 20 July); Motor Sport (Tcheremkhovo, De Dion telegram).")
en("1907-07-25","Thursday 25 July 1907","day","dutaillis","Tcheremkhovo, Siberia",
   "Godard begins his day-and-night chase",
   "Back with the car, Godard began driving day and night to catch the two De Dions, which had gone ahead. Du Taillis was the only witness to the effort, and his paper was also the body the rival teams were petitioning to throw Godard out.",
   source_note="Louwman Museum; Motor Sport, September 1997.")
en("1907-07","late July 1907","range","borghese","Moscow and St Petersburg",
   "A detour for dinner",
   "With a lead of weeks, Borghese turned north from Moscow to St Petersburg for a dinner given in the crew's honour, then returned to Moscow and resumed the road west. The detour cost him nothing in the standings.",
   confidence="approx", source_note="Wikipedia: Peking to Paris. Days not confirmed.")
en("1907-08-08","Thursday 8 August 1907","day","dutaillis","Kazan",
   "Catching the De Dions at four in the morning",
   "The Spyker entered Kazan at 4 a.m. and caught Cormier's and Collignon's De Dions. From there the three cars kept company toward Paris. Before Paris, Godard was arrested (at the Russian–German border or outside Berlin; accounts differ) on charges of defrauding the Dutch consulate in Peking; a factory driver took the Spyker on, and du Taillis later told investigators he believed Godard had acted honestly.",
   source_note="Louwman Museum; Motor Sport, September 1997. Arrest date not given in the sources.")
en("1907-08-10","Saturday 10 August 1907","day","borghese","Paris",
   "Entering Paris sixty-one days after Peking",
   "Borghese's Itala reached the Le Matin offices in Paris at about 4.30 in the afternoon, sixty-one days after leaving Peking and some three weeks ahead of the others, after roughly 15,000 km. Contemporary estimates put the crowd along the way in at half a million or more.",
   source_note="History Today (4.30 pm); Louwman Museum (61 days); Wikipedia: Peking to Paris (14,994 km); Unseen Histories (crowd estimate).")
en("1907-08-10","Saturday 10 August 1907","day","barzini","Paris",
   "The reporter arrives with his story already told",
   "Barzini's dispatches had made the Itala's progress a daily serial in Italy and Britain, and the book he made from them appeared before the year was out in Italian and English. His narrative gave the credit for the car's survival to Guizzardi, the mechanic who had nursed it across two continents.",
   confidence="approx", source_note="Wikipedia: Peking to Paris; Open Library record of the 1907 English edition.")
en("1907-08-30","Friday 30 August 1907","day","dutaillis","Paris",
   "The Spyker and the De Dions arrive without Godard",
   "The Spyker, driven from Berlin by a works driver sent by the Spijker company, and the two De Dions reached Paris together, 81 days after Peking. Near the city Godard is said to have tried to retake the wheel and been removed by police; a Paris court later sentenced him to eighteen months for fraud.",
   source_note="Louwman Museum (date, 81 days); Motor Sport (Godard near Paris; sentence).")
en("1908-02-12","Wednesday 12 February 1908","day","schuster","Times Square, New York",
   "Six cars leave Times Square for Paris",
   "Six cars from four nations, with seventeen men, waited in the cold for a start set for 11 a.m.; the mayor was late, and the pistol fired at about 11.15. The New York Times and Le Matin had planned a route across America, over the Alaskan winter and the Bering Strait into Siberia. Schuster rode as the Thomas Flyer's mechanic.",
   source_note="Smithsonian, 'Paris or Bust'.")
en("1908-04-08","Wednesday 8 April 1908","day","schuster","Valdez, Alaska",
   "Alaska ruled impassable",
   "After crossing the United States in winter, Schuster reached Valdez and judged that no car could cross Alaska. The organisers dropped the Bering route and shipped the cars across the Pacific to Japan and Vladivostok, granting the Flyer a 15-day allowance for its Alaskan detour.",
   source_note="Smithsonian, 'Paris or Bust'.")
en("1908-07-30","Thursday 30 July 1908","day","schuster","Paris",
   "Second to arrive, first on the rules",
   "After Siberia, where one wrong turn cost about fifteen hours, the Thomas Flyer reached Paris. The German Protos had arrived on 26 July, but it had been penalised fifteen days for travelling by rail from Ogden to Seattle, so the Thomas was declared the winner after about 22,000 miles.",
   source_note="Smithsonian, 'Paris or Bust' (the NYT report is dated 31 July in its sources); Wikipedia: George Schuster.")

C = ch["claims"]
def cl(d, dd, e, claim, form, ev, conf="verified"):
    C.append(dict(date_iso=d, date_display=dd, eye=e, claim=claim, form=form, evidence=ev, confidence=conf))
cl("1886-01-29","29 January 1886","karl","Patent DRP 37435 filed for a three-wheeled petrol carriage, under 1 hp, about 16 km/h","conceived","DPMA; Mercedes-Benz milestone page")
cl("1886-07-03","3 July 1886","karl","First public drive of the Patent-Motorwagen on the Ringstrasse, Mannheim","tested","Mercedes-Benz milestone page")
cl("1887-10","October 1887","dunlop","Air-filled tyre tested on his son's tricycle in a Belfast yard","tested","Wikipedia: John Boyd Dunlop","approx")
cl("1888-08-05","early August 1888 (5 August most often cited; 12 August in some accounts)","bertha","Mannheim to Pforzheim, about 106 km in roughly 12 hours: the first long-distance petrol-car journey; position: 5 August (DPMA) vs 12 August (Wired) vs 'August' (Mercedes-Benz)","first","DPMA; Mercedes-Benz Group; Wikipedia","approx")
cl("1888-12-07","7 December 1888","dunlop","British pneumatic-tyre patent granted; found invalid c. 1890 because of R. W. Thomson's 1840s patents","other","Wikipedia: John Boyd Dunlop")
cl("1889-05-18","18 May 1889","dunlop","Willie Hume wins all four cycle races at Queen's College Sports, Belfast, on Dunlop tyres","record","Wikipedia: John Boyd Dunlop")
cl("1894-06-25","25 or 27 June 1894","londonderry","Starts from Boston to ride round the world in 15 months; wager and many later claims contested; much of Asia crossed by steamer","other","Wikipedia: Annie Londonderry; Jewish Women's Archive","approx")
cl("1894-07-22","22 July 1894","petitjournal","Paris–Rouen, 126 km: de Dion steam car first in 6 h 48 min (about 19 km/h); prize shared by Panhard et Levassor and Peugeot","first","Wikipedia: Paris–Rouen")
cl("1895-06-11","11–13 June 1895","duncan","Paris–Bordeaux–Paris, 1,178 km: Levassor 48 h 48 min (about 24.5 km/h); official win to Koechlin's Peugeot under four-seat rule","record","Wikipedia: Paris–Bordeaux–Paris")
cl("1895-09-12","12 September 1895","londonderry","Returns to Chicago, about 15 months after leaving Boston; claims to have completed the circuit","other","Wikipedia: Annie Londonderry")
cl("1895-11-28","28 November 1895","timesherald","First US motor race, 54 miles in snow: Duryea 10 h 23 min elapsed (7 h 53 min running), Mueller's Benz second","first","Wikipedia: Chicago Times-Herald race")
cl("1896-08-17","17 August 1896","inquest","Bridget Driscoll killed by a demonstration car at the Crystal Palace; inquest verdict: accidental death; claimed speed 4 mph disputed","inquiry","Wikipedia: Death of Bridget Driscoll")
cl("1896-11-14","14 November 1896","duncan","Locomotives on Highways Act in force (14 mph); London–Brighton run, about 33 starters and 17 finishers; Duryea times excluded","opened","Wikipedia: London to Brighton Veteran Car Run; Grace's Guide")
cl("1907-06-10","10 June 1907","barzini","Five cars leave Peking for Paris; Contal abandoned in the Gobi about eight days later","tested","Wikipedia: Peking to Paris; Motor Sport 1997")
cl("1907-08-10","10 August 1907","borghese","Itala reaches Paris after 61 days and about 14,994 km; other three finishers arrive 30 August after 81 days","record","Louwman Museum; Wikipedia: Peking to Paris")
cl("1908-07-30","30 July 1908","schuster","Thomas Flyer reaches Paris after about 22,000 miles and is declared winner; Protos arrived 26 July but carried a 15-day rail penalty","record","Smithsonian, 'Paris or Bust'")

ch["convergences"] = [
 {"date":"1888-08","label":"Summer 1888: an air tyre and a long drive","eyes":["bertha","karl","dunlop"],"note":"Within weeks of each other, Bertha Benz proved a petrol car could go 100 km and Dunlop was patenting the air tyre that would make bicycles and cars bearable on rough roads. Neither knew of the other; the Benz car ran on solid tyres."},
 {"date":"1888-08-05","label":"The drive to Pforzheim, seen from both ends","eyes":["bertha","karl"],"note":"She tested the machine in the field and came back with a list of faults; he received a telegram and, decades later, made her the one person who believed in him. The only witnesses who wrote it down did so long afterwards."},
 {"date":"1894-07","label":"Summer 1894: a woman on a bicycle and men in motor carriages","eyes":["londonderry","petitjournal"],"note":"While Kopchovsky was pedalling west from Boston on a 42-pound bicycle, Paris was staging the first motor competition. Both were sponsored spectacles: a spring-water company paid for her name, a newspaper for theirs."},
 {"date":"1895","label":"1895: women writing the bicycle","eyes":["willard","londonderry"],"note":"Willard's sober parable of balance and will and Londonderry's self-made legend in the New York World appeared in the same year, two opposite ways of using the bicycle to argue that women could go where they chose."},
 {"date":"1895-11","label":"The motor race comes to America","eyes":["timesherald","duncan"],"note":"Chicago copied the Paris races within months, down to a newspaper sponsor and prize rules that decided the winner. The Duryea brothers' cars connect the Chicago snow of 1895 with the disputed Brighton finish a year later."},
 {"date":"1896","label":"1896: freedom and the first deaths","eyes":["anthony","inquest","duncan"],"note":"In February Anthony called the bicycle women's great emancipator; in August an inquest jury heard how a car had killed a pedestrian at 4 mph or more; in November Britain celebrated 'emancipation' from the red-flag laws. The same word was used for very different freedoms."},
 {"date":"1907-06-10","label":"Departure from Peking","eyes":["barzini","borghese","dutaillis"],"note":"The leader planned an expedition, his reporter planned a serial, and the rival reporter set off with a driver who could not pay for his own petrol. Their accounts diverge almost from the first pass."},
 {"date":"1907-07-25","label":"Late July 1907: one car far ahead, one fighting to stay in","eyes":["borghese","dutaillis","barzini"],"note":"As Godard began his non-stop chase from Tcheremkhovo, Borghese was so far ahead that he could detour from Moscow to St Petersburg for a dinner."},
 {"date":"1907-08-10","label":"The Itala reaches Paris","eyes":["borghese","barzini","dutaillis"],"note":"Borghese and Barzini arrived to crowds; two days earlier the Spyker and De Dions had only just met at Kazan, and Godard would be arrested before he saw Paris."}
]

ch["ties"] = [
 {"a":"bertha","b":"karl","kind":"relative","note":"Married in 1872; her dowry financed his firm, and her drive was the field test he had not made."},
 {"a":"karl","b":"timesherald","kind":"mentioned","note":"Three of the six starters in the Chicago race were Benz cars, and Oscar Mueller's Benz finished second."},
 {"a":"petitjournal","b":"timesherald","kind":"influenced","note":"Kohlsaat's Chicago contest followed the French model of a newspaper-sponsored trial with judged prizes."},
 {"a":"petitjournal","b":"duncan","kind":"influenced","note":"Paris–Rouen led directly to the longer Paris–Bordeaux–Paris of 1895, which Duncan's circle followed from inside the trade."},
 {"a":"timesherald","b":"duncan","kind":"mentioned","note":"Duryea cars ran in both Chicago (1895) and the Emancipation Run (1896), where Duncan later questioned how they reached Brighton."},
 {"a":"inquest","b":"duncan","kind":"influenced","note":"Driscoll was killed while the old speed limits still applied; three months later the new Act took effect and the Brighton run celebrated it."},
 {"a":"willard","b":"anthony","kind":"met","note":"Allies in the women's movement who worked together through the National Council of Women; both turned the bicycle into an argument for women's independence in 1895–96."},
 {"a":"anthony","b":"londonderry","kind":"opposite sides","note":"The veteran campaigner praised the bicycle in principle; the young rider used it to sell herself and her sponsors. The same New York World printed both."},
 {"a":"barzini","b":"borghese","kind":"met","note":"Travelled together in the Itala for the whole journey; Borghese wrote the preface to Barzini's book."},
 {"a":"barzini","b":"dutaillis","kind":"opposite sides","note":"Rival correspondents for rival papers and cars, filing from the same telegraph stations across Mongolia and Siberia."},
 {"a":"borghese","b":"dutaillis","kind":"opposite sides","note":"The best-equipped entrant and the reporter in the poorest car; Le Matin, du Taillis's paper, received the winner in Paris."},
 {"a":"dutaillis","b":"schuster","kind":"mentioned","note":"Le Matin co-organised the 1908 New York–Paris race, and Charles Godard entered it too, in a Motobloc that never reached the Pacific coast."}
]

ch["threads_out"] = [
 {"to":"rainhill-1830","note":"Britain's red-flag rules were written in the 1860s for heavy steam road locomotives, and only the 1896 Act freed light motor cars from them. William Huskisson's death at the opening of the Liverpool and Manchester Railway in 1830 and Bridget Driscoll's in 1896 are the best-known first fatalities of the two modes."},
 {"to":"kitty-hawk","note":"Wilbur and Orville Wright opened their bicycle shop in Dayton in 1892, at the height of the craze traced here; the bicycle trade paid for their flying experiments and taught them the light machining they used."},
 {"to":"v6:seneca-falls","note":"Susan B. Anthony, who praised the bicycle in 1896, had worked with Elizabeth Cady Stanton, an organiser of the 1848 Seneca Falls convention, since 1851; the bicycle debate of the 1890s ran through the same suffrage movement."},
 {"to":"oceans-1869","note":"Annie Londonderry's eastward leg from Marseille to Colombo and on to Asia went by steamer through the Suez Canal, which had opened in 1869 and made such a round-the-world trip practical."},
 {"to":"v3:embassies-1403","note":"Five centuries after Timurid envoys travelled overland between Herat and Beijing by caravan, the Peking–Paris cars set out from the same capital to cross Inner Asia by land, relying on camel caravans to carry their fuel ahead."}
]

ch["images"] = [
 {"url":DPMA,"title":"Bertha Benz and patent DE 37435 (DPMA)","caption":"The German patent office's page on Bertha Benz, with the patent of 29 January 1886 and period images of the Benz family and car. The patent is on UNESCO's Memory of the World register.","date":"1886–1888","credit":"Deutsches Patent- und Markenamt; Automuseum Dr. Carl Benz, Ladenburg"},
 {"url":"https://mercedes-benz-publicarchive.com/marsClassic/en/instance/ko/First-automobile-race-Paris---Rouen-126km.xhtml?oid=7419","title":"Paris–Rouen, 1894 (Mercedes-Benz Classic archive)","caption":"Archive record for the 126 km Paris–Rouen trial of 22 July 1894, the first motor competition on public roads; the winning Panhard and Peugeot cars used Daimler-licensed engines.","date":"1894","credit":"Mercedes-Benz Classic Archive"},
 {"url":"https://mercedes-benz-publicarchive.com/marsClassic/en/instance/ko/Paris---Bordeaux---Paris-race-1895.xhtml?oid=7398","title":"Paris–Bordeaux–Paris, 1895 (Mercedes-Benz Classic archive)","caption":"Archive record for the 1,178 km race of June 1895 in which Levassor drove almost the whole distance alone but was denied first prize by the four-seat rule.","date":"1895","credit":"Mercedes-Benz Classic Archive"},
 {"url":"https://mercedes-benz-publicarchive.com/marsClassic/en/instance/ko/London---Brighton-1896.xhtml?oid=7422","title":"London–Brighton, 1896 (Mercedes-Benz Classic archive)","caption":"Archive record for the Emancipation Run of 14 November 1896, held to celebrate the end of the old speed limits for light motor vehicles.","date":"1896","credit":"Mercedes-Benz Classic Archive"},
 {"url":LOUWMAN,"title":"The Spyker in the Peking–Paris race (Louwman Museum)","caption":"The Dutch museum that holds the largest Spyker collection tells the story of Godard and du Taillis's car, which reached Paris without its driver on 30 August 1907. The race car itself was later dismantled.","date":"1907","credit":"Louwman Museum, The Hague"},
 {"url":"https://newseumed.org/artifact/nellie-bly-interviews-susan-b-anthony-1896/","title":"Nellie Bly interviews Susan B. Anthony (NewseumED)","caption":"Educational archive page for the New York World interview of 2 February 1896, in which Anthony called the bicycle the greatest emancipator of women.","date":"1896","credit":"New York World; NewseumED"}
]

ch["further"] = [
 {"title":"Frances E. Willard, A Wheel Within a Wheel (1895), Project Gutenberg","url":WILLARD},
 {"title":"Luigi Barzini, Pekin to Paris (1907 English translation), scanned PDF","url":BARZ_PDF},
 {"title":"Barzini, La metà del mondo vista da un'automobile, chapter I (Italian Wikisource)","url":BARZ_IT},
 {"title":"Carl Benz, 'A New Bicycle (1867)', German History in Documents and Images","url":GHDI},
 {"title":"Smithsonian Magazine: 'Paris or Bust: The Great New York-to-Paris Auto Race of 1908'","url":SMITH},
 {"title":"The Spectator, 25 April 1908: review of 'Pekin to Paris in a Motor-Car'","url":SPECTATOR},
 {"title":"Motor Sport, September 1997: '1907 — a race odyssey'","url":MOTORSPORT}
]

json.dump(ch, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(ch["eyes"]), len(ch["entries"]), len(ch["claims"]), len(ch["convergences"]), len(ch["ties"]), len(ch["threads_out"]), len(ch["images"]), len(ch["further"]))
