import json,sys
sys.path.insert(0,'.')
from eyes import eyes
from entries import entries
from rest import *
intro=[
 "On 28 October 312 Constantine's army broke the army of Maxentius on the Tiber north of Rome, and Maxentius drowned when the bridge behind him gave way. Within a generation the victory was being told as the moment the Roman emperor turned to the Christian God, after a sign from heaven. This chapter lays out how that story was told, by whom, and when.",
 "There are no diaries here. The record is made of court speeches delivered before the emperor (the Latin panegyrics of 310, 313 and 321), a Christian pamphlet history (Lactantius, c. 314–315), a church history and a biography by the same bishop written some twenty-five years apart (Eusebius), an inscription in stone, coins and medallions, laws and an imperial letter, and a hostile pagan history written nearly two centuries later (Zosimus). Each entry carries a form and a source-kind tag; most are secondhand, and the gap between event and writing is given where it matters.",
 "Set side by side by date, the accounts form a sequence. In 310 an orator at Trier says Constantine saw Apollo, with Victory, offering laurel wreaths at a temple in Gaul. In 313 a second orator says a divine mind urged him on against the soothsayers, but mentions no sign. About 314–315 Lactantius, the earliest Christian witness, says Constantine was told in a dream on the eve of battle to put the heavenly sign of God on his soldiers' shields. Eusebius's Church History (c. 313–316 or later) describes the battle with no vision at all. Only in the Life of Constantine, written after the emperor's death in 337, does a cross of light appear above the noon sun with the words 'Conquer by this', seen by the army and sworn to by Constantine himself, who, Eusebius says, told him long afterwards.",
 "Around those texts stand the official records: the Senate's arch of 315, which credits 'the prompting of the divinity' without naming a god; a silver medallion with a tiny chi-rho on the emperor's helmet; coins that went on honouring the Unconquered Sun for years; and the letter of 313, issued by Licinius in Nicomedia, that granted Christians and all others freedom of worship. Licinius has his own heaven-sent victory, an angel's prayer reported by Lactantius. Maxentius, the defeated emperor, is known only through his enemies and his coins; both a Christian and a pagan writer say he trusted the Sibylline books.",
 "The book takes no position on what, if anything, Constantine saw. Scholars have read the accounts as a religious experience, a natural sky phenomenon such as a solar halo, a political story shaped after the fact, or several of these at once; those readings are reported here as positions. What can be dated is how the story grew, and what followed: toleration in 313, the Council of Nicaea in 325, a new capital in 330, and an emperor baptised on his deathbed in 337.",
]
cal="All dates are AD and in the Julian calendar, as historians cite them; date_iso uses the proleptic Julian form. The ancient sources date by Roman reckoning, which has been converted: Lactantius places the battle on the sixth day before the kalends of November (28 October) and the posting of Licinius's letter on the ides of June (13 June) in the year when Constantine and Licinius were consuls for the third time (313). Speeches, histories and coin types are often datable only to a year or a range; those entries carry precision 'year' or 'range'."
ch=dict(id="constantine-312",title="The Sign Before the Milvian Bridge",short_title="The Sign Before the Milvian Bridge",
 subtitle="Constantine's vision and the battle at the Tiber: Gaul, Rome and the East, 310–337",span="310–337",
 intro=intro,calendar_note=cal,eyes=eyes,entries=sorted(entries,key=lambda e:e['date_iso']),claims=claims,
 convergences=convergences,ties=ties,threads_out=threads_out,images=images,further=further,
 vantage_key="0 = emperors who acted on the signs (Constantine, Maxentius, Licinius); 1 = court orators and official records made close to the events; 2 = writers within a few years; 3 = later or distant writers; 4 = hostile historian two centuries later.")
out="/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/vol16/ch-constantine-312.json"
json.dump(ch,open(out,'w'),ensure_ascii=False,indent=1)
d=json.load(open(out))
ids={e['id'] for e in d['eyes']}
assert all(e['eye'] in ids for e in d['entries']); assert all(c['eye'] in ids for c in d['claims'])
assert all(set(c['eyes'])<=ids for c in d['convergences']); assert all(t['a'] in ids and t['b'] in ids for t in d['ties'])
for e in d['eyes']: assert len(e['short'])<=16,e['short']
for e in d['entries']:
    assert len(e['quote'].split())<=12, e['quote']
print(len(d['eyes']),len(d['entries']),len(d['claims']),len(d['convergences']),len(d['ties']),len(d['threads_out']),len(d['images']),len(d['further']),len(d['short_title']))
from collections import Counter;print(Counter(e['eye'] for e in d['entries']))
