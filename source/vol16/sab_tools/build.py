import json
OUT="/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/vol16/ch-sabbatai-1665.json"
POSEN_NATHAN="https://www.posenlibrary.com/entry/letter-shabbetai-tzvi"
POSEN_RJ="https://posenlibrary.com/node/6472"
POSEN_AMS="https://www.posenlibrary.com/entry/letter-hailing-shabbetai-tzvi-messiah"
JE="https://jewishencyclopedia.com/articles/13480-shabbethai-zebi-b-mordecai"
JE_NEH="https://www.jewishencyclopedia.com/articles/11426"
EVELYN="https://gutenberg.org/files/38327/38327-h/38327-h.htm"
PEPYS="https://standardebooks.org/ebooks/samuel-pepys/the-diary/text/chapter-74"
SPIN="https://sacred-texts.com/phi/spinoza/corr/corr13.htm"
LOKER="https://www.jhse.org/pre-2015articles/english-contemporary-opinions-on-the-sabbatean-movement"
TEPL="https://keydocuments.net/article/teplitsky-glikl"
JHOM="https://www.jhom.com/personalities/gluckel/shabtai.htm"
DWECK="https://dweck.scholar.princeton.edu/document/24"
TOI="https://blogs.timesofisrael.com/the-rabbi-who-stood-alone-against-sabbateanism/"
HALP="https://www.cambridge.org/core/books/sabbatai-zevi/0FC38AC02719729799A89A2E37F84466"
SISMAN="https://www.tabletmag.com/sections/arts-letters/articles/sabbatai-sevis-conversion-to-islam"
SABAH="https://www.dailysabah.com/opinion/op-ed/converting-to-ottoman-world-false-messiah-sabbatai-zevi/amp"
WP_N="https://en.wikipedia.org/wiki/Nathan_of_Gaza"
WP_S="https://en.wikipedia.org/wiki/Sabbatai_Zevi"
ENC="https://www.encyclopedia.com/history/encyclopedias-almanacs-transcripts-and-maps/shabbetai-tzevi-also-sabbatai-sevi-zevi-or-zebi"
DBNL="https://www.dbnl.org/tekst/aa__001biog04_01/aa__001biog04_01_0756.php"
KEST="https://www.kestenbaum.net/auction/lot/auction-15/015-145/"
STCN="https://data.cerl.org/stcn/843146729?lang=en"

d={}
d["id"]="sabbatai-1665"
d["title"]="The Messianic Year"
d["short_title"]="The Messianic Year"
d["subtitle"]="Nathan of Gaza, Sabbatai Zevi and the Jewish world from Gaza to Hamburg, 1665–1676"
d["span"]="1665–1676"
d["intro"]=[
"In the spring of 1665 a young kabbalist in Gaza, Nathan ben Elisha Ashkenazi, announced that a vision had shown him the redeemer: Sabbatai Zevi, a scholar from Smyrna nearly twenty years his senior, long known for strange fasts, ecstasies and moments when he broke the law on purpose. Sabbatai had first made such claims in 1648 and had been expelled from several cities for them. This time, with a prophet beside him, the message spread. Letters from Gaza, Cairo, Aleppo and Smyrna carried it to Venice, Livorno, Amsterdam, Hamburg, London and the towns of Poland. Within a year, communities across the Jewish world were reciting new prayers for 'our king', doing penance, and in some places packing to leave for the Land of Israel.",
"The year ended on 16 September 1666 at Edirne (Adrianople), where Sultan Mehmed IV kept his court. Arrested in the Sea of Marmara in February 1666 and held first in Constantinople and then in the castle on the Dardanelles that his followers called the Tower of Strength, Sabbatai was brought before the sultan's officials and offered Islam or death. He put on a turban and took the name Aziz Mehmed Efendi. Most believers turned away in grief. Nathan and a committed minority read the conversion as a hidden stage of redemption. From that minority came later Sabbatean circles in Europe and, in Salonica, the Dönme, families who lived outwardly as Muslims while keeping their own rites. Their descendants continue as a community in Turkey today.",
"Laid side by side, the record holds the believers' own words: Nathan's letters and prayer books, Sabbatai's signed proclamations, the Amsterdam brotherhood's letter of homage, and Baruch of Arezzo's devout memorial written after Sabbatai's death. Against them stand the sceptic rabbi Jacob Sasportas in Hamburg and the Livorno rabbi Joseph Halevi, both writing letters that argued, mocked and warned. Further off, Christian observers saw the year through their own hopes and fears: a Dutch Reformed minister in Smyrna, an English diplomat at the Porte, a Royal Society secretary writing to Spinoza, a London news-writer, and Samuel Pepys recording a wager. From the Ottoman court comes the official chronicle that set the conversion down as one more sign of the sultan's reign.",
"Almost none of this is a diary. The honest record is letters, proclamations, newsletters, a court chronicle, histories written within a few years, and two memoirs written decades later: Glückel of Hameln's recollection of crates of linen waiting in her Hamburg house, and Baruch's Memorial. Each entry below is tagged by kind of source, and the witness ledger notes how long after the event each claim was written down. Many famous details, including the exact words at Edirne, come only through hostile or later tellings.",
"This chapter takes no position on whether Nathan's vision came from God or whether Sabbatai was what his followers believed. It records what each witness said, what believers and opponents concluded, and what followed. The tradition that mourned him as a false messiah and the community that still honours him are both reported in their own terms."
]
d["calendar_note"]="Jewish witnesses dated by the Hebrew calendar (year 5425 began in September 1664, 5426 on 10 September 1665, 5427 in September 1666). Ottoman sources used the Hijri calendar (the conversion fell in Rabiʿ I 1077). English writers such as Pepys, Oldenburg and Muddiman used the Julian (Old Style) calendar, ten days behind the Gregorian, and began the legal year on 25 March, so Pepys's '19 February 1665/6' is 1 March 1666 New Style. Dutch, Italian and Hamburg Christians mostly used the Gregorian calendar already. Every date_iso is Gregorian. Hebrew and Julian equivalents were computed with standard conversion tables: 17 Sivan 5425 = 31 May 1665; 4 Tevet 5426 = Saturday 12 December 1665; 14 Nisan 5426 (eve of Passover) = 19 April 1666; 9 Av 5426 = 10 August 1666; 16 Elul 5426 = Thursday 16 September 1666 (some modern accounts give 17 September); 10 Tishri 5437 (Yom Kippur) = 17 September 1676. Evelyn's 'Sunday, the fifth of Sevat' for the Constantinople rabbis' letter falls on Sunday 30 January 1667 (5 Shevat 5427), which supports that reading."

E=[]
def eye(**k): E.append(k)
eye(id="nathan",short="Nathan of Gaza",name="Nathan Benjamin ben Elisha ha-Levi Ashkenazi (Nathan of Gaza)",life="c. 1643–1680",
 role="Young kabbalist in Gaza, about 21–22 in 1665; son of a Jerusalem rabbi; the movement's prophet and theologian",
 side="Jewish; Sabbatean believers (Gaza, later the Balkans and Italy)",where="Gaza in 1665–66; afterwards wandering (Smyrna, Venice, Rome, the Balkans)",
 lat=31.50,lon=34.47,waypoints=[{"lat":31.50,"lon":34.47,"label":"Gaza 1665–66"},{"lat":45.44,"lon":12.33,"label":"Venice, March 1668"},{"lat":41.90,"lon":12.50,"label":"Rome 1668"},{"lat":42.00,"lon":21.43,"label":"Üsküp (Skopje), d. 1680"}],
 vantage=0,vantage_label="the prophet who announced him",form="dated letters, prayer manuals and treatises",language="Hebrew",
 authenticity="Nathan's letters survive in copies made by believers and opponents (several are preserved inside Sasportas's hostile collection). His account of his own vision comes from a letter of 1673, eight years after the event. Posen Library dates the Raphael Joseph letter to 1666; Scholem places it in autumn 1665.",
 bio="A gifted student of Lurianic kabbalah, Nathan was known in Gaza as a healer of souls when Sabbatai came to him in 1665. He gave the movement its programme of penance, its prayers and its timetable, and after the conversion its theology of a messiah who must descend into the 'husks' of impurity to redeem them. He never recanted, except under pressure in Venice, and died in the Balkans in 1680.",
 sources=[{"title":"Posen Library: Nathan of Gaza, Letter to Shabbetai Tzvi (tr. B. Ogren, from Benayahu 1973)","url":POSEN_NATHAN},{"title":"Posen Library: Nathan of Gaza, Letter to Raphael Joseph","url":POSEN_RJ},{"title":"Wikipedia: Nathan of Gaza (dates of visions, Venice, death)","url":WP_N}])
eye(id="sabbatai",short="Sabbatai Zevi",name="Sabbatai Zevi (Shabbetai Tzvi), after 1666 Aziz Mehmed Efendi",life="1626–1676",
 role="Smyrna-born rabbi and kabbalist, aged 39 in 1665; proclaimed messiah; after September 1666 an Ottoman court pensioner",
 side="Jewish messianic claimant; after 1666 a Muslim convert at the Ottoman court",where="Gaza, Smyrna, Constantinople, the Dardanelles castle, Edirne, finally Ulcinj (Dulcigno)",
 lat=38.42,lon=27.14,waypoints=[{"lat":31.50,"lon":34.47,"label":"Gaza, spring 1665"},{"lat":38.42,"lon":27.14,"label":"Smyrna, autumn 1665"},{"lat":41.01,"lon":28.98,"label":"Constantinople, Feb 1666"},{"lat":40.15,"lon":26.40,"label":"Dardanelles castle, Apr–Sep 1666"},{"lat":41.68,"lon":26.56,"label":"Edirne, Sep 1666"},{"lat":41.93,"lon":19.21,"label":"Ulcinj, 1673–76"}],
 vantage=0,vantage_label="the man proclaimed messiah",form="proclamations and dated letters",language="Hebrew (proclamations known also in contemporary translation)",
 authenticity="Few documents in his own hand survive. His proclamations are known through copies and translations circulated in 1666 (an English version is printed in Evelyn's 1669 History from Rycaut's papers). A circular letter of Nisan 1676 and a letter to the community of Berat (August 1676) are among the latest.",
 bio="Born in Smyrna in 1626, Sabbatai studied kabbalah and from youth went through periods of exaltation and despair, during which he sometimes broke religious law deliberately. Expelled from Smyrna, Salonica and Constantinople, he was living in Egypt and Jerusalem when he went to Nathan in Gaza in 1665. His own surviving words are short and royal in tone. After his conversion he lived at the Ottoman court, still teaching a circle of followers, until he was exiled to the Adriatic coast in 1673.",
 sources=[{"title":"Jewish Encyclopedia (1906): Shabbethai Ẓebi b. Mordecai","url":JE},{"title":"Evelyn, The History of Sabatai Sevi (1669), Project Gutenberg","url":EVELYN},{"title":"Halperin, Sabbatai Zevi: Testimonies to a Fallen Messiah (2011), appendix 2: circular letter of Nisan 1676","url":HALP}])
eye(id="coenen",short="Coenen",name="Thomas Coenen",life="d. 1688",
 role="Dutch Reformed minister to the Dutch merchant community at Smyrna (1660–72)",side="Dutch Protestant; foreign observer",
 where="Smyrna, through the winter of 1665–66",lat=38.42,lon=27.14,waypoints=[{"lat":38.42,"lon":27.14,"label":"Smyrna 1660–72"},{"lat":52.37,"lon":4.90,"label":"Amsterdam, book printed 1669"}],
 vantage=1,vantage_label="Christian minister in the same city",form="history (written within three years, with eyewitness passages)",language="Dutch",
 authenticity="Ydele verwachtinge der Joden ('Vain Expectations of the Jews'), Amsterdam: Joannes van den Bergh, 1669, with engraved portraits of Sabbatai and Nathan. It mixes Coenen's own observation in Smyrna with reports from Jewish informants. Scholem relied on it heavily. No English translation was available to check, so Smyrna details here are given as approximate.",
 bio="Coenen lived in Smyrna's European quarter and knew Jewish merchants personally. His book is hostile in its title and Protestant in its theology, but it is also close and specific about the Smyrna weeks. He returned to the Netherlands in 1672 and became a pastor at Nieuwersluis.",
 sources=[{"title":"DBNL biographical entry: Thomas Coenen","url":DBNL},{"title":"STCN record of Ydele verwachtinge der Joden (1669)","url":STCN},{"title":"Kestenbaum catalogue description of the 1669 edition","url":KEST}])
eye(id="rycaut",short="Rycaut",name="Sir Paul Rycaut",life="1629–1700",
 role="Secretary to the English ambassador at Constantinople (1661–67), then consul of the Levant Company at Smyrna (1667–78)",side="English; Levant Company and embassy",
 where="Constantinople and the embassy's Ottoman contacts, 1666; Smyrna after 1667",lat=41.03,lon=28.97,waypoints=[{"lat":41.03,"lon":28.97,"label":"Constantinople (Pera), 1666"},{"lat":38.42,"lon":27.14,"label":"Smyrna consulate 1667–78"}],
 vantage=2,vantage_label="English diplomat at the Ottoman capital",form="reports, later printed as history",language="English",
 authenticity="Rycaut's account first reached print in John Evelyn's The History of the Three Late Famous Impostors (London, 1669), which its modern editor says is drawn almost entirely from Rycaut, and then in Rycaut's own History of the Turkish Empire from 1623 to 1677 (1680). His texts translate Jewish letters and proclamations, and he wrote as a Protestant sceptic.",
 bio="An experienced observer of Ottoman government, Rycaut wrote from the capital where Sabbatai was jailed, with access to embassy informants, Jewish creditors of English merchants, and court gossip from Edirne. His version of the scene before the sultan, with archers and a stake at the palace gate, became the standard European telling.",
 sources=[{"title":"Evelyn, The History of Sabatai Sevi (1669; Augustan Reprint Society 1968), Project Gutenberg","url":EVELYN}])
eye(id="oldenburg",short="Oldenburg",name="Henry Oldenburg",life="c. 1619–1677",
 role="Secretary of the Royal Society of London, aged about 46; Europe's busiest scientific correspondent",side="English (German-born); Protestant learned world",
 where="London (Pall Mall)",lat=51.507,lon=-0.135,vantage=4,vantage_label="London, hearing news from Holland and the Levant",form="dated letters",language="Latin and English",
 authenticity="Letter to Spinoza of 8 December 1665 printed in Spinoza's Opera posthuma (1677), English translation by Elwes (1883). Letters to Boyle printed in Birch's Life of Boyle (1744) and in the Hall edition of Oldenburg's Correspondence.",
 bio="Oldenburg collected news as other men collected coins, and the messianic reports reached him through Dutch correspondents such as the millenarian Peter Serrarius. He wrote about them to Spinoza, a former member of Amsterdam's Jewish community, and to Robert Boyle, swinging between curiosity, hope and doubt.",
 sources=[{"title":"Spinoza, Correspondence, tr. Elwes (1883), sacred-texts","url":SPIN},{"title":"Loker, 'English contemporary opinions on the Sabbatean movement', JHSE","url":LOKER}])
eye(id="pepys",short="Pepys",name="Samuel Pepys",life="1633–1703",role="Clerk of the Acts to the Navy Board, aged 32; Fellow of the Royal Society from 1665",
 side="English; Navy Office",where="London (Seething Lane)",lat=51.510,lon=-0.079,vantage=4,vantage_label="London, news and wagers",form="diary",language="English (shorthand)",
 authenticity="Written in Shelton shorthand, deciphered in the nineteenth century; the 19 February 1665/6 entry is in all modern editions.",
 bio="Pepys did not care about messiahs but cared a great deal about money and talk. His single entry shows how the Smyrna news had become, in London, a betting proposition on the Exchange.",
 sources=[{"title":"Diary of Samuel Pepys, February 1665–66 (Standard Ebooks)","url":PEPYS}])
eye(id="muddiman",short="Muddiman",name="Henry Muddiman",life="1629–1692",role="Government news-writer at Whitehall; author of manuscript newsletters sent to subscribers across England",
 side="English; Secretary of State's news office",where="Whitehall, London",lat=51.504,lon=-0.127,vantage=4,vantage_label="London, writing the news",form="manuscript newsletters",language="English",
 authenticity="Newsletters in The National Archives, State Papers Domestic 29/151 and 29/156, cited by Zvi Loker (JHSE).",
 bio="Muddiman's newsletters went to country gentlemen and officials who could not read the Levant correspondence themselves. In spring 1666 he passed on both the excitement in Amsterdam and a false report of Sabbatai's execution, showing how rumour moved through official channels.",
 sources=[{"title":"Loker, 'English contemporary opinions on the Sabbatean movement', JHSE","url":LOKER}])
eye(id="sasportas",short="Sasportas",name="Jacob Sasportas",life="c. 1610–1698",role="Sephardi rabbi from North Africa living in Hamburg, aged about 55; former rabbi in Tlemcen and Salé",
 side="Jewish; rabbinic opponent of the movement",where="Hamburg, among the Portuguese community",lat=53.55,lon=9.99,vantage=3,vantage_label="sceptic rabbi in a believing city",form="dated letters (collected and edited later)",language="Hebrew",
 authenticity="His collection Tsitsat Novel Tsevi ('The Fading Flower of Zevi') stayed in manuscript in his lifetime, appeared in truncated form after his death, then in Jacob Emden's edition (Kitzur, Altona 1757), and critically in Isaiah Tishby's edition (1954). Scholars, Yaacob Dweck most fully (2019), have shown that Sasportas revised and arranged his letters after the apostasy, so some may sound more certain than they were when sent.",
 bio="Almost alone among prominent rabbis, Sasportas refused to believe from the start. He argued from Maimonides that a messiah is known by deeds, not by a prophet's word, and he bore the hostility of his own Hamburg congregation for saying so. His collection keeps copies of believers' letters too, and is one of the main sources for the movement.",
 sources=[{"title":"Dweck, 'Jacob Sasportas and Jewish Messianism' (2019)","url":DWECK},{"title":"'The rabbi who stood alone against Sabbateanism' (Times of Israel blog)","url":TOI}])
eye(id="gluckel",short="Glückel",name="Glückel (Glikl) of Hameln",life="1646–1724",role="Jewish merchant's wife and mother in Hamburg, aged about 20 in 1666; later a businesswoman in her own right",
 side="Jewish; Ashkenazi community of Hamburg",where="Hamburg",lat=53.55,lon=9.99,vantage=3,vantage_label="young wife watching the synagogue and her own house",form="memoir (written later)",language="Yiddish",
 authenticity="Written in two stages, beginning after her husband Haim's death in 1689 and resumed after 1712; first printed by David Kaufmann (1896); English translations by Marvin Lowenthal (1932) and Beth-Zion Abrahams (1962); critical edition by Chava Turniansky. The 1666 passage is a recollection set down about 25 years later.",
 bio="Glückel wrote for her children, not for history, and the Sabbatean year enters her memoir as a family story. Her witness is that of a young woman seeing the Portuguese youths' finery and her father-in-law's crates. She looks back with sorrow, not scorn, and with her faith intact.",
 sources=[{"title":"Teplitsky, 'Messianic Hope in Hamburg, 1666', Key Documents of German-Jewish History (2018)","url":TEPL},{"title":"JHOM excerpt from the Lowenthal translation","url":JHOM}])
eye(id="eliahu",short="Eliahu Leon",name="Eliahu ben Michael Judah Leon and the Yeshuot Meshiho brotherhood",life="fl. 1666",role="Member of a learned society founded in Amsterdam in Sabbatai's honour; one of 24 signatories",
 side="Jewish; Amsterdam Portuguese community, believers",where="Amsterdam",lat=52.37,lon=4.90,vantage=4,vantage_label="believers abroad",form="letter (collective)",language="Hebrew",
 authenticity="Manuscript in the Ets Haim–Livraria Montezinos library, Amsterdam (EH 47 A 11 001), published in the Posen Library vol. 5. Signatures are original.",
 bio="Amsterdam's prosperous Sephardi community, many of them descendants of former conversos, was among the most fervent in the West. The brotherhood's name, 'Salvations of His Messiah', and its letter of homage show sober merchants and scholars putting their names to the hope.",
 sources=[{"title":"Posen Library: Letter Hailing Shabbetai Tzvi as the Messiah (Amsterdam, 1666)","url":POSEN_AMS}])
eye(id="halevi",short="Joseph Halevi",name="Joseph Halevi of Livorno",life="17th century",role="Rabbi and preacher in Livorno",
 side="Jewish; rabbinic opponent",where="Livorno, Tuscany",lat=43.55,lon=10.31,vantage=4,vantage_label="sceptic in an Italian port",form="dated letters",language="Hebrew",
 authenticity="Two long letters, preserved in Sasportas's collection; translated in Halperin's Testimonies (2011). The exact dates are not given here because they could not be confirmed; they belong to 1666–67.",
 bio="Halevi received the same flood of letters as Livorno's believers and answered with angry, detailed ones of his own, collecting what he heard about Sabbatai's behaviour in Smyrna and afterwards. He and Sasportas strengthened each other's resistance.",
 sources=[{"title":"Halperin, Sabbatai Zevi: Testimonies to a Fallen Messiah, Second Testimony","url":HALP}])
eye(id="abdi",short="Abdi Pasha",name="Abdurrahman Abdi Pasha",life="d. 1692",role="Court chronicler to Sultan Mehmed IV, later a provincial governor",
 side="Ottoman court",where="Edirne, where the court resided",lat=41.68,lon=26.56,vantage=1,vantage_label="the sultan's own chronicler",form="court chronicle (Vekāyiʿnāme)",language="Ottoman Turkish",
 authenticity="The Vekāyiʿnāme records events of Mehmed IV's reign as the sultan wished them remembered; modern historians, notably Marc David Baer, use it for the Edirne hearing. Its wording could not be checked directly here, so the entry is approximate.",
 bio="Abdi Pasha wrote at the sultan's side, and for him the episode was a conversion story that added to the glory of a pious ruler. He shows the court's view: no messiah, only a troublesome Jew brought to Islam by the sultan's wisdom and his preacher's arguments.",
 sources=[{"title":"Büyükaksoy, 'Converting to Ottoman world' (Daily Sabah, 2026)","url":SABAH},{"title":"Sisman, 'Sabbatai Sevi's Conversion to Islam' (Tablet)","url":SISMAN}])
eye(id="baruch",short="Baruch Arezzo",name="Baruch of Arezzo",life="fl. 1670s",role="Italian Sabbatean believer and biographer",
 side="Jewish; Sabbateans who kept faith after 1666",where="Italy (probably), far from the events",lat=43.46,lon=11.88,vantage=3,vantage_label="devout biographer after the fact",form="memoir-biography (written later)",language="Hebrew",
 authenticity="Zikkaron li-Venei Yisrael ('Memorial to the Children of Israel'), written shortly after Sabbatai's death in 1676; translated by David Halperin (2011). It draws on believers' letters and testimony, not on Baruch's own sight of most events.",
 bio="Baruch wrote as one who still believed, calmly and without the polemic of the sceptics, and Halperin calls his memorial a sober yet devout biography. He shows how the faithful minority told the story to themselves, apostasy included.",
 sources=[{"title":"Halperin, Sabbatai Zevi: Testimonies to a Fallen Messiah, First Testimony","url":HALP}])
d["eyes"]=E

N=[]
def en(date_iso,date_display,precision,eye,place,headline,digest,quote,confidence,source_kind,source_note):
    N.append(dict(date_iso=date_iso,date_display=date_display,precision=precision,eye=eye,place=place,headline=headline,digest=digest,quote=quote,confidence=confidence,source_kind=source_kind,source_note=source_note))

en("1626-07-23","9 Av 5386 (23 July 1626)","day","baruch","Smyrna (as told later)","A birth remembered on the fast of the Temple's fall",
"Believers' tradition put Sabbatai's birth on the Ninth of Av, the fast day mourning the destruction of the Temple, on which rabbinic legend said the messiah would be born. Baruch's memorial and later sources repeat the date. In 1666 it became the reason given for turning that fast into a feast.",
"","approx","secondhand","Jewish Encyclopedia (1906) gives 9 Ab = 23 July 1626; Baruch of Arezzo in Halperin (2011). The date came to carry religious weight, so the record cannot be checked independently.")
en("1648","1648 (5408)","year","baruch","Smyrna","A young scholar speaks the forbidden Name",
"Believers and opponents agree that around 1648, in his early twenties, Sabbatai first hinted at his mission in Smyrna, in part by pronouncing the divine Name that Jewish law reserves for the Temple. The year was already feared for the massacres in Poland and Ukraine. The rabbis of Smyrna reproved him and later expelled him.",
"","approx","secondhand","Jewish Encyclopedia (1906), 'ominous year' 1648; encyclopedia.com (Zilfi) on the 1648 reprimand. Baruch's Memorial recounts the early years.")
en("1665-05-20","Shavuot eve, 6 Sivan 5425 (c. 20 May 1665)","range","nathan","Gaza","A night of study ends in a voice",
"At a Shavuot vigil in Gaza, Nathan fell into a trance in which those present said a voice spoke through him, a maggid as kabbalists called it, naming Sabbatai as the anointed one. Nathan later described an earlier vision, at about twenty, in which he saw the figure of Sabbatai engraved before him for about a day. That account dates from a letter of 1673, eight years after the event.",
"","approx","later firsthand","Wikipedia, 'Nathan of Gaza' (citing Scholem pp. 201–204): Shavuot vision spring 1665; 1673 letter on the earlier vision. Shavuot 5425 computed as 20–21 May 1665.")
en("1665-05-31","17 Sivan 5425 (Sunday 31 May 1665)","day","sabbatai","Gaza","Sabbatai, urged by Nathan, declares himself",
"After weeks with Nathan, who told him his soul was the messiah's, Sabbatai publicly accepted the role in Gaza. He rode about on horseback, appointed followers to represent the tribes of Israel, and in Gaza Nathan's word carried much of the community. Rabbis in Jerusalem, where he had collected funds, were far more doubtful and later excommunicated him.",
"","approx","secondhand","encyclopedia.com (Zilfi), 'May 1665' citing Scholem pp. 220–221; the day 17 Sivan is Scholem's, converted here.")
en("1665-09","autumn 1665 (late 5425 / early 5426)","month","nathan","Gaza","A timetable for redemption sent to Cairo",
"Nathan wrote to Raphael Joseph, the wealthy treasury official (chelebi) who led Cairo's Jews, setting out what would happen. The sultan would yield his crown without war, Sabbatai would bring back the lost tribes from beyond the river Sambatyon, and in the meantime Israel must repent with fasts and prayer. Copies of the letter spread to Europe and set the expectation for 1666.",
"","approx","firsthand","Posen Library, 'Letter to Raphael Joseph' (dated there 1666); Scholem dates it autumn 1665. Contents as summarised in standard accounts; full text not accessible.")
en("1665-09","autumn 1665","month","coenen","Smyrna","The messiah comes home to Smyrna",
"Sabbatai returned to his native city, where Coenen ministered to the Dutch merchants, and for some weeks lived quietly. Then he began appearing in public with followers and announcing, by acts as much as words, that the time had come. Coenen reports that the city's Jews divided sharply between believers and those who remembered the youth they had expelled.",
"","approx","later firsthand","Coenen, Ydele verwachtinge (1669); Wikipedia 'Sabbatai Zevi' (arrival autumn 1665). Coenen's text not checked directly.")
en("1665-12-12","Sabbath, 4 Tevet 5426 (Saturday 12 December 1665)","day","coenen","Smyrna, the Portuguese synagogue","Doors forced, and kingdoms handed out",
"Coenen and later historians describe Sabbatai and a crowd forcing their way into the Portuguese synagogue, whose leaders opposed him. He read from the Torah himself, pronounced the divine Name and declared himself the anointed one. He then named followers as kings of the nations of the world and announced a date for redemption in June 1666. The city's chief rabbi was set aside in favour of a believer.",
"","approx","later firsthand","encyclopedia.com (Zilfi): December 1665 forced entry into the opposition synagogue; the day follows Scholem, converted here; Coenen (1669) is the main early account. JE dates the public declaration to New Year 1665, a different tradition.")
en("1665-12","December 1665","month","rycaut","Smyrna (reported from Constantinople)","A sceptic's daughters fall into ecstasies",
"Rycaut's account tells of a Smyrna merchant, Pennia, who opposed Sabbatai until his own daughters began to prophesy and fall into trances, after which he became a believer. Similar prophesying by women and children was reported across the city. Business stopped, Rycaut wrote, as people sold goods and prepared for the journey to Jerusalem.",
"his daughters prophesie, and fall into strange extasies","approx","secondhand","Evelyn, History of Sabatai Sevi (1669), from Rycaut; Project Gutenberg 38327.")
en("1665-12-18","Friday 8 December 1665 (O.S.) = 18 December 1665 (N.S.)","day","oldenburg","London","'Everyone here is talking' of a return",
"Oldenburg asked Spinoza in Amsterdam what the Jews there made of the news. London, he wrote, was full of the report that the scattered Jews were about to return to their land. He thought that if true it might mean the end of the world, and he asked for word of how the Amsterdam community was taking it. There is no known reply from Spinoza on the point.",
"Few here believe in it, but many desire it.","verified","firsthand","Oldenburg to Spinoza, London 8 Dec. 1665; Elwes translation (1883), sacred-texts corr13; dated also by pepysdiary.com annotation.")
en("1665-12-30","late December 1665 – January 1666","range","rycaut","Smyrna to the Sea of Marmara","Sailing to claim the sultan's crown",
"Sabbatai left Smyrna by sea for Constantinople, where believers expected the sultan to hand him the crown. Rycaut's account gives the voyage as 39 days, slowed by winter storms. The Ottoman authorities had already been warned.",
"","approx","secondhand","Evelyn (1669) from Rycaut: sailed January 1666, 39 days at sea; Scholem gives departure 30 December 1665.")
en("1666-02","February 1666","month","rycaut","Constantinople","Arrest, and a cell instead of a throne",
"Ottoman officers took Sabbatai off his ship before it reached the capital. On the grand vizier's order he was held in a Constantinople prison, where, Rycaut says, his followers still flocked to him and Jewish debtors stopped paying English creditors at Galata. Rycaut, with the embassy, watched the city's Jews divide over what the arrest meant.",
"","approx","secondhand","Evelyn (1669) from Rycaut ('indebted to our Merchants at Galata'); Wikipedia and encyclopedia.com: arrest February 1666 on the grand vizier's order.")
en("1666-02","around February 1666","month","gluckel","Hamburg, Portuguese synagogue","Green silk ribbons and letters read aloud",
"Glückel remembered letters from Smyrna being read out in the Sephardi synagogue, with German Jews crowding in to hear. The Portuguese young men came in their best clothes with broad green silk ribbons, which she called Sabbatai's livery, and there was dancing with timbrels. She wrote this about 25 years later.",
"","approx","later firsthand","Teplitsky (2018): news reached Hamburg around February 1666; JHOM excerpt of Lowenthal translation pp. 45–47.")
en("1666-02","winter 1665–66","range","sasportas","Hamburg","A rabbi asks for proof, not prophecy",
"Sasportas wrote to the Amsterdam rabbinate and its leader Isaac Aboab da Fonseca urging caution. Citing Maimonides on the laws of kings, he argued that a messiah is recognised by what he achieves, not by a prophet's announcement. About six months later he wrote again, asking what text required belief in a messiah who had done no messianic deeds.",
"","approx","firsthand","Dweck (2019), chapter 2: open letter at the outbreak, second letter about six months later; exact dates not given.")
en("1666-03-01","Monday 19 February 1665/6 (O.S.) = 1 March 1666 (N.S.)","day","pepys","London","Ten pounds now, a hundred if he is King",
"Pepys heard of a Jew in London offering wagers on behalf of others. He would pay £100 for £10 laid down if a certain person now at Smyrna were acknowledged within two years by the princes of the East, the sultan above all, as king of the world. Pepys noted that £1,100 had already been placed this way, and wrote it down as a curiosity.",
"particularly the grand Signor as the King of the world","verified","firsthand","Pepys diary 19 Feb 1665/6 (Standard Ebooks, February 1665–66).")
en("1666-03-16","6 March 1665/6 (O.S.) = 16 March 1666 (N.S.)","day","oldenburg","London","Letters from Constantinople, from Christians too",
"Writing to Robert Boyle, Oldenburg passed on news from Holland that Christians as well as Jews at Constantinople were confirming the reports. His tone had warmed since December. Loker's study describes the letter as hopeful.",
"Christians as well as Jews write from Constantinople","approx","firsthand","Loker (JHSE), citing Oldenburg Correspondence III no. 493 and Birch, Life of Boyle; the letter is dated '6 March 1665', read here as 1665/6.")
en("1666-03","March 1666","month","sasportas","Hamburg","A congregation orders prayers, and an Amen from doubters",
"The Hamburg Portuguese community introduced a prayer for Sabbatai to be said on Sabbaths, Mondays and Thursdays, and required those who doubted to stay and answer Amen aloud. Its leaders called doubters heretics. Sasportas, who would not join, recorded the jubilation with contempt, including his anger that the crowd cared more about Christian onlookers than about the law.",
"","approx","firsthand","Jewish Encyclopedia (prayers, compulsory Amen); Teplitsky (prayers introduced in March 1666); Dweck (Sasportas's criticism).")
en("1666-03-25","15 March 1665/6 (O.S.) = 25 March 1666 (N.S.)","day","muddiman","Whitehall, London","Amsterdam's Jews 'hurry out', says the newsletter",
"Muddiman's newsletter told subscribers that Amsterdam's Jews were hurrying off to join their brethren in great expectation. The same report dismissed the claimant as an ordinary fellow and a baker's son, which was untrue: Sabbatai's father had been a poultry dealer and merchant agent. English readers got hope and contempt in the same paragraph.",
"","verified","firsthand","National Archives SP 29/151 ff. 23–5, quoted in Loker (JHSE); the correction about his father (poultry dealer, later agent for English merchants) follows Scholem.")
en("1666-04-19","eve of Passover, 14 Nisan 5426 (Monday 19 April 1666)","day","baruch","The castle on the Dardanelles","A prison becomes the 'Tower of Strength'",
"After about two months Sabbatai was moved to the fortress at Gallipoli on the Dardanelles, arriving on the eve of Passover. Believers' accounts say he celebrated the festival there, and opponents later charged that he had a paschal lamb slaughtered, a rite forbidden since the Temple's fall. Followers called the castle Migdal Oz, the Tower of Strength. Bribed guards let him receive visitors and hold court.",
"","approx","secondhand","Wikipedia 'Sabbatai Zevi' (moved about two months later, arriving the day before Passover); JE (paschal lamb); 14 Nisan computed. Baruch's Memorial in Halperin.")
en("1666-05-25","15 May 1666 (O.S.) = 25 May 1666 (N.S.)","day","muddiman","Whitehall, London","A false report: 'hanged in chains'",
"Muddiman's newsletter reported that the new messiah of the Jews had been hanged in chains at Constantinople after confessing. It was untrue: Sabbatai was alive and receiving visitors at the Dardanelles castle. The report shows how fast and how wrongly news moved between the Levant and London.",
"","verified","firsthand","SP 29/156 f. 38, cited in Loker (JHSE) note 5.")
en("1666-06","summer 1666","range","rycaut","The castle on the Dardanelles","Pilgrims from Poland to Amsterdam at the gate",
"Rycaut's account lists visitors arriving at the castle from Poland, Germany, Livorno, Venice and Amsterdam, paying the guards for an audience. The Turks, he wrote, profited from the traffic. Sabbatai received them in state, and the visitors carried new instructions home.",
"","approx","secondhand","Evelyn (1669) from Rycaut, Project Gutenberg 38327.")
en("1666-06-18","15 Sivan 5426 (18 June 1666)","day","coenen","Smyrna","The appointed day passes in a prison",
"The redemption Sabbatai had announced in Smyrna for 15 Sivan arrived while he was still held at the Dardanelles. Believers did not treat this as a failure, since the imprisonment itself was read as part of the drama. Coenen, writing afterwards, counted it among the hopes that came to nothing.",
"","approx","later firsthand","Date of the announcement follows Scholem; Coenen (1669). Not verified from Coenen directly.")
en("1666-07","summer 1666 (Tammuz 5426)","month","sabbatai","The castle on the Dardanelles","Fasts turned into festivals",
"A proclamation in Sabbatai's name, signed with the title of God's only and firstborn son, told the children of Israel to turn their mourning into joy and their fasts into festivals. The fasts of 17 Tammuz (20 July 1666) and 9 Av (10 August 1666), the latter his birthday, were to be feasts. Many communities obeyed, while others kept the fasts and were denounced for it.",
"The Onely, and First-borne Son of God","approx","firsthand","Evelyn (1669), English translation of the proclamation from Rycaut's papers; JE on the 17 Tammuz and 9 Av changes. Hebrew dates converted.")
en("1666","1666","year","eliahu","Amsterdam","Twenty-four signatures for 'our king'",
"Members of the Amsterdam brotherhood Yeshuot Meshiho signed a Hebrew letter hailing Sabbatai as messiah and redeemer and pledging their loyalty. That year Amsterdam printers also issued Nathan's penitential prayer manuals, one with a frontispiece showing Sabbatai enthroned beneath a crown. The signatories were respected men of the community.",
"","approx","firsthand","Posen Library, 'Letter Hailing Shabbetai Tzvi as the Messiah' (Ets Haim EH 47 A 11 001); Posen, Tikun keriyah frontispiece (1666). Exact month not established.")
en("1666-08-10","9 Av 5426 (Tuesday 10 August 1666)","day","sasportas","Hamburg","The day of mourning kept as a feast",
"On the Ninth of Av, the anniversary of the Temple's destruction, many believing communities feasted at Sabbatai's instruction instead of fasting. For Sasportas this was the clearest sign of a movement overturning the law on the word of a prisoner. He kept the fast and recorded his opponents' contempt for those who did.",
"","approx","firsthand","JE (Ninth of Ab turned to a feast); Dweck (2019) on Sasportas; the Hamburg observance on that day is inferred from these accounts, not separately dated.")
en("1666-09","beginning of September 1666 (Elul 5426)","range","rycaut","The castle on the Dardanelles","A Polish kabbalist leaves as an accuser",
"Nehemiah ha-Kohen, a kabbalist sent from Poland, reached the castle and argued with Sabbatai over several days. He left convinced he was an impostor and, by Rycaut's account and Jewish ones, informed the Ottoman officials. Jewish tradition adds that, fearing for his life, he declared himself a Muslim on the spot, and later returned to Judaism.",
"","approx","secondhand","Evelyn (1669) from Rycaut; Jewish Encyclopedia 'Nehemiah ha-Kohen' (citing Emden); JE main article: arrival beginning of September 1666; Dweck dates the visit to summer 1666.")
en("1666-09-16","16 Elul 5426 / 16 Rabiʿ I 1077 (Thursday 16 September 1666)","day","abdi","Edirne, the imperial palace","The sultan's chronicler: a Jew becomes Aziz Mehmed",
"In the court chronicle the episode is a hearing in the sultan's presence. Mehmed IV followed it unseen from behind a screen, while the preacher Vani Mehmed Efendi and the palace physician Hayatizade Mustafa Efendi, himself a convert from Judaism who acted as go-between, dealt with the prisoner. Sabbatai accepted Islam and was given the name Aziz Mehmed Efendi, an honorary post as a palace gatekeeper, and a daily stipend. The chronicler presents it as the sultan's triumph.",
"","approx","official record","Daily Sabah (2026): Abdi Pasha recorded the trial, the sultan watching from behind a curtain; Sisman (Tablet): Hayatizade, name, kapıcıbaşı post and stipend of 150 aspers; Hijri date computed. Sisman gives 17 September.")
en("1666-09-16","16 September 1666","day","rycaut","Edirne (reported from Constantinople)","Archers, a stake, and a turban",
"Rycaut's version has Sabbatai brought before the sultan, asking for an interpreter and looking downcast, without the courage he had shown in the synagogue. Offered a test, to stand naked before the royal archers and show whether arrows could hurt him, he refused and denied any special mission. Told the stake was ready at the palace gate, he agreed to become a Muslim.",
"contented to turn Turk","approx","secondhand","Evelyn, History of Sabatai Sevi (1669), from Rycaut; Project Gutenberg 38327. Rycaut was not present at Edirne.")
en("1666-09-16","16 September 1666","day","baruch","Edirne (as believers told it)","Believers' telling: a turban as a hidden mission",
"Baruch's memorial tells the conversion as a mystery rather than a betrayal. The messiah had gone down among the nations to raise the sparks of holiness trapped there, a teaching Nathan developed in letters after the event. For the faithful minority, his remaining a Jew in secret was proof that the drama continued.",
"","approx","secondhand","Halperin (2011), First Testimony; Baruch wrote after 1676.")
en("1666-09-25","about 25 September 1666 (late Elul 5426)","range","sabbatai","Edirne","'The ninth day of my regeneration'",
"A short letter from Sabbatai to his brothers in Smyrna after the conversion described himself as now an Ishmaelite, a Muslim, by God's will. He dated it by the ninth day of his renewal, as if a new era had begun. Opponents copied it as proof of apostasy, and believers as proof that he still commanded them.",
"","approx","firsthand","Jewish Encyclopedia (1906): letter calling himself an 'Ishmaelite' and dated the 'ninth day of my regeneration'; day reckoned from 16 September.")
en("1666-11","autumn 1666","range","nathan","Gaza and Syria","The prophet does not recant",
"When news of the conversion reached him, Nathan did not abandon his message. He judged it unsafe to stay in Ottoman Syria and prepared to go north toward Sabbatai, and his letters began to explain the apostasy as the messiah's descent into the realm of impurity, a step before final redemption. A letter in praise of Sabbatai written in this period speaks of the insults and rejection Nathan suffered from his own people.",
"","approx","firsthand","Wikipedia 'Nathan of Gaza'; Posen Library letter to Shabbetai Tzvi (1666, from Benayahu 1973, pp. 384–389), tr. Ogren.")
en("1666-11-20","10 November 1666 (O.S.) = 20 November 1666 (N.S.)","day","oldenburg","London","The news passed on to the Secretary of State's office",
"Oldenburg was still relaying reports about Sabbatai to Joseph Williamson, the under-secretary who ran the government's news network. By now the subject was the apostasy and its aftermath rather than a return to Zion. The letter's text is not quoted in the source used here.",
"","approx","firsthand","Oldenburg to Williamson, 10 Nov 1666, SP 29/136, cited in Loker (JHSE).")
en("1666-12","late 1666 – 1667","range","halevi","Livorno","A Livorno rabbi takes his revenge in ink",
"Joseph Halevi wrote long letters, sharp in style and full of detail, about Sabbatai's conduct in Smyrna and his followers' credulity, mocking those who had threatened unbelievers. Sasportas kept them in his collection. Halevi's detail is valuable, but it comes from an opponent who had been insulted and threatened during the movement and wrote in anger.",
"","approx","firsthand","Halperin (2011), Second Testimony; Times of Israel blog (Sasportas's exchange with Halevi). Exact letter dates not confirmed.")
en("1666-12","after September 1666","range","rycaut","Constantinople","'Ashamed of their easy belief'",
"Rycaut described the Jewish communities as stunned and ashamed when the conversion became known. Christians mocked them in the streets, and Jewish leaders worked to quiet the affair before Ottoman anger fell on whole communities. He did not see that a minority still believed.",
"ashamed of their easie belief","approx","secondhand","Evelyn (1669) from Rycaut, Project Gutenberg 38327.")
en("1667-01-30","Sunday 5 Shevat 5427 (30 January 1667)","day","rycaut","Constantinople","The rabbis of Constantinople close the book",
"Rycaut's dossier includes a letter from the rabbis of Constantinople to their colleagues, dated 5 Shevat, condemning belief in the convert and ordering the old fasts and customs restored. The weekday the letter gives fits the year 5427, after the conversion. Similar bans went out from Smyrna.",
"","approx","official record","Evelyn (1669), letter dated 'Sunday, the fifth of Sevat'; year inferred from the weekday (5 Shevat 5427 = Sunday 30 Jan 1667).")
en("1667","1667","year","gluckel","Hamburg","Opening the crates in her house",
"Her father-in-law in Hameln had given up his home and sent two great casks of linen and dried food to Glückel's house in Hamburg, ready to sail for the Holy Land. After more than a year the family feared the food would spoil and asked her to unpack it and save the linen. He went on waiting for the signal for about three years.",
"","approx","later firsthand","JHOM excerpt (Lowenthal tr.); Teplitsky (2018): crates in Hamburg over a year; he settled in Hildesheim. Written c. 1690.")
en("1668-03","March 1668","month","nathan","Venice","Venice makes the prophet sign",
"Travelling in disguise through Italy, Nathan was detained in Venice, where the rabbinate and the city authorities made him sign a statement that his prophecies had come from his own imagination. He continued on to Rome, was recognised there and expelled, and then went back to the Balkans. His followers did not take the Venice statement as his true view.",
"","verified","official record","Wikipedia 'Nathan of Gaza' (Venice, March 1668).")
en("1669","1669","year","coenen","Amsterdam (printed)","'Vain Expectations': the Smyrna minister's book",
"Coenen published his account in Amsterdam with engraved portraits of Sabbatai, in a turban pointing to an open book, and of Nathan. He wrote as a Reformed preacher drawing a lesson about false messiahs, but from close knowledge of Smyrna. It remains one of the principal early sources.",
"","verified","later firsthand","STCN record; Kestenbaum catalogue; Posen Library portrait (Allard Pierson ROK A 914).")
en("1669","1669","year","rycaut","London (printed)","Rycaut's reports become an English book",
"John Evelyn published The History of the Three Late Famous Impostors, whose Sabbatai section is built almost entirely from Rycaut's reports and translations. Rycaut's own History of the Turkish Empire from 1623 to 1677 retold the story in 1680. Through these books English readers learned the story mainly as a warning against credulity.",
"","approx","secondhand","Evelyn (1669), Augustan Reprint introduction (Grose); pepysdiary.com encyclopedia note on Evelyn giving a copy to Charles II on 13 Feb 1669.")
en("1673-01","beginning of 1673","month","baruch","Edirne to Ulcinj","Exile to the Adriatic shore",
"After years at court in which he prayed as a Muslim but also met Jewish followers, Sabbatai was accused of backsliding and banished to Dulcigno (Ulcinj), a small fortress port on the Adriatic. Baruch's memorial follows him there through the believers' letters. A few disciples, among them his last wife, went with him.",
"","approx","secondhand","Wikipedia 'Sabbatai Zevi' (exile beginning of 1673); encyclopedia.com gives 1672. Halperin (2011).")
en("1676-03","Nisan 5436 (March–April 1676)","month","sabbatai","Ulcinj","A circular letter from exile",
"From Dulcigno Sabbatai sent a circular letter to believers in the spring of 1676, one of the few texts in his own name from his last years. David Halperin translates it as an appendix to his Testimonies. Its exalted tone is unchanged after ten years as a Muslim.",
"","approx","firsthand","Halperin (2011), Appendix 2: 'Sabbatai Zevi's Circular Letter (Nisan 1676)'. Content not read directly.")
en("1676-08","August 1676 (Elul 5436)","month","sabbatai","Ulcinj","Last letter, to the believers of Berat",
"Weeks before his death Sabbatai wrote to the community of believers at Berat in Albania, asking for religious books. It is his last known letter. Nothing in it suggests he expected to die soon.",
"","approx","firsthand","Wikipedia 'Sabbatai Zevi' (letter to Berat, August 1676).")
en("1676-09-17","10 Tishri 5437, Yom Kippur (Thursday 17 September 1676)","day","baruch","Ulcinj","Death on the Day of Atonement",
"Sabbatai died in exile at Dulcigno. Believers dated his death to Yom Kippur, and some held that he had not died but gone into hiding, to return. Nathan, told the news, is said to have spoken of a disappearance rather than a death. The Jewish Encyclopedia gives 30 September, which does not match Yom Kippur that year.",
"","approx","secondhand","Wikipedia infobox c. 17 Sept 1676; JE gives 30 Sept 1676 'according to some'; Yom Kippur 5437 computed as 17 Sept 1676; Baruch in Halperin (2011).")
en("1677","c. 1677","year","baruch","Italy","A memorial for the children of Israel",
"Shortly after Sabbatai's death Baruch set down the story as a believer, from birth through Gaza, Smyrna, the castle, the turban and the exile. He wrote for the faithful, explaining each reverse as part of the plan, and without the scorn of the sceptics' letters. Scholars rely on it because it records what the believers themselves said.",
"","approx","later firsthand","Halperin (2011), First Testimony ('written shortly after his death').")
en("1680-01-11","11 January 1680","day","nathan","Üsküp (Skopje)","The prophet dies in the Balkans",
"Nathan died in the Ottoman Balkans, most sources say at Üsküp (Skopje), where his grave was visited by Sabbateans for generations. The tomb inscription as later reported gives a different date, 16 Shevat 5440, a few days later. He had remained loyal to Sabbatai to the end.",
"","approx","secondhand","Wikipedia 'Nathan of Gaza' (11 Jan 1680; Skopje or Sofia; tomb inscription 16 Shevat 5440 per Konfino).")
en("1690","c. 1690–91","range","gluckel","Hamburg","Writing it down a quarter-century later",
"Widowed, Glückel began her memoir for her children, and the messianic year became a lesson on hope and sin. She compared the long expectation to a woman in labour who gives birth only to wind. She blamed the community's quarrels for its unworthiness and still affirmed that God would keep his promise.",
"","approx","later firsthand","JHOM excerpt (Lowenthal tr.); Teplitsky (2018) on the two stages of writing.")
d["entries"]=N

C=[]
def cl(date_iso,date_display,eye,claim,form,evidence,confidence): C.append(dict(date_iso=date_iso,date_display=date_display,eye=eye,claim=claim,form=form,evidence=evidence,confidence=confidence))
cl("1665-05-20","Shavuot 1665","nathan","Nathan in trance names Sabbatai as messiah; his account of an earlier vision was written in 1673, eight years on","vision account","Nathan's 1673 letter, via Scholem","approx")
cl("1665-05-31","17 Sivan 5425","sabbatai","Sabbatai publicly accepts the messianic role in Gaza (known from later believers' and opponents' accounts)","other","Scholem; encyclopedia.com","approx")
cl("1665-09","autumn 1665","nathan","Nathan foretells the sultan's surrender of his crown and the return of the lost tribes, and calls for penance","letter","Letter to Raphael Joseph of Cairo","approx")
cl("1665-12-12","12 December 1665","coenen","Sabbatai forces entry into the Portuguese synagogue of Smyrna, names kings of the nations, sets June 1666 for redemption (printed 1669)","report","Coenen, Ydele verwachtinge (1669)","approx")
cl("1665-12-18","8 Dec 1665 O.S.","oldenburg","London is 'talking of a report' of the Jews' return; few believe, many desire it","letter","Oldenburg to Spinoza, Opera posthuma; Elwes 1883","verified")
cl("1666-02","winter 1665–66","sasportas","A messiah must be known by deeds, not a prophet's word; the Amsterdam rabbis should be cautious","letter","Tsitsat Novel Tsevi (revised later by Sasportas)","approx")
cl("1666-03-01","19 Feb 1665/6 O.S.","pepys","A London Jew offers 10-to-1 that the man at Smyrna will be owned as king of the world within two years","diary","Pepys's diary","verified")
cl("1666-03","March 1666","sasportas","Hamburg's Portuguese leaders order prayers for Sabbatai and an Amen from doubters, calling unbelievers heretics","letter","Sasportas; Jewish Encyclopedia","approx")
cl("1666-05-25","15 May 1666 O.S.","muddiman","The 'New Messias' has been hanged in chains at Constantinople (false)","newspaper","Newsletter, SP 29/156","verified")
cl("1666-07","summer 1666","sabbatai","As God's 'First-borne Son', Sabbatai orders the fasts turned into festivals","other","Proclamation, English translation in Evelyn (1669)","approx")
cl("1666","1666","eliahu","Twenty-four Amsterdam notables hail Sabbatai as messiah and redeemer","letter","Ets Haim MS EH 47 A 11 001","verified")
cl("1666-09-16","Rabiʿ I 1077","abdi","Before the sultan's officials the Jew Sabbatai accepts Islam, is named Aziz Mehmed and given a palace post","report","Abdi Pasha, Vekāyiʿnāme","approx")
cl("1666-09-16","16 Sep 1666","rycaut","Facing the stake, Sabbatai denies his mission and is 'contented to turn Turk' (printed 1669, not an eyewitness)","report","Evelyn (1669) from Rycaut","approx")
cl("1666-09-25","late Elul 5426","sabbatai","Sabbatai writes that God has made him an Ishmaelite, dating the letter by his 'regeneration'","letter","Copy cited in Jewish Encyclopedia","approx")
cl("1666-11","autumn 1666","nathan","The apostasy is a hidden stage of redemption, and the prophecy stands","letter","Nathan's letters (Benayahu 1973)","approx")
cl("1690","c. 1690","gluckel","The Hamburg hope of 1666 was like a labour that gave birth to wind; recalled about 25 years after","other","Glückel's memoir, Book III","approx")
d["claims"]=C

d["convergences"]=[
 {"date":"1665-05-31","label":"Gaza, spring 1665: the prophet and the messiah","eyes":["nathan","sabbatai","baruch"],"note":"Nathan's own later account, Sabbatai's acceptance and Baruch's devout retelling all come from the believing side. No sceptic saw Gaza in these weeks, so the founding scene survives only in believers' words."},
 {"date":"1665-12-12","label":"December 1665: Smyrna erupts, London talks","eyes":["coenen","rycaut","oldenburg"],"note":"Within a week of the Smyrna synagogue scene, Oldenburg in London was asking Spinoza what Amsterdam's Jews believed. Coenen saw the city's Jews divide, Rycaut recorded prophesying daughters, and in London the news was received in apocalyptic terms."},
 {"date":"1666-03-01","label":"Late winter 1666: arrest in the East, ecstasy in the West","eyes":["rycaut","gluckel","sasportas","pepys","oldenburg","muddiman"],"note":"As Sabbatai sat in a Constantinople prison, Hamburg's Portuguese youths danced in green silk, Sasportas wrote warning letters, Pepys recorded a wager and Oldenburg and Muddiman passed on reports of departures from Amsterdam. News of the arrest travelled more slowly than news of the hope."},
 {"date":"1666-05-25","label":"Spring 1666: the Tower of Strength and a false death","eyes":["baruch","muddiman","rycaut"],"note":"Believers remember a royal Passover in the castle. In Whitehall, Muddiman's newsletter had him hanged. Rycaut, nearest of the three, describes guards selling access to pilgrims."},
 {"date":"1666-08-10","label":"Summer 1666: fasts become feasts","eyes":["sabbatai","eliahu","sasportas"],"note":"Sabbatai's proclamation, the Amsterdam brotherhood's homage and Sasportas's refusal show the same summer from three positions: command, loyalty and resistance."},
 {"date":"1666-09-16","label":"16 September 1666: the turban at Edirne","eyes":["abdi","rycaut","baruch","sabbatai"],"note":"For the sultan's chronicler it was a pious conversion, for Rycaut cowardice under threat, and for Baruch a hidden mission. Sabbatai's own letter days later dated a new era. None of the four tellings is a verbatim record of the hearing."},
 {"date":"1666-12","label":"Winter 1666–67: grief, bans and a theology of the descent","eyes":["nathan","halevi","rycaut","gluckel","oldenburg"],"note":"Nathan wrote that the prophecy stood, Halevi and the Constantinople rabbis wanted the affair closed, Rycaut saw only shame, and in Hamburg Glückel's household still kept the packed crates."},
 {"date":"1676-09-17","label":"1676: last letters and death in exile","eyes":["sabbatai","baruch","nathan"],"note":"Sabbatai's last letters from Dulcigno, Baruch's account of his death on Yom Kippur, and Nathan's refusal to call it death were where the believers' story stood ten years after the conversion."}
]
d["ties"]=[
 {"a":"nathan","b":"sabbatai","kind":"met","note":"Sabbatai came to Nathan in Gaza in spring 1665. Nathan proclaimed him and remained his prophet for the rest of both their lives."},
 {"a":"sasportas","b":"halevi","kind":"read each other","note":"The two sceptic rabbis corresponded, and Halevi's letters survive because Sasportas kept them."},
 {"a":"sasportas","b":"gluckel","kind":"same street","note":"Both lived in Hamburg's small Jewish world in 1666 and describe the same synagogue jubilation, he with contempt, she with remembered wonder."},
 {"a":"sasportas","b":"eliahu","kind":"opposite sides","note":"Sasportas wrote to the Amsterdam rabbinate urging caution, while the Yeshuot Meshiho brotherhood in the same community pledged loyalty to Sabbatai."},
 {"a":"oldenburg","b":"pepys","kind":"same street","note":"Pepys was elected to the Royal Society in 1665, the year Oldenburg was its secretary, and both recorded the London talk in the same winter."},
 {"a":"pepys","b":"muddiman","kind":"mentioned","note":"Pepys knew Muddiman as a news-writer and mentions him in the diary."},
 {"a":"oldenburg","b":"muddiman","kind":"same street","note":"Oldenburg's news letters went to Joseph Williamson's office, whose newsletters and Gazette Muddiman wrote."},
 {"a":"rycaut","b":"coenen","kind":"same street","note":"The English consul at Smyrna from 1667 and the Dutch minister there until 1672 were both Protestant observers in the city's European quarter, writing about the same events."},
 {"a":"rycaut","b":"abdi","kind":"opposite sides","note":"The English diplomat and the sultan's chronicler wrote the two best-known accounts of the Edirne hearing, one as a lesson in Jewish credulity, the other as the sultan's triumph."},
 {"a":"abdi","b":"sabbatai","kind":"mentioned","note":"Abdi Pasha wrote at the court where Sabbatai lived as Aziz Mehmed Efendi from 1666 to 1673. Whether he attended the hearing in person is not stated in the sources used."},
 {"a":"baruch","b":"nathan","kind":"influenced","note":"Baruch's memorial adopts Nathan's explanation of the apostasy as a hidden mission."},
 {"a":"coenen","b":"nathan","kind":"mentioned","note":"Coenen's 1669 book printed an engraved portrait of Nathan beside Sabbatai's."}
]
d["threads_out"]=[
 {"to":"v1:london-1666","note":"Pepys's messiah wager (February 1666) and Oldenburg's letters come from the London of 1666, the year of plague and the Great Fire. Some Londoners, Jews and Christians, read 1666 as a year of apocalyptic signs."},
 {"to":"v2:vienna-1683","note":"Mehmed IV, before whose court Sabbatai converted at Edirne in 1666, was the sultan whose army besieged Vienna in 1683. The defeat ended his reign in 1687."},
 {"to":"v15:hidden-christians-1865","note":"The Dönme of Salonica, who lived outwardly as Muslims while keeping Sabbatean rites, and Japan's hidden Christians, who kept their faith under outward Buddhism, are two of the best-documented communities that preserved a concealed faith for generations."},
 {"to":"mahdi-1881","note":"Both Sabbatai in 1665–66 and Muhammad Ahmad in 1881 were proclaimed the long-awaited redeemer of their tradition within Ottoman-ruled lands, and both prompted letters, prophecies and mass movements that alarmed Ottoman and foreign authorities."}
]
d["images"]=[
 {"url":"https://posenlibrary.com/node/5735","title":"Tikun keriyah frontispiece, Amsterdam 1666","caption":"Frontispiece of an edition of Nathan of Gaza's penitential prayers printed in Amsterdam by David de Castro Tartas in 1666. It shows Sabbatai enthroned under a crown, with a scene of scholars studying below. It is evidence of how openly Amsterdam's printers and readers embraced the movement.","date":"1666","credit":"Allard Pierson, University of Amsterdam (ROK A 1682), via the Posen Library"},
 {"url":"https://posenlibrary.com/entry/portrait-shabbetai-tzvi","title":"Portrait of Sabbatai Zevi from Coenen (1669)","caption":"Engraving from Thomas Coenen's Ydele verwachtinge der Joden, Amsterdam 1669, showing a turbaned man pointing to an open book, captioned as a true portrait. The artist is unknown and the likeness cannot be confirmed.","date":"1669","credit":"Allard Pierson, University of Amsterdam (ROK A 914), via the Posen Library"},
 {"url":"https://www.posenlibrary.com/entry/portrait-nathan-gaza","title":"Portrait of Nathan of Gaza from Coenen (1669)","caption":"The companion engraving of Nathan in Coenen's book. Like Sabbatai's portrait it was made in Amsterdam by an artist who almost certainly never saw him.","date":"1669","credit":"Posen Library"},
 {"url":"https://ego-plone.uni-trier.de/en/mediainfo/shabtai-zvi","title":"Shabtai Zvi, copper engraving","caption":"Another copy of the Coenen engraving, in the Göttingen State and University Library (8 H E ECCL 932/1), presented by the European History Online project.","date":"before 1669","credit":"SUB Göttingen, via EGO"},
 {"url":"https://cdn.jwa.org/media/sabbateanism","title":"Shabbatai Tzvi enthroned (Tikkun, Amsterdam 1666)","caption":"The 1666 Amsterdam enthronement image as reproduced in the Jewish Encyclopedia (1901–06); public domain.","date":"1666","credit":"Jewish Women's Archive"}
]
d["further"]=[
 {"title":"Gershom Scholem, Sabbatai Sevi: The Mystical Messiah (Princeton, 1973)","url":""},
 {"title":"David J. Halperin, Sabbatai Zevi: Testimonies to a Fallen Messiah (Littman, 2011)","url":HALP},
 {"title":"John Evelyn (from Paul Rycaut), The History of Sabatai Sevi (1669), Project Gutenberg","url":EVELYN},
 {"title":"Joshua Teplitsky, 'Messianic Hope in Hamburg, 1666' (Key Documents of German-Jewish History)","url":TEPL},
 {"title":"Zvi Loker, 'English contemporary opinions on the Sabbatean movement' (JHSE)","url":LOKER},
 {"title":"Yaacob Dweck, 'Jacob Sasportas and Jewish Messianism' (2019)","url":DWECK},
 {"title":"Cengiz Sisman, 'Sabbatai Sevi's Conversion to Islam' (Tablet)","url":SISMAN}
]
d["vantage_key"]="0 = the prophet and the man proclaimed messiah; 1 = in the same city or at the court when it happened; 2 = in the Ottoman capital, hearing through officials and informants; 3 = in Jewish communities in Europe, or writing later from believers' testimony; 4 = abroad, receiving news, rumour and letters."
json.dump(d,open(OUT,"w"),ensure_ascii=False,indent=1)
ids={e["id"] for e in E}
for x in N+C: assert x["eye"] in ids,x
for c in d["convergences"]:
  for e in c["eyes"]: assert e in ids
for t in d["ties"]: assert t["a"] in ids and t["b"] in ids
for x in N:
  assert len(x["quote"].split())<=12,x["quote"]
for e in E: assert len(e["short"])<=16,e["short"]
print(len(E),len(N),len(C),len(d["convergences"]),len(d["ties"]))
