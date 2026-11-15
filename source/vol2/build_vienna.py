import json

V = (48.2085, 16.3731)
OUT = "/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/vol2/ch-vienna-1683.json"

URL_TAAFFE = "https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/A34352?show=full"
URL_JOURNAL = "https://distantreader.org/stacks/earlyprint/txt/A46317.txt"
URL_PARTIC = "https://distantreader.org/stacks/earlyprint/txt/A56484.txt"
URL_TRUE_EN = "https://germanhistorydocs.org/en/the-holy-roman-empire-1648-1815/the-turkish-defeat-at-vienna-september-12-1683"
URL_TRUE_PDF = "https://germanhistorydocs.org/en/the-holy-roman-empire-1648-1815/the-turkish-defeat-at-vienna-september-12-1683.pdf"
URL_TRUE_DE = "https://germanhistorydocs.org/de/das-heilige-roemische-reich-1648-1815/ghdi:document-3580"
URL_ACTON = "https://languagecollections-blog.lib.cam.ac.uk/2014/02/07/the-siege-of-vienna-in-the-acton-library"
URL_INLIBRIS = "https://inlibris.com/item/bn48823/?cur=eur"
URL_WIL_LETTER = "https://wilanow-palac.pl/en/knowledge/letter-of-jan-iii-sobieski-to-maria-kazimiera-13-ix-1683"
URL_WIL_BANNER = "https://wilanow-palac.pl/en/knowledge/banner-of-the-grand-vizier-and-the-roman-celebrations-of-john-iii-sobieski-and-the-vienna-victory"
URL_ZPE = "https://zpe.gov.pl/a/jan-iii-sobieski-pod-wiedniem/DKv8YVKq9"
URL_WBLP = "https://literat.ug.edu.pl/autors/sobies.htm"
URL_PH1910 = "https://bazhum.muzhp.pl/media/texts/przeglad-historyczny/1910-tom-10-numer-3/przeglad_historyczny-r1910-t10-n3-s351-371.pdf"
URL_KLU = "https://eeo.uni-klu.ac.at/wwwg.uni-klu.ac.at/eeo/Wien_Belagerung.pdf"
URL_KREUTEL_TDV = "https://islamansiklopedisi.org.tr/kreutel-richard-franz"
URL_KARAMUSTAFA_WGW = "https://www.geschichtewiki.wien.gv.at/Kara_Mustapha"
URL_SILAHDAR = "https://en.wikipedia.org/wiki/Silahdar_Findiklili_Mehmed_Agha"
URL_KULCZ = "https://en.wikipedia.org/wiki/Jerzy_Franciszek_Kulczycki"
URL_IUV = "https://iuv.guide/?p=1424"
URL_BATTLE = "https://en.wikipedia.org/wiki/Battle_of_Vienna"
URL_ELDEBATE = "https://www.eldebate.com/historia/20220828/sitio-viena-1683-iv-defensa_56413_amp.html"
URL_STARH_NDB = "https://www.deutsche-biographie.de/sfz74869.html"
URL_STARH_WP = "https://en.wikipedia.org/wiki/Ernst_R%C3%BCdiger_von_Starhemberg"
URL_AVIANO_AF = "https://austria-forum.org/af/AEIOU/Marco_d´Aviano"
URL_AVIANO_NDB = "https://www.deutsche-biographie.de/sfz58102.html"
URL_DYAK = "https://www.czasopisma.uni.lodz.pl/polonica/article/view/29855"
URL_DYAK_FRAG = "https://moodle.inspire.lab.dariah.pl/pluginfile.php/179/mod_page/content/3/Fragment%20pami%C4%99tnika%20Miko%C5%82aja%20Dyakowskiego.pdf"
URL_HABS = "https://habsburger.net/en/chapter/turk-gates-vienna-episode-2"
URL_KAHL_DE = "https://germanhistorydocs.org/de/das-heilige-roemische-reich-1648-1815/die-schlacht-am-kahlenberge-sieg-der-kaiserlichen-truppen-ueber-die-tuerken-am-12-september-1683-spaetes-17-jahrhundert"
URL_KAHL_EN = "https://germanhistorydocs.org/en/the-holy-roman-empire-1648-1815/the-battle-of-kahlenberg-imperial-troops-defeat-the-turks-on-september-12-1683-late-17th-century"
URL_GEFFELS = "https://germanhistorydocs.org/de/das-heilige-roemische-reich-1648-1815/die-belagerung-wiens-durch-die-tuerken-im-jahre-1683-ca-1685.pdf"

eyes = [
 {
  "id": "teshrifatci", "short": "Ottoman diarist",
  "name": "Anonymous Master of Ceremonies of the Sublime Porte (teşrifatçı)",
  "life": "fl. 1683",
  "role": "Court ceremonial official marching in the Grand Vizier's train; name unknown",
  "side": "Ottoman Empire", "where": "The Grand Vizier's camp west of the walls, then the retreat to Raab, Buda and Belgrade",
  "lat": 48.203, "lon": 16.345,
  "waypoints": [
    {"lat": 47.687, "lon": 17.635, "label": "Raab (Győr), June–July advance"},
    {"lat": 48.203, "lon": 16.345, "label": "Camp before Vienna, 14 July–12 Sept"},
    {"lat": 47.687, "lon": 17.635, "label": "Retreat towards Raab, Sept"},
    {"lat": 44.817, "lon": 20.457, "label": "Belgrade, 25 Dec"}],
  "vantage": 1, "vantage_label": "inside the besieging army's command tent",
  "form": "diary", "language": "Ottoman Turkish",
  "authenticity": "A day-by-day campaign diary in Ottoman Turkish, kept by the Porte's master of ceremonies and preserved in manuscript. Richard F. Kreutel translated it into German as 'Kara Mustafa vor Wien' (1955; revised with Karl Teply, 1982). The diarist's name is unknown. The day-by-day entries take for granted that God favours the Ottoman cause. A closing analysis, written after the defeat, is more self-critical. Following the brief, nothing from it is quoted here, and the exact Hijri day of each entry was not checked against the edition.",
  "bio": "This is the only true day-by-day diary kept on the Ottoman side of the walls. Its author's job was protocol: who stood where, what robes were handed out, how the Vizier received envoys. Those details let us watch the siege as a court on the move. Its ending turns into a cool list of the reasons the campaign failed.",
  "sources": [
    {"title": "R. F. Kreutel (tr.), Kara Mustafa vor Wien: Das türkische Tagebuch der Belagerung Wiens 1683 (1955; rev. with K. Teply 1982), entry on Kreutel, TDV İslâm Ansiklopedisi", "url": URL_KREUTEL_TDV},
    {"title": "Excerpt, Ottoman ceremonial diary (Kreutel/Teply), University of Klagenfurt teaching dossier 'Wien Belagerung'", "url": URL_KLU}]
 },
 {
  "id": "silahdar", "short": "Silahdar",
  "name": "Silahdar Fındıklılı Mehmed Ağa",
  "life": "1658–c.1726",
  "role": "24-year-old page in the palace service who went on the campaign; later the sultan's sword-bearer and a court historian",
  "side": "Ottoman Empire", "where": "With the Ottoman army on the 1683 campaign (his exact post that day is not recorded)",
  "lat": 48.21, "lon": 16.34,
  "vantage": 1, "vantage_label": "Ottoman participant, writing history later",
  "form": "chronicle", "language": "Ottoman Turkish",
  "authenticity": "His Zeyl-i Fezleke (Silahdar Tarihi) is a chronicle arranged year by year, written later from his own memory and from court material. It is not a diary. The Istanbul edition appeared in 1928. It is flagged here as a chronicle. Entries are dated only by year.",
  "bio": "Born in Galata in 1658, Silahdar served in the palace and went on the Vienna expedition himself. His chronicle is a key Ottoman narrative of the year, and it calls the battle a disaster outright. He had been there, but he wrote afterwards as a historian, judging events rather than recording them on the day.",
  "sources": [
    {"title": "Silahdar Findiklili Mehmed Agha (overview; Silahdar Tarihi, Istanbul 1928)", "url": URL_SILAHDAR},
    {"title": "Battle of Vienna: cites Silahdar's verdict on the defeat", "url": URL_BATTLE}]
 },
 {
  "id": "garrison-journal", "short": "Garrison journal",
  "name": "Anonymous officer of the Vienna garrison (journal sent to Ratisbon)",
  "life": "fl. 1683",
  "role": "Officer who stayed in the city through the whole siege; wrote a running journal for the Imperial Commissioner at the Diet of Ratisbon (Regensburg)",
  "side": "Habsburg garrison of Vienna", "where": "On the walls of Vienna, chiefly the Burg and Löbel bastions",
  "lat": 48.2075, "lon": 16.3640,
  "vantage": 1, "vantage_label": "on the walls, day by day",
  "form": "journal", "language": "German (English translation, London 1684)",
  "authenticity": "Printed in London in 1684 as 'A most Particular Account of all that passed in the Late Siege of Vienna', 'translated out of High-Dutch by His Majesties Command'. The officer is not named. Some day numbers in the August and September sections are misprinted, so dates were checked against the order of events. Because the English is a translation, it is not quoted here. It may share material with the other official journals of the siege.",
  "bio": "This officer wrote things down as they happened: two letters of summons left unanswered, a fire in the Schottenhof, mines under the counterscarp, rockets at night. He records small omens with as much care as the assaults: storks overhead, a white pigeon from the enemy camp. He gives the clearest day-by-day view from inside the walls that survives in an early English text.",
  "sources": [
    {"title": "A most Particular Account of all that passed in the Late Siege of Vienna (London: H. Rogers and M. Gylliflower, 1684), EEBO-TCP text", "url": URL_JOURNAL}]
 },
 {
  "id": "vaelckeren", "short": "Vaelckeren",
  "name": "Johann Peter von Vaelckeren",
  "life": "fl. 1683",
  "role": "Imperial official in the besieged city; described as judge-advocate of the Imperial army and as an Imperial councillor of war",
  "side": "Habsburg administration", "where": "Inside Vienna for the whole siege",
  "lat": 48.2088, "lon": 16.3700,
  "vantage": 1, "vantage_label": "official inside the besieged city",
  "form": "diary", "language": "Latin",
  "authenticity": "Published in Latin as 'Vienna a Turcis obsessa, a Christianis eliberata, sive diarium obsidionis Viennensis' (1683; Brussels edition 1684). French and English translations followed in 1684, the English as 'A Relation or Diary of the Siege of Vienna'. It is laid out day by day from 6 May to 15 September 1683. As a printed, officially minded account it should be read as shaped for publication. Its full text was not read for this chapter, so its entries are pinned to dates every source agrees on and are marked approximate.",
  "bio": "Vaelckeren's diary became Europe's standard printed account of the siege. Within a year it was out in Latin, French and English, with plans of the Ottoman camp and of the battle order of 12 September. He wrote as an official: he counts weapons, lists the captured stores and praises the commanders. That makes his account a useful foil to the officer's rougher journal.",
  "sources": [
    {"title": "Cambridge University Library, 'The Siege of Vienna in the Acton Library' (Latin, French and English editions)", "url": URL_ACTON},
    {"title": "A Relation or Diary of the Siege of Vienna (London 1684), bookseller description", "url": URL_INLIBRIS}]
 },
 {
  "id": "hocke", "short": "Hocke",
  "name": "Nikolaus Hocke",
  "life": "fl. 1683–1685",
  "role": "Secretary of Vienna's city council during the siege",
  "side": "City of Vienna (burghers)", "where": "Inside Vienna, at the town hall",
  "lat": 48.2110, "lon": 16.3700,
  "vantage": 1, "vantage_label": "civic official inside the city",
  "form": "diary", "language": "German",
  "authenticity": "His siege account came out in Vienna in 1685, two years after the events, as 'Kurtze Beschreibung dessen, was in wehrender Türckischen Belägerung der Kayserlichen Residentz-Statt Wienn ... passiret'. It is arranged as a diary. For this chapter it was identified from the brief and the bibliography but not opened, so his one entry is a general summary marked approximate. Treat it as a placeholder until the 1685 text is checked.",
  "bio": "Hocke wrote for the city council, not the army: rationing, fire watches, the burgher companies and the death of Mayor Liebenberg. Where Vaelckeren wrote for the court and the officer for the Diet, Hocke wrote for the town.",
  "sources": [
    {"title": "Nikolaus Hocke, Kurtze Beschreibung dessen, was in wehrender Türckischen Belägerung der Kayserlichen Residentz-Statt Wienn ... passiret (Vienna 1685)", "url": ""}]
 },
 {
  "id": "starhemberg", "short": "Starhemberg",
  "name": "Ernst Rüdiger von Starhemberg",
  "life": "1638–1701",
  "role": "Commandant of Vienna, aged 44; led the garrison of about 11,000 soldiers and the burgher militia",
  "side": "Habsburg Monarchy", "where": "On the Burg and Löbel bastions; wounded twice in July",
  "lat": 48.2070, "lon": 16.3645,
  "vantage": 0, "vantage_label": "commander of the besieged city",
  "form": "dated letters", "language": "German",
  "authenticity": "His dated reports and notes to Charles of Lorraine survive in the Vienna archives and in the Habsburg war-history editions, and secondary works cite them. For this chapter his words reach us through the garrison journal and modern summaries, so the digests describe what he did and reported. They do not quote him.",
  "bio": "Starhemberg refused the summons to surrender and was hit by stones twice in the first fortnight. By early September his reports to Lorraine counted the remaining able men in a few thousands. His view is that of the man who had to choose, night after night, which breach to plug with what was left.",
  "sources": [
    {"title": "Neue Deutsche Biographie: Starhemberg, Ernst Rüdiger Graf von", "url": URL_STARH_NDB},
    {"title": "Ernst Rüdiger von Starhemberg (overview)", "url": URL_STARH_WP},
    {"title": "El Debate, 'El sitio de Viena (1683) IV: la defensa' (his 8 September report)", "url": URL_ELDEBATE}]
 },
 {
  "id": "kolschitzky", "short": "Kolschitzky",
  "name": "Georg Franz Kolschitzky (Jerzy Franciszek Kulczycki)",
  "life": "1640–1694",
  "role": "Polish-Ruthenian interpreter and trader who knew Turkish; volunteered as a courier",
  "side": "Habsburg garrison (volunteer)", "where": "Slipped through the Ottoman lines in Turkish dress to Lorraine's camp and back",
  "lat": 48.2085, "lon": 16.3731,
  "waypoints": [
    {"lat": 48.2085, "lon": 16.3731, "label": "Leaves Vienna, mid-Aug"},
    {"lat": 48.27, "lon": 16.45, "label": "Through Ottoman lines to Lorraine across the Danube"},
    {"lat": 48.2085, "lon": 16.3731, "label": "Back in the city, 17 Aug"}],
  "vantage": 1, "vantage_label": "courier crossing the lines",
  "form": "memoir (written later)", "language": "German",
  "authenticity": "His mission is real and the garrison journal records it, though not by name. Later legend grew around him. The story that he founded Vienna's first coffeehouse with captured Ottoman beans was shown in 1980 (Karl Teply) to go back to Gottfried Uhlich in 1783. The Armenian Johannes Diodato (Theodat) is now credited with Vienna's first coffeehouse licence, in 1685. Sources disagree over his departure date by a few days. A short printed account of his journey, attributed to him, has not been verified here. Flagged.",
  "bio": "Kolschitzky's value as an 'eye' lies in the gap between the man and the myth. The record shows a courier with his servant, Đorđe Mihajlović, who walked out through the trenches in Turkish dress and came back with word that relief was coming. A century later, the coffee story made him a Viennese folk hero.",
  "sources": [
    {"title": "Jerzy Franciszek Kulczycki (mission, Mihajlović, Teply's critique of the coffee legend)", "url": URL_KULCZ},
    {"title": "Encyclopedia of Ukraine: Kulchytsky, Yurii Frants", "url": "https://www.encyclopediaofukraine.com/pages%5CK%5CU%5CKulchytskyYuriiFrants.htm"},
    {"title": "iuv.guide biography (gives 15–17 August for the letters)", "url": URL_IUV}]
 },
 {
  "id": "lorraine", "short": "Lorraine",
  "name": "Charles V Leopold, Duke of Lorraine",
  "life": "1643–1690",
  "role": "Imperial field commander, aged 40, brother-in-law of Emperor Leopold I",
  "side": "Habsburg Monarchy / Holy Roman Empire", "where": "With the Imperial field army along the Danube north and east of Vienna; left wing on 12 September",
  "lat": 48.2900, "lon": 16.3500,
  "waypoints": [
    {"lat": 48.1486, "lon": 17.1077, "label": "Pressburg, 27 July"},
    {"lat": 48.3780, "lon": 16.8270, "label": "Angern, 7 Aug"},
    {"lat": 48.3310, "lon": 16.0550, "label": "Tulln, early Sept"},
    {"lat": 48.2620, "lon": 16.3560, "label": "Nussdorf, 12 Sept"}],
  "vantage": 1, "vantage_label": "field commander outside the ring",
  "form": "dated letters", "language": "French / German",
  "authenticity": "His dispatches to the Emperor and his ministers survive and are cited in older Austrian and Polish studies. This chapter uses only dated dispatches it found cited in print: Pressburg 27 July and Angern 7 August. Their content is summarised second-hand.",
  "bio": "Lorraine kept a small army in being while the city was surrounded. He fought Thököly's Hungarians and the Tatars along the Danube, received Kolschitzky's messages and commanded the left wing on the day of the battle. He sees the siege from outside the ring, as a commander waiting for allies.",
  "sources": [
    {"title": "Przegląd Historyczny 10 (1910), pp. 351–371, citing Lorraine's dispatches of 27 July and 7 August", "url": URL_PH1910},
    {"title": "Battle of Vienna (Lorraine's defeat of Thököly at Bisamberg)", "url": URL_BATTLE}]
 },
 {
  "id": "sobieski", "short": "Sobieski",
  "name": "Jan III Sobieski",
  "life": "1629–1696",
  "role": "King of Poland and Grand Duke of Lithuania, aged 54; supreme commander of the relief army",
  "side": "Polish-Lithuanian Commonwealth", "where": "Marched from Kraków, crossed the Danube at Tulln and commanded from the Kahlenberg heights, then the Vizier's tents",
  "lat": 48.2740, "lon": 16.3340,
  "waypoints": [
    {"lat": 50.0614, "lon": 19.9366, "label": "Kraków, 15 Aug"},
    {"lat": 48.3310, "lon": 16.0550, "label": "Tulln, Danube crossing, early Sept"},
    {"lat": 48.2740, "lon": 16.3340, "label": "Kahlenberg, 11–12 Sept"},
    {"lat": 48.2030, "lon": 16.3450, "label": "Vizier's tents, 13 Sept"}],
  "vantage": 0, "vantage_label": "supreme commander of the relief",
  "form": "dated letters", "language": "Polish (with French)",
  "authenticity": "His letters to Queen Marie Casimire ('Marysieńka') survive and are edited by Leszek Kukulski in 'Listy do Marysieńki' (1962); the 13 September 1683 letter is on pp. 520–524. His Latin note to Pope Innocent XI, carried to Rome by his secretary Tommaso Talenti, opens with the well-known 'Venimus, vidimus, Deus vicit'. The other campaign letters (12, 17 and 19 September) are dated as cited in the 1910 Przegląd Historyczny article.",
  "bio": "Sobieski wrote to his wife nearly every day of the campaign, in a private voice full of affection and complaint. On the night after the battle he wrote from inside Kara Mustafa's own tents, listing the plunder as a tired soldier would. Within a week the tone turns sour: horses stolen, allies ungrateful.",
  "sources": [
    {"title": "Wilanów Palace Museum: Letter of Jan III Sobieski to Maria Kazimiera, 13 IX 1683 (English translation by K. Michałowicz)", "url": URL_WIL_LETTER},
    {"title": "Zintegrowana Platforma Edukacyjna: Jan III Sobieski pod Wiedniem (Polish text of the letter)", "url": URL_ZPE},
    {"title": "Wirtualna Biblioteka Literatury Polskiej: Sobieski, Listy", "url": URL_WBLP},
    {"title": "Wilanów: 'Banner of the grand vizier' and the Roman celebrations", "url": URL_WIL_BANNER}]
 },
 {
  "id": "jakub", "short": "Prince Jakub",
  "name": "Jakub Ludwik Sobieski",
  "life": "1667–1737",
  "role": "Eldest son of Jan III, aged 15, riding with his father on the campaign",
  "side": "Polish-Lithuanian Commonwealth", "where": "With the Polish right wing coming down from the Vienna Woods",
  "lat": 48.2420, "lon": 16.3000,
  "vantage": 1, "vantage_label": "teenage prince in the battle",
  "form": "diary", "language": "Latin",
  "authenticity": "A campaign diary in Latin, known as 'Diarium principis Jacobi', which Polish historians have cited since the 19th century. The 1910 Przegląd Historyczny article draws on it for the fighting at Pötzleinsdorf and Dornbach. Only that cited material was seen here. Entries are approximate.",
  "bio": "Jakub fought his first battle beside his father, who in his letters worried constantly about the boy. His diary follows the Polish wing across the hills in the afternoon, so we can set a son's account beside his father's version written the same night.",
  "sources": [
    {"title": "Przegląd Historyczny 10 (1910), citing the Diarium principis Jacobi", "url": URL_PH1910}]
 },
 {
  "id": "aviano", "short": "Marco d'Aviano",
  "name": "Marco d'Aviano (Carlo Domenico Cristofori)",
  "life": "1631–1699",
  "role": "Capuchin friar and preacher, aged 51; papal legate to the relief army and confidant of Leopold I",
  "side": "Papacy / Catholic Church", "where": "With the relief army on the heights above Vienna",
  "lat": 48.2780, "lon": 16.3490,
  "vantage": 1, "vantage_label": "chaplain and peacemaker in the allied camp",
  "form": "dated letters", "language": "Italian",
  "authenticity": "He corresponded with Emperor Leopold I from 1680 until his death, and the letters were edited by Onno Klopp in 1888. Sources disagree on where he said Mass on the morning of the battle: some say the Kahlenberg chapel, others the Leopoldsberg. Here the Mass is marked approximate as to place. None of his letters was read for this chapter.",
  "bio": "Marco kept the jealous princes of the relief army working together and gave the army its sense of crusade. His letters to Leopold also show the private worries of an emperor who had fled his own capital.",
  "sources": [
    {"title": "Austria-Forum (AEIOU): Marco d'Aviano", "url": URL_AVIANO_AF},
    {"title": "Deutsche Biographie: Marco d'Aviano", "url": URL_AVIANO_NDB}]
 },
 {
  "id": "taaffe", "short": "Count Taaffe",
  "name": "Francis Taaffe (later 3rd Earl of Carlingford)",
  "life": "1639–1704",
  "role": "Irish Catholic officer in Imperial service, chamberlain to Charles of Lorraine, aged 44",
  "side": "Habsburg army (Irish émigré)", "where": "In Lorraine's camp and on the left wing on 12 September",
  "lat": 48.2620, "lon": 16.3560,
  "vantage": 1, "vantage_label": "foreign officer in the relief army",
  "form": "dated letters", "language": "English",
  "authenticity": "Printed in London in 1684 as 'Count Taaffe's Letters from the Imperial Camp to his Brother the Earl of Carlingford' (Wing C592), with two letters from a young English volunteer. A CC0 transcription exists in the Oxford Text Archive (EEBO-TCP A34352). The full text could not be opened here, so the entries are summaries of what the published letters cover, dated only to the month. No quotes are given.",
  "bio": "Taaffe was an Irishman serving the Habsburgs, writing home in English to a brother at the Stuart court. His letters took the battle to an English Catholic readership, and they speak for the many exiled Irish soldiers who served in Habsburg armies.",
  "sources": [
    {"title": "Oxford Text Archive A34352: Count Taaffe's letters from the imperial camp (London 1684)", "url": URL_TAAFFE},
    {"title": "Francis Taaffe, 3rd Earl of Carlingford", "url": "https://en.wikipedia.org/wiki/Francis_Taaffe,_3rd_Earl_of_Carlingford"}]
 },
 {
  "id": "london-press", "short": "London press",
  "name": "London news pamphlets (Samuel Crouch, John Smith, 1683)",
  "life": "1683",
  "role": "Anonymous London printers' 'relations' turning Continental letters into English news",
  "side": "England (Julian calendar), news only", "where": "London print shops",
  "lat": 51.5136, "lon": -0.0983,
  "vantage": 4, "vantage_label": "abroad, news in print",
  "form": "press (printed news relations)", "language": "English",
  "authenticity": "Two real 1683 pamphlets: 'A True and Exact Relation of the Raising of the Siege of Vienna' (London: Samuel Crouch), reprinted by Macartney (1970) and online at GHDI, and 'A Particular Account of the Sudden and Unexpected Siege of Vienna', 'made English from the High-Dutch' (London: John Smith). Both put foreign reports into English. They carry rumour along with fact. The press is flagged: these are not eyewitness diaries. They use the Continental dates even though England kept the Julian calendar.",
  "bio": "For readers in London the siege was a summer of rumours, then a triumph in print. These pamphlets show how the news was spun, with Vienna as 'the Key of Germany' and Sobieski as one of the great kings of Christendom, and how much they got wrong.",
  "sources": [
    {"title": "A True and Exact Relation of the Raising of the Siege of Vienna (London 1683), GHDI", "url": URL_TRUE_EN},
    {"title": "Same, PDF", "url": URL_TRUE_PDF},
    {"title": "A Particular Account of the Sudden and Unexpected Siege of Vienna (London 1683), EEBO-TCP text", "url": URL_PARTIC}]
 },
 {
  "id": "dyakowski", "short": "Dyakowski",
  "name": "Mikołaj Dyakowski",
  "life": "c.1660s–after 1730",
  "role": "Young Polish nobleman and royal courtier on the campaign",
  "side": "Polish-Lithuanian Commonwealth", "where": "In the king's entourage on 12 September",
  "lat": 48.2600, "lon": 16.3100,
  "vantage": 1, "vantage_label": "courtier remembering, half a century on",
  "form": "memoir (written later)", "language": "Polish",
  "authenticity": "His 'Diariusz wiedeńskiej okazyi' is titled a diary but was written nearly fifty years later, as a short memoir. Scholars study it as much for its literary shaping as for its facts. Flagged as a later memoir.",
  "bio": "Dyakowski shows how an old man remembered the day of his youth that mattered most: vivid and proud, and sharpened by fifty years of retelling. Set beside Sobieski's letter of the same night, it shows how memory works on an event.",
  "sources": [
    {"title": "'O literackości Diariusza wiedeńskiej okazyji Mikołaja Dyakowskiego', Folia Litteraria Polonica 9 (2007)", "url": URL_DYAK},
    {"title": "Fragment of Dyakowski's memoir (Polish teaching PDF)", "url": URL_DYAK_FRAG}]
 },
]

E = []
def e(date_iso, disp, prec, eye, place, head, dig, conf, note, quote=""):
    E.append({"date_iso": date_iso, "date_display": disp, "precision": prec, "eye": eye, "place": place,
              "headline": head, "digest": dig, "quote": quote, "confidence": conf, "source_note": note})

# --- JULY ---
e("1683-07-07", "Wednesday 7 July 1683", "day", "garrison-journal", "Vienna",
  "Panic in the city as the Emperor leaves by night",
  "False reports that the army had been beaten set off a panic in the streets. That evening, at about eight o'clock, Emperor Leopold and his court left the city, and crowds of people fled after them. The officer notes that the Turks did not chase the refugees, a relief he records almost in passing.",
  "verified", "Journal, entry 'On the 7.' (EEBO-TCP A46317)")
e("1683-07-07", "Wednesday 7 July 1683", "day", "vaelckeren", "Vienna",
  "The court departs; the officials who stay begin their count",
  "Vaelckeren's diary, which begins in May, marks the Emperor's departure for Linz and Passau as the moment the city was left to its commandant. From here on he writes as one of the officials left behind, counting what the city had to defend itself with.",
  "approx", "Diarium obsidionis Viennensis (runs 6 May–15 Sept 1683), per Cambridge Acton Library description; detail not checked in the text")
e("1683-07-13", "Tuesday 13 July 1683", "day", "garrison-journal", "Vienna, bastions",
  "Turkish horsemen on the heights; summons left unanswered",
  "Large bodies of Ottoman troops gathered on the high ground outside the town and were driven back by cannon from the bastions. Two letters summoning the city to surrender were left for Count Starhemberg. The officer notes that the commandant did not reply.",
  "verified", "Journal, entry 'On the 13.'")
e("1683-07-14", "Wednesday 14 July 1683", "day", "teshrifatci", "Camp before Vienna",
  "The army reaches Vienna and the Vizier's tents go up",
  "The diarist records the army's arrival before the city after weeks of marching and plundering up the Danube from Raab. To him the day is mostly ceremony: the Grand Vizier's great tent is set up, the pashas and the Tatar contingents are assigned their places, and the formal call to surrender is sent in. He writes with complete confidence that the city will fall.",
  "approx", "Kreutel tr., Kara Mustafa vor Wien; Ottoman arrival on 14 July confirmed by all sources, entry wording not consulted (c. 19 Receb 1094)")
e("1683-07-14", "Wednesday 14 July 1683", "day", "garrison-journal", "Vienna",
  "The Turkish camp spreads around the walls",
  "The Ottomans widened their camp and moved their lines round towards the Rote Hof. The officer watched them lay out their siege works about two hundred paces from the counterscarp, ready to open the trenches that night.",
  "verified", "Journal, entry 'On the 14.'")
e("1683-07-14", "Wednesday 14 July 1683", "day", "starhemberg", "Vienna, Burg bastion",
  "The commandant refuses to surrender",
  "Starhemberg took the Ottoman summons and did not answer it, which in the customs of siege warfare meant no quarter if the city were stormed. He had already burned the suburbs outside the glacis to clear the field of fire, leaving the besiegers nothing to shelter behind.",
  "approx", "Battle of Vienna (surrender demand 14 July, refused); Starhemberg biography gives 15 July; journal 13 July")
e("1683-07-15", "Thursday 15 July 1683", "day", "garrison-journal", "Vienna, Löbel bastion",
  "Trenches opened, a fire at the Schottenhof, the commandant hit",
  "The Turks opened their trenches and began firing on the Burg (Court) bastion. A fire broke out at the Schottenhof, and in their fear the townspeople blamed arsonists; several suspects were killed by crowds. Starhemberg was hit on the head by a stone on the Löbel bastion and stayed indoors for several days.",
  "verified", "Journal, entry 'On the 15.'")
e("1683-07-23", "Friday 23 July 1683", "day", "garrison-journal", "Vienna, counterscarp",
  "The first mines under the counterscarp",
  "Two mines went off near the outer angle of the counterscarp in front of the Löbel and Burg bastions. Each assault that followed was beaten back, and the attackers gained no ground. The officer writes about this new kind of war, fought under the ground, quite calmly.",
  "verified", "Journal, entry 'On the 23.'")
e("1683-07-25", "Sunday 25 July 1683", "day", "garrison-journal", "Vienna, Burg ravelin",
  "A mine at the ravelin; three assaults; Starhemberg wounded again",
  "A mine was sprung on the counterscarp near the ravelin in front of the Burg gate, and three assaults followed, all beaten back. Several officers were killed, and Starhemberg was wounded in the hand by a stone.",
  "verified", "Journal, entry 'On the 25th.'")
e("1683-07-25", "Sunday 25 July 1683", "day", "starhemberg", "Vienna, Burg ravelin",
  "Wounded in the hand, still on the ravelin",
  "For the second time in ten days the commandant was hit, this time a stone to the hand during the fight for the ravelin. He stayed in command. The garrison journal shows him on the bastions again within days.",
  "verified", "Journal, entry 'On the 25th.'; El Debate on the 25 July mine")
e("1683-07-27", "Tuesday 27 July 1683", "day", "lorraine", "Pressburg (Bratislava)",
  "Polish horse fight alone near Pressburg",
  "In a dispatch from Pressburg, Lorraine reported a sharp fight in which Polish cavalry serving with his army had taken on Hungarian rebels and Turks unsupported. He was trying to hold the Danube crossings east of Vienna against Thököly's Kuruc forces.",
  "verified", "Lorraine to the court, Pressburg 27 July 1683, as cited in Przegląd Historyczny 10 (1910)")
# --- AUGUST ---
e("1683-08-04", "Wednesday 4 August 1683", "day", "garrison-journal", "Vienna",
  "A Pole slips in with news of the relief",
  "A Polish man got through the lines into the town with news that a Polish party had fought the Turks and that a relief army was gathering. He brought news in but carried nothing out. The officer notes that the defenders were desperate for any word from outside.",
  "verified", "Journal, entry 'On the 4th.' (August)")
e("1683-08-07", "Saturday 7 August 1683", "day", "lorraine", "Angern, Marchfeld",
  "Six hundred horse scatter four thousand Hungarians",
  "Writing from Angern on the Marchfeld, Lorraine reported that about six hundred Polish horse under Grocholski had routed a much larger body of Thököly's Hungarians. Small wins like this kept the north bank of the Danube open for the allies who were coming.",
  "verified", "Lorraine, Angern 7 August 1683, as cited in Przegląd Historyczny 10 (1910)")
e("1683-08-12", "Thursday 12 August 1683", "day", "garrison-journal", "Vienna, Burg ravelin",
  "Afternoon storm repulsed; the garrison paid",
  "In the afternoon the Turks stormed part of the defences but fell back when they met resistance; elsewhere it is reported that a mine had opened part of the ravelin, where the attackers kept a foothold. The officer also notes that the garrison was given another half-month's pay. Money still mattered in the fourth week of the siege.",
  "verified", "Journal, entry 'On the 12th.' (August); El Debate on the 12 August mine at the ravelin")
e("1683-08-13", "13–17 August 1683", "range", "kolschitzky", "Through the Ottoman lines to Lorraine's camp and back",
  "In Turkish dress through the siege lines",
  "Kolschitzky and his servant Mihajlović left the city disguised as Ottoman subjects, crossed the trenches and the camp, and reached Lorraine with Starhemberg's letters. He came back with Lorraine's promise that relief was on its way. Sources disagree by a couple of days on when he left; most put it on the night of 13 August. His return on the 17th is borne out by the garrison journal.",
  "approx", "Kulczycki biography; iuv.guide (letters delivered 15 Aug, return 17 Aug); journal 'On the 17.'")
e("1683-08-17", "Tuesday 17 August 1683", "day", "garrison-journal", "Vienna",
  "The messenger returns; three rockets in the night",
  "The man sent out for news came back with word that relief was certain. That night three rockets went up to tell the friendly forces outside that he had made it in. The officer never names the messenger, but the dates match Kolschitzky's mission.",
  "verified", "Journal, entry 'On the 17.' (August)")
e("1683-08-23", "Monday 23 August 1683", "day", "garrison-journal", "Vienna",
  "Another courier: relief by the end of the month",
  "A second messenger, sent out a few nights earlier with signals to mark his crossing, came back promising relief by the end of August. The officer passes the promise on without comment, but his entries show the garrison living on these messages.",
  "verified", "Journal, entries 'On the 20th.' and 'On the 23.' (August)")
e("1683-08-15", "15 August 1683", "day", "sobieski", "Kraków",
  "The King sets out from Kraków",
  "Sobieski left Kraków with the Polish army on the feast of the Assumption, beginning a forced march through Silesia and Moravia. His letters to the Queen continue along the road, giving her a running account of the march.",
  "approx", "Departure 15 Aug: Battle of Vienna; content of road letters general, per Listy do Marysieńki (not consulted entry by entry)")
# --- SEPTEMBER ---
e("1683-09-03", "Friday 3 September 1683", "day", "garrison-journal", "Vienna, Burg ravelin",
  "Storks over the town; the ravelin given up",
  "Eight storks flew over the town from the Kahlenberg, and the garrison took it as a good omen. That night the defenders abandoned the ravelin and the caponiers they had held for weeks and set them on fire, and the Ottomans moved in. Both events sit side by side in the same entry.",
  "verified", "Journal, entry '3rd.' (September)")
e("1683-09-04", "Saturday 4 September 1683", "day", "garrison-journal", "Vienna, Burg bastion",
  "The great mine opens the Burg bastion",
  "A great mine blew out part of the right face of the Burg bastion, and the Ottomans stormed into the gap. After about an hour and a half of fighting they kept a foothold in the breach. That night the garrison sent out another messenger.",
  "verified", "Journal, entry '4th.' (September)")
e("1683-09-06", "Monday 6 September 1683", "day", "garrison-journal", "Vienna, Löbel bastion",
  "Mines bring down both faces of the Löbel bastion",
  "Mines toppled both faces of the Löbel bastion. The Ottomans attacked but gave up the position, partly because the broken ground gave them no footing and partly because of heavy fire from the walls. Two bastions on the same front were now breached.",
  "verified", "Journal, entry '6th.' (September)")
e("1683-09-06", "6 September 1683", "day", "sobieski", "Tulln, on the Danube",
  "The Polish army crosses the Danube at Tulln",
  "On the same day that the Löbel bastion was coming down twenty miles away, the King's army was crossing the Danube at Tulln to join the Imperial and German forces. His letters to the Queen kept up their near-daily rhythm through the crossing.",
  "approx", "Tulln crossing dated 6 Sept in Battle of Vienna; letter content general")
e("1683-09-06", "Early September 1683", "range", "lorraine", "Tulln",
  "The allied armies meet at Tulln",
  "Lorraine's Imperial corps, the Saxons, Bavarians and Franconians met the Polish army around Tulln, and the commanders agreed the plan of attack over the Vienna Woods. Lorraine accepted Sobieski as supreme commander, which allowed a crowned king to lead the allied army.",
  "approx", "Battle of Vienna; date range of the council not pinned to a day here")
e("1683-09-08", "Wednesday 8 September 1683", "day", "starhemberg", "Vienna",
  "About four thousand fit men, little powder, more mines coming",
  "Starhemberg reported to Lorraine that he had about four thousand men still fit for duty, that gunpowder was running low, and that at least five more mines were being dug towards the ditch. The garrison had beaten off more than twenty assaults. His message was that the city could not hold much longer.",
  "approx", "Report summarised in El Debate (8 Sept); exact wording and date of dispatch not checked against archive")
e("1683-09-08", "Wednesday 8 September 1683", "day", "garrison-journal", "Vienna, Löbel bastion",
  "Case-shot holds the Löbel flank; fires on the hills",
  "Two more mines went off at the lower flank of the Löbel bastion, and both assaults were driven back by cannon firing case-shot. That night many fires were seen on the hills to the west, and the officer hoped they meant the relief army was there.",
  "verified", "Journal, entry '8th.' (September)")
e("1683-09-09", "Thursday 9 September 1683", "day", "garrison-journal", "Vienna",
  "A white pigeon from the enemy camp",
  "Most of the Ottoman army was seen drawn up facing the woods rather than the walls, and a prisoner described great dismay in the camp. A white pigeon flew into the town from the enemy lines, another omen that the officer records.",
  "verified", "Journal, entry '9th.' (September)")
e("1683-09-10", "c. 10 September 1683", "day", "hocke", "Vienna, town hall",
  "The council's secretary keeps the town's account",
  "Hocke's diary follows the siege from the town's side: burgher companies on the walls, rationing, dysentery, and the death of Mayor Johann Andreas von Liebenberg in the last days before the relief. This digest is a placeholder summary of the 1685 diary's scope; its day entries were not checked for this chapter.",
  "approx", "Hocke, Kurtze Beschreibung (Vienna 1685); Liebenberg's death in early September per standard accounts; not checked in the text")
e("1683-09-11", "Saturday 11 September 1683", "day", "garrison-journal", "Vienna",
  "Troops on the Kahlenberg; rockets answer rockets",
  "In the afternoon the Ottomans pulled troops back from the trenches towards the hills, bringing men over the bridges from the Leopoldstadt. The garrison saw troops coming down from the Kahlenberg, and that night fires and rockets signalled that the relief army had arrived. The officer could see the battle forming before it began.",
  "verified", "Journal, entry '11th.' (September)")
e("1683-09-11", "Saturday 11 September 1683", "day", "sobieski", "Kahlenberg heights",
  "On the heights, looking down on the Turkish camp",
  "Having led his army over the wooded ridges of the Vienna Woods, Sobieski reached the heights by the Kahlenberg. From there he could see the city and the huge Ottoman camp below, its trenches turned towards the walls rather than towards the hills.",
  "approx", "Arrival on the heights 11 Sept: Battle of Vienna, GHDI painting description; letter content general")
e("1683-09-12", "Sunday 12 September 1683", "day", "aviano", "Kahlenberg (or Leopoldsberg) chapel",
  "Mass before dawn on the hill",
  "Before the attack, Marco d'Aviano said Mass for the commanders in a ruined chapel on the heights; Sobieski is said to have served at it. Sources disagree on whether it was on the Kahlenberg or the Leopoldsberg. To him the battle was a crusade and he blessed the troops as one.",
  "approx", "Austria-Forum (Leopoldsberg); polishhistory.pl (Kahlenberg, St Joseph's chapel)")
e("1683-09-12", "Sunday 12 September 1683, before dawn", "day", "sobieski", "Kahlenberg",
  "A note at three in the morning: we attack at dawn",
  "In a short letter written in the small hours, Sobieski told the Queen that the army would go down towards Nussdorf at first light. It is the last thing he wrote before the battle.",
  "approx", "Letter of 12 Sept 1683 (about 3 a.m.) as cited in Przegląd Historyczny 10 (1910); details of content partly general")
e("1683-09-12", "Sunday 12 September 1683", "day", "lorraine", "Nussdorf–Heiligenstadt",
  "The left wing fights down the vineyards to Nussdorf",
  "The Imperial left under Lorraine took the brunt of the morning fighting. By midday it had cleared Nussdorf and Heiligenstadt along the Danube, then waited for the Poles to come out of the woods on the right before the whole line moved forward.",
  "approx", "Sequence from Battle of Vienna (Nussdorf and Heiligenstadt taken by midday); Lorraine's own report not consulted")
e("1683-09-12", "Sunday 12 September 1683", "day", "jakub", "Pötzleinsdorf–Dornbach",
  "The Polish wing comes out of the woods",
  "The fifteen-year-old prince's diary follows the Polish wing through the hills around Pötzleinsdorf and Dornbach in the afternoon. It shows his father directing the attack wherever the fire was heaviest. The diary gives places and movements, not feelings.",
  "approx", "Diarium principis Jacobi, as cited in Przegląd Historyczny 10 (1910)")
e("1683-09-12", "Sunday 12 September 1683", "day", "teshrifatci", "Ottoman camp",
  "Word at dawn; five or six hours of fighting; the rout",
  "Early in the morning word reached the camp that the Christians were advancing, and the Grand Vizier led the army out to meet them. After five or six hours of fighting the line broke. The diarist notes bitterly that the Tatar khan gave the flank no real help. He describes the flight back through the camp and on towards Raab.",
  "verified", "Kreutel/Teply excerpt, Klagenfurt dossier 'Wien Belagerung' (Sunday 12 September; c. 20 Ramazan 1094)")
e("1683-09-12", "Sunday 12 September 1683", "day", "garrison-journal", "Vienna, on the walls",
  "From the walls: the relief breaks the camp",
  "At daybreak the relief army attacked. The officer watched from the walls as the Ottomans fell back to their camp, and by about four in the afternoon they had abandoned it with their cannon, stores and baggage. Count Auersperg rode off to tell the Emperor.",
  "verified", "Journal, entry '12th.' (September)")
e("1683-09-12", "Sunday 12 September 1683", "day", "taaffe", "Lorraine's wing",
  "An Irish officer writes home about the relief",
  "Taaffe's letters to his brother describe the great battles before and during the lifting of the siege from his place in Lorraine's army. They were printed in London the next year to show English readers that their countrymen had been there. This entry summarises the published letters, which were not read in full for this chapter.",
  "approx", "Count Taaffe's Letters from the Imperial Camp (London 1684), OTA A34352 catalogue summary")
e("1683-09-12", "Sunday 12 September 1683", "year", "silahdar", "With the Ottoman army",
  "An Ottoman courtier calls it a disaster",
  "In his later chronicle Silahdar calls the defeat at Vienna a disaster without qualification, the worst the empire had suffered. Writing as a court historian, he blames bad command and the Grand Vizier's choices rather than fate.",
  "approx", "Silahdar Tarihi, as cited in Battle of Vienna; chronicle, written later")
e("1683-09-12", "Sunday 12 September 1683", "year", "dyakowski", "In the King's suite",
  "Fifty years on, a courtier remembers the charge",
  "Writing as an old man around 1730, Dyakowski remembered riding in the King's suite on the great day. His account has the colour and confidence of a story told many times. Scholars read it as much for how a Polish noble shaped the memory of the battle as for its facts.",
  "approx", "Folia Litteraria Polonica 9 (2007) on the Diariusz wiedeńskiej okazyi")
e("1683-09-12", "Sunday 12 September 1683", "day", "london-press", "London (from foreign letters)",
  "London learns the city was relieved on Sunday",
  "The Crouch pamphlet tells English readers that the sixty-day siege had brought Vienna almost to its last gasp, with its palaces wrecked by the guns. It then describes the relief army coming down from the hills and the Grand Vizier's flight. Sobieski gets the greatest share of the glory, and an unverified tale about a Turkish commander's execution is passed on as fact.",
  "verified", "A True and Exact Relation (London: Samuel Crouch, 1683), GHDI", quote="The City was relieved on Sunday")
e("1683-09-13", "Monday 13 September 1683", "day", "sobieski", "In the Vizier's tents",
  "Writing to Marysieńka from the Vizier's own tents",
  "That night, in Kara Mustafa's abandoned tents, Sobieski wrote to the Queen that God had given the victory. The guns, the camp and riches beyond counting had fallen to them, and the Vizier had fled with one horse and one coat. He describes the size of the tents, with baths, gardens and animals, and says the Grand Vizier's standard will go to the Pope. He also reports that the Ottoman attack fell on his own right wing.",
  "verified", "Listy do Marysieńki, ed. Kukulski (1962), pp. 520–524; Wilanów translation; ZPE")
e("1683-09-13", "c. 13 September 1683", "day", "sobieski", "Vienna",
  "Venimus, vidimus, Deus vicit",
  "In a short Latin letter to Pope Innocent XI he turned Caesar's boast into a statement of faith: we came, we saw, God conquered. His secretary Talenti left Vienna with the letter and a captured green-and-red banner on 13 September and reached Rome on the 25th, where the banner was later hung in St Peter's.",
  "approx", "Wilanów, 'Banner of the grand vizier' (Talenti left 13 Sept, arrived 25 Sept)", quote="Venimus, vidimus, Deus vicit")
e("1683-09-13", "Monday 13 September 1683", "day", "garrison-journal", "Vienna",
  "The King and the Electors tour the broken walls",
  "The Electors, the King of Poland and the Duke of Lorraine walked the ruined defences and praised Starhemberg and his garrison. The King went to give thanks at the Loreto chapel. Starhemberg had the abandoned Ottoman powder and stores brought into the town, the journal's last practical act.",
  "verified", "Journal, entry '13th.' (September)")
e("1683-09-14", "Tuesday 14 September 1683", "day", "london-press", "London (from foreign letters)",
  "The Emperor comes home through the Stuben Gate",
  "The pamphlet follows Leopold back down the Danube to his damaged capital and through the Stuben gate. It describes his return as a triumph, without asking why he had left.",
  "verified", "A True and Exact Relation (1683), entry 'On the Fourteenth'", quote="entred the City at the Stuben Gate")
e("1683-09-15", "Wednesday 15 September 1683", "day", "london-press", "London (from foreign letters)",
  "Two monarchs on horseback, and a cool meeting",
  "The pamphlet stages the meeting of Emperor and King as a scene of mutual compliments on horseback in front of the Polish army. Other sources, including Sobieski's own letters, remember it as stiff and awkward, a quarrel over precedence played out in public.",
  "verified", "A True and Exact Relation (1683), entry 'On the fifteenth'", quote="complimented each other upon the Victory")
e("1683-09-15", "15 September 1683", "day", "vaelckeren", "Vienna",
  "The diary ends with an inventory of the captured camp",
  "Vaelckeren's diary closes on 15 September. It includes long lists of the weapons, ammunition and equipment found in the Ottoman camp, a final count by an official who had spent two months counting what was left. The lists became one of the most reprinted parts of the book.",
  "approx", "Cambridge Acton Library description (diary ends 15 Sept; inventory of captured stores)")
e("1683-09-17", "17 September 1683", "day", "sobieski", "Camp near Vienna",
  "Stolen horses and sour gratitude",
  "Within five days the triumph had soured. Sobieski complained to the Queen about the share of the spoils and that Viennese townsmen had been stealing Polish horses from the pastures. His letters from these days are full of grievances against the allies.",
  "approx", "Letter of 17 Sept 1683 as cited in Przegląd Historyczny 10 (1910)")
e("1683-09-19", "Sunday 19 September 1683", "day", "london-press", "London (from foreign letters)",
  "Clearing the rubble; the Emperor leaves for Linz",
  "The pamphlet's last Vienna entries have the Emperor leaving again for Linz and the city starting to clear rubble and bury the dead. It then follows the pursuit of the Ottomans towards Pressburg.",
  "verified", "A True and Exact Relation (1683), 'September 19th'")
e("1683-12-25", "Saturday 25 December 1683 (c. 6 Muharrem 1095)", "day", "teshrifatci", "Belgrade",
  "The seal, the banner, the cord: Kara Mustafa's end",
  "Officials came from Istanbul to Belgrade to take back the seal of office, the sacred banner and the key of the Kaaba from the Grand Vizier. After finishing his prayers, Kara Mustafa was strangled. The diarist records the end of his master without comment. His closing analysis blames merchants who fled with their loot, the exhausting sixty days of mining, horses without barley for two months, and failure to give God thanks for earlier success.",
  "verified", "Kreutel/Teply excerpt, Klagenfurt dossier; execution date 25 Dec also Battle of Vienna")

convergences = [
 {"date": "1683-07-14", "label": "Encirclement: the Ottoman army arrives and the summons is refused",
  "eyes": ["teshrifatci", "garrison-journal", "starhemberg"],
  "note": "The same day from both sides. The Ottoman diarist records tents, ranks and the formal summons. The garrison officer records siege works laid out two hundred paces from the counterscarp. Starhemberg's silence answers the summons. Each side treats it as the start of a procedure whose rules both know."},
 {"date": "1683-08-17", "label": "The courier returns: Kolschitzky and three rockets",
  "eyes": ["kolschitzky", "garrison-journal", "lorraine"],
  "note": "The officer's 'messenger' and the legend's Kolschitzky are the same night seen twice. One is an unnamed informer in a terse journal, the other a hero whom a century of storytelling credits with bringing coffee to Vienna."},
 {"date": "1683-09-04", "label": "The August–September mines break the Burg and Löbel bastions",
  "eyes": ["garrison-journal", "starhemberg", "teshrifatci"],
  "note": "The garrison counts each mine and each repulse. Starhemberg counts his remaining men. The Ottoman diarist, looking back, counts the cost: sixty days under the ground wore out the besiegers as well."},
 {"date": "1683-09-06", "label": "Same day, twenty miles apart: Löbel bastion falls, the Poles cross at Tulln",
  "eyes": ["garrison-journal", "sobieski", "lorraine"],
  "note": "Inside, both faces of the Löbel bastion come down. Upstream, the relief armies cross the Danube. Neither side can see the other, and the city only learns of the crossing from rockets and fires."},
 {"date": "1683-09-12", "label": "The battle of the Kahlenberg",
  "eyes": ["aviano", "sobieski", "lorraine", "jakub", "teshrifatci", "garrison-journal", "silahdar", "dyakowski", "taaffe", "london-press"],
  "note": "The heart of the chapter. One day is told as a Mass, a 3 a.m. note, a teenager's itinerary, a five-to-six-hour defeat with an unhelpful Tatar khan, a view from the walls, a historian's 'disaster', an old courtier's memory and a London headline. They agree on the outcome and disagree about who did the fighting."},
 {"date": "1683-09-13", "label": "The morning after: tents, walls and a letter to Rome",
  "eyes": ["sobieski", "garrison-journal", "london-press"],
  "note": "Sobieski writes privately from the Vizier's tents and publicly to the Pope. The garrison journal shows the princes touring the ruins. London later turns it all into a story of royal compliments."},
]

ties = [
 {"a": "teshrifatci", "b": "starhemberg", "kind": "opposite sides", "note": "The diarist recorded the summons sent from the Vizier's tent; Starhemberg was the man who refused it."},
 {"a": "kolschitzky", "b": "lorraine", "kind": "met", "note": "Kolschitzky carried Starhemberg's letters through the lines to Lorraine and came back with his reply."},
 {"a": "kolschitzky", "b": "garrison-journal", "kind": "mentioned", "note": "The journal's unnamed 'messenger' who returned on 17 August, greeted by three rockets, fits Kolschitzky's mission."},
 {"a": "sobieski", "b": "jakub", "kind": "relative", "note": "Father and fifteen-year-old son rode together; the King's letters fret about the boy while the boy's diary follows the King."},
 {"a": "sobieski", "b": "lorraine", "kind": "met", "note": "Lorraine accepted Sobieski's supreme command at Tulln and led the left wing under him on 12 September."},
 {"a": "aviano", "b": "sobieski", "kind": "met", "note": "Marco d'Aviano said Mass on the heights before the battle, with the King reportedly serving."},
 {"a": "taaffe", "b": "lorraine", "kind": "met", "note": "Taaffe was Lorraine's chamberlain and wrote from his camp."},
 {"a": "sobieski", "b": "teshrifatci", "kind": "opposite sides", "note": "Sobieski slept in the Grand Vizier's tents on the night of 13 September; the diarist was fleeing towards Raab with the tents' owner."},
 {"a": "vaelckeren", "b": "garrison-journal", "kind": "same street", "note": "Two official diaries written inside the same walls for different readers, the Imperial court and the Diet at Ratisbon."},
 {"a": "dyakowski", "b": "sobieski", "kind": "met", "note": "Dyakowski rode in the King's suite and wrote his memoir of the day about fifty years after Sobieski's own letter."},
 {"a": "london-press", "b": "taaffe", "kind": "read each other", "note": "Both brought the siege to London readers within a year: the press through translated relations, Taaffe through letters his brother had printed."},
 {"a": "silahdar", "b": "teshrifatci", "kind": "same street", "note": "Two Ottoman courtiers on the same campaign, one keeping a diary on the day, the other writing history years later."},
]

threads_out = [
 {"to": "constantinople-1453", "note": "Kara Mustafa marched under the sacred banner and seal of an empire whose capital Mehmed II had taken in 1453. Vienna was the long-promised 'red apple' beyond that conquest. When the Porte reclaimed the seal and banner in Belgrade on 25 December 1683, it closed the age of Ottoman expansion that 1453 had opened. Both chapters turn on giant siege guns and on mining under the walls."},
 {"to": "v1:thirty-years", "note": "The relief army was the Holy Roman Empire that the Thirty Years' War and the Peace of Westphalia had left behind. The Electors of Saxony and Bavaria brought their own standing armies, as princes with rights they had won in 1648. Lorraine and Starhemberg came out of the Habsburg military establishment that had grown up in that war. The siege also reversed 1618–48 in one way: Catholic emperor, Lutheran Saxony and Catholic Poland fought on the same side."},
 {"to": "v1:long-threads", "note": "The story of coffee arriving with captured Ottoman sacks, credited to Kolschitzky, is an 18th-century invention. Vienna's first licensed coffeehouse (Diodato, 1685) belongs to a longer thread of Ottoman goods and tastes passing into European daily life after the siege."},
]

images = [
 {"url": URL_KAHL_EN, "title": "The Battle of Kahlenberg: Imperial troops defeat the Turks on 12 September 1683", "caption": "Late-17th-century oil painting. Sobieski on horseback leads the relief army down the hills, with St Stephen's Cathedral in the distance. It shows the view from the Kahlenberg described in the King's letters.", "date": "late 17th century", "credit": "Unknown artist; bpk-Bildagentur / Reinhard Krafft (GHDI)"},
 {"url": URL_KAHL_DE, "title": "Die Schlacht am Kahlenberge (German GHDI page)", "caption": "The same painting on the German-language GHDI page, which gives the bpk image number.", "date": "late 17th century", "credit": "Unknown artist; bpk-Bildagentur"},
 {"url": URL_GEFFELS, "title": "Franz Geffels, Die Entsatzschlacht Wiens 1683", "caption": "A panorama of the relief battle by Franz Geffels, painted within a few years of the event. It shows the ring of trenches, the Ottoman camp and the allied advance at the same time.", "date": "c. 1683–1694", "credit": "Franz Geffels; Wien Museum, Inv. 40132"},
 {"url": URL_HABS, "title": "Turkish plan of the Second Siege of Vienna; Merian's view of the Ottoman camp", "caption": "The Habsburger.net chapter shows an Ottoman coloured pen-and-ink siege plan beside Matthäus Merian the Younger's perspective plan of the camp, so the siege can be seen from both sides of the trenches.", "date": "1683", "credit": "Ottoman draughtsman; Matthäus Merian the Younger (via habsburger.net)"},
 {"url": URL_WIL_LETTER, "title": "Sobieski's letter to Marie Casimire, 13 September 1683", "caption": "Wilanów Palace Museum's presentation of the letter written in the Vizier's tents, with an English translation.", "date": "13 September 1683", "credit": "Muzeum Pałacu Króla Jana III w Wilanowie"},
 {"url": URL_WIL_BANNER, "title": "The 'banner of the grand vizier'", "caption": "The red-and-green brocade banner Talenti carried to Rome with the 'Venimus, vidimus, Deus vicit' letter, hung in St Peter's on 17 October 1683.", "date": "1683", "credit": "Muzeum Pałacu Króla Jana III w Wilanowie"},
]

further = [
 {"title": "A most Particular Account of all that passed in the Late Siege of Vienna (London 1684), full text", "url": URL_JOURNAL},
 {"title": "A True and Exact Relation of the Raising of the Siege of Vienna (London 1683), GHDI", "url": URL_TRUE_EN},
 {"title": "German translation of the same, GHDI document 3580", "url": URL_TRUE_DE},
 {"title": "Cambridge University Library: The Siege of Vienna in the Acton Library", "url": URL_ACTON},
 {"title": "Wien Geschichte Wiki: Kara Mustafa", "url": URL_KARAMUSTAFA_WGW},
 {"title": "Battle of Vienna (overview with Ottoman casualty documents)", "url": URL_BATTLE},
]

chapter = {
 "id": "vienna-1683",
 "title": "Vienna Besieged",
 "subtitle": "The Ottoman siege and relief of Vienna, 14 July – 12 September 1683",
 "span": "July–December 1683",
 "intro": [
  "On 14 July 1683 Grand Vizier Kara Mustafa Pasha's army pitched its tents around Vienna, the Habsburg capital, a week after Emperor Leopold I had fled up the Danube. For sixty days about 11,000 soldiers and the city's burgher militia under Count Ernst Rüdiger von Starhemberg held the walls. The besiegers dug mines under the Burg and Löbel bastions, while plague, dysentery and fire spread inside. On 12 September a relief army of Imperial, German and Polish troops under King Jan III Sobieski came down from the Kahlenberg and broke the Ottoman camp in an afternoon.",
  "This chapter sets the siege beside itself. Inside the walls are an anonymous garrison officer whose day-by-day journal was printed in London in 1684, the Imperial official Johann Peter von Vaelckeren and the city secretary Nikolaus Hocke. On the walls is the commandant himself. Kolschitzky crossed the lines and became a legend. Outside the ring are Charles of Lorraine, the Irish officer Francis Taaffe, the Capuchin Marco d'Aviano, and Sobieski and his fifteen-year-old son Jakub. On the other side of the trenches is a rare voice: the Ottoman master of ceremonies, whose campaign diary runs from the march to the Grand Vizier's execution in Belgrade.",
  "Much of the honest record is not diary in the strict sense. Sobieski, Starhemberg, Lorraine, Taaffe and Marco d'Aviano survive as dated letters and dispatches. Silahdar Fındıklılı Mehmed Ağa, who marched with the Ottoman army, wrote a chronicle afterwards. Dyakowski's 'diary' is a memoir written fifty years on. The London pamphlets are press, turning foreign letters into English news with rumour mixed in. Each eye carries its form tag, and the weaker ones are flagged in their notes.",
  "Some voices are missing, and the gaps are worth stating. No diary by a Crimean Tatar on the campaign, or by anyone in Imre Thököly's Hungarian Kuruc army, turned up in this research; the Tatars appear only through the Ottoman diarist's complaint that the khan held back. Evliya Çelebi, often quoted on Vienna, described an earlier embassy of 1665, not this siege, and is left out. The Viennese poor, the refugees and the tens of thousands of villagers killed or carried off by raiders in the countryside left no diaries that we could find.",
  "Read the clusters together. On 14 July a protocol officer and a garrison officer describe the same opening moves of a siege. On 6 September the Löbel bastion falls inside the city while the Poles cross the Danube twenty miles away. On 12 September one battle is told as a Mass, a 3 a.m. note, a teenager's itinerary, a rout, a view from the walls and a London headline."
 ],
 "calendar_note": "All dates are Gregorian (New Style), the calendar of the Habsburg lands, Poland and the papacy in 1683, and date_iso uses them directly. England still used the Julian calendar, ten days behind (12 September N.S. = 2 September O.S.). The London pamphlets nevertheless print the Continental dates from their foreign letters, and those dates are kept here. The Ottoman diary was dated by the Hijri calendar. The siege began about 19 Receb 1094, the battle was about 20 Ramazan 1094, and Kara Mustafa was executed about 6 Muharrem 1095. These conversions use the tabular Islamic calendar and may be a day off. Where only the year is certain (Silahdar's chronicle, Dyakowski's memoir), precision is set to 'year' even though the entry is filed under the battle day.",
 "eyes": eyes,
 "entries": sorted(E, key=lambda x: x["date_iso"]),
 "convergences": convergences,
 "ties": ties,
 "threads_out": threads_out,
 "images": images,
 "further": further,
 "vantage_key": "0 = principal commanders (Starhemberg inside, Sobieski outside); 1 = eyewitnesses on the walls, in the camps or in the battle; 2 = elsewhere in or near Vienna; 3 = elsewhere in the Habsburg or Ottoman lands; 4 = abroad, news only (the London press)."
}

json.dump(chapter, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
ids = {x["id"] for x in eyes}
assert all(en["eye"] in ids for en in E)
assert all(all(i in ids for i in c["eyes"]) for c in convergences)
assert all(t["a"] in ids and t["b"] in ids for t in ties)
assert all(len(x["short"]) <= 16 for x in eyes), [x["short"] for x in eyes if len(x["short"])>16]
assert all(len(en["quote"].split()) <= 12 for en in E)
print(len(eyes), "eyes", len(E), "entries")
