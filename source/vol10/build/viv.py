import json
OUT="/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/vol10/ch-vivekananda-1893.json"
CHI=(41.8796,-87.6237)
VNET="https://vivekananda.net/knownletters-1893america"
NEWS="https://sreyas.in/2117/english/swami-vivekananda/complete-works/american-newspaper-reports-on-swami-vivekanandas-speech"
DATES="https://mail.vivekananda.net/Dates/1893/sep.html"
CHRON="https://vedanta.org/wp-content/uploads/2016/10/Swami-Vivekananda-in-the-West-A-Chronology.pdf"
DUB="https://vivekananda.net/newspaperreports-29sep93"
SUN="https://archiv.oriens-extremus.org/54/OE54-03.pdf"
ZHENG="https://nirc.nanzan-u.ac.jp/journal/6/article/1507/pdf/download"
BRAY="https://www.theinterfaithobserver.org/journal-articles/2012/11/15/pan-asian-participation-in-the-1893-parliament.html"
MERCER="https://distantreader.org/stacks/trust/uc2/uc2_ark+=13960=t3ws8ns6q.txt"
BU="https://people.bu.edu/wwildman/bce/worldparliamentofreligions1893.htm"
HIRAI="https://sites.miamioh.edu/empire/files/2024/10/1893-Hirai-Real-Position-of-Japan-toward-Christianity.pdf"
WEBBPDF="https://sites.miamioh.edu/empire/files/2024/11/1893-Webb-Influence-of-Islam-on-Social-Conditions.pdf"
CRITICS="https://sites.miamioh.edu/empire/files/2024/10/1893-Asian-critics-of-Western-missionaries.pdf"
BARROWSX="https://sites.miamioh.edu/empire/files/2025/08/1893-Barrows-Worlds-Parliament-of-Religions.pdf"
HATHI="https://catalog.hathitrust.org/Record/100253147"
PTSEM="https://commons.ptsem.edu/id/worldsparliamen01barr"
MOZ1="https://mozoomdar-at-sea.netlify.com/journey/farewell-to-kolkata/"
MOZ2="https://mozoomdar-at-sea.netlify.com/journey/conclusion/"
THEO="https://theosophy.wiki/en/Anagarika_Dharmapala"
JAINP="https://parliamentofreligions.org/1893-chicago/honoring-our-jain-delegate-from-india-at-1893-parliament-lawyer-virchand-raghavji-gandhi-1864-1901/"
ZIOL="https://otani.repo.nii.ac.jp/record/8667/files/EB26-1-04.pdf"
NIKH="https://vivekananda.net/biographical-biography-parliamentreligions"
PLUR="https://pluralism.org/at-the-1893-world%E2%80%99s-parliament-of-religions"
WEBBW="https://en.wikipedia.org/wiki/Alexander_Russell_Webb"
BARW="https://en.wikipedia.org/wiki/John_Henry_Barrows"

eyes=[
 dict(id="vivekananda",short="Vivekananda",name="Swami Vivekananda (Narendranath Datta)",life="1863–1902",
  role="Bengali monk of the Ramakrishna order, aged 30; an uninvited, unaccredited delegate who joined the Parliament at the last moment",
  side="India (Hindu, Vedanta)",where="Chicago (Art Institute, the Hale household on Dearborn Avenue); then lecture circuits in the Midwest, Detroit, New York, Thousand Island Park, London",
  lat=CHI[0],lon=CHI[1],
  waypoints=[dict(lat=35.44,lon=139.64,label="Yokohama, July 1893"),dict(lat=49.28,lon=-123.12,label="Vancouver, 25 July 1893"),dict(lat=41.88,lon=-87.62,label="Chicago, Parliament, Sept 1893"),dict(lat=42.33,lon=-83.05,label="Detroit, Feb–Mar 1894"),dict(lat=44.29,lon=-76.03,label="Thousand Island Park, June–Aug 1895"),dict(lat=51.51,lon=-0.13,label="London, 1895–96")],
  vantage=0,vantage_label="the visitor who became the Parliament's centre",form="speeches (as printed) and dated letters",language="English; Bengali",
  authenticity="Speeches printed by Barrows (1893) and in newspapers; letters collected in The Complete Works of Swami Vivekananda (Advaita Ashrama, first collected edition from 1907 onward). Some newspaper texts of speeches differ from Barrows's condensed versions.",
  bio="A disciple of Ramakrishna who had wandered India as a monk before sailing east via China and Japan. He arrived in America short of money and without credentials, was vouched for by the Harvard classicist John Henry Wright, and left the Parliament a celebrity. His letters home mix wonder at American wealth and women's education with fierce criticism of Indian caste and of Christian missions.",
  sources=[dict(title="Letters written from America, 1893 (vivekananda.net)",url=VNET),dict(title="Dates in the life of Swami Vivekananda, September 1893",url=DATES),dict(title="Swami Vivekananda in the West: A Chronology (Vedanta Society)",url=CHRON)]),
 dict(id="mozoomdar",short="Mozoomdar",name="Protap Chunder Mozoomdar",life="1840–1905",
  role="Leader of the Brahmo Samaj of India (New Dispensation), aged 53, on his third visit to America",
  side="India (Brahmo Samaj, reformed theism)",where="Calcutta; Chicago",lat=CHI[0],lon=CHI[1],
  waypoints=[dict(lat=22.57,lon=88.36,label="Calcutta, farewell sermon 9 July 1893"),dict(lat=41.88,lon=-87.62,label="Chicago, Sept 1893")],
  vantage=0,vantage_label="the Indian delegate Americans already knew",form="speeches (as printed); sermons in The Interpreter",language="English; Bengali",
  authenticity="His Parliament addresses are in Barrows (1893); his farewell sermon was printed in the Brahmo journal The Interpreter (1893) and later in Lectures in America and Other Papers (Calcutta, 1955). No diary of the Chicago weeks is known; letters to his wife from this period are not known to survive.",
  bio="Author of The Oriental Christ (1883), he was the best-known Indian religious figure in America before 1893 and had befriended Unitarian circles on earlier tours. In Chicago he was praised in the press, but fell ill with diabetes and was eclipsed by the younger Vivekananda; relations between the two soured afterwards.",
  sources=[dict(title="Mozoomdar at Sea: Farewell to Kolkata",url=MOZ1),dict(title="Mozoomdar at Sea: Conclusion",url=MOZ2)]),
 dict(id="dharmapala",short="Dharmapala",name="Anagarika Dharmapala (born Don David Hewavitarne)",life="1864–1933",
  role="Sinhalese Buddhist revivalist, aged 28, general secretary of the Maha Bodhi Society",
  side="Ceylon (Theravada Buddhist)",where="Colombo; London; Chicago; Honolulu on the way home",lat=CHI[0],lon=CHI[1],
  waypoints=[dict(lat=6.93,lon=79.85,label="Colombo"),dict(lat=51.51,lon=-0.13,label="London, July–Aug 1893"),dict(lat=41.88,lon=-87.62,label="Chicago, Sept 1893"),dict(lat=21.31,lon=-157.86,label="Honolulu, Oct 1893")],
  vantage=0,vantage_label="Buddhist delegate, Theosophists' protégé",form="speeches (as printed); diary (manuscript, extracts published later)",language="English; Sinhala",
  authenticity="Parliament papers printed in Barrows (1893). He kept diaries throughout his life; extracts ('Diary Leaves') were published in the Maha Bodhi Journal from the 1940s and used by later biographers. No 1893 diary entry has been checked directly for this chapter.",
  bio="Raised in Christian schools in Colombo and drawn into Buddhism by Olcott and Blavatsky, he came to Chicago sponsored by the Theosophists and sat on the platform beside Vivekananda. He spoke against missionary intolerance and presented Buddhism as a scientific, ethical religion compatible with evolution.",
  sources=[dict(title="Anagarika Dharmapala (Theosophy Wiki)",url=THEO),dict(title="Asian critics of Western missionaries, 1893 (excerpts from Barrows)",url=CRITICS)]),
 dict(id="shaku-soen",short="Shaku Sōen",name="Shaku Sōen (Soyen Shaku)",life="1860–1919",
  role="Rinzai Zen abbot of Engaku-ji, Kamakura, aged 33; one of the Japanese Buddhist delegation",
  side="Japan (Rinzai Zen)",where="Kamakura; Chicago",lat=CHI[0],lon=CHI[1],
  waypoints=[dict(lat=35.33,lon=139.55,label="Engaku-ji, Kamakura, send-off 30 July 1893"),dict(lat=41.88,lon=-87.62,label="Chicago, Sept 1893")],
  vantage=0,vantage_label="Zen delegate speaking through a translator",form="speeches (translated and read by others)",language="Japanese (papers translated into English by D. T. Suzuki)",
  authenticity="His papers were written in Japanese, rendered into English by his lay student Suzuki Daisetsu (D. T. Suzuki), and read aloud for him; the English texts are in Barrows (1893). A travel diary (Saiyū nikki) exists in a 1941 edition but concerns earlier travel; no day-by-day Chicago diary has been checked for this chapter.",
  bio="Trained in Zen and educated at Keiō, he had studied in Ceylon before the Parliament. In Chicago he met the publisher Paul Carus, a connection that later brought D. T. Suzuki to America and opened the Western reception of Zen.",
  sources=[dict(title="Zheng, 'Buddhist Networks: The Japanese Preparation for the World's Parliament of Religions' (JJRS 2019)",url=ZHENG),dict(title="Ziolkowski, 'The Literary Bearing of Chicago's 1893 Parliament' (Eastern Buddhist)",url=ZIOL)]),
 dict(id="pung",short="Pung Kwang Yu",name="Pung Kwang Yu (Peng Guangyu)",life="1844–?",
  role="First Secretary of the Chinese Legation in Washington, sent by the Zongli Yamen as China's official representative",
  side="Qing China (official Confucian)",where="Washington; Chicago (9 August – 1 October 1893)",lat=CHI[0],lon=CHI[1],
  waypoints=[dict(lat=38.9,lon=-77.04,label="Washington legation"),dict(lat=41.88,lon=-87.62,label="Chicago, 9 Aug – 1 Oct 1893")],
  vantage=0,vantage_label="imperial envoy who spoke little English",form="paper (translated, read by others); official report",language="Classical Chinese (English translation by Yong Kwai)",
  authenticity="His 30,000-word paper 'Confucianism' was translated at the legation and read for him; printed in Barrows (1893). A Chinese version, Shuo jiao, was submitted to the throne and printed by the Tongwen Guan in Beijing in 1896.",
  bio="A Fujianese official who had served in Korea and in the Washington legation since 1886. His paper argued that Confucianism was an ethical system, questioned Western categories of 'religion', and criticised missionaries for knowing only the lowest strata of Chinese society.",
  sources=[dict(title="Sun Jiang, on 'Chinese religions' at the 1893 Parliament (Oriens Extremus 54)",url=SUN)]),
 dict(id="hirai",short="Hirai",name="Hirai Kinzō (Kinza Riuge M. Hirai)",life="1859–1916",
  role="Japanese lay Buddhist and English-speaking lecturer, aged about 34, in the United States since 1892",
  side="Japan (lay Rinzai Buddhist)",where="California; Chicago",lat=CHI[0],lon=CHI[1],
  vantage=0,vantage_label="critic of Christian nations from the platform",form="speech (as printed)",language="English",
  authenticity="Printed apparently in full in Barrows (1893) and, from a stenographer's transcript with small differences, in Neely's History of the Parliament of Religions (1893).",
  bio="Hirai had come to America in 1892 and lectured to Theosophists before the Parliament. His speech tied Japanese suspicion of Christianity to the unequal treaties and to anti-Japanese discrimination in the United States, and drew cries of 'Shame!' from an audience that applauded him.",
  sources=[dict(title="Hirai, 'The Real Position of Japan toward Christianity' (1893, teaching excerpt)",url=HIRAI),dict(title="Pluralism Project: at the 1893 Parliament",url=PLUR)]),
 dict(id="gandhi",short="V. R. Gandhi",name="Virchand Raghavji Gandhi",life="1864–1901",
  role="Bombay lawyer, aged 29, secretary of the Jain Association of India, deputed in place of the monk Atmaramji",
  side="India (Jain)",where="Bombay; Chicago",lat=CHI[0],lon=CHI[1],
  waypoints=[dict(lat=18.94,lon=72.83,label="Bombay"),dict(lat=41.88,lon=-87.62,label="Chicago, Sept 1893")],
  vantage=0,vantage_label="Jain delegate and defender of India",form="speeches (as printed)",language="English; Gujarati",
  authenticity="Speeches printed in Barrows (1893); later American lectures were collected in the twentieth century.",
  bio="Sent because Jain monks did not travel by sea, he spoke at the opening, on Jain philosophy, and in reply to attacks on Hindu morality. He stayed on to lecture in America and England.",
  sources=[dict(title="Parliament of the World's Religions: honouring Virchand Gandhi",url=JAINP),dict(title="Braybrooke, Pan-Asian participation in the 1893 Parliament",url=BRAY)]),
 dict(id="nagarkar",short="Nagarkar",name="B. B. Nagarkar",life="dates not verified",
  role="Brahmo Samaj delegate from Bombay, travelling with Mozoomdar's party",
  side="India (Brahmo Samaj)",where="Chicago; Midwest lecture tour",lat=CHI[0],lon=CHI[1],
  waypoints=[dict(lat=41.88,lon=-87.62,label="Chicago, Sept 1893"),dict(lat=41.59,lon=-93.62,label="Des Moines, Dec 1893")],
  vantage=1,vantage_label="junior Indian delegate",form="speech (as printed)",language="English; Marathi",
  authenticity="His Parliament paper is printed in Barrows (1893); press notices of his later tour survive in Iowa newspapers.",
  bio="A reformer of the Bombay (Prarthana/Brahmo) circle, he spoke on social reform in India and toured the Midwest after the Parliament, a few weeks behind Vivekananda.",
  sources=[dict(title="Braybrooke, Pan-Asian participation in the 1893 Parliament",url=BRAY)]),
 dict(id="webb",short="Webb",name="Mohammed Alexander Russell Webb",life="1846–1916",
  role="American journalist and former US consul in Manila, a convert to Islam, aged 46",
  side="American Muslim (Islam's sole speaker)",where="New York; Chicago",lat=CHI[0],lon=CHI[1],
  waypoints=[dict(lat=40.71,lon=-74.0,label="New York, The Moslem World, 1893"),dict(lat=41.88,lon=-87.62,label="Chicago, 20–21 Sept 1893")],
  vantage=0,vantage_label="home-grown convert speaking for the East",form="speeches (as printed); his monthly paper",language="English",
  authenticity="Barrows printed an abridged version; Neely's History (1893) gives a fuller stenographic text.",
  bio="A Missouri newspaperman who embraced Islam while consul in the Philippines, he returned to found a mission and a paper in New York. At the Parliament he was the only speaker for Islam; the press called him 'the Yankee Mohammedan', and his remarks on polygamy drew the Parliament's only audible protest.",
  sources=[dict(title="Alexander Russell Webb (Wikipedia)",url=WEBBW),dict(title="Webb, 'The Influence of Islam on Social Conditions' (1893, teaching excerpt)",url=WEBBPDF)]),
 dict(id="barrows",short="Barrows",name="John Henry Barrows",life="1847–1902",
  role="Pastor of First Presbyterian Church, Chicago, aged 46; chairman of the Parliament's General Committee and its official historian",
  side="American host (liberal Protestant)",where="Chicago; later India and Japan (1896–97)",lat=41.88,lon=-87.63,
  waypoints=[dict(lat=41.88,lon=-87.63,label="Chicago, 1893"),dict(lat=22.57,lon=88.36,label="Calcutta, Haskell lectures, 1896–97")],
  vantage=0,vantage_label="host, organiser and editor of the record",form="official history (1893) and addresses",language="English",
  authenticity="The World's Parliament of Religions (2 vols, Chicago: Parliament Publishing Co., 1893) is the official record; he condensed many speeches, so his texts are not verbatim throughout.",
  bio="Barrows organised the invitations and chaired most sessions. He welcomed the Asian delegates warmly, but held that Christianity was the fulfilment of other faiths, and he answered Vivekananda's attacks on missions in his own footnotes and later lectures in India.",
  sources=[dict(title="The World's Parliament of Religions (HathiTrust record)",url=HATHI),dict(title="Barrows vol. 1 (Princeton Theological Seminary digital commons)",url=PTSEM),dict(title="Barrows excerpt with notes (Miami University)",url=BARROWSX)]),
 dict(id="bonney",short="Bonney",name="Charles Carroll Bonney",life="1831–1903",
  role="Chicago lawyer, aged 62, Swedenborgian layman, president of the World's Congress Auxiliary",
  side="American host",where="Chicago, Hall of Columbus, Art Institute",lat=CHI[0],lon=CHI[1],
  vantage=0,vantage_label="presiding host",form="speeches (as printed)",language="English",
  authenticity="Opening and closing addresses printed in Barrows (1893) and Mercer's review (1893).",
  bio="Bonney conceived the congresses that ran alongside the Exposition and appointed Barrows. His opening address framed differences of belief as spurs to inquiry rather than grounds for conflict.",
  sources=[dict(title="Boston Collaborative Encyclopedia: World's Parliament of Religions 1893",url=BU),dict(title="Mercer, Review of the World's Religious Congresses (1893), full text",url=MERCER)]),
 dict(id="benson",short="Abp Benson",name="Edward White Benson",life="1829–1896",
  role="Archbishop of Canterbury, aged about 63",
  side="Church of England (absent critic)",where="Lambeth Palace, London",lat=51.4955,lon=-0.1197,
  vantage=4,vantage_label="abroad, refusing to come",form="letter (printed by Barrows)",language="English",
  authenticity="His letter of refusal was printed by Barrows in the introductory history of The World's Parliament of Religions (1893), vol. 1.",
  bio="Benson declined to take part or to send a representative, objecting that Christianity could not sit in a parliament of religions without implying parity with other faiths. His refusal became the best-known objection from the Christian side.",
  sources=[dict(title="Boston Collaborative Encyclopedia: opposition to the Parliament",url=BU),dict(title="John Henry Barrows (Wikipedia)",url=BARW)]),
 dict(id="lucy-monroe",short="Lucy Monroe",name="Lucy Monroe",life="1865–1950",
  role="Chicago writer, sister of the poet Harriet Monroe; Chicago correspondent of The Critic (New York)",
  side="American host (literary press)",where="Chicago",lat=CHI[0],lon=CHI[1],
  vantage=1,vantage_label="reporter in the hall",form="dated letters to a weekly (newspaper)",language="English",
  authenticity="Her Chicago letters appeared in The Critic in 1893; the excerpts used here are reprinted on vivekananda.net. Attribution of each unsigned Critic paragraph to her is as given by that compilation.",
  bio="Reporting for an East Coast literary weekly, she judged the Parliament as a spectacle of eloquence and singled out Vivekananda and Dharmapala as its most impressive figures.",
  sources=[dict(title="Newspaper reports, 29 September 1893 and The Critic (vivekananda.net)",url=DUB)]),
 dict(id="harriet-monroe",short="H. Monroe",name="Harriet Monroe",life="1860–1936",
  role="Chicago poet, aged 32, author of the Exposition's official Columbian Ode",
  side="American host (Chicago literary elite)",where="Chicago",lat=CHI[0],lon=CHI[1],
  vantage=1,vantage_label="audience member, remembering",form="memoir (written later)",language="English",
  authenticity="Her autobiography A Poet's Life was published posthumously in 1938; it is a recollection decades after the event, not a contemporary record.",
  bio="Monroe, later founder of Poetry magazine, watched the Parliament sessions. Her memoir remembers Vivekananda as the man who stole the show, a judgment much quoted since.",
  sources=[dict(title="Ziolkowski, 'The Literary Bearing of Chicago's 1893 Parliament' (cites Monroe)",url=ZIOL)]),
 dict(id="press",short="US newspapers",name="American newspapers (Chicago Record, Inter Ocean, Dubuque Times, Critic, Midwest and Eastern papers)",life="1893–1896",
  role="Unsigned reporters and syndicated dispatches covering the Parliament and the lecture tours that followed",
  side="American host (popular press)",where="Chicago; Madison; Des Moines; Detroit; Saginaw; Baltimore; New York",lat=CHI[0],lon=CHI[1],
  waypoints=[dict(lat=41.88,lon=-87.62,label="Chicago, Sept 1893"),dict(lat=43.07,lon=-89.4,label="Madison, Nov 1893"),dict(lat=41.59,lon=-93.62,label="Des Moines, Nov–Dec 1893"),dict(lat=42.33,lon=-83.05,label="Detroit, Feb–Mar 1894"),dict(lat=39.29,lon=-76.61,label="Baltimore, Oct 1894"),dict(lat=40.71,lon=-74.0,label="New York, 1894–96")],
  vantage=1,vantage_label="the hosts' collective gaze",form="newspaper",language="English",
  authenticity="A collective eye, not one person: dated, mostly unsigned reports, compiled in The Complete Works of Swami Vivekananda and in Marie Louise Burke's research; texts as reprinted there.",
  bio="The press made the Asian delegates famous and fixed their image: robes, turbans, complexions, 'perfect' English. Reports swing between admiration and condescension, and record the racial categories of the day.",
  sources=[dict(title="American newspaper reports on Vivekananda (Complete Works vol. 9, via sreyas.in)",url=NEWS),dict(title="Dubuque Times, 29 September 1893 (vivekananda.net)",url=DUB)]),
]

E=[]
def e(d,disp,prec,eye,place,head,dig,conf,src,quote=""):
    E.append(dict(date_iso=d,date_display=disp,precision=prec,eye=eye,place=place,headline=head,digest=dig,quote=quote,confidence=conf,source_note=src))

e("1892","1892 (letter undated in sources consulted)","year","benson","Lambeth Palace, London","The Archbishop of Canterbury declines to attend",
  "Benson's reply to the organisers refused any part in the Parliament. He argued that Christianity was not one religion among several but the one religion, and that it could not take a seat in such an assembly without implying an equality with other faiths that he denied.",
  "approx","Letter printed by Barrows 1893, vol. 1, pp. 20–22, as summarised in the Boston Collaborative Encyclopedia; exact date not checked",quote="the Christian religion is the one religion")
e("1893-05-12","12 May 1893","day","webb","New York","First issue of The Moslem World",
  "Webb launched a monthly paper from New York to explain Islam to Americans, the organ of his small propagation movement. It ran seven issues and closed in November 1893, weeks after his Chicago addresses.",
  "verified","Wikipedia, Alexander Russell Webb")
e("1893-07-09","Sunday 9 July 1893","day","mozoomdar","Brahmo Samaj, Calcutta","A farewell sermon full of worry",
  "Two days before sailing, Mozoomdar told his congregation he feared for his health and for his power to do God's work abroad, and asked them to pray for his wife left alone in Calcutta. He also begged the quarrelling branches of the Brahmo Samaj to make peace while he was away.",
  "verified","The Interpreter 2:1 (1893), as summarised by Mozoomdar at Sea, 'Farewell to Kolkata'")
e("1893-07-10","10 July 1893","day","vivekananda","Yokohama","Japan as a lesson for India",
  "Writing to his Madras disciples from Yokohama, Vivekananda praised the cleanliness, order and modern energy he had seen in Japan, and urged young Indians to travel and see it for themselves rather than sit at home in old prejudices.",
  "approx","Letter to Alasinga Perumal, Yokohama, July 1893, in Complete Works vol. 5; date as commonly printed, not re-checked here")
e("1893-07-30","30 July 1893","day","shaku-soen","Engaku-ji, Kamakura","A temple send-off for the Zen delegate",
  "More than 150 guests gathered at Engaku-ji to see off Shaku Sōen, part of a fundraising campaign that paid for the Japanese Buddhist delegation. Sōen had paid his student Suzuki Daisetsu to translate his papers into English.",
  "verified","Zheng, JJRS 46/2 (2019)")
e("1893-08-04","4 August 1893","day","shaku-soen","Yokohama","Five Japanese Buddhist delegates sail",
  "The delegation of Japanese Buddhists, Sōen among them with the Shingon priest Toki Hōryū and others, left Japan for Chicago after a farewell banquet for more than 130 dignitaries the day before.",
  "verified","Zheng, JJRS 46/2 (2019)")
e("1893-08-09","9 August 1893","day","pung","Chicago","The emperor's envoy arrives early",
  "According to the Chinese minister's report to the throne, Pung reached Chicago on 9 August, a month before the Parliament opened, and stayed until 1 October. He was the only delegate formally sent by a government.",
  "verified","Sun Jiang, Oriens Extremus 54, citing Ambassador Yang's memorial")
e("1893-08-20","20 August 1893","day","vivekananda","Breezy Meadows, Metcalf, Massachusetts","Down to his last coins in rich America",
  "Vivekananda told Alasinga that America was ruinously expensive and his money had fallen to about 130 dollars. He described Americans as spending lavishly, and resolved to hold on rather than go home defeated.",
  "verified","Letter to Alasinga, 20 Aug 1893, summarised on vivekananda.net",quote="spend money like water")
e("1893-09-02","2 September 1893","day","dharmapala","New York","Arriving with Annie Besant",
  "Dharmapala reached the United States with the Theosophist Annie Besant, who had upgraded his steamer ticket from third class to first. He came as the Theosophists' candidate to speak for 'Southern Buddhism'.",
  "verified","Theosophy Wiki, Anagarika Dharmapala")
e("1893-09-04","4 September 1893","day","vivekananda","Salem, Massachusetts","Letters of introduction to the Parliament",
  "Vivekananda thanked Professor John Henry Wright for the letters that would open the Parliament's doors to him, and sent him a poem on the search for God. Wright had told the organisers that the monk was more learned than all their professors together.",
  "verified","Letter to J. H. Wright, 4 Sept 1893 (vivekananda.net); Wright's remark as reported in biographies")
e("1893-09-11","Monday 11 September 1893, morning","day","bonney","Hall of Columbus, Art Institute, Chicago","Ten strokes of the bell open the Parliament",
  "Bonney opened the gathering before an audience of some four thousand, arguing that different conceptions of the divine should drive people to inquire more deeply, not to quarrel. The platform was crowded with robed delegates from Asia beside Protestant, Catholic and Jewish clergy.",
  "verified","Boston Collaborative Encyclopedia; Mercer, Review (1893)")
e("1893-09-11","Monday 11 September 1893","day","barrows","Hall of Columbus, Chicago","A welcome to the wise men of the East",
  "Barrows hailed delegates from the farthest isles of Asia and from India, 'mother of religions'. His language was generous and biblical at once: the visitors were cast as the Magi coming to the cradle of a Christian fulfilment.",
  "verified","Barrows's opening address, quoted in Mercer, Review (1893)",quote="Welcome, most welcome, O wise men of the East")
e("1893-09-11","Monday 11 September 1893","day","pung","Hall of Columbus, Chicago","The envoy's greeting, read by his host",
  "Pung's English was too limited to speak, so Barrows read his greeting. Barrows found that the sheet handed to him by Pung's secretary was the very text he himself had typed out in advance.",
  "verified","Sun Jiang, Oriens Extremus 54; Mercer, Review (1893)")
e("1893-09-11","Monday 11 September 1893","day","mozoomdar","Hall of Columbus, Chicago","The familiar Indian voice replies",
  "Mozoomdar answered the welcome for the Brahmo Samaj. The Unitarian Christian Register later wrote that no voice at the Parliament commanded more attention or sympathy than his.",
  "verified","Mercer, Review (1893) (speaker order); Christian Register as quoted in The Interpreter 2:4 (1893), via Mozoomdar at Sea")
e("1893-09-11","Monday 11 September 1893","day","gandhi","Hall of Columbus, Chicago","A Jain layman greets the assembly",
  "Gandhi gave a short welcome on behalf of the Jains in the afternoon session, one of a string of brief replies from Asian delegates seated in a row of coloured robes and turbans.",
  "verified","Parliament of the World's Religions article on Gandhi; Mercer, Review (1893)")
e("1893-09-11","Monday 11 September 1893, afternoon","day","vivekananda","Hall of Columbus, Chicago","Five words and a standing ovation",
  "Vivekananda had put off his turn several times, too nervous to rise. When he finally spoke, his opening salutation brought the crowd to its feet for about two minutes; he went on to speak of tolerance and of all religions as paths to one goal, citing the Gita.",
  "verified","vivekananda.net date table; Nikhilananda biography; text in Barrows 1893",quote="Sisters and Brothers of America")
e("1893-09-11","Monday 11 September 1893","day","press","Chicago","A parlor talk with the orange turban",
  "The Chicago Record interviewed the delegates informally. It described Vivekananda's orange turban, noted with evident surprise that his English was very good, and let him talk of his travels and of teaching students in India.",
  "verified","Chicago Record, 11 Sept 1893, in Complete Works vol. 9 (sreyas.in)")
e("1893-09-13","Wednesday 13 September 1893 (third day)","day","pung","Hall of Columbus, Chicago","Thirty thousand words on Confucianism, read by another",
  "Pung's paper was read for him by William Pipe. It argued that Confucianism was an ethical teaching, challenged the Western word 'religion', and in its last part criticised missionaries for knowing only the lowest classes of China and nothing of its institutions.",
  "verified","Sun Jiang, Oriens Extremus 54")
e("1893-09-13","mid-September 1893 (day not confirmed)","range","hirai","Hall of Columbus, Chicago","'If this is Christian ethics, we are heathen'",
  "Hirai told the hall that Japan distrusted Christianity because Christian nations imposed unequal treaties on it, and because Japanese in America met school bans, exclusion and signs barring them. The largely white audience shouted 'Shame!' at the injustices he listed and applauded him at the end.",
  "approx","Hirai's speech in Barrows (1893) via Miami Univ. teaching excerpt; Pluralism Project; exact day not confirmed")
e("1893-09-15","Friday 15 September 1893","day","vivekananda","Hall of Columbus, Chicago","The frog in the well",
  "In an unscheduled talk, 'Why We Disagree', Vivekananda told the fable of a frog who believes his well is the whole world, and applied it to Hindus, Christians and Muslims alike, each sure that his own well is the ocean.",
  "verified","vivekananda.net date table; text in Barrows 1893")
e("1893-09","September 1893 (day not confirmed)","month","shaku-soen","Hall of Columbus, Chicago","Karma explained to the West in Suzuki's English",
  "Sōen's paper on the law of cause and effect, translated by Suzuki and read aloud for him, set Buddhist karma against the idea of God as a first mover, and claimed that the Buddha's teaching agreed with modern science.",
  "approx","Pluralism Project; Barrows 1893 (text); date and reader not confirmed")
e("1893-09-19","Tuesday 19 September 1893","day","vivekananda","Hall of Columbus, Chicago","The paper on Hinduism",
  "Vivekananda's prepared paper presented the Vedas, the soul's divinity and rebirth, and insisted that Hindus did not worship idols as Christians imagined but used images as aids. He described India's religion as large enough to embrace all others.",
  "verified","vivekananda.net date table; text in Barrows 1893")
e("1893-09-20","Wednesday 20 September 1893","day","vivekananda","Hall of Columbus, Chicago","India needs bread, not more sermons",
  "Turning on the missionaries, Vivekananda said Christians spent fortunes saving Indian souls while famine went unrelieved, and that it was an insult to offer religion to a starving people. Barrows later called the charge unfounded.",
  "verified","vivekananda.net date table; Barrows footnote, Miami Univ. excerpt",quote="It is an insult to a starving people to offer them religion")
e("1893-09-20","20–21 September 1893","range","webb","Hall of Columbus, Chicago","The Yankee Muslim defends Islam",
  "Webb's two addresses argued that Islam was a religion of peace and sobriety unfairly judged by Western standards, and denied that it required polygamy or the seclusion of women. When he first touched on polygamy, voices in the hall cried 'Shame', the only open protest of the seventeen days; Barrows recorded that he was afterwards heard patiently.",
  "approx","Wikipedia (dates 20 and 21 Sept); Braybrooke; Neely's History text via Miami Univ.; which address drew the protest not confirmed")
e("1893-09-21","Thursday 21 September 1893","day","press","Chicago","The monk in orange, bubbling with good nature",
  "The Inter Ocean reported Vivekananda's attack on missions, picturing him in orange robe and scarlet turban, smiling and good-humoured even as he lectured Christians on their failures in India.",
  "verified","Chicago Inter Ocean, 21 Sept 1893, in Complete Works vol. 9 (sreyas.in)",quote="fairly bubbling with an expression of good nature")
e("1893-09","September 1893 (day not confirmed)","range","nagarkar","Hall of Columbus, Chicago","Social reform as India's real religion",
  "Nagarkar spoke for the Brahmo Samaj on the work of social reform in India, setting the reformers' campaigns on caste, widowhood and child marriage before an audience used to hearing of India only through missionary reports.",
  "approx","Braybrooke; Barrows 1893 (paper printed); title and date not confirmed")
e("1893-09-25","about 25 September 1893","range","gandhi","Hall of Columbus, Chicago","Jainism explained, and India defended",
  "Gandhi gave an exposition of Jain philosophy and ethics, and on another day rose to answer a speaker who had attacked the morality of Hindu religion, arguing that India's abuses existed in spite of its religions, as in any country. The hall applauded his reply.",
  "approx","Parliament of the World's Religions article; Braybrooke; exact days not confirmed")
e("1893-09-26","Tuesday 26 September 1893","day","vivekananda","Hall of Columbus, Chicago","Buddhism as Hinduism fulfilled",
  "Vivekananda spoke on Buddhism as the fulfilment of Hinduism, honouring the Buddha while arguing that Buddhism and Brahminical religion needed each other: the heart of the one and the intellect of the other.",
  "verified","vivekananda.net date table")
e("1893-09","late September 1893 (reported 28 September)","range","dharmapala","Hall of Columbus, Chicago","A Sinhalese blessing, then 'The World's Debt to Buddha'",
  "Dharmapala began by singing a Sinhalese benediction, then presented the Buddha as a teacher of ethics without a creator, whose teaching agreed with evolution. In the session on missions he said plainly that missionaries in Ceylon, Burma and China were intolerant and selfish.",
  "approx","Dubuque Times dispatch of 28 Sept 1893 (vivekananda.net); Barrows text via Miami Univ. excerpt; date of paper not confirmed",quote="The missionary is intolerant; he is selfish.")
e("1893-09-27","Wednesday 27 September 1893","day","vivekananda","Hall of Columbus, Chicago","The closing words: help, not fight",
  "Before more than seven thousand people, Vivekananda's final address said the Parliament had shown that holiness and charity belonged to no single church, and that each religion should grow by its own law while absorbing the spirit of the others.",
  "verified","vivekananda.net; Boston Collaborative Encyclopedia (attendance)")
e("1893-09-27","Wednesday 27 September 1893","day","bonney","Hall of Columbus, Chicago","The president's farewell",
  "Bonney closed the seventeen days, presenting the Parliament as proof that men of every faith could meet in courtesy. The closing session ran late into the night amid hymns and repeated applause for the Asian delegates.",
  "approx","Mercer, Review (1893); Boston Collaborative Encyclopedia; detail of his remarks not checked")
e("1893-09-27","end of September 1893","range","mozoomdar","Chicago","Celebrated in public, ill in private",
  "By the Parliament's close Mozoomdar had been diagnosed with diabetes and forbidden to work. Friends in Chicago feared he would die of kidney disease; little of this shows in his eloquent public addresses.",
  "verified","Mozoomdar at Sea, 'Conclusion', citing Bose's Life and Jenkin Lloyd Jones's letter of 15 Dec 1893")
e("1893-09-28","Thursday 28 September 1893 (printed 29 September)","day","press","Chicago (dispatch to the Dubuque Times)","Courtesy wearing thin in the Parliament",
  "A syndicated dispatch reported that ill feeling ran under the politeness. Joseph Cook mocked Hindu cosmology; Bishop Newman accused the Orientals of slandering missionaries and was met with what the writer called a calm, supercilious smile. Vivekananda, 'out of humor', charged Christian nations with prospering on others' misery.",
  "verified","Dubuque Times, 29 Sept 1893 (vivekananda.net)")
e("1893-10-02","2 October 1893","day","vivekananda","Chicago","A nervous man who spoke almost every day",
  "Writing to Wright, Vivekananda admitted his fright before the crowd and said he had spoken almost daily once admitted at the last moment. He praised his fellow Indian delegates, the orator Mozoomdar among them.",
  "verified","Letter to J. H. Wright, 2 Oct 1893 (vivekananda.net)")
e("1893-10-07","7 October 1893 (Chicago letter dated 3 October)","day","lucy-monroe","Chicago, for The Critic, New York","Two orators from the East",
  "The Critic's Chicago correspondent named Vivekananda and Dharmapala as the most impressive figures of the Parliament. She admired the Hindu's strong, intelligent face and thought the lesson of tolerance best put in his closing address, which she quoted at length.",
  "approx","The Critic, 7 Oct 1893, and Lucy Monroe's dispatch of 3 Oct, as reprinted on vivekananda.net; attribution of each paragraph as given there",quote="an orator by divine right")
e("1893-10-10","10 October 1893","day","vivekananda","Chicago","The Parliament as advertisement",
  "Vivekananda told Mrs. Tannatt Woods that his fame from the Parliament now earned him thirty to eighty dollars a lecture, with more engagements coming. The penniless visitor of August had become a paid speaker.",
  "verified","Letter to Mrs. Tannatt Woods, 10 Oct 1893 (vivekananda.net)")
e("1893-10-18","about 18 October 1893","range","dharmapala","Honolulu","A chance meeting on the way home",
  "Homeward bound, Dharmapala's ship called at Honolulu, where he met Mary Elizabeth Foster, a Hawaiian-born woman who became the chief benefactor of his Buddhist work for the rest of his life. He records the meeting in his diaries.",
  "approx","Theosophy Wiki (Honolulu stop, Foster); date as commonly cited in biographies, not checked against diary")
e("1893-11-02","2 November 1893","day","vivekananda","Chicago","The fullest account: the day's hit",
  "In a long letter to Alasinga, Vivekananda described his terror before speaking and the roar that greeted his first words, and reported that the papers called his speech the hit of the day. He praised American women's education and freedom, and turned the comparison into a sharp attack on Indian caste and priestcraft.",
  "verified","Letter to Alasinga, 2 Nov 1893 (vivekananda.net); phrase as quoted in Nikhilananda biography",quote="my heart was fluttering and my tongue nearly dried up")
e("1893-11-11","11 November 1893","day","press","Chicago letter, The Critic (New York)","A musical voice, and something Jesuitical",
  "A Critic profile admired Vivekananda's deep, musical voice and its rise to rich eloquence, yet detected something Jesuitical in his mind. The phrase cast the Hindu as both fascinating and slippery, a familiar Western image of the clever Oriental.",
  "verified","New York Critic, 11 Nov 1893, in Complete Works vol. 9 (sreyas.in)",quote="something Jesuitical in the character of his mind")
e("1893-11-19","19 November 1893","day","vivekananda","541 Dearborn Avenue, Chicago","The Church of England stayed away",
  "Leaving for Madison and Minneapolis, Vivekananda remarked to Mrs. Woods on Dr. Momerie, the English clergyman who had come to Chicago despite the Archbishop of Canterbury's opposition, and noted that the English church had sent no representative.",
  "verified","Letter to Mrs. Tannatt Woods, 19 Nov 1893 (vivekananda.net)")
e("1893-11-21","21 November 1893","day","press","Madison, Wisconsin (Daily Cardinal)","The student paper describes a dusky face",
  "The University of Wisconsin paper described the visitor's cream turban, yellow gown and cardinal sash, his low pleasant voice, and his 'dusky' face, and reported his parable of the blind men and the elephant. Colour and costume came before argument in almost every such notice.",
  "verified","Daily Cardinal, 21 Nov 1893, in Complete Works vol. 9 (sreyas.in)",quote="a pleasant, clear-cut, dusky face")
e("1893-11-24","24 November 1893","day","vivekananda","Minneapolis","First snow",
  "Vivekananda wrote to Mrs. Hale of his first snowfall, sleigh rides and the frozen falls, and said the winter scene pleased him more than anything else he had seen in America.",
  "verified","Letter to Mrs. G. W. Hale, 24 Nov 1893 (vivekananda.net)")
e("1893-12-01","1 December 1893","day","press","Des Moines, Iowa (Iowa State Register)","The Brahmo visitor follows the monk",
  "Reporting on Vivekananda's praise of the Brahmo Samaj, the Register noted that Nagarkar was now the city's visitor from the East. Asian lecturers were moving through the same Midwestern church and club circuits within weeks of each other.",
  "verified","Iowa State Register, 1 Dec 1893, in Complete Works vol. 9 (sreyas.in)")
e("1893-12-28","28 December 1893","day","vivekananda","Chicago","Not here to satisfy curiosity",
  "To Haripada Mitra in India, Vivekananda contrasted the education and freedom of American women with early marriage at home, and said he had come to America to find means to help India's poor, not out of curiosity.",
  "verified","Letter to Haripada Mitra, 28 Dec 1893 (vivekananda.net)",quote="I came to this country not to satisfy my curiosity")
e("1894-03-11","11 March 1894","day","press","Detroit (Detroit Tribune)","Detroit hears the case against missions",
  "The Tribune reported a lecture in which Vivekananda, in orange robe and turban, attacked missionary methods in India. Detroit clergy and some former patrons turned against him that spring, and rumours about his conduct circulated among his critics.",
  "verified","Detroit Tribune, 11 Mar 1894, in Complete Works vol. 9; Nikhilananda biography for the hostility")
e("1894-03-21","21 March 1894","day","press","Saginaw, Michigan (Saginaw Evening News)","His complexion resembles an Indian's",
  "A small-town paper announced the Hindu's arrival, noted that he dressed like a well-to-do American and spoke excellent English, and compared his complexion to that of an American Indian, sorting him into the racial categories it knew.",
  "verified","Saginaw Evening News, 21 Mar 1894, in Complete Works vol. 9 (sreyas.in)")
e("1894-08-11","11 August 1894 (talk of 3 August)","day","press","Greenacre, Eliot, Maine (Boston Evening Transcript)","A Hindu defends Muhammad under the pines",
  "The Transcript reported that at the Greenacre summer school Vivekananda had defended the Prophet Muhammad and the doctrine of rebirth, and that his audience was deeply moved.",
  "verified","Boston Evening Transcript, 11 Aug 1894, in Complete Works vol. 9 (sreyas.in)")
e("1894-10-13","13 October 1894","day","press","Baltimore (Baltimore News)","A flaming red cloak in a Baltimore hotel",
  "The News described the visitor's red cloak and yellow turban, his whistling and humour, and his views on immigration and divorce. Novelty and costume remained the hook, a year after the Parliament.",
  "verified","Baltimore News, 13 Oct 1894, in Complete Works vol. 9 (sreyas.in)",quote="a flaming red cloak and a gaudy yellow turban")
e("1895-08-06","18 June – 6 August 1895","range","vivekananda","Thousand Island Park, New York","Seven weeks with a handful of disciples",
  "Turning from public lecturing, Vivekananda taught a small group of American students at a cottage on the St Lawrence; their notes became the Inspired Talks. The last class was held on 6 August before he left for New York and Europe.",
  "verified","Vedanta Society chronology")
e("1895-11-10","10 November 1895","day","vivekananda","63 St George's Road, Belgravia, London","A London drawing room and Margaret Noble",
  "At Lady Isabel Margesson's house Vivekananda spoke to a small gathering that included the Irish teacher Margaret Noble, who later followed him to India as Sister Nivedita.",
  "approx","Vedanta Society chronology (index date); detail from standard biographies")
e("1896","1896 (Guangxu 22)","year","pung","Beijing","The Parliament reported to the throne",
  "The Zongli Yamen submitted the Chinese version of Pung's paper, Shuo jiao, to the emperor, and it was printed by the Tongwen Guan. The Chinese text called the gathering a parliament on 'Nestorianism', and the Chinese minister described the paper as mocking Western missionaries.",
  "verified","Sun Jiang, Oriens Extremus 54")
e("1896-05-28","28 May 1896","day","vivekananda","Oxford","Calling on Max Müller",
  "Vivekananda visited the Sanskritist Friedrich Max Müller, whose books had shaped European ideas of India, and came away moved by the old scholar's devotion to Ramakrishna, about whom Müller was then writing.",
  "approx","Vedanta Society chronology (index date); impressions as in Vivekananda's article on Max Müller (1896), not re-checked")
e("1896-12","December 1896 – early 1897","range","barrows","India (Calcutta and other cities)","The host lectures in the visitor's country",
  "Barrows travelled to India to give the Haskell lectures on Christianity as the world religion, retracing the Parliament's encounter on Indian ground just as Vivekananda prepared to return home in triumph.",
  "approx","Wikipedia, John Henry Barrows; Barrows, A World Pilgrimage (1897); dates approximate")
e("1938","1938 (recalling September 1893)","year","harriet-monroe","Chicago (memoir)","Remembering who stole the show",
  "In her posthumous autobiography Monroe recalled the Parliament as a pageant and judged that Vivekananda had stolen the whole show and captured the city, while Dharmapala too had spoken well. It is a memory written more than forty years later.",
  "verified","Harriet Monroe, A Poet's Life (1938), as quoted in Ziolkowski, Eastern Buddhist 26:1")

claims=[
 dict(date_iso="1892",date_display="1892",eye="benson",claim="Christianity is the one religion and cannot sit as an equal among others",form="letter",evidence="Printed in Barrows 1893, vol. 1",confidence="approx"),
 dict(date_iso="1893-08-20",date_display="20 Aug 1893",eye="vivekananda",claim="Americans are lavish with money; the country is crushingly expensive for a poor monk",form="letter",evidence="Letter to Alasinga, Breezy Meadows",confidence="verified"),
 dict(date_iso="1893-09-11",date_display="11 Sept 1893",eye="barrows",claim="Hails the Asian delegates as 'wise men of the East' come to a Christian gathering",form="speech",evidence="Opening address, in Mercer 1893",confidence="verified"),
 dict(date_iso="1893-09-11",date_display="11 Sept 1893",eye="press",claim="Remarks with surprise that the turbaned Hindu speaks very good English",form="newspaper",evidence="Chicago Record, 11 Sept 1893",confidence="verified"),
 dict(date_iso="1893-09-13",date_display="13 Sept 1893",eye="pung",claim="Missionaries know only China's lowest classes and nothing of its institutions",form="speech",evidence="'Confucianism', read by William Pipe; Sun Jiang",confidence="verified"),
 dict(date_iso="1893-09-13",date_display="mid-Sept 1893",eye="hirai",claim="Christian nations impose unequal treaties on Japan and bar Japanese from American schools",form="speech",evidence="Barrows 1893; Neely's History",confidence="approx"),
 dict(date_iso="1893-09-20",date_display="20 Sept 1893",eye="vivekananda",claim="Christians send preachers to India but not bread to its starving",form="speech",evidence="'Religion not the crying need of India'",confidence="verified"),
 dict(date_iso="1893-09-20",date_display="20–21 Sept 1893",eye="webb",claim="Americans judge Islam by Western standards and slander it as a religion of the sword",form="speech",evidence="Neely's History; Barrows (abridged)",confidence="verified"),
 dict(date_iso="1893-09-21",date_display="21 Sept 1893",eye="press",claim="The Hindu critic of missions is pictured as smiling, colourful and good-natured",form="newspaper",evidence="Chicago Inter Ocean",confidence="verified"),
 dict(date_iso="1893-09-28",date_display="28 Sept 1893",eye="press",claim="The 'Orientals' meet a bishop's accusations with a supercilious smile",form="newspaper",evidence="Dubuque Times, 29 Sept 1893",confidence="verified"),
 dict(date_iso="1893-09",date_display="Sept 1893",eye="dharmapala",claim="Missionaries in Asia are intolerant and selfish; Buddhist preachers win by compassion",form="speech",evidence="Barrows 1893, missions session",confidence="verified"),
 dict(date_iso="1893-10-07",date_display="7 Oct 1893",eye="lucy-monroe",claim="Vivekananda is an orator by divine right, the Parliament's most impressive figure",form="newspaper",evidence="The Critic",confidence="approx"),
 dict(date_iso="1893-11-02",date_display="2 Nov 1893",eye="vivekananda",claim="American women are the most educated and free in the world; India's caste and priestcraft shame it",form="letter",evidence="Letter to Alasinga",confidence="verified"),
 dict(date_iso="1893-11-11",date_display="11 Nov 1893",eye="press",claim="The Hindu's mind has 'something Jesuitical' about it",form="newspaper",evidence="New York Critic",confidence="verified"),
 dict(date_iso="1893-12",date_display="late 1893",eye="barrows",claim="Calls Vivekananda's charge against missions unfounded, while praising his influence over audiences",form="other",evidence="Barrows 1893, footnote and narrative",confidence="verified"),
 dict(date_iso="1894-03-21",date_display="21 Mar 1894",eye="press",claim="Sorts the visitor by skin colour, likening him to an American Indian",form="newspaper",evidence="Saginaw Evening News",confidence="verified"),
]

conv=[
 dict(date="1893-09-11",label="Opening day of the Parliament",eyes=["bonney","barrows","pung","mozoomdar","gandhi","vivekananda","press"],note="Hosts speak of welcome and fulfilment; the visitors answer one by one. Pung's greeting is read in Barrows's own typed text, Mozoomdar is the voice Americans know, and the unknown monk takes the hall; the Record notes chiefly his turban and his English."),
 dict(date="1893-09-13",label="Third day: Asia's charges against Christendom",eyes=["pung","hirai"],note="A Qing official, through a reader, and a Japanese layman, in his own English, both explain resistance to Christianity by the conduct of Christian nations and missions rather than by the faults of Asia."),
 dict(date="1893-09-20",label="Missions under fire, Islam on trial",eyes=["vivekananda","webb","press","barrows"],note="Vivekananda tells Christians India needs bread; Webb asks Americans to stop judging Islam by Western standards and is met with cries of 'Shame'. The Inter Ocean renders the critic as colourful and smiling; Barrows answers in a footnote."),
 dict(date="1893-09-26",label="Buddhist week's end",eyes=["vivekananda","dharmapala","press"],note="The Hindu speaks of Buddhism as Hinduism fulfilled while the Buddhist from Ceylon claims the Buddha for science; a Midwestern dispatch hears only rising acrimony and Oriental condescension."),
 dict(date="1893-09-27",label="Closing session",eyes=["vivekananda","bonney","mozoomdar"],note="Vivekananda's call for mutual assimilation closes the Parliament before seven thousand; Bonney celebrates concord; Mozoomdar leaves it diagnosed and forbidden to work."),
 dict(date="1893-10-07",label="Verdicts in print and in letters",eyes=["lucy-monroe","vivekananda"],note="The Critic crowns Vivekananda an orator by divine right in the same week he confesses to Wright how frightened he had been."),
 dict(date="1893-11",label="On the Midwestern circuit",eyes=["vivekananda","press","nagarkar","benson"],note="Vivekananda's letters record snow, fees and the absent Church of England; student and small-city papers record his complexion and costume; the Brahmo delegate Nagarkar follows a few weeks behind on the same route."),
]

ties=[
 dict(a="vivekananda",b="mozoomdar",kind="met",note="Vivekananda called Mozoomdar an old acquaintance and praised him as an orator in October 1893; relations later soured as the Brahmo leader was eclipsed and critics of the monk multiplied."),
 dict(a="vivekananda",b="dharmapala",kind="met",note="They sat side by side on the platform and were singled out together by The Critic; both attacked missionary conduct in Asia."),
 dict(a="vivekananda",b="barrows",kind="opposite sides",note="Barrows praised the monk's hold on audiences but called his charge against missions unfounded, and later carried his own case for Christianity to India."),
 dict(a="vivekananda",b="benson",kind="mentioned",note="Vivekananda's letter of 19 November 1893 notes the Archbishop's opposition and the Church of England's absence."),
 dict(a="pung",b="barrows",kind="met",note="Barrows read Pung's greeting on the opening day, from a text he had himself typed."),
 dict(a="pung",b="dharmapala",kind="met",note="Barrows mentions Dharmapala travelling across the Pacific with 'Mr. Pung'."),
 dict(a="hirai",b="shaku-soen",kind="same street",note="Both Japanese Rinzai Buddhists at the Parliament: the abbot spoke through a translator on doctrine, the layman in English on politics and discrimination."),
 dict(a="mozoomdar",b="nagarkar",kind="met",note="Fellow Brahmo Samaj delegates in Chicago."),
 dict(a="bonney",b="barrows",kind="influenced",note="Bonney conceived the congresses and appointed Barrows to organise the Parliament; Bonney's pluralist framing and Barrows's fulfilment theology sat uneasily together."),
 dict(a="gandhi",b="vivekananda",kind="met",note="Both Indian delegates spoke on the opening afternoon and both rose to defend Indian religion against missionary charges."),
 dict(a="lucy-monroe",b="harriet-monroe",kind="relative",note="Sisters: Lucy reported the Parliament for The Critic in 1893; Harriet remembered it in her 1938 memoir in very similar terms."),
 dict(a="webb",b="vivekananda",kind="opposite sides",note="Not opponents in debate, but mirror images: an American who took an Eastern faith, and an Indian who preached Vedanta to Americans; in 1894 Vivekananda publicly defended Muhammad at Greenacre."),
 dict(a="press",b="vivekananda",kind="mentioned",note="The papers turned him into the 'cyclonic Hindu' and followed him city to city, mixing praise with racial description."),
]

threads=[
 dict(to="iwakura-1871",note="Hirai's complaint about extraterritoriality and tariff limits concerned the very treaties the Iwakura embassy had tried, and failed, to revise in 1871–73; revision came only in 1894."),
 dict(to="v5:exposition-1889",note="Chicago's World's Columbian Exposition was built to outdo the Paris Exposition of 1889, and its Congress Auxiliary, which held the Parliament, imitated the congresses of Paris."),
 dict(to="v4:darwin-wallace",note="Dharmapala and Shaku Sōen both presented Buddhism to Chicago as compatible with evolution, enlisting Darwin's theory in an argument against Christian creation."),
 dict(to="v9:bombay-1896",note="Vivekananda returned to India in early 1897 as bubonic plague spread from Bombay; the order he founded organised plague relief in Calcutta in 1898."),
 dict(to="v5:gitanjali-1912",note="The Brahmo Samaj that sent Mozoomdar and Nagarkar to Chicago was the reformed theism of the Tagore family, from which Rabindranath Tagore's own Western reception grew two decades later."),
]

images=[
 dict(url="https://www.wikipedia.org/wiki/File:The_World%27s_Parliament_of_Religions_-_an_illustrated_and_popular_story_of_the_World%27s_First_Parliament_of_Religions,_held_in_Chicago_in_connection_with_the_Columbian_exposition_of_1893_(1893)_(14578851807).jpg",title="Illustration from Barrows's popular history (1893)",caption="A page image from the illustrated 1893 history of the Parliament, scanned from a library copy; the book's portraits and views shaped how Americans pictured the Asian delegates.",date="1893",credit="Internet Archive Book Images, via Wikimedia Commons"),
 dict(url="https://wikipedia.com/wiki/File:The_World%27s_Parliament_of_Religions_-_an_illustrated_and_popular_story_of_the_World%27s_First_Parliament_of_Religions,_held_in_Chicago_in_connection_with_the_Columbian_exposition_of_1893_(1893)_(14762867784).jpg",title="Further illustration from the 1893 history",caption="Another scanned page image from the same 1893 illustrated account of the Parliament.",date="1893",credit="Internet Archive Book Images, via Wikimedia Commons"),
 dict(url="https://www.wikipedia.com/wiki/File:The_World%27s_Parliament_of_Religions_-_an_illustrated_and_popular_story_of_the_World%27s_First_Parliament_of_Religions,_held_in_Chicago_in_connection_with_the_Columbian_exposition_of_1893_(1893)_(14742287306).jpg",title="Page from the 1893 illustrated history",caption="A third page image from the 1893 popular history of the Parliament; subjects of individual plates are as labelled on the Commons file page.",date="1893",credit="Internet Archive Book Images, via Wikimedia Commons"),
]

further=[
 dict(title="Barrows, The World's Parliament of Religions (1893), HathiTrust record",url=HATHI),
 dict(title="Barrows, vol. 1, Princeton Theological Seminary digital commons",url=PTSEM),
 dict(title="Mercer, Review of the World's Religious Congresses (1893), full text",url=MERCER),
 dict(title="Vivekananda: letters written from America, 1893",url=VNET),
 dict(title="American newspaper reports on Vivekananda, 1893–96",url=NEWS),
 dict(title="Sun Jiang on the representation of Chinese religions at the 1893 Parliament",url=SUN),
 dict(title="Zheng, The Japanese preparation for the World's Parliament of Religions",url=ZHENG),
 dict(title="Braybrooke, Pan-Asian participation in the 1893 Parliament",url=BRAY),
]

intro=[
 "In September 1893, beside the white plaster palaces of the World's Columbian Exposition, Chicago staged what its organisers called the first Parliament of the World's Religions. For seventeen days, in the new Art Institute on Michigan Avenue, clergy of every Christian denomination shared a platform with a Hindu monk, a Jain lawyer, Brahmo reformers, Buddhists from Ceylon and Japan, an envoy of the Chinese emperor and an American convert to Islam. Christians gave about 152 of the 194 papers; the handful of Asian speakers took most of the attention.",
 "The record is mostly speeches and letters rather than diaries. The speeches survive as printed by John Henry Barrows, the Presbyterian pastor who chaired the Parliament and edited its two-volume history, sometimes in condensed form; several of the visitors never spoke in English at all, and their words were read for them by Barrows or others. The fullest private voice is Vivekananda's, whose letters to his disciples in Madras and to his new American friends track his journey from penniless stranger to paid celebrity. Dharmapala kept diaries, published only in extracts; Pung Kwang Yu's paper went home as an official report to the throne.",
 "The hosts looked back through their own lenses. Barrows welcomed the 'wise men of the East' while holding that Christianity was the fulfilment of all faiths; the Archbishop of Canterbury refused to come at all. Newspapers in Chicago and in the small cities of the Midwest described the visitors' robes, turbans, voices and complexions before their arguments, swinging between admiration and racial condescension. Those descriptions are reported here as written.",
 "The visitors were not neutral either. Hirai Kinzō told the hall that Christian nations had imposed unequal treaties on Japan and barred Japanese children from American schools; Pung, Dharmapala and Vivekananda all charged missionaries with ignorance or arrogance. Vivekananda's letters praise American women and wealth and pour scorn on Indian caste, turning the comparison against his own country as much as his hosts'.",
 "A coda follows Vivekananda on the lecture circuit from Madison to Detroit to Baltimore, to a summer of teaching on the St Lawrence and to London and Oxford, where the gaze reverses again: the Indian monk calling on the European scholar who had interpreted India to the West."
]

cal="All dates are Gregorian. Japan had adopted the Gregorian calendar in 1873, so Japanese records of the delegation's departure in Meiji 26 (1893) fall on the same days. Pung Kwang Yu's report Shuo jiao was submitted and printed in Guangxu 22, which ran from February 1896 to January 1897; it is filed here under 1896. Several Parliament days are not confirmed for individual speakers and are marked as ranges with confidence 'approx'."

ch=dict(id="vivekananda-1893",title="Sisters and Brothers: Asia Speaks in Chicago",short_title="Chicago 1893",
 subtitle="The World's Parliament of Religions, World's Columbian Exposition, Chicago, 11–27 September 1893, and Vivekananda's American and English tour",
 span="1893–1896",intro=intro,calendar_note=cal,eyes=eyes,entries=sorted(E,key=lambda x:x["date_iso"]),claims=claims,
 convergences=conv,ties=ties,threads_out=threads,images=images,further=further,
 vantage_key="0 = a speaker or organiser at the Parliament; 1 = in the hall or reporting from Chicago and the lecture circuit; 2 = the same city; 3 = the same country at a distance; 4 = abroad, judging from afar.")
DROPH={"Social reform as India's real religion","A flaming red cloak in a Baltimore hotel","First snow","A temple send-off for the Zen delegate","The president's farewell"}
ch["entries"]=[x for x in ch["entries"] if x["headline"] not in DROPH]
ch["eyes"]=[x for x in ch["eyes"] if x["id"]!="nagarkar"]
ch["ties"]=[t for t in ch["ties"] if "nagarkar" not in (t["a"],t["b"])]
for c in ch["convergences"]: c["eyes"]=[i for i in c["eyes"] if i!="nagarkar"]
eyes=ch["eyes"]; E=ch["entries"]
json.dump(ch,open(OUT,"w"),ensure_ascii=False,indent=1)
print(len(eyes),len(E),len(claims),len(conv),len(ties),len(threads),len(images),len(further))
for x in eyes: assert len(x["short"])<=16,x["short"]
ids={x["id"] for x in eyes}
for x in E: assert x["eye"] in ids
for c in conv:
  for i in c["eyes"]: assert i in ids
for q in E:
  if q["quote"]: assert len(q["quote"].split())<=12,q["quote"]
