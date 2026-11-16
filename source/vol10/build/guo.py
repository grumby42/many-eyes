import json
OUT="/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/vol10/ch-guo-1877.json"
LON=(51.521,-0.145)
FRODSHAM="https://asj.upd.edu.ph/mediabox/archive/ASJ-05-03-1967/frodsham-record-envoy-voyage-west.pdf"
BIBLIO="https://biblioasia.nlb.gov.sg/vol-19/issue-4/jan-mar-2024/qing-ambassadors-guo-song-tao/"
LIJQ="https://www.cuhk.edu.hk/ics/journal/articles/v71p119.pdf"
WANG="https://www.aisixiang.com/data/134087.html"
PAPER="https://www.thepaper.cn/newsDetail_forward_2800153"
WS11="https://zh.wikisource.org/zh-hans/%E5%80%AB%E6%95%A6%E8%88%87%E5%B7%B4%E9%BB%8E%E6%97%A5%E8%A8%98/%E5%8D%B711"
WS1="https://zh.wikisource.org/zh-hans/%E5%80%AB%E6%95%A6%E8%88%87%E5%B7%B4%E9%BB%8E%E6%97%A5%E8%A8%98/%E5%8D%B701"
BOULGER="https://www.cambridge.org/core/books/the-life-of-sir-halliday-macartney-kcmg/1A5D6619B464CBBB17C36FDB120F8907"

eyes=[
 dict(id="guo",short="Guo Songtao",name="Guo Songtao (Kuo Sung-t'ao, 郭嵩燾)",life="1818–1891",
  role="Hunanese scholar-official aged 58, former acting governor of Guangdong; vice-president of the Board of War; first resident Qing minister to Britain (and from 1878 to France)",
  side="Qing China; the 'foreign affairs' (yangwu) reformers around Li Hongzhang",
  where="At sea Shanghai–Southampton (Dec 1876–Jan 1877), then the legation at 49 Portland Place, London; Paris in 1878",
  lat=LON[0],lon=LON[1],
  waypoints=[{"lat":31.23,"lon":121.47,"label":"Shanghai, sails 2 Dec 1876"},{"lat":22.28,"lon":114.16,"label":"Hong Kong, 6–7 Dec 1876"},{"lat":1.29,"lon":103.85,"label":"Singapore, 13–14 Dec 1876"},{"lat":6.03,"lon":80.22,"label":"Galle, 21–22 Dec 1876"},{"lat":35.9,"lon":14.51,"label":"Malta, 12 Jan 1877"},{"lat":51.521,"lon":-0.145,"label":"London, 21 Jan 1877 – early 1879"}],
  vantage=0,vantage_label="the envoy himself",form="diary (a voyage diary sent home and printed; and a full private diary)",language="Classical Chinese",
  authenticity="Two texts. Shi xi jicheng (使西紀程, Record of an Envoy's Journey to the West) is the voyage section of his diary, finished in early February 1877, sent to the Zongli Yamen and printed by the Tongwen guan in 1877; it was suppressed and its blocks destroyed after a memorial of 16 June 1877, but copies survived and it was reprinted in the 1891 travel collection Xiaofanghuzhai yudi congchao. The full diary (Guo Songtao riji, Hunan renmin chubanshe, 4 vols, 1980–83; the London–Paris part also issued as Lundun yu Bali riji, Yuelu shushe 1984) is a private day-by-day record. English: J. D. Frodsham, The First Chinese Embassy to the West (Oxford, 1974). Digests here only.",
  bio="A Hunan classicist who had fought the Taiping alongside Zeng Guofan and had argued since 1859 that China must study the West. Sent to London first to apologise for the killing of the British interpreter Augustus Margary, he became the first Chinese official to live and write inside a Western capital for two years. What he admired — schools, prisons, railways, Parliament, learned societies — was exactly what ruined him at home.",
  sources=[{"title":"J. D. Frodsham, 'Record of an Envoy's Voyage to the West' (Asian Studies 5:3, 1967), translation of Shi xi jicheng","url":FRODSHAM},{"title":"Lundun yu Bali riji, juan 11 (GX 3/8), Wikisource","url":WS11},{"title":"Lundun yu Bali riji, juan 1 (GX 2/2–10), Wikisource","url":WS1}]),
 dict(id="liu",short="Liu Xihong",name="Liu Xihong (Liu Hsi-hung, 劉錫鴻; courtesy name Yunsheng)",life="d. c. 1891",
  role="Cantonese juren and minor official, appointed deputy envoy in 1876; from 1877 minister to Germany",
  side="Qing China; conservative critics of 'foreign matters'",
  where="49 Portland Place with Guo until late 1877, then Berlin",
  lat=LON[0],lon=LON[1],waypoints=[{"lat":31.23,"lon":121.47,"label":"Shanghai, Dec 1876"},{"lat":51.521,"lon":-0.145,"label":"London 1877"},{"lat":52.52,"lon":13.40,"label":"Berlin, from late 1877"}],
  vantage=0,vantage_label="the rival inside the legation",form="travel notes (diary-based) and memorials",language="Classical Chinese",
  authenticity="His Ying yao siji (英軺私記, Private Notes of a Mission to England) survives and was reprinted in the modern Zou xiang shijie series (Yuelu shushe); translated in Frodsham (1974). His impeachment of Guo (spring 1878) is known from court documents and later studies. Digest only.",
  bio="An old acquaintance of Guo from Guangdong, he was attached to the embassy late, and was widely read as a watchman for the conservatives. His own notes are more curious about Britain than his reputation suggests, but in London he and Guo fell into a quarrel that ended with mutual impeachments and his anonymous-letter campaign.",
  sources=[{"title":"Frodsham (1967), footnote on Liu's appointment to Germany","url":FRODSHAM},{"title":"The Paper: Guo and Liu's feud (Chinese)","url":PAPER}]),
 dict(id="zhang",short="Zhang Deyi",name="Zhang Deyi (Chang Te-i, 張德彝)",life="1847–1918",
  role="Bannerman graduate of the Tongwen guan (foreign-language college), interpreter to the legation, aged about 30",
  side="Qing China; the new corps of trained interpreters",
  where="49 Portland Place, London",lat=LON[0],lon=LON[1],
  vantage=1,vantage_label="interpreter in the room",form="diary",language="Chinese",
  authenticity="His fourth travel diary, Suishi Ying E ji (隨使英俄記, Record of Accompanying the Envoy to England and Russia), part of his 'Hanghai shuqi' series, survives in manuscript and modern editions; translated in part by Frodsham (1974). Digest only.",
  bio="Already a veteran of three journeys west (from 1866), Zhang noticed food, furniture, guests and gadgets more than doctrine. His diary is the gossipy, close-up counterpart to Guo's reflections and Liu's suspicions.",
  sources=[{"title":"Wang Ding on the Russell visit in three diaries (Dushu 2022)","url":WANG}]),
 dict(id="macartney",short="Macartney",name="Sir (Samuel) Halliday Macartney",life="1833–1906",
  role="Scottish former army surgeon, ex-director of the Nanjing arsenal; English secretary and counsellor to the legation (1876–1906)",
  side="British in Qing service",where="With the embassy at sea and at Portland Place",lat=LON[0],lon=LON[1],
  vantage=1,vantage_label="go-between",form="letters (to The Times and to family), later used by his biographer",language="English",
  authenticity="His letters and papers underlie D. C. Boulger, The Life of Sir Halliday Macartney (1908), chapter XI 'The Kwoh Embassy' (pp. 244–277); his letter to The Times appeared on 23 May 1878. Boulger's text is out of copyright but was not consulted directly here.",
  bio="He chose the house in Portland Place, translated Guo's speeches and notes, and explained Britain to the envoy — and the envoy to Britain. He stayed on to serve Zeng Jize and his successors for thirty years.",
  sources=[{"title":"Boulger, Life of Sir Halliday Macartney (1908; Cambridge reissue page)","url":BOULGER}]),
 dict(id="he",short="He Jinshou",name="He Jinshou (何金壽)",life="d. 1882",
  role="Hanlin compiler and diarist-of-the-court (rijiang qijuzhu guan) in Beijing",
  side="Qing court; the qingyi 'pure criticism' censorial current",where="Beijing",lat=39.906,lon=116.397,
  vantage=3,vantage_label="critic at court",form="memorial (court record)",language="Classical Chinese",
  authenticity="His memorial of 16 June 1877 asking that Shi xi jicheng be suppressed, and the same-day edict, are documented in Qing records and cited by Li Jiaqi (2020).",
  bio="He never saw London. His memorial treated the envoy's praise of Western order as a betrayal of the dynasty's dignity, and the court agreed the same day.",
  sources=[{"title":"Li Jiaqi, Western-language sources on Shi xi jicheng (2020)","url":LIJQ}]),
 dict(id="lihz",short="Li Hongzhang",name="Li Hongzhang (李鴻章)",life="1823–1901",
  role="Governor-general of Zhili and superintendent of trade for the northern ports; negotiator of the Chefoo Convention; Guo's patron",
  side="Qing China; yangwu reformers",where="Tianjin",lat=39.13,lon=117.2,
  vantage=3,vantage_label="patron at home",form="dated letters",language="Classical Chinese",
  authenticity="Letters of 1 May, 9 May, 24 July and 8 November 1877 in his collected correspondence (Li Hongzhang quanji), as cited by Li Jiaqi (2020), who notes that the editors misdated the 24 July letter to 1878.",
  bio="He had signed the convention that sent Guo abroad and protected him as far as he dared. His letters track the diary's journey from welcome reading to forbidden book.",
  sources=[{"title":"Li Jiaqi (2020)","url":LIJQ}]),
 dict(id="lici",short="Li Ciming",name="Li Ciming (李慈銘)",life="1830–1894",
  role="Zhejiang scholar and minor Board official in Beijing, famous diarist",
  side="Qing literati",where="Beijing",lat=39.9,lon=116.38,
  vantage=3,vantage_label="reader in the capital",form="diary",language="Classical Chinese",
  authenticity="Yuemantang riji (越縵堂日記), a celebrated multi-decade diary published in facsimile; the entry of 28 July 1877 is cited by Li Jiaqi (2020).",
  bio="One of the sharpest pens of late-Qing Beijing, he read the envoy's diary and condemned it in terms that echoed the memorial: the kind of reader Guo's text met at home.",
  sources=[{"title":"Li Jiaqi (2020)","url":LIJQ}]),
 dict(id="punch",short="Punch",name="Punch, or the London Charivari",life="1841–2002",
  role="London weekly comic magazine",side="British press (hosts)",where="Fleet Street, London",lat=51.514,lon=-0.106,
  vantage=2,vantage_label="host satirists",form="newspaper (comic weekly)",language="English",
  authenticity="The issue of 10 February 1877 carried a comic poem on the envoy's arrival; it is reproduced from the Heidelberg University Library digitisation in the BiblioAsia article cited.",
  bio="Punch turned every foreign visitor into verse and caricature. Its treatment of Guo is a measure of how London first framed him: as an exotic oddity arriving to say sorry.",
  sources=[{"title":"BiblioAsia (2024), reproducing Punch 10 Feb 1877","url":BIBLIO}]),
 dict(id="times",short="The Times",name="The Times (London) and its correspondents",life="1785–",
  role="London daily newspaper; letters from R. S. Gundry, former editor of the North-China Herald",
  side="British press (hosts)",where="Printing House Square, London",lat=51.512,lon=-0.102,
  vantage=2,vantage_label="host newspaper",form="newspaper",language="English",
  authenticity="Items cited from Li Jiaqi (2020) and from a reprint in the Christchurch Globe, 24 January 1879 (Papers Past).",
  bio="The Times printed Macartney's translation of Guo's anti-opium speech, letters about his disgrace, and leaders on his successor. It is the hosts' record of how the envoy's troubles at home looked from London.",
  sources=[{"title":"Li Jiaqi (2020)","url":LIJQ},{"title":"Globe (Christchurch), 24 Jan 1879, 'Chinese Progress' (reprint from The Times)","url":"https://dynamic-rsnz.natlib.govt.nz/newspapers/GLOBE18790124.2.20"}]),
 dict(id="thomson",short="Lock & Whitfield",name="Lock and Whitfield, photographers (copyright owner John Thomson)",life="studio active 1856–c.1895",
  role="Regent Street portrait studio; John Thomson (1837–1921), the photographer of China, registered the copyrights",
  side="British (hosts)",where="Regent Street, London",lat=51.512,lon=-0.140,
  vantage=2,vantage_label="host camera",form="dated photographs with copyright entry forms",language="English",
  authenticity="National Archives, Kew, COPY 1/36/174 and 175, entry forms registered 14 February 1877 with the photographs attached. A woodburytype from the same studio appeared in Men of Mark (1880).",
  bio="Thomson had photographed China from Canton to Peking (1868–72); three weeks after the envoys landed his name was on the copyright of their portraits. The camera is one of the few host 'eyes' that recorded Guo and Liu without words.",
  sources=[{"title":"TNA COPY 1/36/174","url":"https://beta.nationalarchives.gov.uk/catalogue/id/C16775934"},{"title":"TNA COPY 1/36/175","url":"https://beta.nationalarchives.gov.uk/catalogue/id/C16775935"}]),
 dict(id="ipswich",short="Ipswich Journal",name="The Ipswich Journal",life="1720–1902",
  role="Suffolk provincial weekly",side="British press (hosts)",where="Ipswich",lat=52.059,lon=1.155,
  vantage=2,vantage_label="provincial host press",form="newspaper",language="English",
  authenticity="'Visit of the Chinese Ambassadors to Ipswich', Ipswich Journal, 3 July 1877, held in the P. A. Crush Chinese Railway Collection (Hong Kong Railway Society) and cited in Wikipedia's Guo Songtao article; not seen directly.",
  bio="Ransomes and Rapier of Ipswich had built the locomotives for the short-lived Woosung railway near Shanghai (1876). The town paper recorded the Chinese envoys walking through the works that made them.",
  sources=[{"title":"Guo Songtao (Wikipedia), citing the Ipswich Journal","url":"https://en.wikipedia.org/wiki/Guo_Songtao"}]),
 dict(id="portpress",short="Port press",name="The treaty-port and colonial press (Hong Kong Daily Press, North-China Herald, Singapore Daily Times, Christchurch Globe)",life="1850s–",
  role="English-language newspapers of Hong Kong, Shanghai, Singapore and New Zealand",side="British colonial and treaty-port communities",
  where="Hong Kong, Shanghai, Singapore",lat=22.28,lon=114.16,
  vantage=4,vantage_label="watching from the colonies",form="newspaper",language="English",
  authenticity="Dates from Li Jiaqi (2020), BiblioAsia (2024) and Papers Past.",
  bio="These papers translated the envoy's diary and reported its ban before London did: the British in Asia read Guo as a test of whether Qing China would ever reform.",
  sources=[{"title":"Li Jiaqi (2020)","url":LIJQ},{"title":"BiblioAsia (2024)","url":BIBLIO}]),
 dict(id="zeng",short="Zeng Jize",name="Zeng Jize (Marquis Tseng, 曾紀澤)",life="1839–1890",
  role="Eldest son of Zeng Guofan, inheritor of the marquisate; Guo's successor as minister to Britain and France (1878/79–1886)",
  side="Qing China",where="From Shanghai to Paris and London",lat=LON[0],lon=LON[1],
  waypoints=[{"lat":31.23,"lon":121.47,"label":"Shanghai, late 1878"},{"lat":48.857,"lon":2.352,"label":"Paris, Jan 1879"},{"lat":51.521,"lon":-0.145,"label":"London, Jan 1879"}],
  vantage=1,vantage_label="the successor",form="diary",language="Classical Chinese",
  authenticity="Chushi Ying Fa E guo riji (出使英法俄國日記), beginning in the seventh month of Guangxu 4 (Aug 1878); an English selection, 'Diary of the Marquis Tseng', appeared in 1884. Digest only.",
  bio="The son of Guo's old commander, he had taught himself English and arrived with the advantage of rank and lineage that Guo lacked. His diary picks up where Guo's ends.",
  sources=[{"title":"Chushi Ying Fa E guo riji (text listing)","url":"https://simplelits.com/books/classical/classical-09047-出使英法俄国日记"}]),
]

E=[]
def e(date,disp,prec,eye,place,head,dig,conf,note,quote=""):
    E.append(dict(date_iso=date,date_display=disp,precision=prec,eye=eye,place=place,headline=head,digest=dig,quote=quote,confidence=conf,source_note=note))

e("1876-10-31","31 October 1876 (Guangxu 2, 9th month, 15th day)","day","guo","Beijing","Audience before the long voyage",
  "Guo memorialised for an audience and nominated the staff of the mission, then was received with Liu by the Empress Dowager before leaving the capital. The diary shows how small and improvised the first legation was.","verified","Lundun yu Bali riji juan 1, GX2/9/15 (Wikisource).")
e("1876-12-02","Saturday 2 December 1876 (GX 2/10/17–18)","day","guo","Woosung anchorage, Shanghai, P&O Travancore","Midnight sailing after a two-day delay",
  "The first entry of Shi xi jicheng: the steamer weighed anchor at midnight, about two days late because the British minister Thomas Wade had asked for a delay. Guo, Liu, Zhang Deyi, Macartney and a small staff were aboard.","verified","Frodsham (1967), first entry and footnote.")
e("1876-12-06","6–7 December 1876 (GX 2/10/21–22)","range","guo","Hong Kong","A colonial school and a clean prison",
  "Laid up for storm repairs, Guo toured a government school and the gaol. He praised the strict timetable of the school and the order and cleanliness of the prison, and noted how fast the colony had grown.","verified","Frodsham (1967), Hong Kong entries.")
e("1876-12-13","Wednesday 13 December 1876 (GX 2/10/28)","day","guo","Singapore","Fort Canning and a Qing gunboat",
  "The ship docked about eleven in the morning. Guo inspected Fort Canning, whose layout struck him as quite unlike a Chinese fort, and saw the crew of the Fuzhou-built corvette Yangwu drill and fire for the visitors.","verified","Frodsham (1967); BiblioAsia (2024).")
e("1876-12-14","Thursday 14 December 1876 (GX 2/10/29)","day","guo","Singapore","A courtroom, a governor and Whampoa's garden",
  "In rain and thunder Guo watched a hearing before Judge Theodore Ford, called on Governor Jervois, and was entertained in the garden of the merchant Hoo Ah Kay (Whampoa), who would become the first Qing consul in Singapore. Liu, by contrast, left no impression of the town.","verified","BiblioAsia (2024), citing Shi xi jicheng (2016 Beijing ed., pp. 7–9).")
e("1876-12-21","21 December 1876 (GX 2/11/6)","day","guo","Galle, Ceylon","How Europeans take a country",
  "After seeing a prison and an old royal palace, Guo concluded that Europeans held countries like Ceylon less by soldiers than by administration, commerce and law. Next day the party changed to the P&O Peshawur.","verified","Frodsham (1967), Galle entries.")
e("1876-12-28","28 December 1876 (GX 2/11/13)","day","guo","Red Sea, off Aden","Macartney's tale of Perim",
  "Guo wrote down Macartney's story of how the British had seized the island of Perim at the mouth of the Red Sea, and admired the orderly commercial rules of the ports. The secretary was already his main window on British power.","verified","Frodsham (1967), entry of 28 Dec.")
e("1877-01-02","2 January 1877 (GX 2/11/18)","day","guo","Mediterranean, at sea","The passage that would sink the book",
  "Reflecting on policy, Guo argued that the Western states had a long civilisation and political order of their own and should be met with reason and good faith rather than empty bluster. Frodsham's notes identify this passage as the one that most enraged readers at home.","verified","Frodsham (1967), entry of 2 Jan and note.")
e("1877-01-12","12 January 1877 (GX 2/11/28)","day","guo","Valletta, Malta","Heavy guns and a hospitable governor",
  "Arriving in the small hours, Guo described the fortifications and the great guns, the plan of the town, and the governor's hospitality.","verified","Frodsham (1967).")
e("1877-01-16","16 January 1877 (GX 2/12/3)","day","guo","Gibraltar","Five thousand soldiers and a library",
  "Guo noted the garrison of about five thousand, the garrison library, and that the waters nearby were where Nelson had fought at Trafalgar.","verified","Frodsham (1967).")
e("1877-01-21","Sunday 21 January 1877 (GX 2/12/8)","day","guo","Southampton, then 49 Portland Place","Aground in fog, then a city of lights",
  "The Peshawur ran aground in fog before reaching Southampton. That evening the embassy came up by train to London and the house at 49 Portland Place; Guo was struck by the brightly lit towns and the crowded streets and carriages.","verified","Frodsham (1967), last entry; Tong (MUSE chapter).")
e("1877-01-24","24 January 1877","day","guo","49 Portland Place","Asking Lord Derby for an audience",
  "Guo wrote to the Foreign Secretary, Lord Derby, signing himself envoy of the Emperor, to settle when he might present his letter to the Queen.","verified","Li Jiaqi (2020).")
e("1877-02-07","Wednesday 7 February 1877 (GX 2/12/25)","day","guo","Windsor Castle","The apology delivered to the Queen",
  "Guo presented the imperial letter of regret for Margary's death and his credentials to Queen Victoria, with Liu and Macartney in attendance. The North-China Herald's review of 1877 recorded the audience and the letter of apology.","approx","Date as commonly given; the audience itself is confirmed by the North-China Herald review cited in Li Jiaqi (2020).")
e("1877-02-08","8 February 1877","day","guo","49 Portland Place","The diary goes home",
  "Guo sent his first official dispatch to Beijing. The fair copy of the voyage diary, finished in early February, went to the Zongli Yamen, which had ordered envoys to record what they saw.","verified","Li Jiaqi (2020); Frodsham (1967) intro.")
e("1877-02-10","Saturday 10 February 1877","day","punch","London","Punch rhymes the envoy's arrival",
  "Punch ran a comic poem on the Chinese embassy's arrival, playing on the strangeness of the visitors and the errand of apology. It was the satirical frame through which many readers first met Guo.","verified","BiblioAsia (2024), reproducing Punch 10 Feb 1877 (Heidelberg University Library).")
e("1877-02-14","Wednesday 14 February 1877","day","thomson","Regent Street, London","Two envoys registered at Stationers' Hall",
  "John Thomson registered the copyright of two Lock and Whitfield portraits: the Chinese Ambassador in three-quarter face looking down, and the 'second Chinese Ambassador', full face, in furs. Within a month of landing, the envoys had become saleable images.","verified","TNA COPY 1/36/174–175.")
e("1877-03-25","Sunday 25 March 1877 (GX 3/2/11)","day","guo","Pembroke Lodge, Richmond Park","Tea with an old prime minister",
  "Lady Russell's tea party: Guo found the 85-year-old Earl Russell still studying Latin and urging them to see a great cathedral. He also chatted with two grandsons; the four-year-old answered his age in English and reeled off his full name, and Guo wondered why Englishmen needed so many names. The child was Bertrand Russell.","verified","Lundun yu Bali riji juan 5, as analysed by Wang Ding (Dushu 2022).")
e("1877-03-25","Sunday 25 March 1877 (GX 3/2/11)","day","liu","Pembroke Lodge, Richmond Park","The earl is glad to meet Chinese scholars",
  "Liu's account centres on the aged former premier, who said he was glad to meet scholars from China, and notes that Thomas Wade arranged the visit. He says nothing of the family or the children.","verified","Ying yao siji, same day, per Wang Ding (2022).")
e("1877-03-25","Sunday 25 March 1877 (GX 3/2/11)","day","zhang","Pembroke Lodge, Richmond Park","Tea, bread and a guest book",
  "Zhang described the house on the hill, the white-haired earl seated by his bed, neighbours arriving for tea and bread, and a granddaughter asking the guests to sign her album. He recorded the grandchildren as a boy and a girl, though both were boys.","verified","Suishi Ying E ji, per Wang Ding (2022).")
e("1877-03","March–April 1877 (GX 3/2)","month","times","London","Guo's opium speech in Macartney's English",
  "At a London anti-opium meeting Guo spoke against the trade, and The Times printed a translation by Macartney. Guo later complained that the English version did not render what he had said.","approx","Thepaper.cn feature on Guo and Liu (GX3/2); Times issue not seen.")
e("1877-05-01","1 May 1877","day","lihz","Tianjin","The diary has arrived",
  "Writing to the Zongli Yamen, and again to Guo on 9 May, Li Hongzhang acknowledged receiving the envoy's diary. Nothing yet suggested danger.","verified","Li Jiaqi (2020).")
e("1877-06-16","16 June 1877 (GX 3/5/6)","day","he","Beijing","A memorial against the book",
  "He Jinshou memorialised that the envoy's diary flattered foreigners and slighted the dynasty, and asked that it be suppressed. The court agreed the same day; the printing blocks were to be destroyed.","verified","Li Jiaqi (2020).")
e("1877-07-03","Tuesday 3 July 1877","day","ipswich","Ipswich","Chinese ambassadors at the locomotive works",
  "The paper reported the envoys' tour of Ransomes and Rapier, the firm whose engines had run on the Woosung line near Shanghai. Guo is said to have praised British railways, remarking that a two-hour train journey would take two or three days in China.","approx","Ipswich Journal 3 July 1877 as cited in Wikipedia; visit day not fixed.")
e("1877-07-24","24 July 1877","day","lihz","Tianjin","The ban, told to a brother",
  "In a letter to his elder brother Li named the diary and its banning. The editors of his letters misdated this one to 1878.","verified","Li Jiaqi (2020).")
e("1877-07-28","28 July 1877","day","lici","Beijing","A capital diarist condemns the envoy",
  "Li Ciming recorded his disgust at Guo's diary, repeating the memorial's charge that it praised the barbarians beyond all measure. The private diary shows the official view had become literati opinion.","verified","Yuemantang riji, cited Li Jiaqi (2020).")
e("1877-08-17","17 August 1877 (GX 3/7/9)","day","guo","A coastal fort (甲敦炮台) on an official visit","A borrowed cloak and a quarrel",
  "On a visit to a fortress Guo accepted a cloak offered against the cold by his British hosts; Liu objected that an envoy should not wear foreign clothes even if he froze, and the two quarrelled. The cloak became one of Liu's formal charges.","approx","Thepaper.cn feature; site of fort not identified here.")
e("1877-08-18","18 August 1877","day","guo","49 Portland Place","News of the ban arrives",
  "A letter from Zhang Sigui told Guo that his diary had been banned. Two months after the edict he learned that his attempt to explain Britain had made him a target.","verified","Li Jiaqi (2020).")
e("1877-09-08","8 September 1877 (GX 3/8/2)","day","guo","49 Portland Place","A servant exposes the anonymous letter",
  "Officials described Liu's wild accusations, and Liu's own servant Sheng Kui revealed that an anonymous letter circulating against Guo had been written by Liu. Two days later Guo called his deputy a false envoy who brought harm and no benefit.","verified","Lundun yu Bali riji juan 11, GX3/8/2 and 8/4.")
e("1877-09-12","12 September 1877 (GX 3/8/6)","day","guo","49 Portland Place","Macartney describes Bell's talking wire",
  "Macartney told Guo of a Scottish inventor named Bell whose device carried the voice about sixty li along a wire. Guo noted it, and later (8/21) recorded the same invention again, with its use in sieges.","verified","Lundun yu Bali riji juan 11, GX3/8/6 and 8/21.")
e("1877-09-22","22 September 1877 (GX 3/8/16)","day","guo","49 Portland Place","Liu refuses to come",
  "Liu declined a summons, resentful at being questioned about the anonymous letter, while another member of the mission denied the letter ever existed. The legation had split into two households.","verified","Lundun yu Bali riji juan 11, GX3/8/16.")
e("1877-10-12","12 October 1877","day","guo","49 Portland Place","A memorial in his own defence",
  "Guo memorialised the throne that he had been falsely attacked while handling foreign affairs, defending his conduct and his book, and charged that Liu and He Jinshou had acted together.","verified","Li Jiaqi (2020); thepaper.cn (GX3/9).")
e("1877-11","November 1877 (GX 3/10)","month","liu","London, leaving for Berlin","The deputy departs for Germany",
  "Liu left Portland Place to take up his post as minister in Berlin, to which he had been named in May. Guo soon impeached him again, this time over his spending.","approx","Thepaper.cn (GX3/10); Frodsham (1967) note.")
e("1877-11-08","8 November 1877","day","lihz","Tianjin","Li breaks the news to Guo",
  "Li Hongzhang wrote to Guo informing him formally of the ban on his diary, softening the blow as a patron could.","verified","Li Jiaqi (2020).")
e("1877-12-14","14 December 1877","day","portpress","Hong Kong","Hong Kong reports the ban",
  "The Hong Kong Daily Press told its readers that the Chinese envoy's travel diary had been suppressed in Peking.","verified","Li Jiaqi (2020).")
e("1878-01-21","21 January 1878","day","portpress","Singapore","Singapore reads the envoy on Singapore",
  "The Singapore Daily Times printed an abbreviated English extract of Guo's diary, including what he had written about the colony a year earlier.","verified","BiblioAsia (2024), endnote.")
e("1878-02-14","14 February 1878","day","portpress","Shanghai","The North-China Herald's year in review",
  "The Shanghai weekly's review of 1877 recorded the audience with the Queen, the letter of apology, and the banning of the diary.","verified","Li Jiaqi (2020).")
e("1878-03","March 1878 (GX 4/2)","month","liu","Berlin","Ten charges against the envoy",
  "Liu impeached Guo on ten counts: that he had worn a foreign cloak at a fort, stood up to greet the Emperor of Brazil as if to a fellow sovereign, picked up and read the programme at a Buckingham Palace concert in foreign fashion, and in his book despised the dynasty's institutions to imitate foreigners.","approx","Thepaper.cn summary of the impeachment.")
e("1878-03-28","28 March 1878","day","portpress","Shanghai","Shanghai blames the deputy",
  "An anonymous report in the North-China Daily News named Liu as the likely instigator of the attack on Guo's diary.","verified","Li Jiaqi (2020).")
e("1878-05-08","8 May 1878","day","times","London","Gundry's letter on the envoy's disgrace",
  "The Times published a letter from R. S. Gundry, dated 21 March, explaining the banning of Guo's diary to British readers and attributing the impeachment to Liu.","verified","Li Jiaqi (2020).")
e("1878-05-23","23 May 1878","day","macartney","London","Macartney corrects the record",
  "Macartney wrote to The Times to clarify the account of the affair, speaking for the legation he served.","verified","Li Jiaqi (2020), noting its own text gives 28 May but cites 23 May.")
e("1878","1878","year","guo","London","Testing the telephone",
  "At an electrical works Guo tried the new telephone himself while Zhang Deyi answered from another instrument downstairs. He asked if he could be heard, was told yes, and noted that long sentences came through blurred and only a few words were clear.","approx","Guo diary entry anthologised as 'Ji dianhua (1878)'; The World of Chinese (2019) gives 1877.")
e("1878","1878","year","zhang","London","A word for the telephone",
  "Zhang described the device in his diary and rendered 'telephone' by sound as delüfeng, one of the first Chinese names for the instrument.","approx","The World of Chinese (2019).")
e("1878-08","August 1878 (GX 4/7)","month","zeng","Beijing","Named to replace Guo",
  "Zeng Jize's diary of his mission begins in the seventh month of Guangxu 4, when the court ordered him to succeed Guo in London and Paris and named Li Fengbao to replace Liu in Berlin.","approx","Thepaper.cn (GX4/7 edict); simplelits listing of the diary.")
e("1878-08-08","8 August 1878","day","guo","49 Portland Place","The Times man calls",
  "Guo recorded a visit from Gundry, the correspondent whose letter had told London about his disgrace.","verified","Li Jiaqi (2020).")
e("1878-08-23","23 August 1878","day","times","London","A second letter on Guo",
  "The Times printed Gundry's second letter on the envoy and his critics, dated 20 August.","verified","Li Jiaqi (2020).")
e("1878-12-30","Monday 30 December 1878 (GX 4/12/7)","day","guo","Lyceum Theatre, London","Irving's Hamlet",
  "Guo was invited to the opening night of Henry Irving's Hamlet at the Lyceum, perhaps the first Chinese official to see Shakespeare performed. He noted the invitation in his diary.","verified","e-aoi China–West chronology (Zurich), citing Zhang Xiaoyang and Lai & Wong.")
e("1879-01-24","24 January 1879","day","portpress","Christchurch, New Zealand","The colonies read The Times on Tseng",
  "The Globe reprinted a Times leader welcoming the new minister Zeng Jize and regretting that he, like Guo before him, would be shared with Paris.","verified","Globe, 24 Jan 1879, p. 3 (Papers Past).",quote="like his Excellency Kwoh, with Paris is to be lamented")
e("1879-01","January 1879","month","zeng","Paris and London","The successor arrives",
  "Zeng reached Europe and took over the legation from Guo, recording in his diary the handover and his first calls. He kept Macartney on as counsellor.","approx","Zeng's diary; exact day not verified here.")
e("1879","early 1879","range","guo","Marseilles to Shanghai, then Changsha","Home without reporting to the capital",
  "Guo sailed for China, landed at Shanghai and, pleading illness, went straight home to Hunan rather than to Beijing. He spent his last twelve years teaching and writing, still defending what he had seen.","approx","Wikipedia; chinawriter.com.cn.")

claims=[
 dict(date_iso="1876-12-21",date_display="21 Dec 1876",eye="guo",claim="Traveller: Europeans hold colonies by government and trade more than by force",form="travel journal",evidence="Shi xi jicheng, Galle entry (Frodsham 1967)",confidence="verified"),
 dict(date_iso="1877-01-02",date_display="2 Jan 1877",eye="guo",claim="Traveller: the Western states have their own long civilisation and must be met with reason",form="travel journal",evidence="Shi xi jicheng (Frodsham 1967 note)",confidence="verified"),
 dict(date_iso="1877-01-21",date_display="21 Jan 1877",eye="guo",claim="Traveller: English towns are bright with lamps, streets thronged with carriages",form="travel journal",evidence="Shi xi jicheng, last entry",confidence="verified"),
 dict(date_iso="1877-02-10",date_display="10 Feb 1877",eye="punch",claim="Hosts: the apology envoy as comic exotic in verse",form="newspaper",evidence="Punch 10 Feb 1877 (BiblioAsia)",confidence="verified"),
 dict(date_iso="1877-02-14",date_display="14 Feb 1877",eye="thomson",claim="Hosts: the envoys photographed and registered as saleable portraits",form="other",evidence="TNA COPY 1/36/174–175",confidence="verified"),
 dict(date_iso="1877-03-25",date_display="25 Mar 1877",eye="guo",claim="Traveller: puzzled that one English child bears so many names",form="diary",evidence="Lundun yu Bali riji juan 5 (Wang Ding 2022)",confidence="verified"),
 dict(date_iso="1877-03-25",date_display="25 Mar 1877",eye="zhang",claim="Traveller: misreads two grandsons as a boy and a girl",form="diary",evidence="Suishi Ying E ji (Wang Ding 2022)",confidence="verified"),
 dict(date_iso="1877-03",date_display="Mar–Apr 1877",eye="times",claim="Hosts: print the envoy's anti-opium speech in a translation he disowns",form="newspaper",evidence="Thepaper.cn feature",confidence="approx"),
 dict(date_iso="1877-06-16",date_display="16 Jun 1877",eye="he",claim="Home court: the envoy's praise of the West slights the dynasty",form="court record",evidence="He Jinshou memorial (Li Jiaqi 2020)",confidence="verified"),
 dict(date_iso="1877-07-03",date_display="3 Jul 1877",eye="ipswich",claim="Hosts: the envoys admire the works that built China's first railway engines",form="newspaper",evidence="Ipswich Journal 3 Jul 1877",confidence="approx"),
 dict(date_iso="1877-09-12",date_display="12 Sep 1877",eye="guo",claim="Traveller: a wire that carries the voice sixty li",form="diary",evidence="Lundun yu Bali riji juan 11",confidence="verified"),
 dict(date_iso="1878-03",date_display="Mar 1878",eye="liu",claim="Fellow traveller: standing for Brazil's emperor and reading concert programmes is aping foreigners",form="court record",evidence="Liu's impeachment (thepaper.cn)",confidence="approx"),
 dict(date_iso="1878-05-08",date_display="8 May 1878",eye="times",claim="Hosts: the enlightened envoy is a victim of jealous reactionaries at home",form="newspaper",evidence="Gundry letter (Li Jiaqi 2020)",confidence="verified"),
 dict(date_iso="1878",date_display="1878",eye="guo",claim="Traveller: the telephone is clear for short words, blurred for long sentences",form="diary",evidence="Guo diary, 'Ji dianhua'",confidence="approx"),
 dict(date_iso="1879-01-24",date_display="24 Jan 1879",eye="times",claim="Hosts: regret that China's minister must be shared with Paris",form="newspaper",evidence="Times leader reprinted in Globe 24 Jan 1879",confidence="verified"),
]

conv=[
 dict(date="1877-02-07",label="Arrival weeks: the audience, the Punch poem, the photographs (7–14 Feb 1877)",eyes=["guo","punch","thomson"],note="Guo records a solemn apology to the Queen; within a week Punch makes him comic verse and a Regent Street studio makes him a commodity portrait."),
 dict(date="1877-03-25",label="Tea at Pembroke Lodge with Earl Russell",eyes=["guo","liu","zhang"],note="Three Chinese diaries of one English tea party: Guo talks to the children, Liu sees only the old statesman, Zhang notices the bread and the guest book and gets the grandchildren wrong."),
 dict(date="1877-06-16",label="The ban spreads: memorial, edict, letters and diaries (June–July 1877)",eyes=["he","lihz","lici"],note="A memorial and an edict on one day; within six weeks the patron is writing of the ban to his brother and a capital diarist is echoing the memorial."),
 dict(date="1877-09-08",label="The legation splits (Aug–Sep 1877)",eyes=["guo","liu"],note="The cloak at the fort, the anonymous letter, the refusal to come: the same quarrel seen from both sides of Portland Place."),
 dict(date="1877-09-12",label="Bell's telephone enters the legation",eyes=["guo","macartney","zhang"],note="Macartney explains it, Guo notes it, and later Guo speaks into one while Zhang listens downstairs and finds a Chinese name for it."),
 dict(date="1878-05-08",label="London learns of the disgrace (Mar–May 1878)",eyes=["liu","portpress","times","macartney"],note="Liu's ten charges in Berlin, a Shanghai report blaming Liu, Gundry's Times letter and Macartney's correction arrive within weeks of one another."),
 dict(date="1878-08",label="Recall and the press (Aug 1878)",eyes=["zeng","guo","times"],note="The edict naming Zeng, Gundry calling on Guo at Portland Place, and Gundry's second Times letter all fall in one month."),
 dict(date="1879-01",label="Succession (Jan 1879)",eyes=["zeng","portpress","guo"],note="The new minister arrives, the colonial papers reprint The Times on sharing him with Paris, and Guo prepares to leave."),
]

ties=[
 dict(a="guo",b="liu",kind="opposite sides",note="Envoy and deputy, old acquaintances, who impeached each other from London and Berlin."),
 dict(a="guo",b="macartney",kind="met",note="Macartney sailed with Guo, translated for him and explained Britain to him daily."),
 dict(a="guo",b="zhang",kind="met",note="Zhang interpreted for Guo and answered his first telephone call."),
 dict(a="he",b="guo",kind="opposite sides",note="He Jinshou's memorial got Guo's diary banned; Guo accused him of acting in concert with Liu."),
 dict(a="he",b="liu",kind="influenced",note="Guo's memorial of autumn 1877 charged that Liu and He colluded against him; the Shanghai press also blamed Liu."),
 dict(a="lihz",b="guo",kind="read each other",note="Li received and read the diary, then wrote to tell Guo of its ban."),
 dict(a="lici",b="he",kind="read each other",note="Li Ciming's diary condemnation echoes the language of He's memorial."),
 dict(a="zeng",b="guo",kind="met",note="Zeng succeeded Guo in London and Paris; Guo had served under Zeng's father against the Taiping."),
 dict(a="macartney",b="zeng",kind="met",note="Macartney stayed on and became Zeng's counsellor for the rest of his mission."),
 dict(a="times",b="macartney",kind="read each other",note="The Times printed Macartney's translation of Guo's speech and his letter of May 1878."),
 dict(a="thomson",b="guo",kind="met",note="Guo and Liu sat for the Lock and Whitfield camera within three weeks of landing."),
 dict(a="portpress",b="times",kind="read each other",note="The colonial papers reprinted and answered London's coverage of the envoys."),
 dict(a="ipswich",b="guo",kind="met",note="The Ipswich paper reported Guo's tour of the town's locomotive works."),
]

threads=[
 {"to":"naser-1873","note":"Naser al-Din Shah's London visit of 1873 was still talked of when Guo arrived; Guo's diary refers to the recent visit of the Persian king, the obvious precedent for an Asian monarch's envoy being feted and caricatured in the same city."},
 {"to":"iwakura-1871","note":"The Iwakura embassy had toured Britain in 1872, four years before Guo; Japan already kept a legation and students in London when he arrived, and the contrast between Tokyo's embrace of Western learning and Beijing's suspicion of it frames how his mission is read."},
 {"to":"v13:telephone-1876","note":"Bell's telephone, patented in 1876, reached Guo's legation by September 1877 through Macartney's description, and Guo and Zhang Deyi then tried it themselves."},
 {"to":"v2:opium-war","note":"The treaty order created by the Opium Wars framed both the Margary affair and Guo's 1877 memorials asking the throne to ban opium, which he also spoke against in London."},
]

images=[
 {"url":"https://collection.sciencemuseumgroup.org.uk/objects/co8228220/kuo-tajen","title":"Kuo Tajen (Guo Songtao)","caption":"Woodburytype portrait from the Lock and Whitfield studio, published in the series Men of Mark with a biographical note by Thompson Cooper; the studio had photographed the envoy in February 1877.","date":"1880","credit":"Lock and Whitfield; Kodak Collection, National Science and Media Museum / Science Museum Group"},
 {"url":"https://beta.nationalarchives.gov.uk/catalogue/id/C16775934","title":"Photograph of the Chinese Ambassador, three-quarter face looking down","caption":"Copyright entry form with attached photograph, registered 14 February 1877; copyright owner John Thomson, author Lock and Whitfield. Catalogue entry only; the image is not online.","date":"14 February 1877","credit":"The National Archives, Kew, COPY 1/36/174"},
 {"url":"https://beta.nationalarchives.gov.uk/catalogue/id/C16775935","title":"Photograph of second Chinese Ambassador, full face, in furs","caption":"The companion registration for the deputy envoy, almost certainly Liu Xihong. Catalogue entry only.","date":"14 February 1877","credit":"The National Archives, Kew, COPY 1/36/175"},
 {"url":"https://npgshop.org.uk/products/kuo-sung-tao-npg-4707-14-print","title":"Kuo Sung-tao, by Sir Leslie Ward","caption":"A portrait of Guo by the caricaturist Leslie Ward ('Spy'), held by the National Portrait Gallery as NPG 4707(14); the page linked is the gallery's print-sales listing and gives no date.","date":"undated on the linked page","credit":"Leslie Ward; National Portrait Gallery, London"},
 {"url":BIBLIO,"title":"Punch, 10 February 1877, and portraits of Guo, Liu and Macartney","caption":"BiblioAsia article reproducing the Punch page that satirised the envoy's arrival (Heidelberg University Library), portraits of Guo and Liu from Frodsham (1974), and Singapore scenes of the embassy's December 1876 stop.","date":"1877 (Punch)","credit":"National Library Board, Singapore; Heidelberg University Library"},
]

further=[
 {"title":"J. D. Frodsham, 'Record of an Envoy's Voyage to the West' (Asian Studies, 1967)","url":FRODSHAM},
 {"title":"The Curious Visit of Qing Ambassadors to Singapore (BiblioAsia, 2024)","url":BIBLIO},
 {"title":"Li Jiaqi, Western-language sources on Guo's Shi xi jicheng (Journal of Chinese Studies 71, 2020; Chinese)","url":LIJQ},
 {"title":"Wang Ding, the Russell tea in three Chinese diaries (Dushu 2022; Chinese)","url":WANG},
 {"title":"Q. S. Tong, 'Guo Songtao in London: An Unaccomplished Mission of Discovery' (excerpt)","url":"https://muse.jhu.edu/books/9789888052103/9789888052103-10.pdf"},
 {"title":"Jenny Huangfu Day, Qing Travelers to the Far West (Cambridge, 2018)","url":"https://www.cambridge.org/core/books/qing-travelers-to-the-far-west/3FB02283AEE938D8946BEC0CA607BDFE"},
 {"title":"D. C. Boulger, The Life of Sir Halliday Macartney (1908)","url":BOULGER},
 {"title":"Guo Songtao, Lundun yu Bali riji, juan 11 (Wikisource)","url":WS11},
]

intro=[
 "In February 1875 the British consular interpreter Augustus Margary was killed on the Yunnan–Burma border. The Chefoo Convention that Li Hongzhang signed with Sir Thomas Wade on 13 September 1876 settled the affair on British terms, and one term was a mission of apology to London. The man chosen was Guo Songtao, a 58-year-old Hunanese scholar who had long argued that China must understand the West. He was to deliver the apology and then stay: the first resident minister the Qing had ever posted to a Western capital.",
 "The court had ordered its envoys to keep diaries and send them home. Guo did so with unusual frankness. The voyage diary he posted from London in February 1877, Shi xi jicheng, praised the schools, prisons, ports and laws he had seen from Hong Kong to Southampton, and argued that the Western states had a civilisation of their own. The Zongli Yamen printed it; in June a court memorial called it disloyal, and the blocks were destroyed. For the next eighteen months Guo lived in Portland Place knowing that every line he wrote would be read in Beijing as evidence.",
 "This chapter sets the envoy's own diary beside those of his deputy Liu Xihong, who became his enemy, and his interpreter Zhang Deyi, who noticed bread, guest books and gadgets. Around them are the people who read and judged them: a patron in Tianjin, a memorialist and a diarist in Beijing, Punch, The Times, a Regent Street photographer, an Ipswich weekly, and the English papers of Hong Kong, Shanghai and Singapore. The record is mixed: diaries on the Chinese side, but also memorials, letters and newspapers, and on the British side mostly press and archive entries rather than private diaries.",
 "The clearest day is Sunday 25 March 1877, when all three Chinese diarists went to tea with the aged Earl Russell at Pembroke Lodge and each saw a different party; Guo talked with a four-year-old grandson who turned out to be Bertrand Russell. The longest thread runs from the ban of June 1877 to Liu's ten charges in 1878, as London newspapers explained to their readers why the envoy they found so reasonable was disgraced at home.",
 "Guo was recalled in August 1878. His successor Zeng Jize arrived in January 1879, and Guo went home to Hunan without reporting to the capital. His full diary waited a century to be published.",
]

cal=("Qing documents and the three Chinese diaries date by the Guangxu reign and the Chinese lunisolar calendar. Guangxu 2 began on 26 January 1876 and Guangxu 3 on 13 February 1877; Guangxu 4 began on 2 February 1878. Conversions here use standard tables and agree with the Western dates printed in Frodsham's translation: GX 2/10/17 = 2 December 1876 (departure); GX 2/12/8 = 21 January 1877 (arrival); GX 2/12/25 = 7 February 1877; GX 3/2/11 = 25 March 1877; GX 3/5/6 = 16 June 1877; GX 3/7/9 = 17 August 1877; GX 3/8/1 = 7 September 1877; GX 4/2 = 4 March–2 April 1878; GX 4/7 = 30 July–27 August 1878; GX 4/12/7 = 30 December 1878. Where a source gives only a lunar month, date_iso gives the Western month in which most of it falls.")

ch=dict(id="guo-1877",title="The Envoy Who Wrote Too Much",short_title="Guo Songtao in London",
 subtitle="Qing China's first resident minister in London and Paris, 1876–1879",span="1876–1879",
 intro=intro,calendar_note=cal,eyes=eyes,entries=sorted(E,key=lambda x:x["date_iso"]),claims=claims,convergences=conv,ties=ties,
 threads_out=threads,images=images,further=further,
 vantage_key="0 = the envoys themselves; 1 = staff inside the legation or the successor; 2 = London and provincial hosts; 3 = readers and judges in China; 4 = colonial and treaty-port press watching from afar.")
json.dump(ch,open(OUT,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(len(eyes),len(E),len(claims),len(conv),len(ties))
