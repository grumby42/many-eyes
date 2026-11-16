import json
OUT="/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/vol10/ch-tahtawi-1826.json"
SIL="https://psi427.cankaya.edu.tr/uploads/files/Silvera%2C%20First%20Egyptian%20Students%20in%20France%20under%20Muhammad%20Ali%20%281980%29.pdf"
NEWC="https://durham-repository.worktribe.com/OutputFile/1572893"
LOU="https://open.unive.it/hitrade/books/LoucaRifaa.pdf"
MUE="https://www.wpsanet.org/papers/docs/MuenchWPSA21.docx"
APP="https://fr.wikisource.org/wiki/Autour_de_la_R%C3%A9volution_de_1830/02"
BER="https://www.gutenberg.org/ebooks/38150.epub.images"
TDV="https://islamansiklopedisi.org.tr/rifaa-et-tahtavi"
IMA="https://imarabe.org/sites/default/files/2024-11/dossier-enseignants-au-miroir-de-lautre-2.pdf"
ZAR="https://www.wikiwand.com/en/Zarafa_(giraffe)"
HYP="https://hyperallergic.com/413018/zarafa-the-first-giraffe-in-france/"
SAQI="https://www.arabworldbooks.com/en/books/an-imam-in-paris-al-tahtawis-visit-to-france-1826-1831"

eyes=[
 dict(id="tahtawi",short="al-Tahtawi",name="Rifa'a Rafi' al-Tahtawi",life="1801–1873",
  role="Azhar-trained scholar aged about 25, appointed imam (prayer leader and religious guide) to the student mission; became its most celebrated student and translator",
  side="Egypt under Muhammad Ali; al-Azhar ulama",
  where="Alexandria, Marseilles, then Paris (rue de Clichy, later the mission house in rue du Regard and private lodgings)",
  lat=48.849,lon=2.327,
  waypoints=[dict(lat=31.2,lon=29.92,label="Alexandria, sails 13 Apr 1826"),dict(lat=38.19,lon=15.55,label="Messina, first church bells"),dict(lat=43.296,lon=5.37,label="Marseilles, quarantine May 1826"),dict(lat=48.849,lon=2.327,label="Paris 1826–1831"),dict(lat=30.044,lon=31.236,label="Cairo, by Aug 1831")],
  vantage=0,vantage_label="the visitor who wrote it all down",
  form="travel account (rihla) written up from notes during and after the stay; published 1834",
  language="Arabic",
  authenticity="Takhlis al-ibriz fi talkhis Bariz was finished after his return and printed at the Bulaq press in 1834 (1250 AH), with a preface by his teacher Hasan al-'Attar; later editions followed (1848–49, 1905). The manuscript was read in Paris by Silvestre de Sacy and Caussin de Perceval, whose letters he printed in the book. It is arranged by topic, not as a day-by-day diary, so most dates here are those of the events he describes. Modern English translation: Daniel L. Newman, An Imam in Paris (2004; 2nd ed. 2011); French: Anouar Louca, L'Or de Paris (1988).",
  bio="Born in Tahta in Upper Egypt, trained at al-Azhar under Hasan al-'Attar, he went to Paris only as the mission's imam but taught himself French and was allowed to study alongside the students. His book is the first full Arabic description of a modern European capital and its constitution, and it explains French institutions by comparing them with Islamic ideas of justice. Back in Egypt he became a translator, founded the School of Languages (1835) and edited the official gazette.",
  sources=[dict(title="D. L. Newman, An Imam in Paris (Saqi, 2004/2011)",url=SAQI),dict(title="A. Louca, study of Rifa'a (Venice, Hi-Trade)",url=LOU),dict(title="TDV İslâm Ansiklopedisi: Rifâa et-Tahtâvî",url=TDV)]),
 dict(id="jomard",short="Jomard",name="Edme-François Jomard",life="1777–1862",
  role="Geographer and engineer, veteran of Bonaparte's Egyptian expedition and editor of the Description de l'Égypte; director of the Egyptian school in Paris, aged 49 in 1826",
  side="France; Société de géographie; the savants of the Egypt expedition",
  where="Paris: the mission house at 15 rue du Regard and the École des langues orientales",
  lat=48.849,lon=2.327,vantage=1,vantage_label="the host who ran the school",
  form="printed reports, press notices and letters",language="French",
  authenticity="His report on the Egyptian students, with a list of names, was printed in the Nouveau Journal asiatique II (August 1828), pp. 96–116; he also fed notices to the Moniteur. Later memoranda (e.g. 1839) argue his own case and should be read as advocacy.",
  bio="Jomard had measured the pyramids in 1798–1801 and spent decades publishing Egypt for France. In Paris he became the students' headmaster, banker, censor and publicist: he set their pocket money, took them to theatres and museums, arranged examinations and wrote them up for the learned press. His records are the hosts' fullest view of the mission.",
  sources=[dict(title="A. Silvera, 'The First Egyptian Student Mission to France under Muhammad Ali' (1980)",url=SIL)]),
 dict(id="press",short="Paris press",name="Paris press (Moniteur universel, Revue encyclopédique, La Pandore, Gazette de France)",life="1826–1831",
  role="Official, liberal and satirical papers that reported on the Égyptiens and on the pasha's giraffe",
  side="France: government, liberal and opposition opinion",where="Paris (and Marseilles)",lat=48.866,lon=2.34,
  vantage=2,vantage_label="the city watching the visitors",form="newspapers and reviews",language="French",
  authenticity="Dated issues cited by Silvera (1980) from the Moniteur universel, Revue encyclopédique, La Pandore and Gazette de France; contents summarised here only as far as that study reports them. Barthélemy and Méry's satire La Bacriade (1827) is a printed poem, not journalism.",
  bio="The students arrived in a France split over Muhammad Ali's war against the Greeks, so the same group could be welcomed as a civilising project or mocked as the pasha's agents. The papers recorded their arrival, examinations and Jomard's claims for them, and in 1827 turned the giraffe into a craze.",
  sources=[dict(title="Silvera (1980), notes 42, 45, 58, 60–62, 67, 77",url=SIL)]),
 dict(id="geoffroy",short="Geoffroy",name="Étienne Geoffroy Saint-Hilaire",life="1772–1844",
  role="Professor of zoology at the Muséum d'histoire naturelle, aged 55, another veteran of the Egypt expedition; escorted the giraffe from Marseilles to Paris",
  side="France; Muséum d'histoire naturelle",where="On foot from Marseilles via Lyon to Paris, May–June 1827",
  lat=48.844,lon=2.36,waypoints=[dict(lat=43.296,lon=5.37,label="Marseilles, 20 May 1827"),dict(lat=45.76,lon=4.84,label="Lyon, 6 June 1827"),dict(lat=48.844,lon=2.36,label="Jardin du Roi, 30 June 1827"),dict(lat=48.84,lon=2.22,label="Saint-Cloud, 9 July 1827")],
  vantage=1,vantage_label="walking beside the pasha's gift",form="dated letters and reports from the road",language="French",
  authenticity="His letters to his wife and reports to the ministry from the 1827 journey survive in the Muséum archives and are quoted in modern histories (notably Michael Allin, Zarafa, 1998); the dates of the journey are well established, the letters' wording is not reproduced here.",
  bio="Geoffroy had collected animals in Egypt in 1798–1801. In 1827 he walked some 900 km with the giraffe, her Egyptian and Sudanese keepers and a small herd of cows that supplied her milk. Her keepers, Atir and Hassan, left no surviving firsthand account; Geoffroy's letters are the closest record of the walk.",
  sources=[dict(title="Zarafa (giraffe), encyclopedia summary",url=ZAR),dict(title="Hyperallergic, 'How Zarafa, France's First Giraffe, Became a Cultural Sensation'",url=HYP)]),
 dict(id="muhammad-ali",short="Muhammad Ali",name="Muhammad Ali Pasha",life="1769–1849",
  role="Ottoman governor (wali) of Egypt since 1805, aged about 57; sponsor and paymaster of the mission",
  side="Egypt; Ottoman Empire",where="Cairo and Alexandria",lat=30.03,lon=31.26,vantage=3,vantage_label="the patron at home",
  form="orders, decrees and official correspondence (Ottoman Turkish and Arabic)",language="Ottoman Turkish / Arabic",
  authenticity="His orders survive in the Egyptian National Archives (Dar al-Watha'iq) and in French consular dispatches that report them; most are known through archival studies rather than a single printed edition.",
  bio="Muhammad Ali wanted officers, engineers, doctors and translators for his new army and state, and chose France over Italy for his first large mission. He followed the students' progress through Jomard and his own officials, sent the king a giraffe, and on their return placed them in his schools and offices.",
  sources=[dict(title="Silvera (1980)",url=SIL)]),
 dict(id="drovetti",short="Drovetti",name="Bernardino Drovetti",life="1776–1852",
  role="French consul-general in Egypt, collector of antiquities and long-time adviser to Muhammad Ali",
  side="France in Egypt",where="Alexandria",lat=31.2,lon=29.92,vantage=3,vantage_label="the go-between in Alexandria",form="dated letters",language="Italian / French",
  authenticity="His letters, including one to the minister Boghos Yusufian of 7 January 1826, are cited by Silvera (1980) from the Marro edition of his correspondence.",
  bio="Drovetti lobbied for Paris as the mission's destination and against Italy. He also arranged the giraffe's journey to France, and his Sudanese servant Atir went with her and stayed as her keeper until her death in 1845.",
  sources=[dict(title="Silvera (1980), note 36",url=SIL)]),
 dict(id="attar",short="al-'Attar",name="Hasan al-'Attar",life="c. 1766–1835",
  role="Senior Azhar scholar, Tahtawi's teacher; later Shaykh al-Azhar until his death in 1835",
  side="Egypt; al-Azhar",where="Cairo",lat=30.046,lon=31.263,vantage=4,vantage_label="the teacher who asked for the book",form="preface (printed)",language="Arabic",
  authenticity="His preface (taqriz) appears in the 1834 Bulaq edition of the Takhlis; his earlier advice to Tahtawi is known from Tahtawi's own introduction.",
  bio="Al-'Attar had met French scholars during the occupation of 1798–1801 and was unusually open to European science. He recommended his pupil as the mission's imam, urged him to record what he saw, and endorsed the finished book.",
  sources=[dict(title="Louca, study of Rifa'a",url=LOU)]),
 dict(id="desacy",short="de Sacy",name="Antoine-Isaac Silvestre de Sacy",life="1758–1838",
  role="France's leading Arabist, aged about 72, professor at the École des langues orientales and the Collège de France",
  side="France; Paris orientalists",where="Paris",lat=48.857,lon=2.337,vantage=2,vantage_label="the reader of the manuscript",form="letter of assessment and marginal comments",language="French",
  authenticity="His letter on the manuscript was translated into Arabic and printed by Tahtawi in the Takhlis; a comment of his on Tahtawi's view of French religion is quoted in an Institut du monde arabe teaching dossier.",
  bio="De Sacy taught most of Europe's Arabists and was a stern judge of Arabic style. He read Tahtawi's account before it was printed and praised it while correcting some of its judgements about the French.",
  sources=[dict(title="Institut du monde arabe, 'Au miroir de l'autre' dossier",url=IMA)]),
 dict(id="caussin",short="Caussin",name="Armand-Pierre Caussin de Perceval",life="1795–1871",
  role="Professor of colloquial Arabic at the École des langues orientales; Tahtawi's teacher and friend",
  side="France; Paris orientalists",where="Paris",lat=48.857,lon=2.337,vantage=2,vantage_label="the teacher who introduced the book to Europe",form="letter and published review",language="French",
  authenticity="His letter on the manuscript is printed in the Takhlis; his account of the book appeared in the Nouveau Journal asiatique XI (June 1833).",
  bio="Caussin had lived in the Levant and Egypt and spoke Arabic fluently. He read the Takhlis in manuscript and was the first to describe it at length to European readers, a year before its Arabic printing.",
  sources=[dict(title="TDV İslâm Ansiklopedisi",url=TDV),dict(title="Silvera (1980), note 43",url=SIL)]),
 dict(id="apponyi",short="Apponyi",name="Count Rodolphe (Rudolf) Apponyi",life="1802–1853",
  role="Attaché at the Austrian embassy in Paris, aged 28 in 1830, a kinsman of the ambassador",
  side="Austria; legitimist court society",where="Paris embassy; in Dieppe during the July fighting",lat=48.87,lon=2.315,
  waypoints=[dict(lat=49.92,lon=1.08,label="Dieppe, July 1830"),dict(lat=48.87,lon=2.315,label="Paris, from 1 Sept 1830")],
  vantage=2,vantage_label="a conservative diplomat in the new Paris",form="diary (journal addressed to his stepmother)",language="French",
  authenticity="Edited by Ernest Daudet as Vingt-cinq ans à Paris, journal du comte Rodolphe Apponyi (Plon, from 1913), with extracts in the Revue des Deux Mondes. The editor selected and arranged the text.",
  bio="Apponyi lived in Paris from 1826 and recorded court, salon and street for his family in Vienna. He missed the three days themselves but returned to a city of barricade scars and kept a close diary of the anxious months that followed.",
  sources=[dict(title="Revue des Deux Mondes: 'Autour de la Révolution de 1830', II",url=APP)]),
 dict(id="berlioz",short="Berlioz",name="Hector Berlioz",life="1803–1869",
  role="Composer aged 26, competing for the Prix de Rome at the Institut",
  side="France; Paris Conservatoire",where="Locked in the Institut de France, quai Conti",lat=48.857,lon=2.337,vantage=1,vantage_label="inside the Institut as the shooting began",
  form="dated letters; memoirs (written later)",language="French",
  authenticity="Letters to Humbert Ferrand in Lettres intimes (1882); the editor's dating is generally accepted. His Mémoires (written 1848–1865) retell July 1830 with hindsight and flourish.",
  bio="Berlioz was shut in the Institut writing his cantata Sardanapale when the fighting broke out a few hundred metres away. He won the prize and remembered finishing his score to the sound of gunfire.",
  sources=[dict(title="Berlioz, Lettres intimes (Project Gutenberg)",url=BER)]),
]

E=[]
def e(d,disp,prec,eye,place,head,dig,conf,src,quote=""):
    E.append(dict(date_iso=d,date_display=disp,precision=prec,eye=eye,place=place,headline=head,digest=dig,quote=quote,confidence=conf,source_note=src))

e("1826-01-07","7 January 1826","day","drovetti","Alexandria","Drovetti argues for Paris, not Italy",
 "Writing to Muhammad Ali's minister Boghos, the French consul dismissed the idea of sending the pasha's young men to Italy and pressed the case for Paris. The choice of France was not settled; British and Italian options had their advocates at court.","verified","Drovetti to Boghos, 7 Jan 1826 (Marro ed., pp. 86–87), cited Silvera (1980) n. 36.")
e("1826-02","February–April 1826","range","muhammad-ali","Cairo and Alexandria","The pasha orders the students to Alexandria",
 "After the pro-French faction prevailed, the pasha ordered the chosen students, mostly Turkish- and Circassian-speaking sons of the elite with a few Egyptians and Armenians, to gather at Alexandria. French officers reported the decision home on 26 February, and the consul confirmed it on 4 April.","verified","Boyer to Belliard, 26 Feb 1826; consul's dispatch 4 Apr 1826; Silvera (1980) nn. 37–38.")
e("1826-03","Early 1826 (Sha'ban–Ramadan 1241 AH)","range","attar","Cairo","A teacher's commission: write down everything",
 "Al-'Attar recommended his pupil for the post of imam to the mission and urged him to observe and record what he found in France. Tahtawi later named this request as the origin of his book.","approx","Tahtawi's introduction to the Takhlis, as summarised by Louca and Newman; date inferred from the departure.")
e("1826-04-13","Thursday 13 April 1826 (5 Ramadan 1241 AH)","day","tahtawi","Alexandria harbour, aboard La Truite","Forty-four students sail on a French warship",
 "The mission, forty-four young men with their supervisors and their imam, embarked on the French naval vessel La Truite. Tahtawi, aged about 25, was not yet a student at all, only the group's religious guide. The voyage took about a month.","verified","Silvera (1980), from French Foreign Ministry archives; Louca gives the ship's name and the voyage length.")
e("1826-04","Late April 1826 (Ramadan 1241 AH)","range","tahtawi","Messina, Sicily","Church bells at Messina",
 "When the ship called at Messina, Tahtawi heard church bells for the first time and noted it as a mark of having crossed into the Christian world. The detail opens a long habit in his book of recording small sensory novelties before large ideas.","approx","Silvera (1980), from the Takhlis; day not given.")
e("1826-05-15","Monday 15 May 1826 (7 Shawwal 1241 AH)","day","tahtawi","Marseilles, the lazaret","Landing at Marseilles, then eighteen days' quarantine",
 "The students landed at Marseilles, a city full of sympathy for the Greeks whom the pasha's army was fighting, and were held in the quarantine station for eighteen days. Tahtawi used the confinement to discuss whether quarantine was lawful for Muslims who believed in divine decree, and argued that it was.","verified","Silvera (1980); Newman, Chronos 6 (2002); Louca on the quarantine debate.")
e("1826-05","May 1826","month","press","Paris","A liberal review defends the mission",
 "The Revue encyclopédique answered critics who saw the students as agents of the pasha's war in Greece, presenting the mission as a transfer of knowledge that would serve Egypt's people.","approx","Revue encyclopédique, May 1826, cited Silvera (1980) n. 42; content as summarised there.")
e("1826-06","June–July 1826","range","tahtawi","Marseilles, a rented hotel","The French alphabet in a Marseilles hotel",
 "Released from quarantine, the students stayed in a hotel where they began learning French letters. Tahtawi described his first cafés, theatres of mirrors and well-lit streets, and the novelty of sitting on chairs at tables to eat.","approx","Silvera (1980); details from the Takhlis as summarised in Newman's introduction.")
e("1826-08","Late July–August 1826 (Muharram 1242 AH)","range","tahtawi","Paris, rue de Clichy","By diligence to Paris",
 "After roughly a week on the road by diligence the mission reached Paris and was lodged first in a house in the rue de Clichy. Tahtawi began a description of the city's site, the Seine and its bridges, its climate and its water supply, written as an Arab geographer would describe any new country.","approx","Silvera (1980); Louca. Exact day of arrival not found.")
e("1826-08-13","Sunday 13 August 1826 (9 Muharram 1242 AH)","day","press","Paris","The Moniteur announces the Égyptiens",
 "The official Moniteur universel carried a notice about the Egyptian students, part of a stream of press releases from Jomard. Satirical papers such as La Pandore also took them up later that month.","verified","Moniteur universel 13 Aug 1826; La Pandore 22 and 26 Aug 1826; Silvera (1980) nn. 58, 60.")
e("1826-08","August–September 1826","range","jomard","Paris","Jomard takes charge of daily life",
 "Jomard organised the students' timetable, teachers and pocket money, and arranged visits to theatres, museums and public institutions as part of their education. He also kept their image in the papers, presenting the mission as a credit to France.","approx","Silvera (1980); month inferred from arrival.")
e("1826-10-31","31 October 1826","day","muhammad-ali","Marseilles","The pasha's giraffe lands in France",
 "A young giraffe, sent by Muhammad Ali as a gift to Charles X and arranged through Drovetti, reached Marseilles after a voyage from Alexandria. She wintered there with her keepers, Atir and Hassan, who left no surviving account of their own.","verified","Zarafa (giraffe) summary; Hyperallergic (October 1826).")
e("1827","1827","year","tahtawi","Paris","A first translation: Agoub's 'Broken Lyre'",
 "Tahtawi turned into Arabic La lyre brisée, a poem by Joseph Agoub, the Egyptian-born teacher who helped instruct the mission. It is described as the first French literary text rendered into Arabic, and it marks his shift from imam to student-translator.","verified","Newman, Chronos 6 (2002).")
e("1827","1827","year","press","Paris","A mock-epic mocks the pasha's students",
 "Barthélemy and Méry's satirical poem La Bacriade, aimed at the government, brought the Egyptian students into its cast, a sign that they had become part of Paris's political comedy.","approx","Silvera (1980) n. 62.")
e("1827-05-20","Sunday 20 May 1827","day","geoffroy","Marseilles","Geoffroy and the giraffe set out on foot",
 "Geoffroy Saint-Hilaire, aged 55, left Marseilles walking with the giraffe, dressed in a fitted coat against the cold, with her keepers and a few milk cows. He reported his progress in letters to his wife and to the authorities.","verified","Zarafa (giraffe) summary; letters as described in modern histories.")
e("1827-06-06","Wednesday 6 June 1827","day","geoffroy","Lyon","Thirty thousand people in Lyon",
 "At Lyon a crowd put at about thirty thousand came out to see the animal. Each town turned the procession into a fair, and Geoffroy's worry became the crowds rather than the road.","verified","Zarafa (giraffe) summary.")
e("1827-06-30","Saturday 30 June 1827 (5 Dhu al-Hijja 1242 AH)","day","geoffroy","Jardin du Roi (Jardin des Plantes), Paris","Arrival at the Jardin du Roi",
 "After forty-one days on the road, the giraffe reached the royal garden in Paris, where she was lodged in the menagerie. Hundreds of thousands came to see her in the following months.","verified","Zarafa (giraffe) summary (41-day walk from 20 May); Hyperallergic on visitor numbers.")
e("1827-07-09","Monday 9 July 1827 (14 Dhu al-Hijja 1242 AH)","day","geoffroy","Saint-Cloud","Presented to Charles X",
 "The giraffe was taken to Saint-Cloud and presented to the king, with her keepers in Egyptian dress. Popular prints of the day showed the scene and made the keepers as much a spectacle as the animal.","verified","Thiébault print captioned 9 July 1827 (Philadelphia Museum of Art), reproduced by Hyperallergic; Zarafa summary.")
e("1827-07","July 1827","month","press","Paris","The giraffe revives interest in the Egyptians",
 "The Revue encyclopédique reported the giraffe's arrival, and the craze for all things 'à la girafe' revived curiosity about the Égyptiens; a vaudeville, La Girafe, ou une journée au Jardin du Roi, played on it.","approx","Revue encyclopédique, July 1827, cited Silvera (1980) nn. 60–61.")
e("1827-07","July 1827","month","jomard","Paris","A poor first-year examination",
 "The first examination of the students went badly. Jomard broke up the communal house and placed them in boarding schools and teachers' homes so that they would speak French all day.","approx","Silvera (1980); month as given there.")
e("1827-08-24","Friday 24 August 1827","day","press","Paris","The Gazette de France on the students",
 "The royalist Gazette de France reported on the Egyptian students in Paris, one of several notices that year.","approx","Gazette de France 24 Aug 1827, cited Silvera (1980) n. 45; content not detailed.")
e("1828-02-28","28 February – 1 March 1828 (Sha'ban 1243 AH)","range","jomard","École des langues orientales, rue de Lille","A public examination with an English admiral watching",
 "Jomard staged the students' oral examination at the École des langues orientales, a week after written tests. Sir Sidney Smith and David Morier were among the observers, a reminder that Britain watched France's influence in Egypt closely.","verified","Silvera (1980).")
e("1828-03-12","Wednesday 12 March 1828","day","press","Paris","Jomard's refused salary made public",
 "The Moniteur publicised that Jomard had declined a salary of 10,000 francs a year for directing the school, presenting his work as disinterested.","verified","Moniteur universel 12 Mar 1828, cited Silvera (1980) n. 77.")
e("1828-07-04","Friday 4 July 1828","day","jomard","15 rue du Regard, Paris","Graduation day at the rue du Regard",
 "A ceremony at the mission house closed the general course; specialised studies had begun in April. That autumn some students entered the École polytechnique and the École des mines, others went to Toulon, Brest and a model farm.","verified","Silvera (1980).")
e("1828-08","August 1828","month","jomard","Paris","Jomard's report in the Nouveau Journal asiatique",
 "Jomard published a detailed account of the Egyptian school with a list of its students, their subjects and results, setting out the mission as a scientific and political success for France.","verified","Nouveau Journal asiatique II (Aug 1828), pp. 96–116, cited Silvera (1980) n. 40.")
e("1829","1829","year","tahtawi","Paris","Translating Depping's history of customs",
 "At Jomard's suggestion Tahtawi translated G.-B. Depping's Aperçu historique sur les mœurs et coutumes des nations. Jomard advised him to leave out passages hostile to Islamic customs. It was printed at Bulaq in 1833 (1249 AH).","verified","Louca; Newman, Chronos 6 (2002).")
e("1829","1826–1830","range","tahtawi","Paris","What the Parisians are like",
 "Tahtawi described Parisians as clever, curious and restless, fond of novelty and of argument, hard-working when duty called but extravagant in pleasure and mean in charity. He admired their cleanliness, their love of learning and their newspapers, and he judged French women well treated though, in his view, not always faithful.","approx","Louca's summary of the Takhlis; Newman translation.")
e("1829","1826–1830","range","tahtawi","Paris","'Christians in name only'",
 "Tahtawi wrote that most of the French were Christians only by name and set reason above revelation. When Silvestre de Sacy read the manuscript he marked this judgement as one to be revised.","approx","Institut du monde arabe dossier, quoting de Sacy's annotation.")
e("1830","1830 (1245–1246 AH)","year","tahtawi","Paris","Translating the Charter of 1814",
 "Tahtawi translated the French constitutional Charter article by article and commented on it. He explained the French idea of liberty through the Islamic terms 'adl (justice) and insaf (equity): rule by laws equal for all, so that no ruler can oppress. He noted that much of the Charter could not be found in Islamic sources yet judged it worth knowing.","verified","Takhlis, Newman trans. p. 208 and note, as discussed by Muench (WPSA paper); Newman, Chronos 6 (2002).")
e("1830-07-24","Saturday 24 July 1830","day","berlioz","Institut de France, quai Conti","Shut in for the Prix de Rome",
 "Writing to his friend Ferrand, Berlioz said he was confined in the Institut for the competition and was orchestrating the last air of his cantata Sardanapale. He needed the prize, he said, to win the marriage he hoped for.","verified","Lettres intimes, no. XXVII, dated 24 July 1830.")
e("1830-07","Late July 1830","range","apponyi","Dieppe","News from Paris reaches the seaside",
 "Apponyi was at Dieppe when the first reports of the ordinances and the fighting arrived from Paris, so his diary of the three days is a diary of rumour and waiting.","approx","Revue des Deux Mondes extracts, part II (context given for part I).")
e("1830-07-27","27–29 July 1830 (6–8 Safar 1246 AH)","range","tahtawi","Paris","Three days that unseated a king",
 "Tahtawi wrote a separate account of the revolution. He divided the French into royalists, mostly priests and their followers, and liberals, who included most scholars and the greater part of the people. He blamed Charles X for breaking the Charter's guarantees of free speech and press, and called his chief minister Polignac unjust.","verified","Takhlis, Newman trans. pp. 306–309, as summarised by Muench (WPSA).")
e("1830-07-29","Thursday 29 July 1830","day","berlioz","Institut de France","Finishing a score under gunfire",
 "Berlioz recalled completing his cantata while bullets struck the Institut's walls, then going out into the streets with a pistol once he was released. The recollection comes from his memoirs, written years later.","approx","Mémoires (written 1848–65); confirmed in outline by his letter of 23 Aug 1830.")
e("1830-08","August 1830 (Rabi' I 1246 AH)","month","tahtawi","Paris","A hadith for a fallen king, and the word 'republic'",
 "To explain why the French were right to resist, Tahtawi cited a saying that whoever draws the sword of injustice will be struck by the sword of defeat. He compared a representative republic to the rule of the shaykh Hammam in eighteenth-century Upper Egypt, using jumhuriyya in what Newman identifies as its first modern Arabic sense.","verified","Takhlis, Newman trans. pp. 306–309 and note 3, p. 307, via Muench (WPSA). Month of writing approximate.")
e("1830-08-23","Monday 23 August 1830","day","berlioz","Paris","Prize won, cannon remembered",
 "Berlioz told Ferrand he had won the Grand Prix unanimously and that the sound of the revolution's guns had helped his final number. He asked his friend to stop writing to him about politics.","verified","Lettres intimes, no. XXVIII, dated 23 Aug 1830.")
e("1830-09-01","Wednesday 1 September 1830","day","apponyi","Paris","Bullet marks and the tricolour",
 "Back in Paris, Apponyi found buildings scarred by bullets, trees felled for barricades and the monument at the Place Louis XVI draped in the revolutionary flag. The city felt tense and watchful.","verified","Apponyi journal, 1 Sept 1830, Revue des Deux Mondes extracts II.")
e("1830-09-07","Tuesday 7 September 1830","day","apponyi","Paris","Patriotic plays and collections for the dead",
 "Theatres were staging patriotic pieces and ending performances with collections for the victims of the July days, Apponyi noted with a conservative's unease.","verified","Apponyi journal, 7 Sept 1830.")
e("1830-12-21","15–21 December 1830 (Rajab 1246 AH)","range","tahtawi","Paris, Chamber of Peers","The trial of Charles X's ministers",
 "Tahtawi followed the trial of Polignac and the other ministers before the Chamber of Peers and described it for Egyptian readers as an example of rulers' servants answering to law.","approx","Newman, Chronos 6 (2002), on the Takhlis's account of the trial; dates of the trial from Apponyi.")
e("1830-12-21","19–23 December 1830","range","apponyi","Paris, around the Luxembourg","Paris like an armed camp",
 "During the ministers' trial Apponyi described troops ringing the Luxembourg Palace, the prisoners moved to Vincennes, and Louis-Philippe riding through the crowds to a triumphant reception. The fear was of a massacre of the ministers, not of a new revolution.","verified","Apponyi journal, 19–23 Dec 1830.")
e("1830-10","Late 1830 or early 1831 (sources differ)","range","tahtawi","Paris","The final examination",
 "Tahtawi sat a final examination before Jomard and Paris orientalists, presenting the translations he had made in Paris, among them works on history, geography, mineralogy and the Charter. The report was published in the Revue encyclopédique, and he printed the examiners' verdict in his book.","approx","Silvera (1980) n. 72 (Revue encyclopédique XLVIII); Louca. Exact day not found.")
e("1831-02-14","14–16 February 1831","range","apponyi","Paris","Riots at Saint-Germain-l'Auxerrois",
 "A memorial service for the Duc de Berry set off riots in which the church of Saint-Germain-l'Auxerrois and the archbishop's palace were sacked. Apponyi recorded the damage, and went to a ball at the Rothschilds' the same night.","verified","Apponyi journal, 14–16 Feb 1831.")
e("1831","Early 1831","range","tahtawi","Paris to Alexandria","Going home",
 "Tahtawi left Paris in 1831 with his translations and his manuscript. Six of his fellow students had already been recalled soon after the revolution broke out.","approx","Silvera (1980); Louca. Departure day not found.")
e("1831","1831 (1246–1247 AH)","year","muhammad-ali","Cairo","An appointment for the returned imam",
 "A document of 1831 records Tahtawi's appointment in Muhammad Ali's service on his return; his first post was as a translator in the new state schools, beginning with the medical school at Abu Za'bal.","approx","Document appointing Rifa'a al-Tahtawi (1831), reproduced in a Routledge open-access volume; post as given in standard biographies.")
e("1831-08-16","Tuesday 16 August 1831 (7 Rabi' I 1247 AH)","day","tahtawi","Cairo","A letter to Jomard from Cairo",
 "Writing from Cairo to his old headmaster, Tahtawi reported on his return and his work, keeping open the line to Paris that would bring French books and advice to his later schools.","verified","Letter dated 'Kaire, le 16 août 1831', cited by Louca.")
e("1833-06","June 1833","month","caussin","Paris","Introducing the book to Europe",
 "Caussin de Perceval published in the Nouveau Journal asiatique a long account of Tahtawi's 'Relation d'un voyage en France', a year before the Arabic edition appeared. He presented it as a rare view of France through Muslim eyes.","verified","Nouveau Journal asiatique XI (June 1833), cited Silvera (1980) n. 43 and TDV.")
e("1831","1831 (before publication)","range","caussin","Paris","A teacher's letter on the manuscript",
 "Caussin wrote an assessment of the manuscript praising its accuracy and its plain style, which Tahtawi translated and printed in the book as testimony from a French expert.","approx","Letter printed in the Takhlis (Newman trans.).")
e("1831","1831 (before publication)","range","desacy","Paris","De Sacy's verdict on the manuscript",
 "De Sacy praised the account as faithful and useful, while flagging a few judgements, such as that the French were Christians only in name, as needing revision. Tahtawi printed his letter in Arabic translation.","approx","Letter printed in the Takhlis; annotation quoted in the IMA dossier.")
e("1834","1834 (1250 AH)","year","attar","Bulaq, Cairo","A preface from the Shaykh al-Azhar",
 "The Takhlis was printed at the government press at Bulaq with a preface by al-'Attar, by now head of al-Azhar, endorsing a Muslim scholar's study of a Christian country's sciences and laws.","verified","Louca; TDV (Bulaq 1250 AH).")
e("1834","1834 (1250 AH)","year","tahtawi","Bulaq, Cairo","'The Extraction of Gold' is printed",
 "Takhlis al-ibriz fi talkhis Bariz came off the government press at Bulaq, the first printed Arabic book-length description of a modern European capital. It was reprinted in 1848–49 and again in 1905.","verified","Louca; TDV; Newman.")

claims=[
 dict(date_iso="1826-05",date_display="May 1826",eye="press",claim="Hosts: a liberal review defends the students against the charge that they serve the pasha's war on the Greeks",form="newspaper",evidence="Revue encyclopédique, May 1826 (Silvera n. 42)",confidence="approx"),
 dict(date_iso="1826-05-15",date_display="15 May 1826",eye="tahtawi",claim="Traveller: quarantine is a lawful precaution, not a denial of divine decree",form="travel journal",evidence="Takhlis (Louca; Newman)",confidence="verified"),
 dict(date_iso="1826-08-13",date_display="13 August 1826",eye="press",claim="Hosts: the official press presents the Égyptiens as a French civilising project",form="newspaper",evidence="Moniteur universel 13 Aug 1826 (Silvera n. 58)",confidence="approx"),
 dict(date_iso="1827",date_display="1827",eye="press",claim="Hosts: satire casts the students as comic figures of the pasha's politics",form="poem",evidence="Barthélemy and Méry, La Bacriade (Silvera n. 62)",confidence="approx"),
 dict(date_iso="1827-07-09",date_display="9 July 1827",eye="geoffroy",claim="Hosts: the giraffe's Egyptian and Sudanese keepers become part of the spectacle in prints and crowds",form="other",evidence="Thiébault and Prévost prints, 1827 (Hyperallergic)",confidence="verified"),
 dict(date_iso="1827-07",date_display="July 1827",eye="jomard",claim="Hosts: the students' French is judged too weak; they must be dispersed among French families",form="embassy report",evidence="Silvera (1980)",confidence="approx"),
 dict(date_iso="1828-08",date_display="August 1828",eye="jomard",claim="Hosts: the school is a success that proves Egyptians can master European science",form="other",evidence="Nouveau Journal asiatique II (1828), pp. 96–116",confidence="verified"),
 dict(date_iso="1829",date_display="1826–1830",eye="tahtawi",claim="Traveller: Parisians are clever, curious and clean but restless, extravagant and mean in charity",form="travel journal",evidence="Takhlis (Louca summary)",confidence="verified"),
 dict(date_iso="1829",date_display="1826–1830",eye="tahtawi",claim="Traveller: most French are Christians in name only and trust reason over revelation",form="travel journal",evidence="Takhlis; IMA dossier",confidence="verified"),
 dict(date_iso="1830",date_display="1830",eye="tahtawi",claim="Traveller: French 'liberty' is what Muslims call justice and equity",form="travel journal",evidence="Takhlis, Newman trans. p. 208",confidence="verified"),
 dict(date_iso="1830-07-27",date_display="27–29 July 1830",eye="tahtawi",claim="Traveller: the king fell because he broke the Charter's guarantee of a free press",form="travel journal",evidence="Takhlis, Newman trans. pp. 306–309",confidence="verified"),
 dict(date_iso="1830-09-07",date_display="7 September 1830",eye="apponyi",claim="Hosts (a conservative's view): Paris celebrates the revolution in theatres and collections",form="diary",evidence="Apponyi journal, Revue des Deux Mondes extracts",confidence="verified"),
 dict(date_iso="1830-12-21",date_display="December 1830",eye="tahtawi",claim="Traveller: even a king's ministers stand trial under French law",form="travel journal",evidence="Takhlis (Newman, Chronos 2002)",confidence="approx"),
 dict(date_iso="1831",date_display="1831",eye="desacy",claim="Hosts: the account is faithful, but its verdict on French religion should be revised",form="letter",evidence="De Sacy's letter/annotation (Takhlis; IMA dossier)",confidence="approx"),
 dict(date_iso="1833-06",date_display="June 1833",eye="caussin",claim="Hosts: a rare and valuable view of France through Muslim eyes",form="other",evidence="Nouveau Journal asiatique XI (1833)",confidence="approx"),
]

conv=[
 dict(date="1826-05-15",label="Landing at Marseilles",eyes=["tahtawi","press","drovetti"],note="Tahtawi records the quarantine and his first French city; the Paris press argues over whether the students are pupils or the pasha's agents; Drovetti's lobbying had put them on a French ship."),
 dict(date="1826-08-13",label="The Égyptiens arrive in Paris",eyes=["tahtawi","jomard","press"],note="Tahtawi begins describing Paris as a geographer describes a country; Jomard organises and publicises; the Moniteur announces them and satirists take note."),
 dict(date="1827-07-09",label="Summer 1827: giraffe and examination",eyes=["geoffroy","press","jomard","muhammad-ali"],note="The pasha's giraffe reaches Paris and the king while Jomard's students fail their first examination; Paris is more interested in the animal and its keepers than in the scholars."),
 dict(date="1828-02-28",label="The public examination of 1828",eyes=["jomard","press"],note="Jomard stages the examination with British observers present and the Moniteur advertises his disinterest; the students' own voices are absent."),
 dict(date="1830-07-27",label="The three days of July",eyes=["tahtawi","berlioz","apponyi"],note="Tahtawi analyses the revolution as a lesson in law and justice; Berlioz is locked in the Institut finishing a cantata; Apponyi waits for news in Dieppe."),
 dict(date="1830-12-21",label="The ministers on trial",eyes=["tahtawi","apponyi"],note="Tahtawi presents the trial as rulers answerable to law; Apponyi sees troops, fear and the new king courting the crowd."),
 dict(date="1831-08-16",label="Return and appointment",eyes=["tahtawi","muhammad-ali","jomard"],note="Tahtawi writes to Jomard from Cairo as the pasha places him in state service; the Paris link continues by letter."),
 dict(date="1834",label="The book appears",eyes=["tahtawi","attar","caussin","desacy"],note="Caussin introduces the account in Paris in 1833; al-'Attar's preface and the French scholars' letters frame the 1834 Bulaq edition, so hosts and teacher speak inside the traveller's book."),
]

ties=[
 dict(a="tahtawi",b="jomard",kind="met",note="Jomard directed Tahtawi's studies, suggested translations and examined him; Tahtawi wrote to him from Cairo in 1831."),
 dict(a="tahtawi",b="desacy",kind="read each other",note="De Sacy read and annotated the manuscript; Tahtawi printed his letter in the book."),
 dict(a="tahtawi",b="caussin",kind="met",note="Caussin taught and befriended Tahtawi, wrote on the manuscript and published the first European account of it."),
 dict(a="tahtawi",b="attar",kind="influenced",note="Al-'Attar chose him as imam, asked him to record France, and wrote the preface."),
 dict(a="tahtawi",b="muhammad-ali",kind="mentioned",note="The pasha sent and paid the mission, and Tahtawi's book praised his reforms and was printed at his government press."),
 dict(a="drovetti",b="jomard",kind="influenced",note="Drovetti's lobbying for Paris put the students in Jomard's hands; both were veterans of the French presence in Egypt."),
 dict(a="drovetti",b="geoffroy",kind="mentioned",note="Drovetti arranged the giraffe's journey; his servant Atir walked with Geoffroy to Paris."),
 dict(a="muhammad-ali",b="geoffroy",kind="influenced",note="The pasha's diplomatic gift became Geoffroy's charge and the Muséum's star."),
 dict(a="jomard",b="press",kind="influenced",note="Jomard supplied notices to the Moniteur and other papers about the school."),
 dict(a="tahtawi",b="apponyi",kind="same street",note="Both lived through post-revolution Paris and the ministers' trial; Tahtawi wrote as a liberal admirer of the Charter, Apponyi as a conservative diplomat."),
 dict(a="tahtawi",b="berlioz",kind="same street",note="Both were young men in Paris during the July days, one writing of law and kingship, the other of music and gunfire."),
 dict(a="desacy",b="caussin",kind="met",note="Colleagues at the École des langues orientales who both read Tahtawi's manuscript."),
]

threads=[
 dict(to="v1:french-rev",note="Jomard and Geoffroy Saint-Hilaire were savants of Bonaparte's 1798 expedition to Egypt, a product of the revolutionary era; the Charter Tahtawi translated was the Restoration's settlement of the Revolution's legacy."),
 dict(to="mehmed-1720",note="A century before Tahtawi, Yirmisekiz Mehmed Çelebi wrote an Ottoman embassy report on Paris; together the two texts bracket the early Muslim literature describing France for rulers at home."),
 dict(to="abutaleb-1799",note="Mirza Abu Taleb Khan's account of Britain (1799–1803) and Tahtawi's of France are two of the first works explaining European parliaments and laws to Muslim readers."),
 dict(to="v9:cholera-1832",note="Tahtawi's first post was at the Abu Za'bal medical school founded by Clot Bey, whose group of Egyptian medical students reached Marseilles in 1832, the year cholera swept Paris."),
]

images=[
 dict(url=HYP,title="A female giraffe led by two men in oriental dress",caption="Lithograph after André Prévost, 1827 (Wellcome Collection), reproduced in this article with other giraffe prints, including Thiébault's scene of the presentation at Saint-Cloud on 9 July 1827. The two men are the keepers, unnamed in the print.",date="1827",credit="André Prévost (after); Wellcome Collection; via Hyperallergic"),
 dict(url="https://standardebooks.org/artworks/eugene-delacroix/liberty-leading-the-people",title="Liberty Leading the People",caption="Delacroix's painting of the July days, finished late in 1830 and shown at the Salon of 1831; a Parisian image of the revolution Tahtawi described in Arabic.",date="1830",credit="Eugène Delacroix; Musée du Louvre"),
 dict(url="https://www.taylorfrancis.com/chapters/oa-edit/10.4324/9781003247784-31/document-appointing-rifa-al-%E1%B9%AFah%E1%B9%AFawi-1831-mu%E1%BA%96ammad-ali-pasha",title="Document appointing Rifa'a al-Tahtawi (1831)",caption="An official document of 1831 from Muhammad Ali's administration recording Tahtawi's appointment after his return, reproduced in an open-access Routledge volume.",date="1831",credit="Reproduced in a Routledge open-access volume"),
]

further=[
 dict(title="Alain Silvera, 'The First Egyptian Student Mission to France under Muhammad Ali' (1980)",url=SIL),
 dict(title="Daniel L. Newman, 'Myths and Realities in Muslim Alterist Discourse' (Chronos 6, 2002)",url=NEWC),
 dict(title="An Imam in Paris: Al-Tahtawi's Visit to France 1826–1831, trans. D. L. Newman",url=SAQI),
 dict(title="Anouar Louca on Rifa'a al-Tahtawi (Hi-Trade, Venice)",url=LOU),
 dict(title="Apponyi, 'Autour de la Révolution de 1830' (Revue des Deux Mondes extracts)",url=APP),
 dict(title="Berlioz, Lettres intimes (Project Gutenberg)",url=BER),
 dict(title="Institut du monde arabe, 'Au miroir de l'autre' teaching dossier",url=IMA),
]

ch=dict(id="tahtawi-1826",title="The Imam and the Charter: Egyptian Students in Paris",short_title="Tahtawi in Paris",
 subtitle="Muhammad Ali's student mission to France and the July Revolution, 1826–1834",span="1826–1834",
 intro=[
 "On 13 April 1826 forty-four young men sailed from Alexandria on a French warship, sent by Muhammad Ali, the Ottoman governor of Egypt, to learn the sciences of the French. With them, as their imam, went a 25-year-old Azhar scholar, Rifa'a Rafi' al-Tahtawi. He was not meant to study. He did anyway, and his book about Paris, Takhlis al-ibriz fi talkhis Bariz ('The Extraction of Gold, or a Summary of Paris'), printed at Bulaq in 1834, became the founding Arabic text on modern Europe.",
 "The students reached Paris in the summer of 1826 and were placed under Edme-François Jomard, a veteran of Bonaparte's Egyptian expedition. They studied, sat public examinations, entered French schools and arsenals, and were written up in the official Moniteur, in liberal reviews and in satire. In the summer of 1827 the pasha's other envoy, a giraffe walked from Marseilles by Étienne Geoffroy Saint-Hilaire, outshone them all. Her keepers, Atir and Hassan, were drawn, stared at and paid, but left no account of their own.",
 "In July 1830 Tahtawi saw a French king overthrown in three days. He wrote a chapter on it and translated the Charter of 1814 whose breach had caused it, explaining French liberty through Islamic ideas of justice and equity, and reaching for an Upper Egyptian precedent to explain a republic. On the same days a young Berlioz was locked in the Institut writing a cantata, and an Austrian diplomat, Rodolphe Apponyi, was waiting in Dieppe for news.",
 "The record is uneven. Tahtawi's book is not a day-by-day diary but a topical account written up from notes and finished after his return, so most of its dates are those of the events it describes. The hosts' side is known through Jomard's printed reports, newspaper notices cited by historians, the letters of de Sacy and Caussin de Perceval printed in the Takhlis itself, and diaries and letters of Parisians who never mention the Egyptians at all. That silence is part of the picture: the students were news in 1826–28 and almost invisible by 1830.",
 "Read together, these sources show a two-way examination. Jomard and the orientalists judged the students' French and the accuracy of Tahtawi's account; Tahtawi judged French cleanliness, religion, women, newspapers and law, and his French readers in turn corrected some of his judgements before the book was printed."],
 calendar_note="Tahtawi's book and Egyptian official documents date events by the Islamic (Hijri) lunar calendar. Gregorian dates are given in date_iso; Hijri equivalents in date_display are computed with the standard tabular calendar and may differ by a day from dates fixed by observation of the new moon. Key conversions: 13 April 1826 = 5 Ramadan 1241; 15 May 1826 = 7 Shawwal 1241; 27–29 July 1830 = 6–8 Safar 1246; 16 August 1831 = 7 Rabi' I 1247. The year 1250 AH, in which the Takhlis was printed, ran from about 10 May 1834 to late April 1835.",
 eyes=eyes,entries=sorted(E,key=lambda x:x["date_iso"]),claims=sorted(claims,key=lambda x:x["date_iso"]),
 convergences=conv,ties=ties,threads_out=threads,images=images,further=further,
 vantage_key="0 = the traveller himself; 1 = Parisians on the spot with the students or in the July fighting; 2 = Paris observers, scholars and press; 3 = patrons and agents in Egypt; 4 = Cairo teachers at a distance.")
json.dump(ch,open(OUT,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(len(eyes),len(E),len(claims),len(conv),len(ties))
