import json
OUT = "/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/vol2/ch-black-death.json"

W = "https://en.wikipedia.org/wiki/"
HORROX = {"title": "R. Horrox (ed. & trans.), The Black Death (Manchester UP, 1994) — listed by Princeton 'Middle Ages for Educators'", "url": "https://middleagesforeducators.princeton.edu/node/226/"}

eyes = [
 {"id":"kantakouzenos","short":"Kantakouzenos","name":"John VI Kantakouzenos","life":"c. 1292–1383",
  "role":"Byzantine emperor, newly master of Constantinople after winning the civil war of 1341–47; later a monk and historian",
  "side":"Byzantine Empire (Orthodox Christian)","where":"Constantinople, 1347","lat":41.0082,"lon":28.9784,
  "vantage":0,"vantage_label":"ruler and bereaved father in the first great city struck",
  "form":"memoir (written later)","language":"Byzantine Greek",
  "authenticity":"His Histories were composed after his abdication (1354), as the monk Ioasaph. The plague chapter deliberately borrows phrases from Thucydides' plague of Athens, but T. S. Miller (1976) shows that the clinical detail is his own and largely accurate.",
  "bio":"The emperor who had just fought his way into the capital watched the sickness arrive from the Black Sea and lost his youngest son, Andronikos, in its first days. His account is literary, classicising and personal at once — the earliest major description of the pandemic from inside a Christian capital.",
  "sources":[{"title":"T. S. Miller, 'The Plague in John VI Cantacuzenus and Thucydides', GRBS (1976)","url":"https://grbs.library.duke.edu/index.php/grbs/article/download/7991/4821/14675"},
             {"title":"M. Goodyear, 'When Death Docked in Constantinople', The Medieval Magazine (2020)","url":"https://www.themedievalmagazine.com/past-issue-features/2020/8/5/when-death-docked-in-constantinople-by-michael-goodyear"},
             {"title":"John VI Kantakouzenos (Wikipedia)","url":W+"John_VI_Kantakouzenos"}]},
 {"id":"demussi","short":"de' Mussi","name":"Gabriele de' Mussi","life":"c. 1280–c. 1356",
  "role":"Notary of Piacenza in northern Italy, in his sixties",
  "side":"Latin Christendom (Piacenza, Lombardy)","where":"Piacenza — not, it now seems, at Caffa","lat":45.0526,"lon":9.693,
  "vantage":2,"vantage_label":"at home in Italy, retelling the Black Sea story at second hand",
  "form":"chronicle","language":"Latin",
  "authenticity":"Historia de morbo, written c. 1348–49, survives in a single manuscript at the University of Wrocław library (R 262). Older writers thought he sailed home from Caffa with the plague; modern scholars (Wheelis 2002 and others) conclude he probably never left Piacenza, so his siege story is hearsay. Treat the Caffa episode as a flagged tradition.",
  "bio":"A provincial lawyer who wanted to explain where the catastrophe came from. His dramatic tale of the Mongol army hurling its own dead into besieged Caffa is the most famous origin story of the Black Death — and among the least securely witnessed.",
  "sources":[{"title":"M. Wheelis, 'Biological Warfare at the 1346 Siege of Caffa', Emerging Infectious Diseases 8:9 (2002), via Medievalists.net","url":"https://www.medievalists.net/2012/08/15/biological-warfare-at-the-1346-siege-of-caffa/"},
             {"title":"Gabriel de Mussis (Wikipedia)","url":W+"Gabriel_de_Mussis"}, HORROX]},
 {"id":"heyligen","short":"Heyligen","name":"Louis Heyligen (Ludovicus Sanctus, Petrarch's 'Socrates')","life":"1304–1361",
  "role":"Flemish Benedictine musician and cantor, in the household of Cardinal Giovanni Colonna at the papal court",
  "side":"Latin Christendom (Flemish cleric at the papal court)","where":"Avignon","lat":43.9493,"lon":4.8055,
  "vantage":1,"vantage_label":"eyewitness inside the papal city",
  "form":"dated letters","language":"Latin",
  "authenticity":"His letter of 27 April 1348 to the chapter of St Donatian's, Bruges, survives only partially, copied into a Flemish chronicle; edited by A. Welkenhuysen (1988) and translated in Horrox (1994), pp. 41–45.",
  "bio":"A cathedral cantor from Bruges living in Avignon, close friend of Petrarch. Writing home three months into the epidemic, he sends the most immediate surviving eyewitness report from the papal city — numbers, rumours, and the pope's improvisations.",
  "sources":[{"title":"Lodewijk Heyligen (Wikipedia; cites Welkenhuysen 1988)","url":W+"Lodewijk_Heyligen"}, HORROX]},
 {"id":"chauliac","short":"Guy de Chauliac","name":"Guy de Chauliac","life":"c. 1300–1368",
  "role":"Physician and surgeon to Pope Clement VI, about 48",
  "side":"Latin Christendom (papal court)","where":"Avignon, at the pope's side","lat":43.9493,"lon":4.8055,
  "vantage":0,"vantage_label":"physician who treated the sick and caught the disease himself",
  "form":"memoir (written later)","language":"Latin",
  "authenticity":"His plague account forms part of the Chirurgia magna (Inventarium), completed at Avignon in 1363 (some give 1353) — a retrospective medical record, not a diary.",
  "bio":"The most famous surgeon of his age, who stayed in Avignon when many doctors fled. Fifteen years later he set down a clinically precise description of two distinct forms of the disease, admitted his profession's helplessness, and recorded his own illness and recovery.",
  "sources":[{"title":"Guy de Chauliac (Wikipedia)","url":W+"Guy_de_Chauliac"},
             {"title":"Northeastern Pandemic Teaching Initiative: Guy de Chauliac excerpt (PDF)","url":"https://cssh.northeastern.edu/pandemic-teaching-initiative/wp-content/uploads/sites/43/2020/10/guy-de-chauliac-1.pdf"}]},
 {"id":"clement","short":"Clement VI","name":"Pope Clement VI (Pierre Roger)","life":"1291–1352",
  "role":"Pope at Avignon, 1342–52",
  "side":"Latin Christendom (papacy)","where":"Avignon","lat":43.9493,"lon":4.8055,
  "vantage":1,"vantage_label":"head of the Western Church, issuing decrees from the stricken city",
  "form":"papal bulls (administrative documents)","language":"Latin",
  "authenticity":"Two bulls on the Jews, of 6 July and 26 September 1348 (Sicut Judaeis reissued; Quamvis perfidiam), edited in S. Simonsohn, The Apostolic See and the Jews (1991). One modern textbook misdates the first to 1349.",
  "bio":"Not a diarist but a voice that must be heard: the pope, sitting between fires on his doctor's advice, used his authority to say in writing that the Jews were not poisoning Christendom. His documents record what the Church's highest office saw and tried — and failed — to stop.",
  "sources":[{"title":"Persecution of Jews during the Black Death (Wikipedia; cites Simonsohn 1991)","url":W+"Persecution_of_Jews_during_the_Black_Death"}]},
 {"id":"petrarch","short":"Petrarch","name":"Francesco Petrarca (Petrarch)","life":"1304–1374",
  "role":"Poet and scholar, 43, living in northern Italy under the patronage of the Colonna and the lords of Parma",
  "side":"Latin Christendom (Tuscan exile, Avignon circle)","where":"Verona and Parma, 1348–49","lat":44.8015,"lon":10.3279,
  "waypoints":[{"lat":45.4384,"lon":10.9916,"label":"Verona — news of Laura, May 1348"},{"lat":44.8015,"lon":10.3279,"label":"Parma, 1348–49"}],
  "vantage":2,"vantage_label":"in Italy, losing beloved and friends in Avignon by letter",
  "form":"dated letters","language":"Latin (letters, book note); Italian (sonnets)",
  "authenticity":"The note on Laura's death is in his own hand on a leaf of his Virgil (Biblioteca Ambrosiana, Milan, S.P. 10/27). The Familiares letters were later revised by Petrarch for a collected edition, so wording and dates may have been polished.",
  "bio":"Europe's most celebrated poet lost Laura, his patron Cardinal Colonna and a string of friends within months. His private note and letters turn grief into a question for the future: will anyone believe what we lived through?",
  "sources":[{"title":"Brown University Decameron Web: Petrarch and the plague","url":"https://webhelper.brown.edu/decameron/plague/perspectives/petrarca.php"},
             {"title":"Ambrosian Virgil of Francesco Petrarca (facsimile description)","url":"https://www.facsimiles.com/facsimiles/ambrosian-virgil-of-francesco-petrarca"}]},
 {"id":"boccaccio","short":"Boccaccio","name":"Giovanni Boccaccio","life":"1313–1375",
  "role":"Florentine writer, about 35, son of a merchant-banker",
  "side":"Latin Christendom (Florence)","where":"Florence, 1348","lat":43.7696,"lon":11.2558,
  "vantage":1,"vantage_label":"inside the city (literary frame)",
  "form":"memoir (written later)","language":"Italian (Tuscan)",
  "authenticity":"FLAG — LITERARY: the description is the introduction to the Decameron, composed c. 1349–53 as the frame for fiction. Historians treat its plague passage as a genuine eyewitness description, but its rhetoric owes much to classical models, and its numbers (100,000 dead) are inflated.",
  "bio":"Boccaccio was in Florence during the plague (his father died in 1349). Before his storytellers leave the city he gives a steady, harrowing account of symptoms, flight, abandonment and mass burial — the most read description of the Black Death ever written.",
  "sources":[{"title":"Macmillan, Viewpoints 14.2: Italian and English Views of the Plague (Boccaccio and Knighton excerpts)","url":"https://digfir-published.macmillanusa.com/mckayworld10e/mckayworld10e_ch14_33.html"},
             {"title":"Oregon State OER, 'The Black Death' (contemporary Florentine chronicle, Stefani)","url":"https://open.oregonstate.education/middleearlymodernages/chapter/black-death/"}]},
 {"id":"agnolo","short":"Agnolo di Tura","name":"Agnolo di Tura del Grasso","life":"fl. 1340s–1350s",
  "role":"Sienese shoemaker and tax collector who kept the city's chronicle",
  "side":"Latin Christendom (Siena)","where":"Siena","lat":43.3188,"lon":11.3308,
  "vantage":0,"vantage_label":"direct victim — lost wife and children",
  "form":"chronicle","language":"Italian (Sienese)",
  "authenticity":"His continuation of the Cronaca senese (covering 1329–51) is printed in Rerum Italicarum Scriptores; the plague passage is widely excerpted in translation. A chronicle with first-person passages, written close to events.",
  "bio":"An artisan, not a cleric, he set down the plague's arrival in May 1348 and then, in the middle of the city's record, his own loss. His line about burying his children is the single most quoted sentence of the whole pandemic.",
  "sources":[{"title":"Agnolo di Tura (Wikipedia)","url":W+"Agnolo_di_Tura"},
             {"title":"Macmillan, 'A Town Chronicler Describes the Black Death' (excerpt)","url":"https://digfir-published.macmillanusa.com/mckaywest11e/mckaywest11e_ch11_48.html"}]},
 {"id":"closener","short":"Closener","name":"Fritsche (Friedrich) Closener","life":"d. after 1372 (date uncertain)",
  "role":"Priest of Strasbourg Cathedral, custodian of its Lady altar since 1343",
  "side":"Latin Christendom (Free City of Strasbourg)","where":"Strasbourg","lat":48.5734,"lon":7.7521,
  "vantage":2,"vantage_label":"cleric in the city where the Jews were killed",
  "form":"chronicle","language":"German (Alsatian; early vernacular city chronicle)",
  "authenticity":"FLAG: his German chronicle was completed on 8 July 1362. The dated 1349 details here are known through Jacob Twinger von Königshofen's later chronicle (translated in J. R. Marcus, 1938), which drew on Closener, probably an eyewitness; Closener's own wording was not checked for this chapter.",
  "bio":"A cathedral priest who stayed in Strasbourg through the winter of 1348–49, when guild politics and poisoning rumours ended in the burning of the city's Jews. His chronicle is the root of the Strasbourg record; it is included here because Strasbourg must be seen, soberly, from inside.",
  "sources":[{"title":"Fritsche Closener (Wikipedia)","url":W+"Fritsche_Closener"},
             {"title":"Internet Medieval Sourcebook: The Black Death and the Jews 1348–1349 (Königshofen, after Closener)","url":"https://sourcebooks.web.fordham.edu/jewish/1348-jewsblackdeath.asp"}]},
 {"id":"clyn","short":"John Clyn","name":"Friar John Clyn","life":"c. 1286–c. 1349",
  "role":"Franciscan friar, former guardian of Carrick friary, now in the Kilkenny convent",
  "side":"Anglo-Irish Latin Christendom (Kilkenny)","where":"Kilkenny, Ireland","lat":52.6541,"lon":-7.2448,
  "vantage":0,"vantage_label":"writing inside a dying community, probably among its victims",
  "form":"chronicle","language":"Latin",
  "authenticity":"The Annals of Ireland, ed. R. Butler (Irish Archaeological Society, 1849); English translation by B. Williams (2007). The last entry is after 17 June 1349; a later copyist added that the author seems to have died here.",
  "bio":"A friar annalist who realised as he wrote that he might be the last. He left blank parchment for anyone who survived to carry the record on — one of the most moving acts of the plague years.",
  "sources":[{"title":"John Clyn (Wikipedia)","url":W+"John_Clyn"},
             {"title":"Catholic Encyclopedia: John Clynn","url":"https://www.catholic.com/encyclopedia/john-clynn"},
             {"title":"1348 — the Black Death arrives in Ireland (Coles Lane)","url":"https://coleslane.com/1348---the-black-death-arrives-in-ireland"}]},
 {"id":"knighton","short":"Knighton","name":"Henry Knighton","life":"d. c. 1396",
  "role":"Augustinian canon of St Mary's Abbey (St Mary de Pratis), Leicester",
  "side":"England (Latin Christendom)","where":"Leicester","lat":52.6369,"lon":-1.1398,
  "vantage":2,"vantage_label":"local chronicler, writing decades after",
  "form":"chronicle","language":"Latin",
  "authenticity":"FLAG: the Chronicon was written c. 1378–96, a generation after the plague; its local figures (Leicester parishes, sheep) are valuable but retrospective.",
  "bio":"A monastic chronicler who cared about prices, wages and livestock as well as souls. His plague pages show the economic shock — cheap horses, rotting sheep, unharvested fields, labourers suddenly able to name their price.",
  "sources":[{"title":"M. Carlin, 'The Black Death in the British Isles' (UW–Milwaukee source collection)","url":"https://sites.uwm.edu/carlin/?p=887"},
             {"title":"Henry Knighton (Wikipedia)","url":W+"Henry_Knighton"}]},
 {"id":"ibn-al-wardi","short":"Ibn al-Wardi","name":"Zayn al-Din 'Umar ibn al-Wardi","life":"1291/92–1349",
  "role":"Syrian jurist, deputy judge and poet, about 57",
  "side":"Mamluk Sultanate (Sunni Muslim, Syria)","where":"Aleppo","lat":36.2021,"lon":37.1343,
  "vantage":0,"vantage_label":"victim — wrote of the plague, then died of it",
  "form":"treatise (risala) with dated observations","language":"Arabic (rhymed prose and verse)",
  "authenticity":"Risalat al-naba' 'an al-waba' ('An Essay on the Report of the Pestilence'), translated in prose by Michael Dols (1974). Contemporaneous; ends shortly before his death on 27 Dhu al-Hijja 749 / 18 March 1349. Not to be confused with a later geographer of the same name.",
  "bio":"A learned poet of Aleppo who traced the plague's path across Asia in ornate rhymed prose, answered it with prayer, irony and hope of martyrdom, and was himself carried off before the epidemic ended. His is the clearest Islamic voice from inside a stricken city.",
  "sources":[{"title":"Ibn al-Wardi (Wikipedia)","url":W+"Ibn_al-Wardi"},
             {"title":"Lapham's Quarterly: Ibn al-Wardi","url":"https://www.laphamsquarterly.org/node/10669"},
             {"title":"University of Chicago Mamluk bibliography entry","url":"https://mamluk.lib.uchicago.edu/fullview1.php?id=33174"}]},
 {"id":"ibn-battuta","short":"Ibn Battuta","name":"Abu 'Abdallah Muhammad ibn Battuta","life":"1304–1368/69",
  "role":"Moroccan jurist and traveller, 44, heading home after 24 years abroad",
  "side":"Islamic world (Maliki Muslim from Tangier, travelling in Mamluk lands)","where":"Syria, Palestine and Egypt, 1348; Maghreb 1349","lat":33.5138,"lon":36.2765,
  "waypoints":[{"lat":36.2021,"lon":37.1343,"label":"Aleppo, June 1348"},{"lat":33.5138,"lon":36.2765,"label":"Damascus, July 1348"},{"lat":30.0444,"lon":31.2357,"label":"Egypt, autumn 1348"},{"lat":34.0181,"lon":-5.0078,"label":"Fez, Nov 1349"}],
  "vantage":1,"vantage_label":"traveller moving through the epidemic",
  "form":"memoir (written later)","language":"Arabic",
  "authenticity":"The Rihla was dictated at Fez in 1355–56 to Ibn Juzayy, who shaped it; some passages elsewhere are borrowed or embellished. Gibb's 1929 translation is the standard English selection. Some editions misprint his Aleppo stay as 1347; historians place it in June 1348.",
  "bio":"The great traveller walked straight into the epidemic on his way home, counting the dead town by town. He alone describes the multi-faith procession of Damascus — and he learned on the road that his own mother had died of plague in Morocco.",
  "sources":[{"title":"Internet Medieval Sourcebook: Ibn Battuta, the Black Death (Gibb 1929)","url":"https://sourcebooks.web.fordham.edu/source/1354ibnbattuta-plague.asp"},
             {"title":"Ibn Battuta, Rihla ch. 12 itinerary (R. Gross)","url":"https://rolfgross.dreamhosters.com/Battuta-Web/Rihla-12/Rihla-12.html"},
             {"title":"'Ibn Battuta's Prayer of Damascus', Kervan (Univ. of Turin)","url":"https://ojs.unito.it/index.php/kervan/article/view/5785"}]},
 {"id":"maqrizi","short":"al-Maqrizi","name":"Taqi al-Din Ahmad al-Maqrizi","life":"1364–1442",
  "role":"Cairene historian and former market inspector, writing two generations later",
  "side":"Mamluk Sultanate (Egypt)","where":"Cairo","lat":30.0444,"lon":31.2357,
  "vantage":3,"vantage_label":"later historian of his own city, working from earlier records",
  "form":"chronicle","language":"Arabic",
  "authenticity":"FLAG — LATER CHRONICLE: his Kitab al-suluk was compiled in the early fifteenth century from earlier Mamluk sources. Its plague figures for Cairo are vivid but derivative and often inflated.",
  "bio":"Not an eyewitness but the fullest Egyptian record: Cairo's funerals, the sultan's withdrawal, the price of grave-digging. He is here because Cairo, the largest city of the Mediterranean world, otherwise has no surviving diarist.",
  "sources":[{"title":"Black Death in the Middle East (Wikipedia)","url":W+"Black_Death_in_the_Middle_East"},
             {"title":"Oregon State OER, 'The Black Death' (al-Maqrizi excerpt)","url":"https://open.oregonstate.education/middleearlymodernages/chapter/black-death/"}]},
 {"id":"ibn-khatima","short":"Ibn Khatima","name":"Abu Ja'far Ahmad ibn Khatima","life":"1324–1369",
  "role":"Physician and poet of Almería, about 24",
  "side":"Nasrid Emirate of Granada (al-Andalus)","where":"Almería","lat":36.834,"lon":-2.4637,
  "vantage":1,"vantage_label":"physician treating the sick in his port city",
  "form":"treatise (medical)","language":"Arabic",
  "authenticity":"Tahsil gharad al-qasid fi tafsil al-marad al-wafid, completed in 1349; Spanish translation by M. L. Arvide Cambra (2014). Contemporaneous clinical observation framed within humoral medicine.",
  "bio":"A young doctor at the western edge of the Islamic world who treated plague patients and traced the outbreak in his city to its poorest quarter. With his friend Ibn al-Khatib of Granada he argued that contact with the sick and their clothing spread the disease.",
  "sources":[{"title":"M. Herrera Carranza, 'Regarding pandemics: Ibn Jatima from Almería', Medicina Intensiva (2021)","url":"https://medintensiva.org/en-regarding-pandemics-ibn-jatima-from-articulo-S2173572721000692"},
             {"title":"Brewminate: Ibn al-Khatib and the medieval case for contagion","url":"https://brewminate.com/the-plague-crossed-the-door-ibn-al-khatib-and-the-medieval-case-for-contagion/"}]},
 {"id":"ibn-khaldun","short":"Ibn Khaldun","name":"'Abd al-Rahman ibn Khaldun","life":"1332–1406",
  "role":"Tunisian student of 16–17 in 1348–49; later historian and judge",
  "side":"Hafsid Tunis (Islamic Maghreb)","where":"Tunis","lat":36.8065,"lon":10.1815,
  "vantage":0,"vantage_label":"orphaned by the plague as a teenager",
  "form":"memoir (written later)","language":"Arabic",
  "authenticity":"Recalled in his autobiography (al-Ta'rif) and in the Muqaddimah (drafted 1377). Retrospective, but he is a careful and famous witness to his own loss.",
  "bio":"A brilliant teenager in Tunis whose parents and teachers died in the plague. Thirty years later he set the Black Death at the heart of his theory of history: civilisations shrink and cities empty when the dead outnumber the living.",
  "sources":[{"title":"Ibn Khaldun (Britannica)","url":"https://www.britannica.com/biography/Ibn-Khaldun"}]}
]

E = []
def e(date_iso, disp, prec, eye, place, head, dig, quote, conf, note):
    E.append({"date_iso":date_iso,"date_display":disp,"precision":prec,"eye":eye,"place":place,
              "headline":head,"digest":dig,"quote":quote,"confidence":conf,"source_note":note})

e("1346-06-01","1346 (siege of Caffa; month not given)","year","demussi","Piacenza, retelling events at Caffa, Crimea",
  "The besiegers' dead thrown over Caffa's walls — a hearsay story",
  "De' Mussi tells how the Golden Horde army besieging the Genoese port of Caffa fell sick in huge numbers and, dying, flung corpses into the town by catapult so that the defenders sickened too. Survivors then sailed away and, he says, carried the disease to the Mediterranean. He was almost certainly not there; modern historians accept that plague reached Caffa but doubt that this siege seeded Europe.",
  "","approx","Wheelis, Emerging Infectious Diseases 8:9 (2002); Horrox pp. 14–26; Wikipedia 'Gabriel de Mussis' (manuscript Wrocław R 262)")
e("1347-08-01","1347 (summer–autumn; modern estimates differ)","range","kantakouzenos","Constantinople",
  "Out of the Black Sea, the sickness enters the capital",
  "Kantakouzenos records that the disease came down from the north and fell on Constantinople, sparing no rank. Among its first victims was his youngest son Andronikos, dead within the first days of the outbreak. He frames the epidemic as a divine warning, yet he notes that it also struck the shores and islands far beyond the city.",
  "","approx","Goodyear, Medieval Magazine (2020); Miller, GRBS (1976) dates arrival to autumn 1347")
e("1347-09-01","1347 (later description)","range","kantakouzenos","Constantinople",
  "Fever, blood from the lungs, swellings, dark spots",
  "Borrowing the frame of Thucydides but not his symptoms, the emperor describes a sudden high fever, loss of speech and delirium; in some victims pain in the chest and bloody spittle; in others swellings in the armpit, groin or jaw, with dark blotches on the skin. He notes that whole houses were emptied of their people and even their animals, and that doctors could do nothing.",
  "","approx","Miller, 'The Plague in John VI Cantacuzenus and Thucydides', GRBS (1976)")
e("1348-01-15","January 1348","month","chauliac","Avignon",
  "The great mortality begins at the papal court",
  "Guy later wrote that the mortality began in Avignon in January 1348 and ran about seven months. For the first two months it came as continuous fever with spitting of blood, killing in about three days; thereafter as fever with abscesses and swellings in armpit and groin, killing in about five. He thought the first form the more contagious.",
  "","approx","Chirurgia magna (1363), summarised in Wikipedia 'Guy de Chauliac' and Northeastern excerpt")
e("1348-03-15","Spring (March) 1348","month","boccaccio","Florence",
  "Swellings the size of an apple, then the black spots",
  "Boccaccio says the pestilence reached Florence early in the spring of 1348, unlike the nosebleeds reported in the East: swellings in groin or armpit, some as large as an apple or an egg, followed by dark or livid blotches on arms and thighs. He insists he saw with his own eyes two pigs root among a dead pauper's rags in the street and fall dead within the hour. Physicians, he concludes, knew neither the cause nor the cure.",
  "","approx","Decameron, Introduction to Day One (written c. 1349–53); Macmillan Viewpoints 14.2 excerpt")
e("1348-04-06","Sunday 6 April 1348 (as recorded later in his Virgil)","day","petrarch","Avignon (Laura); Petrarch himself in Verona",
  "Laura dies at dawn, the anniversary of their first meeting",
  "In the note he later wrote into his Virgil, Petrarch records that Laura died in Avignon on 6 April 1348, at the same hour of the same day on which he had first seen her in 1327, and was buried that evening in the church of the Friars Minor. He was far away in Verona and knew nothing of it.",
  "","verified","Autograph note in the Ambrosian Virgil (Milan, S.P. 10/27); Brown Decameron Web, 'Petrarch and the plague'")
e("1348-04-27","27 April 1348","day","heyligen","Avignon (letter to the chapter of St Donatian's, Bruges)",
  "Half of Avignon is dead, a cantor writes home to Bruges",
  "Heyligen tells his colleagues in Bruges that the sickness came from the East on merchant ships to Genoa and Marseille, and that by his reckoning half the city has died. The pope has bought a new field as a cemetery, and some 11,000 bodies already lie in it; when even that failed, Heyligen says, the Rhône itself was blessed so the dead could be committed to the river. The healthy shun the sick, servants refuse to nurse, and rumours of poisoned food and wells are spreading.",
  "","verified","Letter of 27 April 1348, Horrox pp. 41–45; Wikipedia 'Lodewijk Heyligen' confirms origin story, half of Avignon dead, 11,000 in new cemetery; the Rhône blessing and avoidance of the sick follow the Horrox translation and were not re-checked online")
e("1348-05-15","May 1348","month","petrarch","Verona",
  "A letter from Avignon, and a note written where he will see it",
  "News of Laura's death reached Petrarch in Verona in May by letter from a friend — traditionally identified as his 'Socrates', Louis Heyligen. He wrote the facts into his copy of Virgil, the book he read most, choosing that place, he says, so that it would meet his eyes often and remind him that nothing should hold him to this life.",
  "","approx","Brown Decameron Web, 'Petrarch and the plague' (Verona, May, letter from a friend)")
e("1348-05-20","May 1348","month","agnolo","Siena",
  "The mortality begins in Siena",
  "Agnolo records that the dying in Siena began in May, and that it was a thing too cruel and horrible for any tongue. People sickened with swellings and died almost while speaking; families broke apart as father fled child and wife fled husband, for the disease seemed to pass by breath and sight. No one could be found to carry the dead for money or friendship.",
  "","approx","Cronaca senese; Wikipedia 'Agnolo di Tura'; Macmillan excerpt 'A Town Chronicler Describes the Black Death'")
e("1348-06-01","June 1348 (month as in modern chronologies)","month","ibn-battuta","Aleppo",
  "In Aleppo, word that Gaza is losing a thousand a day",
  "Resting in Aleppo on his way west, Ibn Battuta hears that plague has broken out in Gaza and that more than a thousand people die there each day. He sets out south through Syria regardless, into the epidemic rather than away from it.",
  "","approx","Gibb trans. (1929); R. Gross Rihla ch. 12 itinerary (which prints 1347); Wikipedia 'Black Death in the Middle East' (June 1348)")
e("1348-06-10","June 1348","range","ibn-battuta","Homs, then Damascus",
  "Three hundred dead in Homs the day he arrives",
  "At Homs he finds the plague already present, with about three hundred people dying on the day of his arrival. Going on to Damascus, he is told the city is burying some 2,400 a day. His numbers are hearsay from officials and townspeople, but they show how the scale was being talked about street by street.",
  "","approx","Gibb trans. (1929); R. Gross Rihla ch. 12 itinerary")
e("1348-06-15","June 1348","range","ibn-khatima","Almería",
  "The first household falls in the poorest quarter",
  "Ibn Khatima traced Almería's outbreak to its poorest district and identified the first stricken family. Treating patients through the epidemic, he watched the disease move from house to house among people who had been in contact with the sick, and he gathered merchants' reports that it had begun far to the east, in China.",
  "","approx","Herrera Carranza, Medicina Intensiva 45 (2021), summarising the Tahsil")
e("1348-07-06","6 July 1348","day","clement","Avignon",
  "The pope forbids killing or robbing Jews without trial",
  "Clement VI reissues the old papal protection of the Jews, Sicut Judaeis, forbidding Christians to kill, rob or forcibly baptise them without judgment. It is a response to massacres already under way in Provence and Catalonia that spring, where Jews had been blamed for the dying.",
  "","verified","Simonsohn, Apostolic See and the Jews (1991), cited in Wikipedia 'Persecution of Jews during the Black Death' (Toulon massacre April 1348)")
e("1348-07-10","Summer 1348 (after 3 July)","range","petrarch","Parma",
  "'The high column is broken': Colonna and Laura gone",
  "Within three months of Laura, Cardinal Giovanni Colonna — Petrarch's patron and Heyligen's master — died of plague at Avignon. Petrarch mourned both in one sonnet of the Canzoniere (no. 269), lamenting that death had taken in a single season the column and the laurel that had sheltered his life.",
  "","approx","Canzoniere 269; Wikipedia 'Lodewijk Heyligen' (Colonna died of plague in 1348)")
e("1348-07-20","Summer 1348 (June–August)","range","agnolo","Siena",
  "He buries his five children with his own hands",
  "In the middle of the city's record Agnolo writes of himself: he buried his five children with his own hands, and his wife Nicoluccia died too. Great pits were dug and filled; no bells rang and no one wept, because almost everyone expected to die. So many perished that people said it was the end of the world.",
  "buried my five children with my own hands","approx","Cronaca senese; Wikipedia 'Agnolo di Tura'")
e("1348-07-25","A Friday in the latter part of July 1348 (Rabi' II 749 AH)","range","ibn-battuta","Damascus, Mosque of the Footprints",
  "Muslims, Jews and Christians walk together to pray",
  "After a three-day fast ordered by the governor, the whole city gathers at the Umayyad Mosque at dawn on Friday and walks barefoot to the Mosque of the Footprints outside the walls. Ibn Battuta notes that the Jews came with their Torah and the Christians with their Gospel, weeping and pleading alongside the Muslims. He believed the dying in Damascus then eased to fewer than 2,000 a day — against, he was told, 24,000 a day in Cairo.",
  "","approx","Gibb trans. (1929), Fordham Sourcebook (latter part of July 1348, Friday); Kervan article 'Prayer of Damascus'")
e("1348-07-31","March–July 1348","range","boccaccio","Florence",
  "Layer upon layer, like cargo in a ship's hold",
  "By summer, Boccaccio writes, the usual rites had collapsed: neighbours carried out the dead and left them at doors, consecrated ground ran out, and great trenches at the churches were filled with bodies stacked in layers. Many fled to the countryside; others gave themselves to drink and pleasure. He claims more than 100,000 died in Florence between March and July — far more than the city likely held, but a measure of how the toll felt.",
  "","approx","Decameron, Introduction to Day One; Oregon State OER (Stefani: Florence March–September 1348)")
e("1348-08-15","Early August–Christmas 1348","range","clyn","Dublin and Drogheda, recorded at Kilkenny",
  "Fourteen thousand dead in Dublin before Christmas",
  "Clyn records that the pestilence arrived through the ports of Dublin and Drogheda and that from August to Christmas some 14,000 died in Dublin alone. Twenty-three of his own Franciscan brothers died in Dublin and twenty-five at Drogheda. He sees the sickness emptying towns and cities of their people.",
  "","approx","Annals of Ireland (Butler 1849 / Williams 2007), as excerpted by Coles Lane")
e("1348-09-25","25 September 1348 (Sha'ban 749 AH)","day","maqrizi","Cairo",
  "The sultan leaves Cairo as the plague arrives",
  "In the Mamluk record that al-Maqrizi preserves, the plague reached Cairo from Alexandria and the delta in late summer, and the young Sultan al-Nasir Hasan withdrew to his residence at Siryaqus north of the city on 25 September, staying until 22 December. The capital was left to its officials, its preachers and its dead.",
  "","approx","Wikipedia 'Black Death in the Middle East' (Siryaqus 25 Sept–22 Dec; Cairo from September 1348)")
e("1348-09-26","26 September 1348","day","clement","Avignon",
  "Quamvis perfidiam: the Jews are dying too",
  "In a second bull Clement VI declares that those blaming the Jews for poisoning have been deceived by the Devil. His argument is plain observation: the Jews are dying of the same plague, and it rages in places where no Jews have ever lived. He orders bishops to protect them and threatens excommunication — words that would not save the Rhineland communities that winter.",
  "","verified","Simonsohn (1991), cited in Wikipedia 'Persecution of Jews during the Black Death' (bulls of 6 July and 26 September 1348)")
e("1348-10-20","Autumn 1348","range","ibn-battuta","Alexandria and Cairo",
  "Egypt: the dying easing in Alexandria, unimaginable in Cairo",
  "Reaching Egypt, Ibn Battuta hears that Alexandria had lost 1,080 people a day at the height of the epidemic, now easing, and that Cairo had seen as many as 21,000 a day. He passes on through, bound for Mecca, where he arrives on 16 November 1348 for his fourth pilgrimage.",
  "","approx","R. Gross Rihla ch. 12 itinerary (Mecca 16 November 1348)")
e("1348-11-15","November–December 1348 (Ramadan–Shawwal 749 AH)","range","maqrizi","Cairo",
  "Fourteen hundred biers are not enough",
  "Al-Maqrizi's account of Cairo at its worst counts the dead by the funerals and biers: 1,400 biers proved too few, and the dead were carried on boards and doors. Prices for the work of death soared — a Qur'an reciter, a bearer, a gravedigger each named his fee — and a groom's monthly wage nearly tripled. His total for these two months (900,000) is far beyond belief, but the economic details ring true.",
  "","approx","Oregon State OER excerpt of al-Maqrizi (Oct 1348 onward; litters; wages; Nov–Dec figures)")
e("1348-12-01","Late 1348–early 1349 (749 AH)","range","ibn-al-wardi","Aleppo",
  "Fifteen years on the road, and now at Aleppo's gate",
  "Ibn al-Wardi traces the pestilence across the known world in rhymed prose: begun in the far East some fifteen years before, it passed through China and India, Persia and the Crimea, Cyprus, Egypt, Palestine and Syria, until it reached Aleppo. He mixes grief with wit, personifying the plague as a conqueror that besieges city after city. For the believer, he insists, it is martyrdom and mercy; he asks God to lift it.",
  "","approx","Risalat al-naba' 'an al-waba', trans. M. Dols (1974); Wikipedia 'Ibn al-Wardi'")
e("1349-01-15","1348–49 (749–750 AH)","range","ibn-khaldun","Tunis",
  "A teenager loses his parents and his teachers",
  "Ibn Khaldun later recalled that the great plague swept Tunis when he was about seventeen, carrying off his father and mother and most of the scholars who had taught him. The loss ended his first education and, by his own account, shaped his sense of how quickly a learned world can vanish.",
  "","approx","al-Ta'rif (autobiography); Britannica biography (born Tunis 27 May 1332)")
e("1349-02-10","9–10 February 1349","range","closener","Strasbourg",
  "The guilds depose a council that protected the Jews",
  "After a regional meeting at Benfeld on 8 February pressed Strasbourg to act against its Jews, the craft guilds rose and forced out the city's masters, who had resisted the poisoning charges. The council was dissolved and remade within days, and the new rulers had the Jews arrested on Friday 13 February.",
  "","approx","Königshofen chronicle after Closener, trans. Marcus (1938), Fordham Sourcebook; Wikipedia 'Strasbourg massacre'")
e("1349-02-14","Saturday 14 February 1349 (St Valentine's Day)","day","closener","Strasbourg, Jewish cemetery",
  "Strasbourg burns its Jews before the plague arrives",
  "On the Saturday the Jews of Strasbourg were burned in their own cemetery; the chronicle counts about 2,000. Some who accepted baptism, and some children, were spared. Debts owed to Jews were cancelled and their goods divided — the chronicle itself observes that money was the poison that killed them. The plague reached the city that summer anyway and killed thousands.",
  "","verified","Königshofen after Closener, trans. Marcus (1938), Fordham Sourcebook (Friday 13 Feb arrest; Saturday 14 Feb burning; ~2,000; ~16,000 plague dead 1349)")
e("1349-02-20","Christmas 1348–Lent 1349","range","clyn","Kilkenny",
  "Scarcely a house in Kilkenny where only one died",
  "The plague reached Kilkenny by Christmas 1348 and was at its height that Lent. Clyn writes that hardly a house was struck where only one person died; usually husband, wife and children went to the grave together. Friars of his own and other orders died in numbers.",
  "","approx","Annals of Ireland, as excerpted by Coles Lane (Kilkenny by Christmas 1348)")
e("1349-03-18","27 Dhu al-Hijja 749 AH = 18 March 1349","day","ibn-al-wardi","Aleppo",
  "The poet of the plague dies of it",
  "Ibn al-Wardi's essay ends in prayer, and within days its author was dead of the pestilence he had described. Later biographers fixed his death in Aleppo to the last days of the Islamic year 749. His essay survives as a witness that stops mid-epidemic, like Clyn's annals in Ireland.",
  "","verified","Wikipedia 'Ibn al-Wardi' citing Encyclopaedia of Islam (d. 27 Dhu al-Hijja 749 / 18 March 1349)")
e("1349-04-01","Before Easter (12 April) 1349","range","clyn","Kilkenny",
  "Parchment left for anyone still alive",
  "Writing as one waiting among the dead for death to come, Clyn says he has set down what he saw so that the record does not perish with the writer. He leaves parchment for the work to be continued, in case any of the race of Adam should survive the pestilence.",
  "lest the writing perish with the writer","approx","Annals of Ireland; Catholic Encyclopedia 'John Clynn'; Coles Lane")
e("1349-05-15","1349 (month not verified)","year","ibn-khatima","Almería",
  "A physician's ten questions: contact and clothing spread it",
  "Ibn Khatima finished his treatise in 1349. Within the humoral medicine of his day he describes corrupted vapours, but also warns plainly that sitting with the sick and handling their clothes passes on the disease, and urges isolation. His friend Ibn al-Khatib in Granada would press the case for contagion still harder, arguing that experience must outweigh a hadith read too literally.",
  "","approx","Herrera Carranza (2021); Brewminate on Ibn al-Khatib's Muqni'at al-sa'il")
e("1349-05-20","Spring 1349 (Familiares VIII.7, revised later)","range","petrarch","Parma",
  "Will posterity believe a world emptied like this?",
  "Writing to his friend 'Socrates', Petrarch asks where their dear friends are now: houses empty, cities abandoned, fields untilled, a dreadful silence over the earth. He predicts that later generations, having never seen such a thing, will think it a fable — happy people, he says, who will not have known it.",
  "O happy posterity","approx","Familiares VIII.7 (to Socrates, Parma, 1349; widely cited)")
e("1349-06-01","1349 (written c. 1378–96)","range","knighton","Leicester",
  "Three hundred and eighty dead in one small parish",
  "Knighton records that in the little Leicester parish of St Leonard more than 380 died. That year a murrain of sheep ran across the realm too: in one pasture more than 5,000 died, and the carcasses were left to rot because no one would touch them.",
  "","approx","Knighton, Chronicon, in Carlin's 'Black Death in the British Isles' collection")
e("1349-06-20","After 17 June 1349","range","clyn","Kilkenny",
  "The last entry, and another hand: the author seems to have died",
  "Clyn's final entry is a eulogy for the knight Fulk de la Freigne, written after 17 June 1349. Then his hand stops. A later copyist added a line noting that here the author appears to have died — the continuer he had hoped for, but only to record his silence.",
  "","approx","Wikipedia 'John Clyn' (last entry after 17 June 1349); Catholic Encyclopedia (copyist's note)")
e("1349-09-15","Autumn 1349 (written c. 1378–96)","range","knighton","Leicester",
  "Cheap horses, dear reapers",
  "Fear of death made goods cheap, Knighton says: a horse once worth forty shillings went for six and eightpence, a fat ox for four shillings. But at harvest the labourers who were left could not be had for less than eightpence a day with food, mowers twelvepence — crops rotted in fields for want of hands, and lords bargained against the new royal wage laws.",
  "","approx","Knighton, Chronicon, in Carlin collection; cf. Ordinance of Labourers 1349 (Oregon State OER)")
e("1349-10-15","Autumn 1349 (before reaching Fez, 13 November 1349 / Sha'ban 750)","range","ibn-battuta","Taza, Morocco",
  "Almost home, he learns his mother died of the plague",
  "After a winding passage along the North African coast, Ibn Battuta reached Taza and was told that his mother had died of the plague. He went on to Fez and presented himself to the Marinid sultan on 13 November 1349, the end of a quarter-century of travel.",
  "","approx","R. Gross Rihla ch. 12 itinerary (Taza; Fez 13 November 1349)")
e("1363-06-01","1363 (completion of the Chirurgia magna)","year","chauliac","Avignon",
  "The doctor's shame — and his own illness",
  "Looking back, Guy wrote that the plague was useless and shameful for physicians, since they dared not visit the sick and could not help them. He says he himself fell ill near the end of the epidemic, with fever and a swelling in the groin, and recovered after about six weeks. He advised the pope to keep fires burning and see no one, and he rejected the charge that Jews had poisoned the world.",
  "","approx","Chirurgia magna; Wikipedia 'Guy de Chauliac' (fell ill and survived; fires; opposed the poisoning charge)")
e("1377-06-01","1377 (drafting of the Muqaddimah)","year","ibn-khaldun","Qal'at ibn Salama (Algeria), looking back",
  "As if the world's voice had called for its own shrinking",
  "In the Muqaddimah Ibn Khaldun describes the plague of the mid-eighth Islamic century as a destroying pestilence that swept East and West alike, devoured nations and emptied cities, roads and dwellings. Civilisation, he writes, shrank with the shrinking of mankind; it was as if the world had been changed all at once and needed a new history.",
  "","approx","Muqaddimah, introduction (1377); Britannica biography")

convergences = [
 {"date":"1346-06-01","label":"Out of the Black Sea, 1346–47","eyes":["demussi","kantakouzenos"],
  "note":"Two Christian writers point to the same sea: an Italian notary at home retells a lurid siege story, while a Byzantine emperor who actually lived through the arrival names the north and mourns his son. The rumour travelled faster than the facts."},
 {"date":"1348-04-27","label":"Avignon in April 1348","eyes":["heyligen","chauliac","petrarch","clement"],
  "note":"The papal city seen four ways in a single month: a cantor counting graves for colleagues in Bruges, a physician watching the disease change form, a poet's beloved dying unseen, and a pope buying a cemetery and blessing a river."},
 {"date":"1348-07-25","label":"High summer 1348: Siena, Florence, Damascus, Avignon","eyes":["agnolo","boccaccio","ibn-battuta","clement"],
  "note":"In the same weeks Agnolo buries his children without bells, Boccaccio watches trenches filled in layers, Damascus walks barefoot in a procession of three faiths, and the pope tries in writing to stop Christians killing Jews. Solidarity and scapegoating happen at once."},
 {"date":"1348-09-26","label":"Late September 1348: two capitals, two responses","eyes":["clement","maqrizi","clyn"],
  "note":"The day after the Mamluk sultan retreats from Cairo, the pope in Avignon issues his second bull; in Ireland the Dublin toll mounts. Rulers on both shores step back from the crowd while their scholars and friars stay to count."},
 {"date":"1349-02-14","label":"February–March 1349: fire in Strasbourg, silence in Aleppo","eyes":["closener","clyn","ibn-al-wardi","ibn-khaldun"],
  "note":"Strasbourg kills its Jews before the plague even arrives; Kilkenny is at its Lenten peak; Tunis loses a young scholar's parents; and a month later Aleppo's poet dies mid-essay. Each community searched for meaning — some in prayer, one in murder."},
 {"date":"1349-05-15","label":"What spreads it? Physicians and poets argue","eyes":["ibn-khatima","chauliac","boccaccio","ibn-al-wardi"],
  "note":"Ibn Khatima and Guy de Chauliac, a sea apart, both see that contact with the sick is dangerous; Boccaccio swears to the pigs and the rags; Ibn al-Wardi stresses God's decree and martyrdom. The observation and the theology sit side by side in every tradition."},
 {"date":"1349-04-01","label":"Writers who expected to die","eyes":["clyn","ibn-al-wardi","petrarch"],
  "note":"Clyn leaves parchment for a survivor, Ibn al-Wardi's essay ends in prayer days before his death, and Petrarch writes to future readers who will not believe him. Three men, in three languages, addressing a posterity they were not sure would exist."}
]

ties = [
 {"a":"heyligen","b":"petrarch","kind":"read each other","note":"Close friends; Petrarch called Heyligen his 'Socrates' and addressed letters to him, including the plague letter of 1349. News of Laura's death reached Petrarch by a friend's letter, traditionally Heyligen's."},
 {"a":"heyligen","b":"chauliac","kind":"same street","note":"Both served at the papal court in Avignon through the spring of 1348, one in a cardinal's household, the other at the pope's bedside."},
 {"a":"chauliac","b":"clement","kind":"met","note":"Guy was Clement VI's personal physician and advised him to keep fires burning and receive no one during the epidemic."},
 {"a":"clement","b":"closener","kind":"influenced","note":"The pope's bulls of July and September 1348 explicitly rejected the poisoning charge; Strasbourg's new council ignored that teaching in February 1349, as Closener's city chronicle records."},
 {"a":"petrarch","b":"boccaccio","kind":"met","note":"Boccaccio admired Petrarch long before they first met in Florence in 1350, two years after the plague; they remained lifelong friends and correspondents."},
 {"a":"ibn-battuta","b":"ibn-khaldun","kind":"mentioned","note":"In the Muqaddimah Ibn Khaldun recalls the traveller Ibn Battuta at the Marinid court in Fez, whose tales of India some listeners whispered were lies."},
 {"a":"ibn-battuta","b":"ibn-al-wardi","kind":"same street","note":"Both were in Aleppo in June 1348 as the plague approached; there is no evidence that they met."},
 {"a":"clyn","b":"ibn-al-wardi","kind":"opposite sides","note":"At opposite ends of the known world — an Irish friar and a Syrian jurist — both wrote until the plague stopped them in spring 1349."}
]

threads_out = [
 {"to":"v1:london-1666","note":"The Great Plague of London in 1665 belongs to the same long 'second pandemic' of plague that began with the Black Death of 1346–53, recurring across Europe for three centuries. In 1348–49 London buried its dead in new ground at Smithfield; in 1665 Pepys and Allin watched the bills of mortality climb."},
 {"to":"v1:long-threads","note":"The plague writers here — Clyn leaving parchment, Ibn al-Wardi writing to the end, Petrarch addressing a disbelieving posterity — are ancestors of every epidemic diarist in the Long Threads chapter, from Ibn al-Banna's Baghdad notebook to the COVID-19 'Journal of the Plague Year' archive."},
 {"to":"constantinople-1453","note":"Constantinople, struck in 1347 just as Kantakouzenos took power, never recovered its population; by 1453 it held perhaps a tenth of its former people. Kantakouzenos's alliance with the Ottoman ruler Orhan, to whom he married his daughter Theodora in 1346, helped bring the Ottomans into Europe — the road that ended at the walls a century later."}
]

images = [
 {"url":"https://balat.kikirpa.be/en/photo/X004173/","title":"Plague at Tournai, 1349 (Gilles li Muisis, Antiquitates Flandriae, fol. 24v)","caption":"Townspeople carry coffins to burial in Tournai in 1349 — the best-known contemporary image of the Black Death, from the chronicle of a Flemish abbot who lived through it.","date":"c. 1349–53","credit":"KBR, Royal Library of Belgium; photo KIK-IRPA"},
 {"url":"https://identity.wellcomecollection.org/works/tzxaqzck","title":"Burying plague victims of Tournai, 1349","caption":"Wellcome Collection's photographic record of the same Tournai miniature from the annals of Gilles de Muisit.","date":"1349 (miniature); 1949 (photograph)","credit":"Original: Royal Library of Belgium; record: Wellcome Collection"},
 {"url":"https://wwwnc.cdc.gov/eid/article/8/9/01-0536-f2","title":"First page of Gabriele de' Mussi's narrative","caption":"The opening of de' Mussi's account of the siege of Caffa, Wrocław University Library MS R 262, fol. 74r — the only manuscript of the story.","date":"14th century","credit":"University of Wrocław Library, via Emerging Infectious Diseases (Wheelis 2002)"},
 {"url":"https://utpictura18.univ-amu.fr/en/notice/25069-petrarchs-virgil-ambrosiana-frontispiece-to-ms-a-79-inf-simone-martini","title":"Simone Martini's frontispiece to Petrarch's Virgil","caption":"The frontispiece Simone Martini painted for Petrarch's own Virgil — the book in which Petrarch wrote the note recording Laura's death in the plague of 1348.","date":"c. 1336–44 (painting)","credit":"Simone Martini; Biblioteca Ambrosiana, Milan"},
 {"url":"https://www.facsimiles.com/facsimiles/ambrosian-virgil-of-francesco-petrarca","title":"The Ambrosian Virgil of Francesco Petrarca","caption":"Description of the manuscript (Ambrosiana S.P. 10/27) in which Petrarch recorded the deaths of Laura and, later, of his son Giovanni — himself a victim of the 1361 plague.","date":"c. 1300–25 (manuscript)","credit":"Veneranda Biblioteca Ambrosiana, Milan"}
]

further = [
 {"title":"Internet Medieval Sourcebook: Ibn Battuta on the Black Death","url":"https://sourcebooks.web.fordham.edu/source/1354ibnbattuta-plague.asp"},
 {"title":"Internet Medieval Sourcebook: The Black Death and the Jews 1348–1349","url":"https://sourcebooks.web.fordham.edu/jewish/1348-jewsblackdeath.asp"},
 {"title":"Princeton Middle Ages for Educators: Early Transmission of the Black Death","url":"https://middleagesforeducators.princeton.edu/node/226/"},
 {"title":"M. Carlin: The Black Death in the British Isles (sources)","url":"https://sites.uwm.edu/carlin/?p=887"},
 {"title":"Stanford History Education Group: Understanding the Black Death (student materials, PDF)","url":"https://sheg.stanford.edu/sites/default/files/download-pdf/Understanding%20the%20Black%20Death%20Student%20Materials.pdf"},
 {"title":"Wheelis, 'Biological Warfare at the 1346 Siege of Caffa' (EID 2002)","url":"https://www.medievalists.net/2012/08/15/biological-warfare-at-the-1346-siege-of-caffa/"},
 {"title":"Brewminate: Ibn al-Khatib and the medieval case for contagion","url":"https://brewminate.com/the-plague-crossed-the-door-ibn-al-khatib-and-the-medieval-case-for-contagion/"},
 {"title":"Black Death in the Middle East (Wikipedia)","url":W+"Black_Death_in_the_Middle_East"}
]

chapter = {
 "id":"black-death",
 "title":"The Great Mortality",
 "subtitle":"The Black Death seen from Christian Europe and the Islamic world at once, 1346–1349",
 "span":"1346–1349",
 "intro":[
  "Between 1346 and 1353 a single disease — plague, carried by the bacterium Yersinia pestis — swept from the steppe around the Black Sea through Constantinople, Egypt, Syria, Italy, France, Spain, the Maghreb, Germany and the British Isles. Perhaps a third to a half of the people in its path died. Christians called it the great mortality; Arabic writers called it the great annihilation. Neither world knew the cause, and both wrote about it.",
  "There are no diaries in the modern sense from these years. What survives is letters, chronicles, annals, medical treatises, papal bulls, a note scribbled in a beloved book, and travel memoirs dictated later. This chapter uses all of them, tagged honestly: some writers stood inside the dying city and wrote within weeks; others, like Henry Knighton, Guy de Chauliac or al-Maqrizi, looked back years or generations later; and a few famous accounts — Gabriele de' Mussi's siege of Caffa, Boccaccio's Florence — carry flags for hearsay or literary shaping.",
  "Set side by side, the Christian and Muslim witnesses rhyme more than they clash. Heyligen in Avignon and Ibn Battuta in Syria both count the dead per day and pass on numbers they could not check. Boccaccio and Ibn Khatima both see that the sick and their clothing pass the disease on. Petrarch, Ibn al-Wardi and Friar John Clyn all write knowing they may not live to finish — and in two of those cases they did not.",
  "The differences matter too. Damascus answered the plague with a procession in which Muslims, Jews and Christians walked together; much of the Latin West answered it with accusations of poisoning, and in February 1349 Strasbourg burned its Jewish community before the plague had even reached the city, despite a pope who had declared in writing that the Jews were dying like everyone else. Those events are recorded here soberly, as the chroniclers set them down.",
  "Read the timeline slowly. In the same summer of 1348, a Sienese shoemaker buries his children, a Florentine writer watches trenches fill, a Moroccan traveller prays barefoot outside Damascus, and a pope issues his first decree on the Jews. In spring 1349, an Irish friar leaves blank parchment for whoever survives, and a Syrian poet's essay ends in prayer a few days before his death. They never read one another, but they were writing the same book."
 ],
 "calendar_note":"All Christian dates are given as the writers recorded them, in the Julian calendar, which historians cite unchanged for the fourteenth century (it then ran about eight days behind the later Gregorian reckoning); date_iso therefore uses the proleptic Julian date for sorting. English and Irish writers began the year on 25 March (Lady Day), so Clyn's and Knighton's 'Lent 1348' is our Lent 1349. Islamic writers used the lunar Hijri calendar: the year 749 AH ran from about 1 April 1348 to 20 March 1349, and 750 AH from then to March 1350; Ibn al-Wardi's death on 27 Dhu al-Hijja 749 is 18 March 1349. Where a writer gives only a season or a Hijri month, the entry is marked 'month' or 'range' and dated to its approximate middle.",
 "eyes":eyes,
 "entries":sorted(E, key=lambda x: x["date_iso"]),
 "convergences":convergences,
 "ties":ties,
 "threads_out":threads_out,
 "images":images,
 "further":further,
 "vantage_key":"0 = direct victim or the person at the centre (lost family, fell ill, or died); 1 = eyewitness inside a stricken city; 2 = nearby, or in the city but recording at second hand; 3 = writing from a distance in place or time (later historians); 4 = abroad, news only."
}

ids = {x["id"] for x in eyes}
for x in E: assert x["eye"] in ids, x["eye"]
for c in convergences:
    for i in c["eyes"]: assert i in ids, i
for t in ties: assert t["a"] in ids and t["b"] in ids
for x in eyes: assert len(x["short"]) <= 16, x["short"]
for x in E:
    if x["quote"]: assert len(x["quote"].split()) <= 12
json.dump(chapter, open(OUT,"w"), ensure_ascii=False, indent=1)
print(len(eyes), "eyes", len(E), "entries")
