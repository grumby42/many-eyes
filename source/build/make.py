import json, datetime
OUT="/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/ch-london-1666.json"
WD=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
MON=["January","February","March","April","May","June","July","August","September","October","November","December"]
def os_day(y,m,d):
    """English Old Style date -> (iso NS, display)"""
    g=datetime.date(y,m,d)+datetime.timedelta(days=10)
    disp=f"{WD[g.weekday()]} {d} {MON[m-1]} {y} (O.S.)"
    if m<3 or (m==3 and d<25): disp=f"{WD[g.weekday()]} {d} {MON[m-1]} {y-1}/{str(y)[2:]} (O.S.; English year then began 25 March)"
    return g.isoformat(), disp+f" = {g.day} {MON[g.month-1]} {g.year} N.S."
def ns_day(y,m,d,extra=""):
    g=datetime.date(y,m,d); o=g-datetime.timedelta(days=10)
    return g.isoformat(), f"{WD[g.weekday()]} {d} {MON[m-1]} {y} (N.S.){extra} = {o.day} {MON[o.month-1]} {o.year} O.S."

E=[]
def add(iso_disp,prec,eye,place,head,dig,quote="",conf="verified",src=""):
    iso,disp=iso_disp
    E.append(dict(date_iso=iso,date_display=disp,precision=prec,eye=eye,place=place,headline=head,digest=dig,quote=quote,confidence=conf,source_note=src))
def raw(iso,disp): return (iso,disp)

PD="Pepys diary; text via pepysdiary.com / Wheatley ed. (Gutenberg)"
# ---------- 1665 plague ----------
add(os_day(1665,2,24),"day","allin","London (letter to Rye)","A portent from Scotland, months before the plague",
 "In a letter home to his friends at Rye, Allin passes on talk of strange sightings lately seen in Scotland. Like many in the winter of the 1664 comets, he reads the sky for signs, and his letters will soon turn from omens to the real thing.",
 "",
 "verified","W. Durrant Cooper, 'Notices of the Last Great Plague … from the Letters of John Allin', Archaeologia 37 (1857), quoting letter of 24 Feb 1664/5")
add(os_day(1665,6,7),"day","pepys","Drury Lane, Westminster","Red crosses on Drury Lane doors; Pepys buys tobacco",
 "A sweltering day of office work, a tavern dinner and anxious waiting for news of the fleet ends badly. Walking through Drury Lane, Pepys sees for the first time houses shut up and marked with red crosses and a painted prayer. Suddenly frightened for his own body and breath, he buys a roll of tobacco to smell and chew, which calms him.",
 "a red cross upon the doors, and “Lord have mercy upon us”",
 "verified","pepysdiary.com/diary/1665/06/07")
add(os_day(1665,7,16),"day","evelyn","Sayes Court, Deptford","Over a thousand dead in a week; houses shut in his own parish",
 "Evelyn records roughly 1,100 plague deaths in London that week and more than 2,000 the next. The sickness has reached Deptford: two houses in his parish are shut up. He keeps working at his post caring for sick and wounded seamen and prisoners of war.",
 "There died of the plague in London this week 1,100",
 "verified","Evelyn, Diary (Bray ed.), vol. 2, 16 July 1665, Gutenberg #42081")
add(os_day(1665,8,15),"day","pepys","an alley near his home, City","Stumbling on a plague corpse at dusk",
 "Coming home late, Pepys passes a plague victim's body being carried through a narrow alley in the half-dark. The dead are now part of his walk home.",
 "","verified","Pepys 15 Aug 1665 (Lapham's Quarterly 'Plague Posts')")
add(os_day(1665,8,28),"day","evelyn","Sayes Court, Deptford","Evelyn sends his family away, but stays",
 "With the contagion growing round Deptford, Evelyn sends his wife and household to his brother's house at Wotton in Surrey. He himself remains, because the sick seamen and prisoners in his charge cannot be left.",
 "","verified","Evelyn, Diary, 28 Aug 1665")
add(raw("1665-08-11","August–September 1665 (O.S.) — exact days not given"),"range","vincent","a household outside the City walls","Death enters Vincent's own house",
 "In a household of eight, a young maidservant fell sick on a Monday and was dead by Thursday; a youth sickened on a Friday and died on the Sabbath; another youth died the following Wednesday. Vincent dwells on one of the boys, about seventeen, who spoke calmly about dying. The master of the house fell ill and recovered.",
 "","approx","Vincent, God's Terrible Voice in the City (1667); exact days not dated in the text")
add(os_day(1665,8,31),"day","pepys","Navy Office, Seething Lane","The bill says 6,102 of plague; Pepys suspects 10,000",
 "Pepys sets down the weekly figure: about 7,500 deaths, over 6,000 of them plague. He doubts it, reasoning that the poor die uncounted and Quakers and others refuse the bell, so the true number may be near ten thousand.",
 "","verified","Pepys 31 Aug 1665 (Lapham's Quarterly 'Plague Posts')")
add(os_day(1665,9,7),"day","pepys","Navy Office, Seething Lane","The worst bill yet: 8,252 dead, 6,878 of plague",
 "Pepys records the new bill of mortality, the highest so far. He is still crossing the river and the City on navy business, now among shut shops and fires, keeping his diary like a ledger of the city's dying.",
 "","verified","Pepys 7 Sept 1665 (Lapham's Quarterly 'Plague Posts')")
add(os_day(1665,9,7),"day","evelyn","Kent Street, Southwark, to St James's","A walk through a dying city",
 "Evelyn goes all the way through the City and suburbs from Kent Street to St James's. Shops are shut, the streets are mournfully silent, and coffins lie exposed in the open; he reckons ten thousand are dying a week. He goes to the Duke of Albemarle about a pest-ship for infected sailors.",
 "","verified","Evelyn, Diary, 7 Sept 1665")
add(raw("1665-09-11","September 1665 (O.S.) — month"),"month","taswell","Greenwich, then Westminster","A thirteen-year-old sent into the plague city",
 "Taswell's school had scattered to the country; he was at Greenwich. In the worst weeks, his father sent him into London with letters, herbs and food, and he saw the sick, the lame and the dead being carried to burial. His family's old servant Johanna, who had nursed him as a baby, hugged him at the door; she later caught the plague and lived.",
 "","approx","Autobiography and Anecdotes of William Taswell, ed. G.P. Elliott, Camden Miscellany II (1853), Internet Archive")
add(os_day(1665,9,10),"day","josselin","Earls Colne, Essex","A country vicar copies the London bill",
 "Josselin thanks God for his mercies and notes the weather turning cooler, but the London bills still rising: he copies down figures of 6,978 and 8,252 for the week to 5 September. He has heard that fires are to be kept burning at every door in London for three days and nights to purify the air.",
 "","verified","Diary of Ralph Josselin, Earls Colne records, Cambridge (entry 70014870)")
add(os_day(1665,9,17),"day","evelyn","Sayes Court / Thames ports","Three thousand Dutch prisoners and nowhere to put them",
 "As commissioner for sick and wounded seamen and prisoners, Evelyn is sent about 3,000 Dutch prisoners, more than his places can hold or guard. The war has not paused for the plague, and its human cost is landing on his desk.",
 "","verified","Evelyn, Diary, 17 Sept 1665")
add(os_day(1665,9,25),"day","evelyn","Court business","Ten thousand pounds, or the prisoners starve",
 "Evelyn presses the government for £10,000 at once, warning that otherwise the prisoners of war will starve; meanwhile five vessels with guards are used as floating prisons. His diary shows the gap between a crown at war and the money to pay for its captives.",
 "the prisoners would starve",
 "verified","Evelyn, Diary, 25 Sept 1665")
add(raw("1665-09-25","September 1665 (O.S.) — peak weeks"),"month","vincent","London","Only four parishes of 130 clean",
 "At the peak the bills reached about 7,165 in a week, and Vincent noted that only four of some 130 parishes were free of infection. He describes churchyards so full the ground was swollen with bodies; he himself stayed in the city from beginning to end.",
 "","verified","Vincent, God's Terrible Voice in the City (1667)")
add(raw("1665-08-12","Summer–autumn 1665 (O.S.)"),"range","allin","London","An ejected minister turned plague doctor",
 "Allin, a nonconformist minister pushed out of his Rye living, practised physic in London through the epidemic and sent a stream of letters to Philip Fryth and Samuel Jeake back in Sussex. They carry news of the bills, remedies and deaths around him, and his alchemical hope of a cure. Individual letters could not be checked line by line for this chapter.",
 "","approx","Cooper, Archaeologia 37 (1857); L. Thorpe, 'In middest of death' (PhD, Royal Holloway, 2018) abstract; Rye News article")
add(os_day(1665,10,16),"day","pepys","the City of London","Lord, how empty the streets",
 "Walking through the City, Pepys finds the streets empty and melancholy, the sick with sores wandering in them, and every conversation about who is dead or newly sick. It is one of the bleakest pictures in the plague year.",
 "","verified","Pepys 16 Oct 1665 (HA pack)")
add(os_day(1666,6,1),"day","evelyn","Sayes Court garden, then Rochester","Hearing the great guns from his garden",
 "At six in the evening in his garden Evelyn hears heavy gunfire out at sea. He rides that night toward Rochester and the coast but finds no fighting near Deal, and returns to report to an astonished King. It is the first day of the Four Days' Battle.",
 "the great guns go thick off",
 "verified","Evelyn, Diary, 1 June 1666")
add(raw("1666-06-11","1–4 June 1666 (O.S.) = 11–14 June 1666 (N.S.)"),"range","vandevelde","with the Dutch fleet, southern North Sea","A Dutch artist rows among the battle lines",
 "Van de Velde accompanied the Dutch fleet to sketch the Four Days' Battle, reportedly asking De Ruyter for a boat to be rowed about the fleet for a good view. His drawings of ships and smoke were a professional record, made to be turned into paintings later.",
 "","approx","Wikipedia 'Willem van de Velde the Elder' (citing Robinson, Van de Velde Drawings); NMM holds c.1,500 of his drawings")
add(os_day(1666,6,6),"day","evelyn","Whitehall","A victory that turns into a deliverance",
 "Sir Daniel Harvey brings the King the account of the battle and thanksgiving is ordered as for a victory; the King sends an extra physician and surgeons. Then the truth arrives: heavy English losses, the great ship Prince burnt, Admiral Ayscue captured. Evelyn concludes it was a narrow escape rather than a triumph.",
 "rather a deliverance than a triumph",
 "verified","Evelyn, Diary, 6 June 1666")
add(os_day(1666,6,10),"day","josselin","Earls Colne, Essex","Sea news heavy, London's plague creeping back",
 "In Essex, Josselin weighs the sea fight: a heavy loss, yet a deliverance to thank God for. London's plague figures are rising again and Colchester's even faster. A scare involving a neighbour troubles his household.",
 "","verified","Josselin diary, entry 70015155")
add(ns_day(1666,7,6),"day","giustinian","Venetian embassy, Paris","Paris hears the Dutch side of the Four Days",
 "Writing to the Doge and Senate, Giustinian relays the account of the Prince of Monaco, who had sailed with the Dutch fleet: the Dutch won through English overconfidence. From Paris, the battle is a story told mostly in Dutch and French voices.",
 "","verified","Calendar of State Papers Venice, vol. 35, July 1666, no. 25 (british-history.ac.uk)")
add(raw("1666-06-11","June 1666 (O.S.) — month"),"month","mompesson","Eyam, Derbyshire","Sending the children away; sealing the village",
 "As plague returns to Eyam, Mompesson sends his two small children to relatives in Yorkshire, and with the ejected Puritan minister Thomas Stanley persuades the villagers to stay within a boundary of stones about half a mile around the village. The Earl of Devonshire at Chatsworth supplies food left at marker points; coins are left in water to cleanse them. Services move outdoors to the dell called Cucklet Delph.",
 "","approx","William Wood, History and Antiquities of Eyam (1842), plague chapter; Wikipedia 'William Mompesson'")
add(os_day(1666,6,17),"day","josselin","Earls Colne, Essex","Hot, dry and still praying the hand be lifted",
 "A very hot, dry season. Josselin is thankful for peace in his own district, but notes plague rising in London and climbing to about 150 in Colchester, ten miles away. He closes with his recurring prayer for God to take his hand away.",
 "","verified","Josselin diary, entry 70015160")
add(os_day(1666,7,22),"day","josselin","Earls Colne, Essex","Good harvest weather and a servant hurt by a rake",
 "An ordinary day in the shadow of the epidemic: hot weather good for his farming, plague spreading in many parts of England but his own town well. He copies the London and Colchester figures, and records his servant Barrett injured by a rake, a mercy mixed with sorrow.",
 "","verified","Josselin diary, entry 70015200")
add(raw("1666-08-04","25–26 July 1666 (O.S.) = 4–5 August 1666 (N.S.)"),"range","vandevelde","with the Dutch fleet off the Thames estuary","Sketching St James's Day battle",
 "Van de Velde was again with the fleet to draw the St James's Day Battle, a hard English success that nearly wrecked the Dutch fleet. De Ruyter fell seriously ill after it, and Dutch blame fell on Cornelis Tromp.",
 "","approx","Wikipedia 'Willem van de Velde the Elder'; 'Michiel de Ruyter'")
add(raw("1666-08-19","19–20 August 1666 (N.S.) = 9–10 August 1666 (O.S.)"),"range","vandevelde","the Vlie, between Vlieland and Terschelling","Drawing Holmes's Bonfire",
 "Van de Velde made a large wash drawing of the English raid in which Robert Holmes's boats and fireships burned well over a hundred Dutch merchantmen in the Vlie and then torched the town of West-Terschelling. Whether he drew it on the spot or from reports is not stated by the Rijksmuseum; ten years later he painted the same scene for the English Duke of York.",
 "","approx","Rijksmuseum RP-T-1905-20 (drawing, 1666); Royal Collection RCIN 406560 (painting, 1676)")
add(os_day(1666,8,15),"day","pepys","Whitehall and the City","Bonfires in London for the Dutch ships burned",
 "A letter from Sir William Coventry wakes Pepys with news that some 160 Dutch ships have been burned in the Vlie and a town on Schelling destroyed. His joy is as great as the service, and the Tower guns fire and bonfires burn in the streets. Three weeks later the bonfires will be London itself.",
 "","verified","Pepys 15 Aug 1666 (americanliterature.com Aug 1666 text)")
add(os_day(1666,8,26),"day","josselin","Earls Colne, Essex","Plague abating in London, still raging in Colchester",
 "Josselin is thankful for a good harvest and notes London's plague abating. He copies the figures and reproaches himself for the evil of his own heart, a typical blend of farm, epidemic and conscience.",
 "","verified","Josselin diary, entry 70015240")
add(os_day(1666,8,31),"day","mompesson","Eyam rectory","A letter to his children: your mother is a saint in heaven",
 "A week after burying his wife Catherine, who would not leave him and died of the plague on 24 August, Mompesson writes to his two small children far away. He describes her piety, modesty and thrift and the calm of her last illness, and tells them she is now in heaven. He writes as a man who expects to follow her.",
 "","verified","Mompesson to George and Elizabeth Mompesson, Eyam, 31 Aug 1666, printed in Wood, History and Antiquities of Eyam (1842)")
add(os_day(1666,9,1),"day","mompesson","Eyam rectory","A farewell to his patron, the day before London burns",
 "Mompesson writes to his patron Sir George Savile to announce his wife's death and say goodbye. He names Savile an executor, asks him to choose a godly successor for the parish and to pray for his orphans. That night, some 150 miles south, a fire will break out in a Pudding Lane bakery.",
 "","verified","Mompesson to Sir George Savile, Eyam, 1 Sept 1666 (Wood, 1842)")
# ---------- Fire ----------
add(os_day(1666,9,2),"day","pepys","Seething Lane; the Tower; Whitehall; Bankside","Woken at three; pigeons with burning wings",
 "His maid Jane wakes the house about three to see a fire in the City; Pepys judges it far off and goes back to bed. By morning 300 houses are gone. From the Tower and then a boat he watches people throwing goods into the river and pigeons circling their burning houses until their wings catch. He tells the King and Duke to pull houses down, finds the Lord Mayor exhausted and helpless, and at night watches from a Bankside alehouse as the fire becomes one arch of flame.",
 "Lord! what can I do? I am spent",
 "verified","Pepys 2 Sept 1666 (americanliterature.com Sept 1666 text; National Archives extracts)")
add(os_day(1666,9,2),"day","evelyn","Sayes Court, Deptford","A fire near Fish Street at night",
 "Evelyn's entry is brief: a fire has begun in the City near Fish Street. At Deptford, downriver, it is still a distant event; his long entries begin the next day.",
 "","verified","Evelyn, Diary, 2 Sept 1666; National Archives extracts")
add(os_day(1666,9,2),"day","taswell","Westminster Abbey","News of the fire reaches the Abbey sermon",
 "Fourteen-year-old Taswell is standing on the pulpit steps in Westminster Abbey in the late morning when word of the fire runs through the congregation. He slips out to see and watches boats bringing people who escaped with little more than a blanket.",
 "","approx","Taswell, Autobiography (Camden Miscellany II, 1853), written decades later")
add(os_day(1666,9,2),"day","josselin","Earls Colne, Essex","The goodliest city in the world in ashes",
 "Under this Sunday's date Josselin writes of a very dry season, the Dutch on the coast again and troops raised, plague abating in London but feared in Colchester. Then he records the beginning of the great fire, the finest city in the world laid in ashes, adding a Latin tag that no reader could hold back tears. He must have added this after news reached Essex days later.",
 "","verified","Josselin diary, entry 70015245")
add(os_day(1666,9,2),"day","vincent","London","The night sky turns yellow",
 "Vincent remembered the fire starting in a baker's house in Pudding Lane in the dead of night, then rushing down to London Bridge, taking St Magnus' church, and turning west along Thames Street with the wind. By Sunday evening the smoke made the night sky look yellow.",
 "","verified","Vincent, God's Terrible Voice in the City (1667), fire section")
add(os_day(1666,9,3),"day","pepys","Seething Lane to Bethnal Green","Riding a cart in his nightgown with the money",
 "About four in the morning Lady Batten sends a cart, and Pepys rides it in his nightgown to Sir William Rider's at Bethnal Green with his money, plate and best things. Back home, he, his wife and servants haul more goods over Tower Hill to a lighter on the river. The Duke of York rides through with his guards to keep order.",
 "","verified","Pepys 3 Sept 1666")
add(os_day(1666,9,3),"day","evelyn","Bankside and the City","London was, but is no more",
 "Evelyn takes his coach to Bankside and watches the whole riverside burning from the Bridge along Thames Street toward Cheapside; people are too stunned even to try to save their houses. Goods float on the Thames, the poor flee to the fields, and he thinks 10,000 houses are on fire at once. He compares it to the burning of Troy.",
 "London was, but is no more!",
 "verified","Evelyn, Diary, 3 Sept 1666; National Archives extracts")
add(os_day(1666,9,3),"day","taswell","St Dunstan-in-the-East","A schoolboy in the bucket chain",
 "The Dean of Westminster, John Dolben, marches the scholars into the City to fight the fire. Taswell, acting as a page, fetches water from behind St Dunstan-in-the-East for hours, and they put out the fire there.",
 "","approx","Taswell, Autobiography (1853)")
add(os_day(1666,9,3),"day","vincent","Gracechurch Street, Cornhill, the Royal Exchange","The Exchange burns and the King's statues fall",
 "On Monday the fire took Gracechurch Street and swept up Cornhill into the Royal Exchange, filling its galleries with flame and toppling the statues of kings. The noise of falling buildings was deafening and the night was as bright as noon; four fires met at the corner of Cheapside.",
 "","verified","Vincent, God's Terrible Voice in the City (1667)")
add(os_day(1666,9,4),"day","pepys","Seething Lane garden","Burying the wine and the Parmesan",
 "Tower Street is now burning and goods lie in the gutters. Sir William Batten has dug a pit in his garden for his wine, and in the evening Pepys and Sir William Penn dig another for their wine, and Pepys adds his Parmesan cheese. They write to Coventry for leave to pull down houses to save the Navy Office.",
 "and I my Parmazan cheese",
 "verified","Pepys 4 Sept 1666; MOLA article on Seething Lane excavation")
add(os_day(1666,9,4),"day","evelyn","Fleet Street, Ludgate, St Paul's","Molten lead running in the streets",
 "The fire reaches the Inner Temple and burns through Fleet Street, Ludgate Hill, Newgate and Watling Street. Evelyn sees stones of St Paul's flying like grenades and its lead roof melting down the streets; the pavements glow too hot to walk on. The east wind drives it on.",
 "","verified","Evelyn, Diary, 4 Sept 1666")
add(os_day(1666,9,4),"day","taswell","bridge by Westminster Hall","Reading Terence by the light of St Paul's",
 "In the evening Taswell stands near Westminster Hall and watches St Paul's catch fire. By about nine it is light enough a mile and more away to read a little Latin Terence from his pocket.",
 "","approx","Taswell, Autobiography (1853)")
add(os_day(1666,9,4),"day","vincent","Cheapside","Cheapside engulfed in hours",
 "On Tuesday several fronts of fire met in Cheapside and the whole street was engulfed within a few hours before the flames surged into Broad Street. Vincent's account treats the speed as a sign of God's anger at the city.",
 "","verified","Vincent, God's Terrible Voice in the City (1667)")
add(os_day(1666,9,5),"day","pepys","Barking church steeple; Moorfields; the Exchange","The saddest sight; a cat with its fur burnt off",
 "At two in the morning his wife wakes him: the fire is at All Hallows Barking at the end of their lane. He sends her by boat to Woolwich with their gold, about £2,350. Once the fire is checked, he climbs the Barking steeple and sees the saddest sight of desolation, oil cellars and brimstone still burning. Walking through Cheapside to Moorfields he sees a cat pulled alive from a chimney, its hair burnt off.",
 "the saddest sight of desolation that I ever saw",
 "verified","Pepys 5 Sept 1666")
add(os_day(1666,9,5),"day","evelyn","Fetter Lane, Holborn","Ordered by the King to hold the line at Fetter Lane",
 "The fire turns toward Whitehall, and the King orders Evelyn to help stop it near Fetter Lane. Blowing up houses for firebreaks, long resisted by owners, finally works; the wind drops about noon. The homeless poor are camped in fields for miles.",
 "","verified","Evelyn, Diary, 5 Sept 1666")
add(os_day(1666,9,6),"day","pepys","Bishopsgate; Westminster","Fighting a new outbreak at Bishopsgate",
 "Pepys helps put out a new fire at Bishopsgate, watching women sweep water along the gutters and people scooping sugar from broken casks. In Westminster he cannot buy a clean shirt: every shop is shut and goods are piled in the Hall. He eats fried breast of mutton at Deptford.",
 "","verified","Pepys 6 Sept 1666")
add(os_day(1666,9,6),"day","taswell","St Paul's Cathedral","Ground so hot it nearly scorched his shoes",
 "On Thursday Taswell walks to St Paul's, resting on Fleet Bridge because the ground is almost too hot for his shoes. Inside, bell-metal is melting and stones still fall; he pockets some bell-metal and finds the body of an old woman who had fled to the east walls. He also saw a blacksmith strike down a Frenchman with an iron bar, a sign of the mob's hunt for foreign 'incendiaries'.",
 "","approx","Taswell, Autobiography (1853); day-of-week only in source")
add(os_day(1666,9,7),"day","pepys","St Paul's; Creed's lodging","St Paul's fallen into St Faith's",
 "Pepys walks past St Paul's, its roofs and choir collapsed into the church of St Faith below. He borrows a shirt from his colleague Creed, camped on a bed in an emptied house, and hears that the court had moved its own goods and that news from the fleet is uncertain.",
 "","verified","Pepys 7 Sept 1666")
add(os_day(1666,9,7),"day","evelyn","from Whitehall to London Bridge","Walking the ruins; a rumour of French and Dutch invasion",
 "Evelyn walks through the smoking ruins, the ground too hot to stand on, and sees St Paul's roof melted and stones calcined. Only Gresham's statue survives at the Exchange. At Islington and Highgate he finds perhaps 200,000 homeless waiting for help, and sees a panic that the French and Dutch have landed calmed only by troops.",
 "","verified","Evelyn, Diary, 7 Sept 1666")
add(os_day(1666,9,9),"day","josselin","Earls Colne, Essex","A fast day for the burned city",
 "A week on, Josselin has the facts: the fire began at a baker's in Pudding Lane about one in the morning on Sunday and burned almost everything from the Tower area to Temple Bar, with few killed. The parish keeps a fast and prays; Colchester's plague figure has dropped to 37.",
 "","verified","Josselin diary, entry 70015250")
add(os_day(1666,9,13),"day","evelyn","Whitehall","A plan for a new London, nine days after",
 "Evelyn presents the King and Queen with a survey of the ruins and his plan for a rebuilt city; they pore over it with him for nearly an hour. He is one of several, with Wren and Hooke, racing to redraw London.",
 "","verified","Evelyn, Diary, 13 Sept 1666")
add(ns_day(1666,10,5),"day","giustinian","Venetian embassy, Paris","Louis XIV calls the fire a stroke of luck",
 "Giustinian reports that the French king sees the fire as fortunate, since it saved the French fleet from attack, yet also offers relief, sending tents and biscuit. A second dispatch the same day passes on a French minister's view that 250,000 people are homeless and many merchants ruined.",
 "","verified","CSP Venice vol. 35, October 1666, nos. 82, 84")
add(ns_day(1666,10,12),"day","giustinian","Venetian embassy, Paris","Two terrible fires: the Vlie and London",
 "Giustinian pairs the burning of the Dutch merchant fleet in the Vlie with the burning of London, two disasters that between them have dimmed the hopes of both England and Holland. He also reports plans for stone houses and wide streets and a loss reckoned in the many millions.",
 "","verified","CSP Venice vol. 35, October 1666, nos. 87–88")
add(os_day(1666,10,10),"day","evelyn","Deptford parish church","A national fast for fire, plague and war",
 "A general fast is held across England to humble the nation for the fire, the plague and the war. Evelyn hears a sermon on Christ weeping over Jerusalem, and a collection is taken for those burned out.",
 "This day was ordered a general Fast through the Nation",
 "verified","Evelyn, Diary, 10 Oct 1666")
add(os_day(1666,10,10),"day","josselin","Earls Colne, Essex","Six pounds for London",
 "Josselin notes the public fast for the fire and that his parish collected £6 for the sufferers, a country village sending money to the capital.",
 "","verified","Josselin diary, entry 70015280")
add(os_day(1666,11,20),"day","mompesson","Eyam","Seventy-six families visited, 259 dead",
 "Mompesson writes to John Beilby, who is caring for his children, that the plague is over: 76 families struck and 259 dead, no deaths since 11 October. Woollen clothes are being burned and fumigated; his servant caught it and recovered. He says his ears never heard such lamentations, and he survived.",
 "","verified","Mompesson to John Beilby, Eyam, 20 Nov 1666 (Wood, 1842)")
E.sort(key=lambda e:(e["date_iso"]+"-00")[:10])

eyes=[
 dict(id="pepys",name="Samuel Pepys",life="1633–1703",role="32-year-old Clerk of the Acts to the Navy Board, living in the Navy Office, Seething Lane",side="England (London; royal naval administration)",where="Navy Office, Seething Lane, City of London, through both plague and fire",vantage=1,vantage_label="inside the city, eyewitness and official",form="diary",language="English (Shelton shorthand)",authenticity="Autograph shorthand diary (1660–69) in the Pepys Library, Magdalene College, Cambridge; deciphered 1819–22 and published from 1825; complete text Latham & Matthews (1970–83). Contemporaneous, though the Fire days were written up a little afterwards from notes.",bio="A rising, ambitious naval administrator who stayed at his post when the court fled. He notices everything — smells, money, cheese, pigeons — and records his own fear and self-interest without varnish, which makes him the most human of these eyes.",sources=[{"title":"Pepys diary online (pepysdiary.com)","url":"https://pepysdiary.com/diary/1665/06/07"},{"title":"Project Gutenberg, Diary of Samuel Pepys","url":"https://www.gutenberg.org/cache/epub/3331/pg3331.html"},{"title":"National Archives: extracts from Pepys's diary (Fire)","url":"https://www.nationalarchives.gov.uk/education/resources/great-fire-of-london-examine-the-evidence/extracts-from-samuel-pepys-diary/"},{"title":"americanliterature.com: September 1666 text","url":"https://americanliterature.com/author/samuel-pepys/book/the-diary-of-samuel-pepys/september-1666"}]),
 dict(id="evelyn",name="John Evelyn",life="1620–1706",role="45-year-old gentleman virtuoso, Fellow of the Royal Society, Commissioner for Sick and Wounded Seamen and Prisoners of War",side="England (royalist gentry; crown service)",where="Sayes Court, Deptford, and the Kent ports; walked the burning City",vantage=1,vantage_label="official and eyewitness at the edge of the city",form="diary",language="English",authenticity="Manuscript at the British Library; first published 1818; standard edition E.S. de Beer (1955). Evelyn revised and wrote up parts of his diary in later life, so some entries are polished retrospect rather than same-day notes.",bio="A cultivated royalist with a public job that tied him to the war's victims: sick sailors and thousands of Dutch prisoners. His Fire entries are the grand literary set-piece; within days he was handing the King a plan to rebuild.",sources=[{"title":"Project Gutenberg, Diary of John Evelyn vol. 2 (Bray ed.)","url":"https://gutenberg.org/cache/epub/42081/pg42081-images.html"},{"title":"National Archives: extracts from Evelyn's diary","url":"https://www.nationalarchives.gov.uk/education/resources/great-fire-of-london-examine-the-evidence/extracts-from-john-evelyns-diary/"}]),
 dict(id="josselin",name="Ralph Josselin",life="1617–1683",role="Vicar of Earls Colne, Essex, aged about 49; farmer and father",side="England (Puritan-leaning parish clergy)",where="Earls Colne, Essex, about 50 miles from London",vantage=3,vantage_label="same country, at a distance, reading the bills",form="diary",language="English",authenticity="Manuscript diary (private collection); edited by Alan Macfarlane (1976, British Academy); full transcription online in the Earls Colne records, Cambridge. Contemporaneous, though some news (e.g. the Fire) was written under the day it happened, not the day it was heard.",bio="A country vicar who copied London's weekly plague bills into his diary among notes on weather, crops and his own sins. He shows how the capital's catastrophes arrived in the provinces: as numbers, fast days and collections.",sources=[{"title":"Diary of Ralph Josselin, Earls Colne records (Cambridge) — 2 Sept 1666","url":"https://wwwe.lib.cam.ac.uk/earls_colne/diary/70015245.htm"},{"title":"Earls Colne diary index","url":"https://wwwe.lib.cam.ac.uk/earls_colne/diary/index.htm"}]),
 dict(id="mompesson",name="William Mompesson",life="1639–1709",role="27-year-old rector of Eyam, Derbyshire",side="England (Anglican clergy, Peak District village)",where="Eyam, the quarantined 'plague village'",vantage=0,vantage_label="at the centre of a plague, bereaved",form="dated letters",language="English",authenticity="Three letters (31 Aug, 1 Sept, 20 Nov 1666) survive in copies and were printed in 18th–19th c. works including William Wood, History and Antiquities of Eyam (1842). Much of the Eyam story (lovers' tales, exact cordon rules) is later village tradition; the letters and parish register are the core evidence. Catherine Mompesson died 24 Aug and was buried 25 Aug 1666.",bio="A young rector who, with his ejected Puritan predecessor Thomas Stanley, persuaded his parishioners to seal themselves in rather than carry plague across Derbyshire. His wife stayed and died; his letters are the voice of the village that chose to suffer.",sources=[{"title":"Wood, History and Antiquities of Eyam (1842): The Plague, Mompesson and his Letters","url":"https://places.wishful-thinking.org.uk/DBY/Eyam/History/Plague.html"},{"title":"Wikipedia: William Mompesson","url":"https://en.wikipedia.org/wiki/William_Mompesson"}]),
 dict(id="allin",name="John Allin",life="1623–1682",role="Ejected nonconformist minister from Rye, practising as an irregular physician and alchemist in London",side="England (dissenting clergy)",where="London through the plague of 1665",vantage=1,vantage_label="inside the plague city, healer",form="dated letters",language="English",authenticity="About 190 letters (1664–74), mostly to the Rye solicitor Philip Fryth and to Samuel Jeake; extracted by W. Durrant Cooper in Archaeologia 37 (1857) and studied by L. Thorpe (PhD, Royal Holloway, 2018). Only one dated letter was verified line-level for this chapter.",bio="A Puritan minister forced out at the Restoration who came to London just as the plague did and treated the sick. His letters to Sussex give a dissenter's, and a would-be scientist's, view of the epidemic.",sources=[{"title":"Cooper, 'Notices of the Last Great Plague … Letters of John Allin', Archaeologia 37","url":"https://www.cambridge.org/core/journals/archaeologia/article/inotices-of-the-last-great-plague-16656-from-the-letters-of-john-allin-to-philip-fryth-and-samuel-jeake-in-a-letter-to-sir-henry-ellis-kh-director/C676D8A94A3B04CE571EC936E6B73C0D"},{"title":"Thorpe, 'In middest of death' (Royal Holloway thesis)","url":"https://pure.royalholloway.ac.uk/en/publications/in-middest-of-death-medical-responses-to-the-great-plague-of-1665/"},{"title":"Rye News: Digging up new facts on history","url":"https://www.ryenews.org.uk/?p=32466"}]),
 dict(id="vincent",name="Thomas Vincent",life="1634–1678",role="Ejected Puritan minister and teacher, about 31",side="England (nonconformist)",where="London and its edges throughout the plague; in the city during the Fire",vantage=1,vantage_label="inside the city, preacher",form="chronicle",language="English",authenticity="God's Terrible Voice in the City (printed 1667, Wing V440) — a sermon-chronicle written within a year, built round the weekly bills and his own memory. Eyewitness but shaped as a call to repentance; few exact dates beyond days of the week.",bio="Barred from his pulpit, Vincent stayed to preach in empty churches during the plague and then watched the city burn. He reads both catastrophes as one judgement, giving the dissenters' moral map of the events Pepys and Evelyn describe.",sources=[{"title":"God's Terrible Voice in the City (transcription)","url":"https://gracegems.org/C/Vincent_Gods_terrible_voice_in_the_city.htm"},{"title":"Wellcome Collection record (1667 ed.)","url":"https://wellcomecollection.org/works/btw9m8mu"}]),
 dict(id="taswell",name="William Taswell",life="1652–1731",role="Westminster schoolboy, 13 in the plague and 14 in the Fire",side="England (Westminster)",where="Greenwich and Westminster in 1665; Westminster Abbey and the burning City in 1666",vantage=1,vantage_label="a child in the crowd",form="memoir (written later)",language="Latin (English translation 1761 by his grandson)",authenticity="Written in Latin decades later, translated by Henry Taswell in 1761, printed by the Camden Society (Camden Miscellany II, 1853, ed. G.P. Elliott). Vivid but retrospective; dates are by day of week, so entries here are 'approx'.",bio="A boy's-eye view: running out of a sermon, fetching water in a bucket line, reading by firelight and pocketing melted bell-metal. He also records the ugly hunt for French 'incendiaries' in the streets.",sources=[{"title":"Autobiography and Anecdotes of William Taswell (Internet Archive PDF)","url":"https://ia800206.us.archive.org/30/items/autobiographyane00taswrich/autobiographyane00taswrich.pdf"},{"title":"Wikipedia: William Taswell","url":"https://en.wikipedia.org/wiki/William_Taswell"},{"title":"Lord, Old St Paul's — 'The Burning' (quotes Taswell)","url":"https://www.mainlesson.com/books/lord/stpauls/burning.html"}]),
 dict(id="vandevelde",name="Willem van de Velde the Elder",life="1611–1693",role="Official Dutch marine draughtsman, about 55, attached to the fleet",side="Dutch Republic",where="with the Dutch fleet in the North Sea battles of 1666",vantage=1,vantage_label="enemy fleet, artist-eyewitness",form="sketchbook (dated drawings)",language="Dutch (drawings with notes)",authenticity="Hundreds of his battle drawings survive (c.1,500 at the National Maritime Museum, more at the Rijksmuseum). His presence at the Four Days' and St James's Day battles is recorded; whether he saw Holmes's Bonfire himself is not stated by the Rijksmuseum. Drawings are records, not a written diary.",bio="The nearest thing to a Dutch eye in this chapter: a professional who sailed with the fleet to draw battles as they happened. In 1672 he moved to England and worked for Charles II, painting the very English triumphs he had watched from the other side.",sources=[{"title":"Rijksmuseum RP-T-1905-20: Holmes setting the Dutch fleet on fire (drawing, 1666)","url":"https://www.rijksmuseum.nl/en/collection/RP-T-1905-20"},{"title":"Royal Collection RCIN 406560: Holmes's Bonfire (painting, 1676)","url":"https://col.rct.uk/collection/406560/holmess-bonfire-the-burning-of-dutch-merchant-ships-between-terschelling-and"},{"title":"Wikipedia: Willem van de Velde the Elder","url":"https://en.wikipedia.org/wiki/Willem_van_de_Velde_the_Elder"}]),
 dict(id="giustinian",name="Marc'Antonio Giustinian",life="1619–1688",role="Venetian ambassador at the French court (later Doge of Venice)",side="Republic of Venice (neutral observer)",where="Paris",vantage=4,vantage_label="abroad, hearing news",form="dated letters",language="Italian",authenticity="Official dispatches to the Doge and Senate, Venetian State Archives; calendared in English in Calendar of State Papers Venice vol. 35 (ed. A.B. Hinds, 1935). Dated New Style. Calendar summaries are paraphrases; no quotation used here.",bio="A professional listener at Louis XIV's court who passed on French, Dutch and English versions of every battle and disaster. Through him we hear how the Fire looked to England's rivals: as luck, as judgement, and as a strategic fact.",sources=[{"title":"CSP Venice vol. 35: October 1666","url":"https://prod.british-history.ac.uk/node/76898"},{"title":"CSP Venice vol. 35: July 1666","url":"https://www.british-history.ac.uk/node/76895"},{"title":"CSP Venice vol. 35 (contents)","url":"https://prod.british-history.ac.uk/cal-state-papers/venice/vol35"}]),
]
# life of Giustinian: verify? mark
for e in eyes:
    if e["id"]=="giustinian":
        e["life"]="17th century (dates not verified here)"
        e["role"]="Venetian ambassador at the French court"
        e["authenticity"]+=" His later career and life dates were not verified for this chapter."

data=dict(
 id="london-1666",
 title="The Bills, the Bonfire and the Fire",
 subtitle="The Great Plague (1665), the Second Anglo-Dutch War and the Great Fire of London (2–6 September 1666)",
 span="1665–1666",
 intro=[
 "In the summer of 1665 London began to die by the printed page. Every Thursday the parish clerks' Bills of Mortality reported the week's burials, and across England people copied the numbers: 112, then 1,089, then over 6,000 of plague alone in a week. The court fled to Salisbury and Oxford; the rich followed in coaches. Those who stayed — officials, clergy, the poor — lived among red crosses on doors, dead-carts and empty streets. Perhaps a hundred thousand Londoners, nearly a quarter of the city, died in eighteen months.",
 "All the while England was at war with the Dutch Republic, its great rival for trade. The plague did not stop the Second Anglo-Dutch War: thousands of Dutch prisoners filled Kent castles, the fleets fought the Four Days' Battle in June 1666 and the St James's Day Battle in July, and in August an English squadron under Robert Holmes burned well over a hundred Dutch merchant ships in the Vlie and the town of West-Terschelling. London lit bonfires to celebrate.",
 "Three weeks later the bonfire was London. In the small hours of Sunday 2 September 1666 a fire in Thomas Farriner's bakery in Pudding Lane, fanned by an east wind after a dry summer, ran down to the river and across the timber city. By the time it was stopped on the 5th and 6th it had destroyed some 13,200 houses, 87 parish churches, the Royal Exchange, Guildhall and St Paul's. Rumours that the French or Dutch had started it led mobs to attack foreigners; a confused French watchmaker, Robert Hubert, was hanged for it though he had not even been in London.",
 "These eyes stand at every distance from the disaster. Pepys and Evelyn were royal officials inside or beside the city; Vincent and Allin were dissenting ministers who stayed to preach and heal; Taswell was a schoolboy in the crowd. Josselin, a vicar in Essex, met it all as copied numbers and fast days. Far to the north, the rector of Eyam, William Mompesson, wrote letters from a village that had sealed itself in with the plague. Across the sea, the Dutch draughtsman Willem van de Velde sketched the battles from the enemy fleet, and a Venetian ambassador in Paris heard how England's rivals read its ruin.",
 "Read together, they show how one catastrophe looked different from every angle: a ledger of figures, a judgement of God, a chance for profit, a strategic windfall, a personal grief. Notice how often they rhyme — the same bill of mortality copied in London and Essex, the Vlie bonfire and the London fire paired in Paris, and the day a rector in Derbyshire wrote farewell letters just as a baker's oven in London was banked for the night.",
 "One famous source is missing on purpose: Daniel Defoe's A Journal of the Plague Year (1722) is a novel, written by a man who was about five in 1665. It is brilliant and well-researched, but it is fiction, and it is not one of the eyes here."
 ],
 calendar_note="England still used the Julian (Old Style) calendar, which in 1665–66 ran 10 days behind the Gregorian (New Style) calendar used in the Dutch Republic, France and Venice. So the Fire began on Sunday 2 September 1666 in London but on 12 September in Amsterdam or Paris, and Holmes's Bonfire was 9–10 August to the English but 19–20 August to the Dutch. In addition, the English legal year began on 25 March, so a letter of 24 February 1664/5 belongs to what we call 1665. In this chapter date_iso is always the New Style (Gregorian) date so that English and continental entries line up; date_display shows the original style first and its equivalent.",
 eyes=eyes,
 entries=E,
 convergences=[
 {"date":"1665-09-17","label":"The worst bill so far (week to 5 Sept O.S.): 8,252 dead","eyes":["pepys","evelyn","josselin","vincent"],"note":"Pepys copies the figures in Seething Lane; the same day Evelyn walks through a silent city of exposed coffins; three days later Josselin in Essex copies the same numbers into his diary. Vincent later prints them as a sermon of judgement. One statistic, four temperaments."},
 {"date":"1666-06-11","label":"The Four Days' Battle (1–4 June O.S.)","eyes":["evelyn","vandevelde","josselin","giustinian"],"note":"Evelyn hears the guns from his garden and the court first celebrates a victory; Van de Velde draws it from inside the Dutch fleet; Josselin calls it a loss and a deliverance; in Paris, Giustinian relays a Dutch-side account of a Dutch win."},
 {"date":"1666-08-19","label":"Holmes's Bonfire at the Vlie and West-Terschelling (9–10 Aug O.S.)","eyes":["vandevelde","pepys","giustinian"],"note":"The Dutch draughtsman records the burning ships; Pepys rejoices with bonfires in the streets on 15 Aug (O.S.); two months later Giustinian sets 'the Vlie and London' side by side, as Dutch pamphleteers did, as matching disasters."},
 {"date":"1666-09-11","label":"Eve of the Fire: farewell from Eyam (1 Sept O.S.)","eyes":["mompesson"],"note":"Mompesson writes his farewell to Sir George Savile on the eve of the Fire; within hours a bakery in Pudding Lane is alight. Plague and fire, the chapter's two killers, meet on the calendar."},
 {"date":"1666-09-12","label":"Sunday 2 September (O.S.): the Fire begins","eyes":["pepys","evelyn","taswell","josselin","vincent"],"note":"Pepys sees it from his window at 3 a.m. and goes back to bed; Evelyn writes one line; Taswell hears it in the Abbey sermon; Vincent remembers a yellow sky; Josselin, 50 miles away, writes it in under this date though news must have come later."},
 {"date":"1666-09-13","label":"Monday 3 September: the Exchange and the riverside burn","eyes":["pepys","evelyn","taswell","vincent"],"note":"Pepys carts his money to Bethnal Green in his nightgown; Evelyn compares London to Troy from Bankside; Taswell carries buckets at St Dunstan's; Vincent watches the Royal Exchange's statues fall."},
 {"date":"1666-09-14","label":"Tuesday 4 September: St Paul's burns","eyes":["pepys","evelyn","taswell","vincent"],"note":"Pepys buries wine and Parmesan; Evelyn sees molten lead run in the streets; Taswell reads Terence by the light of the burning cathedral; Vincent sees Cheapside go in hours."},
 {"date":"1666-09-16","label":"Thursday 6 September: walking the ruins","eyes":["pepys","taswell"],"note":"Pepys fights a last outbreak at Bishopsgate; the boy Taswell walks to the hot ruins of St Paul's, finds a dead woman and sees a Frenchman struck down by a mob."},
 {"date":"1666-10-20","label":"10 October (O.S.): the national fast","eyes":["evelyn","josselin"],"note":"Evelyn hears a sermon on Christ weeping over Jerusalem at Deptford; Josselin's village sends £6. At Eyam, the plague had claimed its last victim nine days before."}
 ],
 ties=[
 {"a":"pepys","b":"evelyn","kind":"met","note":"Both served the crown's naval war effort — Pepys at the Navy Board, Evelyn as commissioner for sick and wounded — and they were lifelong acquaintances and correspondents."},
 {"a":"pepys","b":"vandevelde","kind":"opposite sides","note":"Pepys celebrated the burning of the Dutch ships that Van de Velde drew; after 1672 Van de Velde worked in England for Charles II and the Duke of York, Pepys's own masters."},
 {"a":"evelyn","b":"vandevelde","kind":"opposite sides","note":"Evelyn fed and housed the captured Dutch seamen from the battles Van de Velde sketched from the Dutch side."},
 {"a":"taswell","b":"pepys","kind":"same street","note":"On 3 September Taswell fetched water at St Dunstan-in-the-East, a few streets from Pepys's Navy Office in Seething Lane, which the fire reached by the 5th."},
 {"a":"vincent","b":"allin","kind":"same street","note":"Both were ejected Puritan ministers who chose to stay in plague-stricken London, one preaching and one practising physic."},
 {"a":"giustinian","b":"vandevelde","kind":"mentioned","note":"Giustinian's dispatches report the Dutch side of the very battles and the Vlie raid that Van de Velde drew."}
 ],
 threads_out=[
 {"to":"thirty-years","note":"The Dutch Republic fighting England here won formal independence from Spain in the Peace of Münster (1648), part of the Westphalia settlement that ended the Thirty Years' War."},
 {"to":"ww2-europe","note":"Wren's new St Paul's, built after this Fire, survived the Luftwaffe raid of 29 December 1940, often called the 'Second Great Fire of London'."},
 {"to":"long-threads","note":"The Fire led to the London Building Act of 1667 (brick and stone), Wren's churches and the Monument, and the first fire-insurance offices of the 1680s; the plague years fed the Bills of Mortality that John Graunt had turned into early statistics in 1662."},
 {"to":"french-rev","note":"Louis XIV, who in 1666 called London's fire a stroke of luck, built the absolutist monarchy whose debts and wars the Revolution of 1789 overthrew."}
 ],
 images=[
 {"url":"https://www.rijksmuseum.nl/en/collection/RP-T-1905-20","title":"Robert Holmes setting the Dutch fleet on fire at Terschelling","caption":"Wash drawing of Holmes's Bonfire, made the same year by the Dutch fleet's official draughtsman — the enemy's view of the raid London celebrated.","date":"1666","credit":"Willem van de Velde the Elder; Rijksmuseum, Amsterdam"},
 {"url":"https://col.rct.uk/collection/406560/holmess-bonfire-the-burning-of-dutch-merchant-ships-between-terschelling-and","title":"Holmes's Bonfire: the burning of Dutch merchant ships between Terschelling and Vlieland","caption":"The same event painted ten years later for the English Duke of York — the Dutch artist now working for the victor.","date":"1676","credit":"Willem van de Velde the Elder; Royal Collection Trust"},
 {"url":"https://cdn.rijksmuseum.nl/en/collection/RP-P-OB-82.343","title":"A true Pourtraict … of that deplorable Fire of London","caption":"A Dutch-collected plan of London marking the burned area, its title dated in New Style (12–16 September) — the calendar gap made visible.","date":"1666","credit":"Anonymous; Rijksmuseum, Amsterdam"},
 {"url":"https://wellcomecollection.org/works/btw9m8mu","title":"God's Terrible Voice in the City","caption":"Thomas Vincent's 1667 account of plague and fire as a single divine judgement.","date":"1667","credit":"Thomas Vincent; Wellcome Collection"},
 {"url":"https://picturethepast.org.uk/image-library/image-overview/poster/dchq002441/posterid/dchq002441.html","title":"Eyam – Cucklett Church in the Delph","caption":"The rock arch where Mompesson preached outdoors to his quarantined parishioners in 1666 (early 20th-century photograph).","date":"c.1910s–1920s","credit":"Derbyshire Local Studies Library / Picture the Past"},
 {"url":"https://www.rmg.co.uk/collections/library/rmgl-56046","title":"A true and perfect narrative of the great and signal success … within the Vlie","caption":"The official English pamphlet celebrating the burning of 160 Dutch ships and the town of 'Brandaris' on Schelling.","date":"1666","credit":"Printed by Thomas Newcomb; National Maritime Museum library"}
 ],
 further=[
 {"title":"National Archives: Great Fire of London — examine the evidence","url":"https://www.nationalarchives.gov.uk/education/resources/great-fire-of-london-examine-the-evidence/extracts-from-john-evelyns-diary/"},
 {"title":"Wikipedia: Great Fire of London","url":"https://en.wikipedia.org/wiki/Great_Fire_of_London"},
 {"title":"Wikipedia: Great Plague of London","url":"https://en.wikipedia.org/wiki/Great_Plague_of_London"},
 {"title":"Wikipedia: Holmes's Bonfire","url":"https://en.wikipedia.org/wiki/Holmes%27s_Bonfire"},
 {"title":"Lapham's Quarterly: Pepys's 'Plague Posts'","url":"https://www.laphamsquarterly.org/node/10820"},
 {"title":"MOLA: Pepys's Seething Lane excavated","url":"https://www.mola.org.uk/node/25836"}
 ],
 vantage_key="0 = inside a plague community or principal sufferer; 1 = eyewitness in the burning or plague-struck city or fleet; 2 = nearby; 3 = elsewhere in England reading the bills; 4 = abroad, receiving news."
)
json.dump(data,open(OUT,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(len(eyes),len(E))
