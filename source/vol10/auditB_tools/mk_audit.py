import json,sys
base='/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/vol10/'
A='abutaleb-1799'; T='tahtawi-1826'
items=[]
def add(ch,where,sev,prob,fix,conf='verified'):
    items.append({"chapter":ch,"where":where,"severity":sev,"problem":prob,"fix":fix,"confidence":conf})
TR=lambda o,n:{"text_replace":{"old":o,"new":n}}
# ---------------- Abu Taleb
add(A,'entry:5','error',"The sentence about judging every sail 'friend or foe' is a compiler's flourish; no source cited records it.",
    TR(" In wartime every sail sighted had to be judged friend or foe.",""))
add(A,'entry:7','error',"In the 1814 text (TOTA reprint) 'resembling a terrestrial paradise' describes gardens and orchards on the opposite side of the river, not Captain Baker's estate. The reprint has Baker visit them at their hotel; the estate 'a few miles from the city' is not in the checked text. The quote itself is exact.",
    {"digest":"His first European landfall was Cork. Captain Baker, whom he had known in Rohilkhand during the Rohilla war, called on him and Richardson at their hotel, and Baker's cook-room was 'the first regular kitchen' he had seen. Across the river, he wrote, the ground was laid out in gardens and orchards 'resembling a terrestrial paradise'. He also wrote that the Irish villages much resembled those of India."})
add(A,'entry:8','error',"The checked chapter does not compare the road with Rohilkhand and Murshidabad. Rohilkhand comes up because he had met Captain Baker there, and Murshidabad as the birthplace of the servant Deen Mohammed. The date, fare and stages (Fermoy, Clonmel, Kilkenny, Carlow; Dublin on the third evening) are confirmed.",
    TR("The chapter compares what he saw with places in India, Rohilkhand and Murshidabad among them.","They breakfasted at Fermoy and slept at Clonmel, breakfasted at Kilkenny and slept at Carlow, and entered Dublin on the following evening."))
add(A,'entry:9','doubt',"The quote and the Leinster House, Wombell and Astley details come only from a 2006 blog review (Dominus), which could not be reached. The quote has not been checked word for word against Stewart's text, so it is blanked and confidence lowered. Banglapedia confirms the Cornwallis purpose and Richardson going ahead.",
    {"quote":"","confidence":"approx"},'approx')
add(A,'entry:10','doubt',"The quote and the comparison with the English and Scots come only from the unreachable Dominus blog. They have not been checked against Stewart's text.",
    {"quote":"","confidence":"approx"},'approx')
add(A,'entry:11','doubt',"No source shows that a 'letter of recommendation' from Cornwallis opened doors 'to ministers'. Sen (2008) says only that Cornwallis introduced him to the Queen. Gresse Street rests on Williamson via Pritchett's notes, which could not be reached.",
    TR("Cornwallis's letter of recommendation opened doors at court and to ministers, and he soon took lodgings.","Cornwallis's introduction later brought him to the Queen's notice, and he took lodgings."),'approx')
add(A,'entry:12','doubt',"Sen (2008) confirms that Cornwallis introduced him to the Queen and gives the phrase 'frequently to court', but the phrase was not checked against Stewart's text itself. The King and the 'within weeks' competition between households are not in the sources checked.",
    {"quote":"","digest":"Through Cornwallis he was introduced to Queen Charlotte, who, he records, commanded him to come frequently to court."},'approx')
add(A,'entry:13','doubt',"Sen (2008, citing p. 96) confirms that the public named him the 'Persian Prince' and that he says he never sought the title. The Vauxhall crowd detail was not visible in the checked text of Sen. Season inferred.",
    {"confidence":"approx"},'approx')
add(A,'entry:20','style',"The Royal Academy record gives only 'mezzotint after Northcote, 1801?', with no description of the pose. 'Half-length' is unsupported.",
    TR("The portrait shows him half-length in turban and robes. ","The portrait shows him in turban and robes. "))
add(A,'entry:21','error',"Sen (2008, citing p. 144) quotes only her request that he promise to publish an account of his travels. Asking him to state frankly what he disliked is not in the source. The translation spells her 'Lady Spenser', so identifying her as Lavinia, Countess Spencer is an inference.",
    {"digest":"Lady Spencer ('Spenser' in the translation), one of his attentive hostesses, particularly requested him, and made him promise, to publish an account of his travels."},'approx')
add(A,'entry:26','error',"Scroll.in, the cited source, does not contain the 'paradise into hell' comparison. It says instead that signs of decay began once he reached French soil. The rest of the digest matches Scroll.in.",
    TR(" Leaving London, he said, felt like falling from paradise into hell.",""))
add(A,'entry:27','style',"Scroll.in has him call London's museums 'child's playthings' beside the Louvre. It does not name the British Museum.",
    {"headline":"The Grand Gallery outshines London's museums"})
add(A,'entry:31','error',"The route across Anatolia and Kurdistan and the stop at Baghdad are not in the cited sources. Live History India and Wikipedia say only that he travelled overland from Constantinople and visited the shrines of Karbala and Najaf.",
    {"place":"Karbala and Najaf (Ottoman Iraq)","digest":"Travelling overland from Constantinople, he made the pilgrimage to the shrines of Husain at Karbala and Ali at Najaf. For a Shi'i traveller this was the religious heart of the journey, after Europe."},'approx')
add(A,'entry:32','error',"The cited source says only that he returned to Calcutta via Bombay. Basra and the Gulf passage are unsupported.",
    {"place":"Bombay","headline":"Back in India by way of Bombay","digest":"He came back into the Company's India at Bombay, before the last passage round to Bengal."},'approx')
add(A,'entry:35','style',"Iranica names the London 1807 edition of his poems as edited and translated by G. Swinton. That editor can be added.",
    TR("His Persian poems were published in London with English renderings,","His Persian poems were published in London in 1807, edited and translated by G. Swinton,"))
add(A,'entry:36','doubt',"The 'intelligent Foreigner' wording matches Sen's (2008) quotation of the preface (p. xxxiii) but was not checked against Stewart's printed preface. The quote is blanked under the word-for-word rule. 'Neither flatterer nor enemy' is not in the quoted passage. The May 1810 date (BnF) stands.",
    {"quote":"","digest":"Stewart dated his dedication and preface in May 1810. He presented the free remarks of an intelligent foreigner, and especially of an Asiatic, on English laws, customs and manners as an object of liberal curiosity. He also smoothed and abridged the text he was introducing."})
add(A,'entry:38','doubt',"The Vade-Mecum's contents list (Gutenberg 53400) confirms the section 'Mirza Alu Taaleb Khan, his ingratitude and vanity, comparison of his poetry with that of Hafiz and Yuqueen', pp. 503–509. The passage itself, and Pritchett's notes, could not be reached, so the quote is unchecked and blanked.",
    {"quote":"","confidence":"approx"},'approx')
add(A,'entry:39','doubt',"The contents list confirms a comparison of his poetry with Hafiz and 'Yuqueen' (Yaqin). 'Rhodomontade' and the imagery details could not be checked in the text.",
    {"confidence":"approx"},'approx')
add(A,'entry:2','doubt',"Williamson's claim to have sailed in the same ship could not be checked: the Vade-Mecum passage and Pritchett's notes were unreachable. Abu Taleb's own account names Richardson as his companion. The entry and convergence 0 already present it as Williamson's claim, which is right, but it remains unverified.",
    {"confidence":"approx"},'approx')
add(A,'entry:42','doubt',"Sen (2008) quotes the 1814 advertisement only on the Bengal government ordering the Persian original printed. That French and German versions are mentioned in the advertisement is not shown. Iranica says the German version was made from a French one, without a date.",
    TR("which was done at Calcutta in 1812, and that French and German versions had appeared. The Mirza, dead since 1805–06, now had readers in four languages.","which was done at Calcutta in 1812. A French version had appeared in 1811, and a German one, made from the French, followed."),'approx')
add(A,'eye:abutaleb','style',"The Broadview edition's listed publication date is 20 November 2008, not 2009.",
    TR("Broadview edition, ed. Daniel O'Quinn (2009)","Broadview edition, ed. Daniel O'Quinn (2008)"))
add(A,'eye:northcote','style',"No source checked says Northcote painted the Mirza 'in turban and robes'; the RA record gives no description. Low risk, but noted.",
    {}, 'approx') if False else None
add(A,'claim:1','doubt',"This claim rests only on the unreachable Dominus blog review.",{"confidence":"approx"},'approx')
add(A,'claim:11','doubt',"The preface wording comes via Sen (2008) and was not checked in Stewart's book; the 'intelligent Foreigner' quote marks should not be treated as checked.",
    {"claim":"Presents the Mirza's free remarks on English laws, customs and manners as those of an intelligent foreigner, worth liberal curiosity","confidence":"approx"},'approx')
add(A,'claim:12','doubt',"The section heading ('ingratitude and vanity') is confirmed by the contents list, but the 'empty title', peeresses and Gresse Street details could not be checked.",{"confidence":"approx"},'approx')
add(A,'claim:13','doubt',"The contents list confirms a comparison of his poetry with Hafiz; the 'rhodomontade' wording is unchecked.",{"confidence":"approx"},'approx')
add(A,'calendar_note:0','style',"The Hijri conversions were recomputed with the tabular calendar and agree (7 Feb 1799 = 2 Ramadan 1213; 8 Dec 1799 = 10 Rajab 1214; 21 Jan 1800 = 24 Sha'ban 1214; 10 Nov 1800 = 22 Jumada II 1215; 7 Jun 1802 = 5 Safar 1217; 4 Aug 1803 = 15 Rabi' II 1218). Iranica gives his death at Lucknow in 1220/1805–06. No change needed.",
    {}, 'verified')
items=[i for i in items if i]
# ---------------- Tahtawi
add(T,'entry:0','style',"Silvera reports only France against Italy; 'British' options are not in the cited source.",
    TR("British and Italian options had their advocates at court","Italy also had its advocates at court"))
add(T,'entry:4','doubt',"Silvera gives 13 April 1826 and a month's voyage, and Louca gives 32 days at sea, which fits a 15 May landing. Newman (Chronos 2002) says he sailed 'in March 1826'. The April date is better supported and is kept, but the discrepancy should be noted.",
    {"source_note":"Silvera (1980) (13 April; month-long voyage); Louca (La Truite; 32 days at sea). Newman, Chronos 6 (2002) gives March 1826."})
add(T,'entry:6','error',"Louca says Tahtawi asked whether quarantine was an impious way of escaping fate and reported the controversy 'sans se prononcer', without taking a side. The digest's claim that he argued it was lawful is contradicted.",
    TR("Tahtawi used the confinement to discuss whether quarantine was lawful for Muslims who believed in divine decree, and argued that it was.","Tahtawi recorded the debate over whether quarantine was a lawful precaution or an impious attempt to escape divine decree, setting out the controversy without deciding it himself."))
add(T,'claim:1','error',"Louca: Tahtawi reported the quarantine controversy without taking a position.",
    {"claim":"Traveller: is quarantine a lawful precaution or an attempt to escape divine decree? He reports the debate without deciding it","confidence":"approx"},'approx')
add(T,'entry:8','error',"Silvera says the first Paris lodging was a hotel on the rue de Clichy. The Hijri gloss is also off: late July 1826 fell in Dhu al-Hijja 1241, and Muharram 1242 began about 5 August.",
    {"date_display":"Late July–August 1826 (Dhu al-Hijja 1241 – Muharram 1242 AH)","digest":"After a journey by diligence of about a week, with a stop at Lyon, the mission reached Paris and was lodged first in a hotel in the rue de Clichy. Tahtawi began a description of the city's site, the Seine and its bridges, its climate and its water supply, written as an Arab geographer would describe any new country."},'approx')
add(T,'entry:21','doubt',"Silvera confirms the oral examination on 28 February and 1 March 1828 at the rue de Lille, with Sidney Smith and Morier present. 'A week after written tests' was not found in the checked text.",
    TR(", a week after written tests",""),'approx')
add(T,'entry:28','doubt',"The detailed claims ('adl/insaf, Newman p. 208) rest on Muench's WPSA paper, which could not be reached. Newman (Chronos 2002) confirms only that the book translates and comments on the 1814 Charter. Downgraded.",
    {"confidence":"approx"},'approx')
add(T,'entry:29','error',"The Revue des Deux Mondes extracts contain no Dieppe entry for July 1830. Apponyi mentions being at Dieppe when the news arrived only in retrospect, in the entries of 30 October and 12 December 1830, so there is no 'diary of the three days'.",
    {"digest":"Apponyi was at Dieppe when news of the ordinances and the fighting reached the coast. He mentions this only in later entries (30 October and 12 December 1830); the published extracts contain no journal written during the three days.","source_note":"Revue des Deux Mondes extracts, part II (entries of 30 Oct and 12 Dec 1830)."},'verified')
add(T,'intro:2','style',"Apponyi's presence at Dieppe is known only from his later entries.",
    TR("was waiting in Dieppe for news","was, by his own later account, at Dieppe waiting for news"))
add(T,'convergence:4','style',"Apponyi wrote no entry from Dieppe during the fighting; he recalled it later.",
    TR("Apponyi waits for news in Dieppe","Apponyi, by his later account, was waiting for news in Dieppe"))
add(T,'entry:31','doubt',"The royalist/liberal division and the blame on Charles X and Polignac come via Muench's WPSA paper, which could not be reached. Downgraded to approx.",
    {"confidence":"approx"},'approx')
add(T,'entry:33','error',"The Hijri gloss is off: August 1830 was mostly Safar 1246, with Rabi' I beginning about 20 August. The hadith, Shaykh Hammam and jumhuriyya details rest on the unreachable Muench paper; Newman (Chronos) mentions only the concept of a republic.",
    {"date_display":"August 1830 (Safar–Rabi' I 1246 AH)","confidence":"approx"},'approx')
add(T,'entry:37','error',"Louca dates the final examination to 1831 ('L'examen final de Rifa'a à Paris (1831)'). Silvera cites the report in the Revue encyclopédique XLVIII (November 1831) and puts the examination in November 1831, which cannot be right if Tahtawi was writing from Cairo on 16 August 1831. 1831, before his return, is the defensible date.",
    {"date_iso":"1831","precision":"range","date_display":"1831, before his return (sources differ on the month)","source_note":"Louca (final examination, 1831); Silvera (1980) n. 72 (Revue encyclopédique XLVIII, November 1831, pp. 521–23). Silvera's 'November 1831' conflicts with the Cairo letter of 16 August 1831."},'approx')
add(T,'entry:39','error',"Apponyi's 23 December entry describes the king leading a march through the faubourgs, escorted by National Guards, not riding through the crowds. The statement about what was feared is not in the extracts.",
    TR("and Louis-Philippe riding through the crowds to a triumphant reception. The fear was of a massacre of the ministers, not of a new revolution.","and Louis-Philippe leading a march through the poorer quarters that Apponyi called a triumphal procession."))
add(T,'entry:40','error',"Silvera says half a dozen students 'had returned immediately after the outbreak of the July Revolution'. 'Recalled' overstates this.",
    {"date_display":"1831 (before August)","digest":"Tahtawi left Paris in 1831 with his translations and his manuscript. About half a dozen of his fellow students had already gone home immediately after the revolution broke out."},'approx')
add(T,'entry:41','doubt',"Louca says Ibrahim Pasha first set him to compile an Arabic–French dictionary in Alexandria, and that he was then attached to the medical school as a translator at Clot Bey's request. 'First post ... at Abu Za'bal' is therefore uncertain. The Routledge document's contents were not checked.",
    TR("his first post was as a translator in the new state schools, beginning with the medical school at Abu Za'bal.","according to Louca he was first set to an Arabic–French dictionary in Alexandria, then attached to the medical school as a translator at Clot Bey's request."),'approx')
add(T,'threads_out:3','style',"Abu Za'bal was not certainly his first post (Louca: an Arabic–French dictionary came first).",
    TR("Tahtawi's first post was at the Abu Za'bal medical school","One of Tahtawi's first posts was at the Abu Za'bal medical school"))
add(T,'entry:43','doubt',"The IMA dossier confirms de Sacy's annotation that the claim that the French have no religion and are Christians only in name 'est à réviser'. That he praised the account as 'faithful and useful' was not found in any reachable source.",
    TR("De Sacy praised the account as faithful and useful, while flagging a few judgements","De Sacy commented on the manuscript, flagging judgements"),'approx')
add(T,'entry:38','style',"Hijri gloss: 15 December 1830 = 29 Jumada II 1246; Rajab began on 16 December.",
    {"date_display":"15–21 December 1830 (Jumada II–Rajab 1246 AH)"})
add(T,'entry:45','error',"Louca reports the letter's content: it was printed in the Nouveau Journal asiatique (November 1831), and in it he says his uncle, now his father-in-law, is the Mufti and that the ulama welcomed him, several coming to see him of their own accord. The digest's 'reported on his work, keeping open the line ...' is unsupported.",
    {"digest":"Writing from Cairo to his old headmaster, Tahtawi reported that the ulama had welcomed him home, several coming to see him of their own accord, and that his uncle, now his father-in-law, was the Mufti. The letter was printed in the Nouveau Journal asiatique that November.","source_note":"Letter dated 'Kaire, le 16 août 1831', printed in Nouveau Journal asiatique (Nov 1831), cited by Louca."})
add(T,'eye:jomard','style',"Jomard was born on 20 November 1777, so he was 48 for most of 1826.",
    TR("aged 49 in 1826","aged 48 in 1826"))
add(T,'claim:9','doubt',"This rests on the unreachable Muench paper (Newman p. 208).",{"confidence":"approx"},'approx')
add(T,'claim:10','doubt',"This rests on the unreachable Muench paper (Newman pp. 306–309).",{"confidence":"approx"},'approx')
add(T,'claim:7','doubt',"This rests on Louca's summary, which the checked extract does not cover.",{"confidence":"approx"},'approx')
add(T,'claim:13','doubt',"Only the annotation is confirmed (IMA). The 'account is faithful' part is not.",
    {"claim":"Hosts: the claim that the French are Christians only in name should be revised"},'approx')
add(T,'eye:drovetti','doubt',"Wikipedia confirms that Atir attended the giraffe until her death (12 January 1845) and Hyperallergic names Hassan and Atir. No change needed.",{}, 'verified')
add(T,'calendar_note:0','style',"The listed conversions were recomputed and agree (13 Apr 1826 = 5 Ramadan 1241; 15 May 1826 = 7 Shawwal 1241; 27–29 Jul 1830 = 6–8 Safar 1246; 16 Aug 1831 = 7 Rabi' I 1247; 1 Muharram 1250 = 10 May 1834). No change needed.",{}, 'verified')
items=[i for i in items if i.get('fix') or i['severity']!='x']
# drop no-op items with empty fix
items=[i for i in items if i['fix']!={}]
# validate
chs={A:json.load(open(base+'ch-abutaleb-1799.json')),T:json.load(open(base+'ch-tahtawi-1826.json'))}
kindmap={'entry':'entries','claim':'claims','convergence':'convergences','image':'images','tie':'ties','threads_out':'threads_out','intro':'intro'}
bad=0
for it in items:
    d=chs[it['chapter']]; k,_,key=it['where'].partition(':')
    if k=='eye': obj=[e for e in d['eyes'] if e['id']==key][0]
    elif k=='calendar_note': obj=d['calendar_note']
    else: obj=d[kindmap[k]][int(key)]
    tr=it['fix'].get('text_replace')
    if tr:
        s=json.dumps(obj,ensure_ascii=False) if not isinstance(obj,str) else obj
        hay=obj if isinstance(obj,str) else ' '.join(str(v) for v in obj.values())
        if tr['old'] not in hay: print('MISSING',it['chapter'],it['where'],tr['old'][:60]); bad+=1
json.dump(items,open(base+'audit-B.json','w'),ensure_ascii=False,indent=1)
json.load(open(base+'audit-B.json'))
from collections import Counter
print(len(items),Counter(i['severity'] for i in items),'bad',bad)
