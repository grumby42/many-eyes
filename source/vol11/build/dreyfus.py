import json
OUT="/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/vol11/ch-dreyfus-1894.json"
LET="https://gutenberg.org/files/64720/64720-h/64720-h.htm"
FIVE="https://dn790001.ca.archive.org/0/items/fiveyearsofmylif00dreyuoft/fiveyearsofmylif00dreyuoft_hocr.html"
FIVEC="https://www.canadiana.ca/view/oocihm.72890?usrlang=en"
CINQ="https://m.gutenberg.org/ebooks/38031"
ZT="https://gutenberg.org/files/68561/68561-h/68561-h.htm"
VERITE="https://www.gutenberg.org/ebooks/56808.kindle.images"
STV="https://distantreader.org/stacks/trust/uc2/uc2_ark+=13960=t0ms3n206.txt"
STVPDF="https://archive.org/download/tragedyofdreyfus00steeuoft/tragedyofdreyfus00steeuoft.pdf"
JE="https://jewishencyclopedia.com/articles/5322-dreyfus-case-l-affaire-dreyfus"
RENNES="https://www.marxists.org/history/france/dreyfus-affair/testimony.htm"
PIC="https://famous-trials.com/dreyfus/2609-testimony-of-georges-picquart"
SHAP="https://shapell.org/historical-perspectives/between-the-lines/the-alfred-dreyfus-degradation-ceremony-paris-france/"
OMAHA="https://nebnewspapers.unl.edu/lccn/sn99021999/1899-09-11/ed-1/seq-1/ocr"
SPEC="https://archive.spectator.co.uk/article/16th-september-1899/1/all-civilised-men-outside-france-were-shocked-to-b"
DUKE_TRAITRE="https://exhibits.library.duke.edu/items/show/5235"
DUKE_JUDAS="https://exhibits.library.duke.edu/items/show/5153"
DUKE_RENNES="https://exhibits.library.duke.edu/items/show/5155"
DHM="https://www.dhm.de/lemo/bestand/objekt/bs000095"
ESTW="https://en.wikipedia.org/wiki/Ferdinand_Walsin_Esterhazy"
PALEO="https://edition-originale.com/en/works/history-4/first-editions-134/paleologue-journal-de-l-affaire-dreyfus-1894-1899-l-affaire-dreyfus-et-le-quai-d-orsay-1955-56211"
DRUMW="https://en.wikipedia.org/wiki/%C3%89douard_Drumont"

def eye(id,short,name,life,role,side,where,lat,lon,vant,vl,form,lang,auth,bio,sources,wp=None):
    d=dict(id=id,short=short,name=name,life=life,role=role,side=side,where=where,lat=lat,lon=lon,vantage=vant,vantage_label=vl,form=form,language=lang,authenticity=auth,bio=bio,sources=[{"title":t,"url":u} for t,u in sources])
    if wp: d["waypoints"]=[{"lat":a,"lon":b,"label":c} for a,b,c in wp]
    return d

eyes=[
eye("court","Court record","The courts: courts-martial of 1894 and 1899, the Seine Assize Court, the Cour de cassation","1894–1906 (record)",
 "The proceedings themselves: the closed court-martial of the Military Government of Paris (Cherche-Midi, December 1894); the court-martial that acquitted Esterhazy (January 1898); the Assize Court that tried Zola (February 1898); the Rennes court-martial under Colonel Jouaust (August–September 1899); and the Cour de cassation, which annulled the 1894 judgment (3 June 1899) and the Rennes judgment (12 July 1906)",
 "The French state's military and civil justice; prosecution and defence both recorded",
 "Cherche-Midi military court, Paris; Palais de Justice, Paris; Lycée of Rennes",48.8497,2.3245,0,"the court's own record",
 "court record (sentences; stenographic transcripts of the public hearings)","French",
 "The 1894 court-martial sat behind closed doors and left no public transcript; what is known of it comes from the judgment, later inquiries and testimony. The Zola trial and the Rennes court-martial were taken down in shorthand and printed in full (Rennes: 'Le Procès Dreyfus devant le conseil de guerre de Rennes', Paris, Stock, 1900, 3 vols). An English edition of the Zola trial was published by Benj. R. Tucker in New York in 1898. The judgments of the Cour de cassation were printed officially.",
 "Not a person but the voice of the proceedings, set beside the people they judged. Over twelve years the same accusation passed through five different tribunals, military and civil, and their records frame every other voice in the chapter.",
 [("Le Procès Dreyfus (Rennes, 1899): Dreyfus's interrogation, English translation by Mitchell Abidor",RENNES),("The Trial of Emile Zola (Tucker, New York, 1898), Project Gutenberg",ZT),("Jewish Encyclopedia (1901–06), 'Dreyfus Case'",JE)],
 wp=[(48.8497,2.3245,"Cherche-Midi court-martial, Dec 1894"),(48.8556,2.3450,"Palais de Justice, Zola trial, Feb 1898"),(48.1089,-1.6747,"Rennes court-martial, Aug–Sept 1899"),(48.8556,2.3450,"Cour de cassation, 12 July 1906")]),
eye("dreyfus","Alfred Dreyfus","Alfred Dreyfus","1859–1935",
 "Captain of artillery, aged 35 at his arrest, a probationer on the General Staff; Alsatian-born, Jewish, from a family of textile manufacturers at Mulhouse",
 "The accused","Cherche-Midi and La Santé prisons, Paris; Saint-Martin-de-Ré; Devil's Island, French Guiana; military prison at Rennes",5.2947,-52.5836,0,"the accused",
 "dated letters; prison diary; memoir (written 1901)","French",
 "His letters to his wife were published in Paris in 1898 as 'Lettres d'un innocent' and in English in 1899 (Harper, tr. L. G. Moreau). 'Cinq années de ma vie' (1901; English 'Five Years of My Life', tr. James Mortimer, 1901) joins a narrative written after his release with the diary he kept on Devil's Island from 14 April 1895 to September 1896, which had been confiscated by the prison administration and was returned to him. Letters were read and copied by officials before delivery, so he wrote knowing they would be.",
 "The one voice that saw everything from inside the cell. He hardly knew, for most of his imprisonment, that an 'Affair' existed: his letters and diary keep returning to honour, to his family and to the search for the real culprit, while Paris fought over his name.",
 [("Lettres d'un innocent: The Letters of Captain Dreyfus to His Wife (1899), Project Gutenberg",LET),("Five Years of My Life (Toronto: Morang, 1901), Internet Archive OCR",FIVE),("Cinq années de ma vie (1901), Project Gutenberg",CINQ),("Shapell Manuscript Foundation: letter of 14 January 1895",SHAP)],
 wp=[(48.8497,2.3245,"Cherche-Midi prison, Oct–Dec 1894"),(48.8512,2.3054,"École Militaire, degradation, 5 Jan 1895"),(46.2022,-1.3658,"Saint-Martin-de-Ré, Jan–Feb 1895"),(5.2947,-52.5836,"Devil's Island, Apr 1895 – June 1899"),(48.1089,-1.6747,"Rennes, July–Sept 1899"),(48.8512,2.3054,"École Militaire, decorated, July 1906")]),
eye("mathieu","Mathieu Dreyfus","Mathieu Dreyfus","1857–1930",
 "Alfred's elder brother, manager of the family mill at Mulhouse; organiser of the family's campaign for revision",
 "The Dreyfus family","Paris and Mulhouse; Rennes in 1899",48.8566,2.3522,2,"family campaigner",
 "dated letter; memoir (written later)","French",
 "His public letter to the Minister of War of 15 November 1897 was printed in the press at once. His memoir 'L'Affaire telle que je l'ai vécue' was written long afterwards and published only in 1978; anything drawn from it is recollection, not a contemporary record.",
 "The man who turned a private catastrophe into a public case. He gathered handwriting evidence, recruited allies and, when the identity of the bordereau's real writer reached him, named him openly.",
 [("Jewish Encyclopedia, 'Dreyfus Case' (Mathieu's letter of 15 Nov 1897)",JE)]),
eye("herzl","Herzl","Theodor Herzl","1860–1904",
 "Paris correspondent of the Vienna Neue Freie Presse, aged 34; playwright and feuilletonist",
 "Viennese liberal press; later founder of political Zionism","In the press seats at the 1894 trial and in the École Militaire courtyard for the degradation",48.8512,2.3054,1,"foreign correspondent at the scene",
 "newspaper dispatches; diary (from 1895); later article","German",
 "His dispatches appeared in the Neue Freie Presse in December 1894 and January 1895. His diaries begin in the spring of 1895 and say little about Dreyfus at first. The well-known statement that the Dreyfus trial made him a Zionist dates from 1899, after the Affair had become a cause; historians treat it as a later reading of his own path, not a description recorded in 1895.",
 "A sharp-eyed theatre writer watching a ritual of public humiliation. What he reported in 1895 and what he later said it meant to him are two different documents, and the chapter keeps them apart.",
 [("Jewish Encyclopedia, 'Dreyfus Case'",JE),("ACJNA: re-thinking Herzl's analysis of the case","https://acjna.org/articles/one-hundred-years-after-the-exoneration-of-alfred-dreyfus-re-thinking-theodor-herzls-analysis-of-this-landmark-case/")],
 wp=[(48.8566,2.3522,"Paris correspondent, 1891–95"),(48.2082,16.3738,"Vienna, literary editor, from July 1895")]),
eye("drumont","La Libre Parole","Édouard Drumont and La Libre Parole","1844–1917",
 "Editor of the Paris daily La Libre Parole, founded 1892; author of 'La France juive' (1886) and founder of the National Antisemitic League (1889)",
 "Antisemitic nationalist press","Editorial offices, Paris",48.8700,2.3430,2,"the anti-Dreyfusard press",
 "newspaper","French",
 "The paper's articles and its illustrated weekly supplement survive in library runs. It was the first paper to publish Dreyfus's name, using information leaked from within the War Ministry; its campaign framed the case from the start as proof of a Jewish conspiracy. Its words are summarised here plainly, without repeating its slurs.",
 "The loudest voice of the accusers in the street. Its role is part of the record because it shaped what the public believed before any trial began, and because it later raised funds in honour of the officer whose forgery was exposed.",
 [("Duke University Libraries exhibit: La Libre Parole illustrée, 10 Nov 1894",DUKE_JUDAS),("Édouard Drumont (encyclopedia article)",DRUMW)]),
eye("picquart","Picquart","Georges Picquart","1854–1914",
 "Lieutenant-colonel, head of the army's Statistical Section (intelligence) from July 1895; earlier a teacher of Dreyfus at the École de Guerre",
 "French army; became a Dreyfusard witness","War Ministry, Paris; then posted to Tunisia; Mont-Valérien and prisons in 1898; witness at Paris and Rennes",48.8566,2.3522,0,"intelligence chief turned witness",
 "testament letter; sworn testimony","French",
 "His sealed letter of 2 April 1897, written at Sousse 'to be delivered to the President of the Republic' in case of his death, survives and is printed in the case literature. His testimony at the Zola trial and at Rennes is in the stenographic records. He was no admirer of Dreyfus personally and shared some of the prejudices of his milieu; his case rested on the documents.",
 "The insider who found that the handwriting of the bordereau matched another officer's and would not let it go. He was moved away, then arrested, then promoted to general and made Minister of War in 1906.",
 [("Picquart's letter of 2 April 1897 (English translation), Famous Trials",PIC),("Steevens, The Tragedy of Dreyfus (1899), ch. VIII 'Picquart'",STV)],
 wp=[(48.8566,2.3522,"War Ministry, 1895–96"),(35.8256,10.6360,"Sousse, Tunisia, 1897"),(48.8735,2.2131,"Mont-Valérien, Jan 1898"),(48.1089,-1.6747,"Rennes witness, Aug 1899")]),
eye("esterhazy","Esterhazy","Ferdinand Walsin Esterhazy","1847–1923",
 "Major of infantry, deeply in debt, in contact with the German military attaché Schwartzkoppen",
 "French army; later self-exiled in England","Paris; tried at Cherche-Midi in January 1898; London and Harpenden from September 1898",48.8497,2.3245,0,"the officer named as the bordereau's writer",
 "court record; newspaper interviews","French",
 "Acquitted by court-martial in January 1898. After fleeing to England he told The Observer (interviews published 18 and 25 September 1898, by the editor Rachel Beer) that he had written the bordereau, saying he had done so on the orders of his superior Colonel Sandherr; that explanation is his own claim, and he gave shifting versions afterwards.",
 "The man whose handwriting matched the bordereau's. He was publicly cleared, cheered and then, abroad, told reporters he was its writer, while insisting he had been acting on orders.",
 [("Ferdinand Walsin Esterhazy (encyclopedia article)",ESTW),("Jewish Encyclopedia, 'Dreyfus Case'",JE)],
 wp=[(48.8497,2.3245,"Cherche-Midi, court-martial, Jan 1898"),(51.5072,-0.1276,"London, Sept 1898"),(51.8155,-0.3566,"Harpenden, later years")]),
eye("henry","Henry","Hubert-Joseph Henry","1846–1898",
 "Major, later lieutenant-colonel, of the Statistical Section; risen from the ranks; principal army witness in 1894",
 "French army intelligence","War Ministry, Paris; court-martial witness box 1894; Zola trial 1898; Mont-Valérien fortress",48.8566,2.3522,0,"accuser and forger",
 "sworn testimony; forged document; official interrogation record","French",
 "No diary. His voice survives in testimony, in the document he forged in 1896 (exposed in August 1898) and in the minutes of his interrogation by the Minister of War, Godefroy Cavaignac, on 30 August 1898. The theatrical words attributed to him at the 1894 hearing are known from later accounts of the closed session.",
 "The accuser whose evidence collapsed. To his defenders in 1898 he was a patriot who had done what the army needed; to the revisionists he was the proof that the case had been built on falsehood.",
 [("Jewish Encyclopedia, 'Dreyfus Case'",JE),("Steevens, The Tragedy of Dreyfus (1899), appendix",STV)],
 wp=[(48.8566,2.3522,"War Ministry, 1894–98"),(48.8735,2.2131,"Mont-Valérien, 30–31 Aug 1898")]),
eye("zola","Zola","Émile Zola","1840–1902",
 "Novelist, aged 57 in 1898, the most widely read French author of his day",
 "Dreyfusard","Paris; the Assize Court of the Seine; exile in and around London, July 1898 – June 1899",48.8566,2.3522,1,"accuser of the accusers, then defendant",
 "open letters and articles; trial declaration","French",
 "His articles of 1897–1900 were collected by Zola himself as 'La Vérité en marche' (1901). 'J'accuse…!' appeared on the front page of L'Aurore on 13 January 1898; its headline was chosen by the paper's editor Georges Clemenceau. His trial was printed in English translation in New York in 1898.",
 "The writer who chose to be prosecuted for libel so that the case would be heard in open court. His trial became a second Dreyfus trial fought through witnesses and the judge's rulings.",
 [("La Vérité en marche (1901), Project Gutenberg",VERITE),("The Trial of Emile Zola (Tucker, 1898), Project Gutenberg",ZT),("Deutsches Historisches Museum: L'Aurore, 13 Jan 1898",DHM)],
 wp=[(48.8566,2.3522,"Paris, 1897–98"),(48.8049,2.1204,"Versailles, 18 July 1898"),(51.4183,-0.0836,"Upper Norwood, London, 1898–99"),(48.8566,2.3522,"Paris, from June 1899")]),
eye("blum","Léon Blum","Léon Blum","1872–1950",
 "Young jurist at the Conseil d'État and literary critic, aged 25 in 1897",
 "Dreyfusard","Paris literary and political circles",48.8566,2.3522,2,"a young Dreyfusard in Paris",
 "memoir (written later)","French",
 "'Souvenirs sur l'Affaire' was written in 1935, when Blum was leader of the Socialist party, nearly forty years after the events. It is a memoir, and its scenes are given here as his later recollection.",
 "A generation's witness: he describes how the Affair split friendships, salons and families, and how it drew him into politics.",
 [("Bibliography of the Dreyfus Affair","https://en.wikipedia.org/wiki/Bibliography_of_the_Dreyfus_Affair")]),
eye("paleologue","Paléologue","Maurice Paléologue","1859–1944",
 "Diplomat at the Quai d'Orsay, liaison between the Foreign Ministry and the War Ministry on intelligence matters; the ministry's delegate at the Rennes court-martial",
 "Foreign Ministry","Paris; Rennes in August–September 1899",48.1089,-1.6747,1,"official observer",
 "journal (published 1955)","French",
 "'Journal de l'affaire Dreyfus, 1894–1899' was published by Plon in 1955, eleven years after the author's death (English 'My Secret Diary of the Dreyfus Case'). How far the text was reworked between writing and publication is not settled; it is treated here as a diary of uncertain finish, and its entries are given only in outline.",
 "A sceptical insider at the edge of the secret files, writing for himself about generals and ministers he dealt with daily.",
 [("Plon 1955 first edition (bookseller record)",PALEO),("My Secret Diary of the Dreyfus Case (library record)","https://folio.caval.edu.au/Record/c000367295/Description")]),
eye("steevens","Steevens","George Warrington Steevens","1869–1900",
 "Special correspondent of the London Daily Mail, aged 30",
 "British press","Press benches in the hall of the Lycée at Rennes",48.1089,-1.6747,1,"reporter in the courtroom",
 "newspaper dispatches collected as a book","English",
 "'The Tragedy of Dreyfus' (London and New York: Harper, 1899) collects and arranges his Rennes reports in twenty chapters with an appendix of documents. Written for an English public largely convinced of Dreyfus's innocence, it is vivid and openly partisan in its judgements, while careful in its description of the room.",
 "The best English eye in the room at Rennes. He describes faces, voices and the hall itself, and records what the verdict sounded like to someone who heard it read.",
 [("The Tragedy of Dreyfus (1899), text",STV),("The Tragedy of Dreyfus (1899), PDF",STVPDF),("The Spectator, 4 Nov 1899, review","https://archive.spectator.co.uk/article/4th-november-1899/12/the-tragedy-of-dreyfus-by-g-w-steevens-harper-and")]),
eye("press","Press abroad","The Associated Press and the English-language weeklies","1899 (reports)",
 "Wire correspondents at Rennes and the London weekly press reporting the verdict to readers abroad",
 "American and British press","Rennes (AP correspondent); London (The Spectator); printed in Omaha, Nebraska",41.2565,-95.9345,4,"abroad, news by cable",
 "newspaper","English",
 "The Omaha Daily Bee of 11 September 1899 printed the AP Rennes dispatch of 10 September with New York World cables from London, Berlin and Rome; the page survives as a scanned original with OCR in Nebraska Newspapers. The Spectator's 16 September 1899 issue is in its own digital archive.",
 "How the rest of the world heard it: by cable, the next morning, in columns that mixed courtroom detail with reports of street reactions from London to Indianapolis.",
 [("Omaha Daily Bee, 11 Sept 1899, p. 1 (OCR)",OMAHA),("The Spectator, 16 Sept 1899, p. 1",SPEC)],
 wp=[(48.1089,-1.6747,"AP correspondent, Rennes"),(51.5072,-0.1276,"The Spectator, London"),(41.2565,-95.9345,"Omaha Daily Bee")]),
eye("twain","Mark Twain","Samuel L. Clemens (Mark Twain)","1835–1910",
 "American author, aged 59, living in Paris in the winter of 1894–95",
 "American; later a public admirer of Zola","Paris",48.8566,2.3522,2,"a foreign writer in Paris, reading the papers",
 "dated note","English",
 "A one-page autograph note signed 'S.L. Clemens' to a Mr Wilson, dated 11 February with the year [1895] supplied by the cataloguers, is in the Shapell Manuscript Collection.",
 "A small, sharp private question from an American in Paris, about how the press was reporting the prisoner's treatment.",
 [("Shapell Manuscript Foundation: Twain's note on Dreyfus",SHAP)]),
]

E=[]
def ent(d,disp,prec,eye,place,head,dig,src,q="",conf="verified"):
    E.append(dict(date_iso=d,date_display=disp,precision=prec,eye=eye,place=place,headline=head,digest=dig,quote=q,confidence=conf,source_note=src))

ent("1894-10-15","Monday 15 October 1894","day","dreyfus","War Ministry, rue Saint-Dominique, Paris",
 "Summoned in civilian dress, made to write a dictated letter",
 "Called to the Ministry early on a Monday, he found Major du Paty de Clam waiting to dictate a letter to him. Du Paty told him sharply that he was trembling; Dreyfus answered that his fingers were cold. The dictation broke off, he was arrested for high treason and taken to the Cherche-Midi prison without being told what he was supposed to have done.",
 "Five Years of My Life (1901), opening narrative, Internet Archive OCR")
ent("1894-11-01","Thursday 1 November 1894","day","drumont","Paris",
 "Libre Parole names the arrested officer and calls him a traitor",
 "After hinting on 29 October at an arrest kept secret, the paper issued a special edition announcing that the arrested officer was Dreyfus and that he was Jewish, presenting the case as high treason and proof of a wider Jewish danger. The War Ministry had not yet announced anything; the leak placed the case in public before any evidence was tested.",
 "Jewish Encyclopedia, 'Dreyfus Case' (dates of 29 Oct and 1 Nov 1894)")
ent("1894-11-10","Saturday 10 November 1894","day","drumont","Paris",
 "Illustrated supplement shows Drumont sweeping Dreyfus away",
 "The weekly 'Libre Parole illustrée' carried a full-page caricature showing a giant Drumont pushing a tiny Dreyfus, drawn in a German spiked helmet, into a drain with tongs, while a soldier stands in the dawn behind. It was the paper's message in one image: the accused was foreign filth and the nation was being cleansed.",
 "Duke University Libraries exhibit, 'A propos de Judas Dreyfus', La Libre Parole illustrée, 10 Nov 1894")
ent("1894-12-19","Wednesday 19 December 1894","day","court","Cherche-Midi military court, Paris",
 "Court-martial opens and the public is sent out",
 "Seven officer-judges of the first court-martial of Paris heard the case. At the prosecutor's request the court ordered a closed hearing over the objection of the defence counsel Edgar Demange, so that no shorthand record of the evidence was published. The case rested chiefly on the bordereau, an unsigned list of documents offered to the Germans, and on conflicting handwriting experts.",
 "Jewish Encyclopedia, 'Dreyfus Case' (four days of hearings from 19 Dec 1894)")
ent("1894-12","December 1894 (during the hearings)","range","henry","Cherche-Midi military court, Paris",
 "The intelligence officer swears the traitor sits in the room",
 "Major Henry, the principal army witness, told the closed court that an honourable person had warned the Statistical Section of a traitor in the ministry and, pointing at the accused, declared that this was the man; he refused to name his informant. The scene is known from later inquiries and accounts of the closed session, not from any contemporary transcript.",
 "Accounts of the closed 1894 hearing in the later case literature (Rennes and Cour de cassation inquiries); no transcript of 1894",conf="approx")
ent("1894-12-22","Saturday 22 December 1894","day","court","Cherche-Midi military court, Paris",
 "Unanimous verdict: guilty, deportation for life, degradation",
 "After the prosecutor's address and Demange's pleading, the judges withdrew and returned a unanimous verdict of guilty. The sentence was deportation for life to a fortified place and military degradation. Later inquiries established that during deliberation the judges had been handed a secret file of documents that the defence never saw.",
 "Jewish Encyclopedia, 'Dreyfus Case'; Cour de cassation judgment of 3 June 1899 on the secret communication")
ent("1894-12","December 1894","month","herzl","Paris",
 "A Viennese correspondent follows the closed trial for Vienna",
 "Herzl reported the case to the Neue Freie Presse as a sensational espionage trial held behind closed doors. Scholars disagree on how far he doubted the verdict at the time; his dispatches do not make the case a cause.",
 "Neue Freie Presse dispatches, Dec 1894, as summarised in the Herzl literature (ACJNA article)",conf="approx")
ent("1894-12-23","Sunday 23 December 1894","day","dreyfus","Cherche-Midi prison, Paris",
 "After the verdict: an appeal signed, a plea to find the culprit",
 "The morning after his conviction he wrote to Lucie that he had signed his appeal, and urged that the search for the real writer of the bordereau must go on. Thoughts of suicide run under the letter; he says he will live for her and the children and for his name.",
 "Letters of Captain Dreyfus to His Wife (Harper, 1899), letter of 23 Dec 1894")
ent("1895-01-05","Saturday 5 January 1895","day","dreyfus","Courtyard of the École Militaire, then La Santé prison",
 "Stripped of rank before troops and a crowd",
 "Before the assembled troops a warrant officer tore the insignia from his uniform and broke his sword. He shouted to the soldiers that an innocent man was being degraded and called out his innocence to the crowd beyond the railings. That evening, in La Santé, he wrote to Lucie that he would not tell her what he had suffered that day, but that he would go on living.",
 "Five Years of My Life (1901); Letters of Captain Dreyfus to His Wife, letter dated 5 Jan 1895, 'In the Prison of La Santé'")
ent("1895-01-05","Saturday 5 January 1895","day","herzl","Courtyard of the École Militaire, Paris",
 "A Viennese reporter watches the sword broken and hears the crowd",
 "Herzl stood among the journalists for the degradation and wired a report for the next day's paper describing the ritual, the condemned man's protest of innocence and the crowd's cries for his death. In 1899, after the Affair had become a cause, he wrote that the mob had shouted against the Jews and that the scene had made him a Zionist; the 1895 dispatch and the 1899 interpretation are separate documents.",
 "Neue Freie Presse, 6 Jan 1895; Herzl's 1899 statement as quoted in the Herzl literature (ACJNA article)",conf="approx")
ent("1895-01-14","Monday 14 January 1895","day","dreyfus","La Santé prison, Paris",
 "To his sister: the infamy on his name and a clean conscience",
 "Nine days after the degradation he wrote to his sister and brother-in-law, Henriette and Joseph Valabrègue, that he suffered horribly from the disgrace fastened to his name, but that a pure conscience gave him strength and he would clear it. The same day he told Lucie that he paced his cell like a caged animal, unable to help in the search.",
 "Shapell Manuscript Collection, autograph letter of 14 Jan 1895; Letters of Captain Dreyfus to His Wife, letter of 14 Jan 1895")
ent("1895-02-11","Monday 11 February [1895]","day","twain","Paris",
 "Twain asks whether a report of an assault was contradicted",
 "In a short note to a Mr Wilson, Clemens asked where he had seen the report that an officer had struck Dreyfus in the face with a sword hilt during his transfer, whether it came from a French paper, whether it had been denied, and whether the paper had condemned the act. The report had circulated in the Paris press in late January.",
 "Shapell Manuscript Collection, ALS 'S.L. Clemens', dated 11 Feb, year supplied by cataloguers",
 q="Has it been contradicted?",conf="approx")
ent("1895-03-12","Tuesday 12 March 1895","day","dreyfus","Aboard ship in the roadstead of the Îles du Salut",
 "Arrival off Guiana: honour above life",
 "After the voyage out from France, he wrote to Lucie on arriving off the Îles du Salut that he could only bear to live if his honour were restored. He was kept aboard for days and landed on 15 March, and he begged her to press the search without pause.",
 "Letters of Captain Dreyfus to His Wife, letters of 12 and 15 March 1895; Five Years of My Life (landing 15 March)")
ent("1895-04-14","Sunday 14 April 1895","day","dreyfus","Devil's Island, Îles du Salut",
 "The first page of the Devil's Island diary",
 "The day after he was moved to the small island set aside for him, he began a diary of what he called his miserable life. He records the hut, the guards who were forbidden to speak to him, and the hours he filled to keep his mind from breaking; he intended the diary for Lucie in case he did not survive.",
 "Five Years of My Life (1901), diary entry of 14 April 1895 (transfer to Devil's Island 13 April)")
ent("1896-03","March 1896","month","picquart","Statistical Section, War Ministry, Paris",
 "A torn express letter points to another officer",
 "Among scraps recovered from the German embassy's waste paper, Picquart's section received a torn express card addressed to Major Esterhazy, apparently from the German attaché. Investigating Esterhazy over the following months, he compared his handwriting with the bordereau and concluded that they matched.",
 "Jewish Encyclopedia, 'Dreyfus Case' (petit bleu, March 1896); Picquart's letter of 2 April 1897",conf="approx")
ent("1896-09-07","Monday 7 September 1896","day","dreyfus","Devil's Island",
 "Put in irons at night without explanation",
 "He recorded that the evening before he had been put in irons, fastened to his bed through the night, and that no reason was given. The next day he wrote of wishing for the grave; on the 9th the commandant called it a precaution, an explanation he rejected. The measure followed false press reports of an escape plot.",
 "Five Years of My Life (1901), diary entries of 6–9 Sept 1896")
ent("1896-11","November 1896 (date assigned in the case literature)","month","henry","Statistical Section, War Ministry, Paris",
 "A letter is manufactured naming Dreyfus",
 "Henry produced a letter presented as written by the Italian attaché that named Dreyfus outright, and passed it to his superiors as confirming the guilt; it was assembled from genuine fragments and forged text. It was shown to ministers and cited in the Chamber in July 1898 before its exposure a few weeks later.",
 "Jewish Encyclopedia, 'Dreyfus Case'; Steevens (1899), appendix (Cavaignac's speech of 7 July 1898)",conf="approx")
ent("1897-04-02","Friday 2 April 1897","day","picquart","Sousse, Tunisia",
 "A sealed letter for the President, to be opened at his death",
 "Removed from Paris and posted to a regiment of tirailleurs in Tunisia, Picquart wrote a statement certifying that Esterhazy was an agent of Germany and that the bordereau was in his hand, that the 1894 trial had relied on a secret file not shown to the defence, and that his superiors had moved him to stop the inquiry. He sealed it for delivery to the President of the Republic only if he died.",
 "Picquart's letter dated Sousse, 2 April 1897 (English translation, Famous Trials)")
ent("1897-11-15","Monday 15 November 1897","day","mathieu","Paris",
 "Mathieu publicly names Esterhazy to the Minister of War",
 "Having learned from a banker who recognised Esterhazy's handwriting in a facsimile of the bordereau, Mathieu wrote to the Minister of War denouncing Esterhazy as its author. The letter was published, forcing the army to open an inquiry into Esterhazy.",
 "Jewish Encyclopedia, 'Dreyfus Case' (letter of the night of 15 Nov 1897)")
ent("1897-11-25","Thursday 25 November 1897","day","zola","Paris",
 "First article in Le Figaro: truth is on the march",
 "Zola's first article on the case defended the senator Scheurer-Kestner, who had taken up the cause, and closed with a sentence that became the Dreyfusards' watchword. He collected it in 1901 in 'La Vérité en marche'.",
 "La Vérité en marche (1901), 'M. Scheurer-Kestner' (Le Figaro)",q="La vérité est en marche",conf="approx")
ent("1897-12","Winter 1897–98 (recalled in 1935)","range","blum","Paris",
 "A young admirer asks Barrès to join, and is refused",
 "Blum recalled going to see Maurice Barrès, the writer his generation revered, sure that he would sign for revision. Barrès hesitated and then declined in writing, choosing the national side; Blum described the moment as the breaking of a literary allegiance. It is a memory set down almost forty years later.",
 "Léon Blum, Souvenirs sur l'Affaire (1935)",conf="approx")
ent("1898-01-11","Tuesday 11 January 1898","day","esterhazy","Cherche-Midi military court, Paris",
 "Acquitted unanimously after two days, mostly in camera",
 "Esterhazy's court-martial sat on 10 and 11 January, hearing the expert evidence behind closed doors, and acquitted him unanimously after a few minutes' deliberation. Crowds outside cheered him as he left.",
 "Jewish Encyclopedia, 'Dreyfus Case'; Esterhazy encyclopedia article")
ent("1898-01-13","Thursday 13 January 1898","day","zola","Paris",
 "'J'accuse…!' fills the front page of L'Aurore",
 "Two days after the acquittal, Zola's open letter to President Félix Faure ran across L'Aurore's front page. It accused by name the generals and officers he held responsible, among them du Paty de Clam, Mercier, Billot, de Boisdeffre and Gonse, and the handwriting experts, and the two courts-martial, and it invited prosecution so that the facts would be aired in open court.",
 "The Trial of Emile Zola (Tucker, 1898), text of the letter; Deutsches Historisches Museum, L'Aurore 13 Jan 1898",q="J'accuse…!")
ent("1898-02-07","Monday 7 February 1898","day","court","Assize Court of the Seine, Palais de Justice, Paris",
 "Zola's libel trial opens; the judge fences off the Dreyfus case",
 "The Ministry of War prosecuted only a few lines of the letter, those accusing the Esterhazy court of acquitting on orders. Again and again over fifteen days the presiding judge Delegorgue refused questions from Labori, Zola's counsel, that touched the 1894 trial, a ruling recorded in the English edition as a refrain.",
 "The Trial of Emile Zola (Tucker, 1898), hearings of 7–23 Feb 1898",q="The question will not be put.")
ent("1898-02-12","Saturday 12 February 1898","day","henry","Assize Court of the Seine, Paris",
 "Henry calls Picquart a liar in open court",
 "Called against Zola, Henry contradicted Picquart's account of the secret file and, when pressed, called him a liar from the witness stand. Picquart answered calmly before the jury; the two later fought a duel. Both men's evidence fills the record of these days.",
 "The Trial of Emile Zola (Tucker, 1898), hearings of 11–12 Feb 1898",conf="approx")
ent("1898-02-21","Monday 21 February 1898","day","zola","Assize Court of the Seine, Paris",
 "Zola's own declaration to the jury",
 "After the Attorney-General's summing-up, Zola read a statement swearing to Dreyfus's innocence, staking his forty years of work and his name on it, and saying that he had not wished his country to stay in falsehood and injustice. Parts of the room protested as he spoke.",
 "The Trial of Emile Zola (Tucker, 1898), Thirteenth Day, 21 Feb 1898")
ent("1898-02-23","Wednesday 23 February 1898","day","court","Assize Court of the Seine, Paris",
 "Zola convicted: one year and a 3,000-franc fine",
 "The jury found Zola and the manager of L'Aurore guilty of defamation. Zola received the maximum, one year's imprisonment and a fine of 3,000 francs. The judgment was quashed on a technicality in April and the case reheard at Versailles.",
 "Jewish Encyclopedia, 'Dreyfus Case' (verdict of 23 Feb 1898)")
ent("1898-07-18","Monday 18 July 1898","day","zola","Versailles, then the night train to Calais",
 "Convicted again at Versailles, he leaves for England",
 "At the retrial in Versailles, after the defence withdrew, Zola was condemned in his absence. On his lawyers' and friends' advice he left that night for London to avoid being served with the judgment, arriving on 19 July; he lived for most of the following year in hotels and rented houses around Norwood, unable to speak English.",
 "Jewish Encyclopedia, 'Dreyfus Case'; Michael Rosen on Zola in London")
ent("1898-08-30","Tuesday 30 August 1898","day","henry","War Ministry, Paris",
 "Questioned by the Minister, Henry admits the forgery",
 "Cavaignac, the Minister of War, had learned that the letter naming Dreyfus was a composite. Questioned in his office in the presence of generals, Henry first denied and then admitted fabricating it, saying he had acted for the good of the country. He was arrested and taken to the fortress of Mont-Valérien.",
 "Minutes of Henry's interrogation (official), as summarised in the Jewish Encyclopedia, 'Dreyfus Case'")
ent("1898-08-31","Wednesday 31 August 1898","day","henry","Fortress of Mont-Valérien",
 "Found dead in his cell the next day",
 "Henry died by suicide in his cell. He left a letter to his wife protesting that he had acted for the good. The news, together with the confession, made revision of the 1894 verdict hard to refuse.",
 "Jewish Encyclopedia, 'Dreyfus Case' (death on 31 Aug 1898)")
ent("1898-09-18","Sunday 18 September 1898","day","esterhazy","London (interview with The Observer)",
 "Esterhazy tells an English paper he wrote the bordereau",
 "Having left France at the start of September, Esterhazy told The Observer that he was the writer of the bordereau, claiming he had written it on Colonel Sandherr's orders to trap a traitor. The paper's editor Rachel Beer published the interviews on 18 and 25 September.",
 "Esterhazy encyclopedia article (Observer, 18 and 25 Sept 1898)")
ent("1898-12","December 1898 – January 1899","range","drumont","Paris",
 "A subscription in Henry's honour fills the paper's columns",
 "La Libre Parole opened a public subscription for Henry's widow to fund her libel suit against a Dreyfusard writer. Day after day it printed the lists of donors with their messages, many of them hostile to Jews, and the 'Monument Henry' became an anti-Dreyfusard rallying cause.",
 "Case literature on the Henry subscription (La Libre Parole, Dec 1898–Jan 1899)",conf="approx")
ent("1899-06-03","Saturday 3 June 1899","day","court","Cour de cassation (united chambers), Paris",
 "Highest court annuls the 1894 judgment, orders a new court-martial",
 "The united chambers quashed the 1894 conviction, citing the secret communication of documents to the judges and new evidence on the bordereau, and sent Dreyfus before a fresh court-martial at Rennes.",
 "Jewish Encyclopedia, 'Dreyfus Case' (decision of 3 June 1899)")
ent("1899-06-05","Monday 5 June 1899","day","zola","Paris",
 "Back from England, Zola writes 'Justice'",
 "With the Cour de cassation's decision announced, Zola returned from exile and published an article in L'Aurore greeting the ruling as the victory of justice. He collected it in 'La Vérité en marche'.",
 "La Vérité en marche (1901)",conf="approx")
ent("1899-06-08","Thursday 8 June 1899","day","dreyfus","Devil's Island",
 "A note in the warder's hand: no longer a convict",
 "Shortly after noon the chief warder gave him a note announcing that the Cour de cassation had annulled the judgment and that he was no longer under the convict regime. The next morning he was rowed out to the cruiser Sfax to sail for France.",
 "Five Years of My Life (1901), narrative of 8–9 June 1899")
ent("1899-07-01","Saturday 1 July 1899","day","dreyfus","Port-Haliguen (Quiberon), then Rennes military prison",
 "Landed at night, and reunited with Lucie at Rennes",
 "Transferred from the Sfax by steam launch in rough weather, he was landed at about two in the morning, taken by carriage and train to the military prison at Rennes by six, and that morning saw his wife for the first time in nearly five years. He wrote that words could not describe the meeting.",
 "Five Years of My Life (1901), narrative of 30 June – 1 July 1899")
ent("1899-08-07","Monday 7 August 1899","day","court","Hall of the Lycée, Rennes",
 "Rennes court-martial opens; the accused is questioned",
 "Seven officer-judges under Colonel Jouaust heard the case in the festival hall of the lycée. The president questioned Dreyfus at length on the bordereau, on the documents he could have known, on his travels and private life and on what he was said to have told an officer on the day of degradation. Dreyfus answered point by point and repeated that he was innocent.",
 "Le Procès Dreyfus devant le conseil de guerre de Rennes (Stock, 1900), interrogation (English tr. Abidor)")
ent("1899-08-07","Monday 7 August 1899","day","steevens","Hall of the Lycée, Rennes",
 "The prisoner walks in, aged far beyond his years",
 "Steevens watched Dreyfus enter and was shocked by how worn he looked: thirty-nine but stiff, thin, his face burned and pale at once, his voice cracking when he declared his innocence. He was struck that the man the world had argued over for years seemed so slight.",
 "The Tragedy of Dreyfus (1899), ch. IV 'Dreyfus'",q="an old, old man of thirty-nine")
ent("1899-08-12","Saturday 12 August 1899","day","steevens","Hall of the Lycée, Rennes",
 "General Mercier holds the floor for three and a half hours",
 "Steevens described the former Minister of War, who had ordered the 1894 prosecution, holding the floor for some three and a half hours to restate the army's case against the prisoner, and the defence's attempts to question him.",
 "The Tragedy of Dreyfus (1899), ch. V 'Mercier'")
ent("1899-08-14","Monday 14 August 1899","day","steevens","Rennes",
 "Labori shot in the street on his way to court",
 "On the Monday morning Dreyfus's counsel Fernand Labori was shot in the back while walking to the hearing; the gunman escaped across the fields and was never caught. Steevens wrote of the shock in the town and of the trial going on without Labori while he recovered.",
 "The Tragedy of Dreyfus (1899), ch. VI 'A Shot in the Street'; Jewish Encyclopedia (14 Aug 1899)")
ent("1899-08","August 1899","month","paleologue","Rennes",
 "The Foreign Ministry's delegate watches the secret file debated",
 "As the ministry's representative, Paléologue followed the closed sessions on the secret dossier, in which diplomatic documents were in question, and kept notes on the generals and ministers involved. His journal, printed only in 1955, is used here only in outline.",
 "Paléologue, Journal de l'affaire Dreyfus (Plon, 1955)",conf="approx")
ent("1899-09-09","Saturday 9 September 1899","day","court","Hall of the Lycée, Rennes",
 "Guilty by five votes to two, 'with extenuating circumstances'",
 "After hearing Demange's closing plea and a brief final statement from Dreyfus, the judges deliberated and found him guilty of treason by five votes to two, with extenuating circumstances, and sentenced him to ten years' detention. The verdict was read in his absence and then to him separately by the clerk, as the procedure required.",
 "Jewish Encyclopedia, 'Dreyfus Case' (9 Sept 1899); Omaha Daily Bee, 11 Sept 1899")
ent("1899-09-09","Saturday 9 September 1899","day","steevens","Hall of the Lycée, Rennes",
 "The verdict heard as a single gasp",
 "Steevens recorded the soldiers presenting arms, the president reading in a thin, nearly inaudible voice, the words 'guilty' and 'ten years' carrying, and the hall answering with one sound, half gasp and half sob. He noticed that both defence counsel were in tears; then the audience filed out silently, past calm streets that seemed to him monstrous in their ordinariness.",
 "The Tragedy of Dreyfus (1899), ch. XIX 'Guilty!'",q="half gasp, half sob")
ent("1899-09-10","Sunday 10 September 1899","day","press","Rennes (AP dispatch), printed in Omaha 11 Sept",
 "AP: the prisoner expects freedom; the world reacts",
 "The Associated Press dispatch reported that Labori had broken the news to Dreyfus, that he was stunned and then rallied, and that he believed his years on Devil's Island would count toward the sentence; the clerk and Demange were quoted disagreeing. Cables from London, Berlin and Rome described newspapers condemning the verdict and calls in Austria and Italy to boycott the coming Paris Exposition.",
 "Omaha Daily Bee, 11 Sept 1899, p. 1 (AP Rennes dispatch of 10 Sept; New York World cables)")
ent("1899-09-12","Tuesday 12 September 1899","day","dreyfus","Military prison, Rennes",
 "Offered a pardon, at the price of withdrawing his appeal",
 "Mathieu came to the prison with the government's offer: a pardon, on condition that Dreyfus dropped his appeal against the Rennes verdict. Dreyfus wrote that he wanted justice, not mercy, but agreed for the sake of his failing health and his family, and on the understanding that he would go on seeking full reparation.",
 "Five Years of My Life (1901), closing narrative (date as given there)",conf="approx")
ent("1899-09-16","Saturday 16 September 1899","day","press","London",
 "The Spectator: civilised opinion shocked outside France",
 "The weekly's lead paragraph reported that the court had found Dreyfus guilty 'with extenuating circumstances' on the Saturday evening and described the verdict as having shocked opinion outside France. It reflected the near-unanimous view of the British press.",
 "The Spectator, 16 Sept 1899, p. 1",q="All civilised men outside France were shocked")
ent("1899-09-19","Tuesday 19 September 1899","day","court","Élysée Palace, Paris",
 "President Loubet signs the pardon",
 "By presidential decree the remainder of the Rennes sentence was remitted. The pardon was an act of clemency, not a judgment: the conviction itself stood. Dreyfus was released the next day.",
 "Jewish Encyclopedia, 'Dreyfus Case' (decree of 19 Sept, release 20 Sept 1899)")
ent("1899-09-20","Wednesday 20 September 1899","day","dreyfus","Rennes, leaving for the south of France",
 "Free, he says liberty is worthless without honour",
 "On the day of his release he published a short note: the government had given him back his liberty, but it meant nothing to him without his honour, and he would go on demanding reparation for what he called a frightful judicial error.",
 "Five Years of My Life (1901), text of the note published on the day of his liberation",conf="approx")
ent("1906-07-12","Thursday 12 July 1906","day","court","Cour de cassation (united chambers), Paris",
 "Rennes verdict annulled without retrial",
 "After a second long inquiry the united chambers annulled the Rennes judgment and ruled that nothing remained of the accusation, so that no new court-martial was needed. Parliament then restored Dreyfus to the army with the rank of major and Picquart with that of brigadier general, and on 21 July 1906 Dreyfus received the Legion of Honour in a courtyard of the École Militaire, near where he had been degraded.",
 "ACJNA article (12 July 1906); case literature on the reinstatement law and the ceremony of 21 July 1906")

claims=[
 dict(date_iso="1894-11-01",date_display="1 November 1894",eye="drumont",claim="La Libre Parole names Captain Dreyfus as a Jewish officer arrested for high treason.",form="newspaper",evidence="La Libre Parole special edition; Jewish Encyclopedia, 'Dreyfus Case'",confidence="verified"),
 dict(date_iso="1894-12",date_display="December 1894",eye="henry",claim="Henry swears that a trustworthy source named a traitor in the ministry, and that the traitor is the accused.",form="court record",evidence="Closed hearing; known from later inquiries, not a transcript",confidence="approx"),
 dict(date_iso="1894-12-22",date_display="22 December 1894",eye="court",claim="Court-martial unanimously finds Dreyfus guilty; deportation for life and degradation.",form="court record",evidence="Judgment of the first court-martial of Paris",confidence="verified"),
 dict(date_iso="1895-01-05",date_display="5 January 1895",eye="dreyfus",claim="At his degradation Dreyfus cries out to the troops that an innocent man is being degraded.",form="memoir",evidence="Five Years of My Life (1901); press reports of the ceremony",confidence="verified"),
 dict(date_iso="1897-04-02",date_display="2 April 1897",eye="picquart",claim="Picquart certifies that Esterhazy is a German agent and the bordereau is in his hand.",form="letter",evidence="Sealed letter dated Sousse, 2 April 1897",confidence="verified"),
 dict(date_iso="1897-11-15",date_display="15 November 1897",eye="mathieu",claim="Mathieu Dreyfus denounces Esterhazy to the Minister of War as the bordereau's author.",form="letter",evidence="Published letter; Jewish Encyclopedia",confidence="verified"),
 dict(date_iso="1898-01-11",date_display="11 January 1898",eye="esterhazy",claim="Court-martial acquits Esterhazy unanimously.",form="court record",evidence="Judgment of the court-martial of Paris",confidence="verified"),
 dict(date_iso="1898-01-13",date_display="13 January 1898",eye="zola",claim="Zola accuses the generals, the experts and both courts-martial of deliberate injustice.",form="newspaper",evidence="L'Aurore, 13 Jan 1898",confidence="verified"),
 dict(date_iso="1898-02-23",date_display="23 February 1898",eye="court",claim="Seine jury convicts Zola of defamation: one year and 3,000 francs.",form="court record",evidence="Assize Court verdict; Tucker edition 1898",confidence="verified"),
 dict(date_iso="1898-08-30",date_display="30 August 1898",eye="henry",claim="Henry admits to the Minister of War that he fabricated the letter naming Dreyfus.",form="official report",evidence="Minutes of the interrogation by Cavaignac",confidence="verified"),
 dict(date_iso="1898-09-18",date_display="18 September 1898",eye="esterhazy",claim="Esterhazy tells The Observer he wrote the bordereau, on Sandherr's orders (his claim).",form="newspaper",evidence="The Observer, 18 and 25 Sept 1898",confidence="verified"),
 dict(date_iso="1899-06-03",date_display="3 June 1899",eye="court",claim="Cour de cassation annuls the 1894 judgment and orders a new court-martial at Rennes.",form="court record",evidence="Judgment of the united chambers",confidence="verified"),
 dict(date_iso="1899-09-09",date_display="9 September 1899",eye="court",claim="Rennes court-martial: guilty, five votes to two, extenuating circumstances, ten years.",form="court record",evidence="Le Procès Dreyfus (Stock, 1900); AP dispatch",confidence="verified"),
 dict(date_iso="1899-09-09",date_display="9 September 1899",eye="steevens",claim="Steevens reports the hall receiving the verdict in stunned silence.",form="newspaper",evidence="Daily Mail reports; The Tragedy of Dreyfus (1899)",confidence="verified"),
 dict(date_iso="1899-09-19",date_display="19 September 1899",eye="court",claim="President Loubet pardons Dreyfus; the conviction itself stands.",form="official report",evidence="Presidential decree",confidence="verified"),
 dict(date_iso="1906-07-12",date_display="12 July 1906",eye="court",claim="Cour de cassation annuls the Rennes verdict without retrial.",form="court record",evidence="Judgment of the united chambers",confidence="verified"),
]

conv=[
 dict(date="1894-12-22",label="The closed court-martial convicts",eyes=["court","dreyfus","henry","herzl"],note="The court's sentence, Henry's sworn accusation in a room with no public record, the prisoner's letter the next morning and a foreign reporter who, like most of Paris, assumed the verdict was sound."),
 dict(date="1895-01-05",label="Degradation at the École Militaire",eyes=["dreyfus","herzl"],note="The man stripped of rank writes that night that he will not describe what he suffered; the reporter writes for the next morning's paper, and years later gives the scene a new meaning of his own."),
 dict(date="1898-01-13",label="Acquittal and 'J'accuse…!'",eyes=["esterhazy","zola","court"],note="Within forty-eight hours a court clears the officer named by Mathieu and Picquart, and a novelist turns the acquittal itself into the charge, daring the state to prosecute him."),
 dict(date="1898-02-12",label="Zola's trial becomes the trial no court would hold",eyes=["court","zola","henry","picquart"],note="The judge rules the 1894 case out of bounds; the two intelligence officers contradict each other before the jury; the defendant swears to an innocence he cannot prove in that room."),
 dict(date="1898-08-31",label="The forgery collapses",eyes=["henry","esterhazy","drumont"],note="Henry confesses and dies; within weeks Esterhazy, abroad, admits the handwriting; the antisemitic press answers by honouring Henry as a patriot."),
 dict(date="1899-08-07",label="Rennes opens",eyes=["court","dreyfus","steevens","paleologue"],note="The stenographic record catches every question and answer; Steevens catches the face; Paléologue watches the secret sessions the public never saw; the accused, back from five years of silence, faces his judges for the second time."),
 dict(date="1899-09-09",label="The second verdict",eyes=["court","steevens","press","dreyfus"],note="Five votes to two and 'extenuating circumstances': read aloud in a whisper, cabled overnight, condemned in London and Berlin, and answered by the prisoner with an appeal he would soon give up."),
 dict(date="1899-09-19",label="Pardon without acquittal",eyes=["court","dreyfus","mathieu"],note="The state remits the punishment; the brother negotiates it; the prisoner accepts and in the same breath refuses to accept the verdict."),
]

ties=[
 dict(a="dreyfus",b="mathieu",kind="relative",note="Brothers; Mathieu led the family's campaign for five years and brought Alfred the pardon offer at Rennes."),
 dict(a="mathieu",b="esterhazy",kind="opposite sides",note="Mathieu named Esterhazy publicly as the bordereau's writer on 15 November 1897."),
 dict(a="picquart",b="esterhazy",kind="opposite sides",note="Picquart's 1896 inquiry identified Esterhazy's handwriting as that of the bordereau."),
 dict(a="picquart",b="henry",kind="opposite sides",note="Colleagues in the Statistical Section; they contradicted each other at the Zola trial and fought a duel in March 1898."),
 dict(a="henry",b="dreyfus",kind="opposite sides",note="Henry was the chief army witness in 1894 and later forged a document naming Dreyfus."),
 dict(a="zola",b="esterhazy",kind="mentioned",note="'J'accuse…!' charged that the court-martial had acquitted Esterhazy on orders."),
 dict(a="zola",b="picquart",kind="influenced",note="Picquart's evidence, relayed through Scheurer-Kestner, underlay Zola's campaign; Picquart testified at Zola's trial."),
 dict(a="drumont",b="henry",kind="mentioned",note="La Libre Parole raised a public subscription for Henry's widow after his death."),
 dict(a="drumont",b="dreyfus",kind="opposite sides",note="The paper first published Dreyfus's name and led the press campaign against him."),
 dict(a="herzl",b="dreyfus",kind="met",note="Herzl watched Dreyfus degraded in the École Militaire courtyard on 5 January 1895; they never spoke."),
 dict(a="steevens",b="dreyfus",kind="met",note="Steevens watched him daily from the press benches at Rennes in August–September 1899."),
 dict(a="blum",b="zola",kind="influenced",note="Blum's 1935 memoir looks back on Zola's campaign as a turning point for the young Dreyfusards of his generation."),
 dict(a="twain",b="dreyfus",kind="mentioned",note="Twain's 1895 note asks how the press reported Dreyfus's treatment in transit."),
 dict(a="paleologue",b="court",kind="met",note="Paléologue attended the Rennes court-martial as the Foreign Ministry's delegate."),
]

threads=[
 dict(to="v5:vienna-1900",note="Herzl left Paris in 1895 to become literary editor of the Neue Freie Presse in Vienna, and from there launched political Zionism with 'Der Judenstaat' (1896) and the Basel congress of 1897."),
 dict(to="v6:paris-1919",note="Georges Clemenceau, who as editor of L'Aurore gave Zola's letter its headline 'J'accuse…!', presided over the Paris Peace Conference as French premier in 1919."),
 dict(to="v1:ww1",note="Dreyfus, restored to the army in 1906, served again from 1914 as a reserve officer of artillery in the First World War; Picquart had been Minister of War in 1906–09."),
 dict(to="v13:cables-1858",note="The Rennes verdict of Saturday evening, 9 September 1899, was in American papers by Monday morning through the transatlantic cables, with reactions cabled from London, Berlin and Rome."),
]

images=[
 dict(url=DUKE_TRAITRE,title="Le Traître",caption="Henri Meyer's colour cover for Le Petit Journal's illustrated supplement shows Dreyfus in profile as his sword is broken and his insignia lie on the cobbles. It is an artist's reconstruction for a mass-circulation paper, made from reports a week after the ceremony, not a drawing from life.",date="13 January 1895",credit="Henri Meyer, Le Petit Journal, Supplément illustré; Duke University Libraries exhibit"),
 dict(url=DUKE_JUDAS,title="A propos de Judas Dreyfus",caption="Antisemitic caricature in La Libre Parole illustrée, ten days after the paper named the prisoner: Drumont as a giant pushing a tiny Dreyfus into a drain. Shown as evidence of the press campaign that preceded the trial.",date="10 November 1894",credit="Chanteclair, La Libre Parole illustrée; Duke University Libraries exhibit"),
 dict(url=DHM,title="L'Aurore, 13 January 1898: 'J'accuse…!'",caption="An original copy of the issue carrying Zola's open letter to the President of the Republic across the front page.",date="13 January 1898",credit="Deutsches Historisches Museum, Berlin, Do 94/120"),
 dict(url=DUKE_RENNES,title="La prison militaire de Rennes",caption="An item in Duke University's Dreyfus exhibit picturing the military prison at Rennes, where Dreyfus was held from 1 July 1899 through the second court-martial.",date="c. 1899",credit="Duke University Libraries exhibit"),
 dict(url=SHAP,title="Dreyfus's letter of 14 January 1895 and Twain's note",caption="Manuscript items from the Shapell collection: Dreyfus's letter from La Santé to his sister and brother-in-law nine days after the degradation, and Mark Twain's note asking about press reports of his treatment.",date="January–February 1895",credit="Shapell Manuscript Foundation"),
]

further=[
 dict(title="Lettres d'un innocent: The Letters of Captain Dreyfus to His Wife (1899), Project Gutenberg",url="https://www.gutenberg.org/ebooks/64720"),
 dict(title="Alfred Dreyfus, Five Years of My Life (1901), Canadiana",url=FIVEC),
 dict(title="Alfred Dreyfus, Cinq années de ma vie (1901), Project Gutenberg",url=CINQ),
 dict(title="The Trial of Emile Zola (Tucker, 1898), Project Gutenberg",url=ZT),
 dict(title="Émile Zola, La Vérité en marche (1901), Project Gutenberg",url=VERITE),
 dict(title="G. W. Steevens, The Tragedy of Dreyfus (1899)",url=STVPDF),
 dict(title="Dreyfus's Rennes interrogation, from the 1900 stenographic record (English tr.)",url=RENNES),
 dict(title="Jewish Encyclopedia, 'Dreyfus Case' (1901–06)",url=JE),
]

intro=[
 "In late September 1894 a torn, unsigned list of military documents offered to the German military attaché reached the French army's intelligence section. Within three weeks Captain Alfred Dreyfus, an Alsatian Jewish artillery officer on the General Staff, had been made to write a dictated letter, judged to have a hand like the list's, and locked in the Cherche-Midi prison. A court-martial sitting behind closed doors convicted him in December; in January he was publicly stripped of his rank, and by April he was alone on Devil's Island off French Guiana.",
 "The case did not end there, and the chapter follows it to its legal end: the discovery in 1896 that another officer's handwriting matched the list; that officer's acquittal in January 1898; Zola's 'J'accuse…!' two days later and his own conviction for libel; the exposure of a forged document and the forger's death in August 1898; the annulment of the 1894 verdict in June 1899; a second court-martial at Rennes that convicted again 'with extenuating circumstances'; a presidential pardon eleven days later; and the Cour de cassation's annulment of the Rennes judgment on 12 July 1906.",
 "The record is uneven, and the chapter says so. The 1894 trial left no transcript; what was said in that room comes from later inquiries. The Zola trial and the Rennes court-martial, by contrast, were taken down in shorthand and printed. Dreyfus's own voice survives in letters that officials read before delivery and in the diary he kept on Devil's Island; Zola's in articles he collected himself. Several voices are memoirs or journals published decades later — Blum's 'Souvenirs' (1935), Paléologue's journal (1955), Mathieu Dreyfus's memoir (1978) — and are marked as such and given only in outline.",
 "The accusers are here in their own documents too: La Libre Parole, which named the prisoner before the army did and campaigned against him as a Jew; Major Henry's testimony and his forgery; Esterhazy's acquittal and his later claims to the English press. They are reported as what they said and did, without the slurs. Abroad, a Viennese correspondent, an English reporter, an American wire service, a London weekly and an American novelist in Paris show how far the case travelled and how differently it was read at a distance.",
 "Guilt and innocence were bitterly contested for twelve years. The chapter keeps to the dated record: what each court ruled, what each witness claimed, and the fact that on 12 July 1906 France's highest court annulled the last conviction and declared that nothing of the accusation remained.",
]

ch=dict(id="dreyfus-1894",title="The Dreyfus Affair",short_title="The Dreyfus Affair",subtitle="Paris, Devil's Island and Rennes, 1894–1906",span="1894–1906",intro=intro,
 calendar_note="All dates are Gregorian. Newspaper dispatches often appeared the day after the events they describe; entries are dated by the event where the report makes it clear, and the edition date is given in the source note.",
 eyes=eyes,entries=sorted(E,key=lambda x:x["date_iso"]),claims=claims,convergences=conv,ties=ties,threads_out=threads,images=images,further=further,
 vantage_key="0 = the accused, the principal accusers and witnesses, and the courts' own record; 1 = in the courtroom or at the scene as reporter, observer or defendant-by-choice; 2 = in Paris, campaigning, publishing or reading the papers; 3 = in France at a distance; 4 = abroad, news by cable.")
json.dump(ch,open(OUT,"w"),ensure_ascii=False,indent=1)
ids={e["id"] for e in eyes}
assert all(x["eye"] in ids for x in E+claims)
assert all(i in ids for c in conv for i in c["eyes"])
assert all(t["a"] in ids and t["b"] in ids for t in ties)
assert all(len(e["short"])<=16 for e in eyes)
for x in E:
    if x["quote"]: assert len(x["quote"].split())<=12, x["quote"]
print(len(eyes),len(E),len(claims),len(conv),len(ties),len(threads),len(images),len(further))
