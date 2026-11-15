import json

OUT = "/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/vol5/ch-gitanjali-1912.json"

U = {
 "radice": "https://www.india-seminar.com/2011/623/623_william_radice.htm",
 "hurwitz": "https://fortnightlyreview.co.uk/?p=10381",
 "chakrabarty": "https://www.cambridge.org/core/journals/modern-asian-studies/article/friendships-in-the-shadow-of-empire-tagores-reception-in-chicago-circa-19131932/E9A8C860F23B1B96F9D28EBBB8AE123E",
 "illinois": "https://archives.library.illinois.edu/slc/?p=5603",
 "ou": "https://www5.open.ac.uk/research-projects/making-britain/content/rabindranath-tagore",
 "eh": "https://www.english-heritage.org.uk/visit/blue-plaques/rabindranath-tagore/",
 "poetry1912": "https://poetryfoundation.org/poetrymagazine/issue/70320/december-1912",
 "poundnote": "https://poetryfoundation.org/poetrymagazine/articles/58894/tagores-poems",
 "lrb": "https://www.lrb.co.uk/v08/n09/ep-thompson/memories-of-tagore",
 "nobelspeech": "https://nobelprize.org/nobel_prizes/literature/laureates/1913/press.html",
 "saffron": "https://www.saffronart.com/auctions/Work.aspx?l=47705",
 "hathi": "https://catalog.hathitrust.org/Record/102402309",
 "blog_yeats": "https://sesquicentinnial.blogspot.com/2011/10/rabindranath-and-yeats-contd-1.html",
 "blog_print": "https://sesquicentinnial.blogspot.com/2011/10/printing-of-gitanjali-indian-society.html",
 "blog_rec": "https://sesquicentinnial.blogspot.com/2011/11/more-on-recommendation-of-nobel-prize.html",
 "blog_won": "https://sesquicentinnial.blogspot.com/2011/11/rabindranath-won-nobel-prize-for.html",
 "blog_won19": "https://sesquicentinnial.blogspot.com/2011/11/rabindranath-won-nobel-prize-for_19.html",
 "blog_welc": "https://sesquicentinnial.blogspot.com/2011/11/rabindranath-welcomed-at-calcutta.html",
 "frontier": "https://frontierweekly.com/archive/vol-number/vol/vol-45-2012-13/45-14-17/45-14-17-Nobel Laurel-The Centenary.html",
 "outlook": "https://www.outlookindia.com/books/the-poet-and-the-prize-news-223618",
 "jsircar": "https://www.jawharsircar.com/articles/gitanjali-tagore-london.html",
 "scots": "https://scotstagore.org/from-gitanjali-to-song-offerings-story-of-a-metamorphosis-by-subhayu-bandyopadhyay/",
 "wiki1913": "https://en.wikipedia.org/wiki/1913_Nobel_Prize_in_Literature",
 "dailystar": "https://www.thedailystar.net/news-detail-189438",
 "caravan": "https://www.caravanmagazine.in/editors-pick/rabindranath-tagore-nobel-prize-literature",
 "bdnovels": "https://en.bdnovels.org/468/",
 "reading": "https://www.open.ac.uk/Arts/reading/UK/record_details.php?id=3457",
}

eyes = [
 {
  "id": "tagore", "short": "Tagore", "name": "Rabindranath Tagore", "life": "1861–1941",
  "role": "Bengali poet, songwriter, novelist and founder of the school at Santiniketan; aged 51 when he sailed in 1912",
  "side": "Bengal; the Tagore family of Jorasanko, Calcutta",
  "where": "Shilaida on the Padma; London (Hampstead, then South Kensington); Urbana and Chicago; Santiniketan",
  "lat": 23.68, "lon": 87.68,
  "waypoints": [
   {"lat": 23.92, "lon": 89.21, "label": "Shilaida, spring 1912: translating"},
   {"lat": 51.563, "lon": -0.175, "label": "3 Villas on the Heath, Hampstead, June–July 1912"},
   {"lat": 40.11, "lon": -88.21, "label": "Urbana, Illinois, Nov 1912 – winter 1913"},
   {"lat": 41.79, "lon": -87.60, "label": "Chicago, January 1913"},
   {"lat": 51.497, "lon": -0.175, "label": "South Kensington, April–September 1913"},
   {"lat": 23.68, "lon": 87.68, "label": "Santiniketan, November 1913"}
  ],
  "vantage": 0, "vantage_label": "the poet who translated himself",
  "form": "dated letters (English and Bengali); a later lecture",
  "language": "Bengali and English",
  "authenticity": "His English letters to William Rothenstein were edited by Mary Lago as Imperfect Encounter: Letters of William Rothenstein and Rabindranath Tagore, 1911–1914 (Harvard, 1972). The Bengali letters to Indira Devi, Ajit Kumar Chakravarty and others are in the Chithipatra volumes and are paraphrased here, never quoted. The notebook of 83 translations he gave Rothenstein is at the Houghton Library, Harvard; a second notebook used on the voyage is lost. His account of hearing the Nobel news comes from his Stockholm lecture of 26 May 1921, eight years after the event.",
  "bio": "Tagore had published the Bengali Gitanjali in 1910. When illness stopped a planned voyage in March 1912, he began putting his own songs into English prose at his family estate on the Padma, and the translations he carried to London became the book that won him the Nobel Prize eighteen months later. His letters show a man pleased, amused, uneasy and finally exasperated by what the English book did to his life.",
  "sources": [
   {"title": "William Radice, 'The universal is personal' (Seminar 623, 2011), on the Rothenstein manuscript", "url": U["radice"]},
   {"title": "Open University, Making Britain: Rabindranath Tagore (dates and addresses in Britain; archive holdings)", "url": U["ou"]},
   {"title": "Nobel Prize: 1913 award ceremony speech and banquet telegram", "url": U["nobelspeech"]}
  ]
 },
 {
  "id": "rathindranath", "short": "Rathindranath", "name": "Rathindranath Tagore", "life": "1888–1961",
  "role": "Tagore's son, aged 24; agriculture graduate of the University of Illinois (B.S. 1909), travelling with his father and his wife Pratima",
  "side": "The Tagore family",
  "where": "London 1912; Urbana, Illinois, 1912–13; Santiniketan",
  "lat": 51.563, "lon": -0.175,
  "waypoints": [
   {"lat": 51.508, "lon": -0.125, "label": "London Underground, June 1912"},
   {"lat": 40.11, "lon": -88.21, "label": "Urbana, graduate courses, late 1912"}
  ],
  "vantage": 1, "vantage_label": "the son who carried the bag",
  "form": "memoir (written later)",
  "language": "English",
  "authenticity": "His memoir On the Edges of Time was published in 1958, more than forty years after the events. It is the source of the story of the lost attaché case and quotes letters received after the Hampstead reading. Because it is a later recollection, its details (including which Underground station) differ from other accounts.",
  "bio": "Rathindranath had studied agriculture at Illinois and returned there for graduate courses during his father's American stay. In London he handled the luggage and the letters, and his memoir is the only first-hand source for the near-loss of the manuscript. His angle is domestic and practical, a family member watching his father become famous.",
  "sources": [
   {"title": "University of Illinois Archives: Tagore in Urbana", "url": U["illinois"]},
   {"title": "Jawhar Sircar on Gitanjali in London (quotes the memoir on the lost case)", "url": U["jsircar"]}
  ]
 },
 {
  "id": "rothenstein", "short": "Rothenstein", "name": "William Rothenstein", "life": "1872–1945",
  "role": "English painter and portrait draughtsman, aged 40; a founder of the India Society (1910); professor at Sheffield",
  "side": "London art world; the India Society",
  "where": "11 Oak Hill Park, Hampstead",
  "lat": 51.555, "lon": -0.183,
  "waypoints": [
   {"lat": 22.585, "lon": 88.357, "label": "Jorasanko, Calcutta, winter 1910–11"},
   {"lat": 51.555, "lon": -0.183, "label": "Oak Hill Park, Hampstead, 1912"}
  ],
  "vantage": 0, "vantage_label": "host and go-between",
  "form": "dated letters; memoir (written later)",
  "language": "English",
  "authenticity": "His letters to Tagore are in Imperfect Encounter (1972, ed. Mary Lago); his papers are at the Houghton Library and the British Library. His memoir Men and Memories (vol. 2, 1932) was written twenty years after the events and shapes much of the familiar story; it is flagged wherever it is the source.",
  "bio": "Rothenstein met Tagore at the family house in Calcutta during his Indian tour of 1910–11 and asked to see his poems. In London he found the poet lodgings, read the notebook, sent copies to Yeats and others and staged the reading at his house. He drew the portrait used as the frontispiece of the first edition. His angle is the patron's: generous, proprietary and later regretful.",
  "sources": [
   {"title": "English Heritage blue plaque: Rabindranath Tagore (Rothenstein found the lodgings)", "url": U["eh"]},
   {"title": "Open University, Making Britain (Rothenstein MSS, Imperfect Encounter)", "url": U["ou"]}
  ]
 },
 {
  "id": "yeats", "short": "Yeats", "name": "William Butler Yeats", "life": "1865–1939",
  "role": "Irish poet and dramatist, aged 47; Abbey Theatre director",
  "side": "Irish literary revival; London literary world",
  "where": "London (Woburn Buildings); Normandy in late summer 1912",
  "lat": 51.527, "lon": -0.130,
  "waypoints": [
   {"lat": 51.555, "lon": -0.183, "label": "Rothenstein's house, 7 July 1912"},
   {"lat": 49.35, "lon": -0.84, "label": "Normandy (Colleville), Aug–Sept 1912"}
  ],
  "vantage": 0, "vantage_label": "editor and introducer",
  "form": "dated letters; printed introduction (September 1912)",
  "language": "English",
  "authenticity": "His introduction, dated September 1912, was printed in the India Society edition (November 1912) and every later edition; it is quoted under the pre-1929 rule. His letters are in The Collected Letters of W. B. Yeats (InteLex/Oxford) and are paraphrased here because they were first published after 1928. How far he altered Tagore's text is debated: William Radice, working from the Rothenstein manuscript, argues he changed the selection, order, paragraphing and wording substantially.",
  "bio": "Yeats read the translations in manuscript in the summer of 1912, read them aloud at Rothenstein's on 7 July, edited them and wrote the introduction in Normandy. His introduction framed Tagore for the West as the voice of an undivided ancient culture. He fought over single sentences with the India Society and later cooled on the poet he had launched.",
  "sources": [
   {"title": "Gitanjali (song offerings), with Yeats's introduction: HathiTrust record", "url": U["hathi"]},
   {"title": "Poetry, December 1912 (contains Yeats's poems beside Tagore's)", "url": U["poetry1912"]}
  ]
 },
 {
  "id": "pound", "short": "Pound", "name": "Ezra Pound", "life": "1885–1972",
  "role": "American poet in London, aged 26; foreign correspondent of Harriet Monroe's new Poetry magazine",
  "side": "Anglo-American avant-garde",
  "where": "Kensington, London",
  "lat": 51.502, "lon": -0.192,
  "vantage": 2, "vantage_label": "the poems' first American agent",
  "form": "published articles (1912–13); dated letters",
  "language": "English",
  "authenticity": "His note 'Tagore's Poems' (Poetry, December 1912) and essay 'Rabindranath Tagore' (Fortnightly Review, March 1913) are quoted under the pre-1929 rule. His letters to Monroe and others are in The Letters of Ezra Pound, 1907–1941 (ed. D. D. Paige, 1950) and are paraphrased only. Harold M. Hurwitz, 'Ezra Pound and Rabindranath Tagore' (American Literature, 1964), traces his turn from enthusiasm to contempt.",
  "bio": "Pound heard the poems at the Hampstead evening and within weeks was sending six of them to Chicago. In print he compared Tagore to Dante; in private letters by spring 1913 he was mocking the philosophy. His record shows how fast a modernist could take up and drop an author.",
  "sources": [
   {"title": "Hurwitz, 'Ezra Pound and Rabindranath Tagore' (1964), Fortnightly Review reprint", "url": U["hurwitz"]},
   {"title": "Poetry Foundation: Pound, 'Tagore's Poems' (Poetry, December 1912)", "url": U["poundnote"]}
  ]
 },
 {
  "id": "andrews", "short": "Andrews", "name": "Charles Freer Andrews", "life": "1871–1940",
  "role": "Anglican priest of the Cambridge Brotherhood, aged 41; teacher at St Stephen's College, Delhi, on leave in England",
  "side": "Cambridge Mission to Delhi; Indian nationalist sympathisers",
  "where": "Rothenstein's house, Hampstead, 7 July 1912; then Delhi",
  "lat": 51.555, "lon": -0.183,
  "waypoints": [
   {"lat": 51.555, "lon": -0.183, "label": "Hampstead, 7 July 1912"},
   {"lat": 28.66, "lon": 77.23, "label": "St Stephen's College, Delhi"}
  ],
  "vantage": 1, "vantage_label": "a stranger in the room who became a disciple",
  "form": "published account (August 1912)",
  "language": "English",
  "authenticity": "His account 'An Evening with Rabindra' appeared in The Modern Review (Calcutta), August 1912, within weeks of the event. It is the nearest thing to a contemporary report of the reading.",
  "bio": "Andrews met Tagore for the first time on the evening of the reading. His article, written for Indian readers, describes what Yeats said and which poems he chose. In 1914 he went to live at Santiniketan and became one of Tagore's closest friends.",
  "sources": [
   {"title": "Sesquicentennial blog: Rabindranath and Yeats (quotes Andrews's Modern Review account)", "url": U["blog_yeats"]},
   {"title": "Reading Experience Database record 3457", "url": U["reading"]}
  ]
 },
 {
  "id": "sinclair", "short": "May Sinclair", "name": "May Sinclair (Mary Amelia St Clair Sinclair)", "life": "1863–1946",
  "role": "English novelist, aged 48; suffragist",
  "side": "London literary world",
  "where": "London",
  "lat": 51.497, "lon": -0.200,
  "vantage": 1, "vantage_label": "a guest at the reading",
  "form": "dated letter",
  "language": "English",
  "authenticity": "Her letter to Tagore of 8 July 1912 is quoted in Rathindranath Tagore's memoir On the Edges of Time (1958); it is paraphrased here.",
  "bio": "Sinclair was one of the guests Rothenstein invited to hear Yeats read. Her note the next morning is one of several thank-you letters that Rathindranath kept, and the only one in this chapter written while the evening was still fresh.",
  "sources": [{"title": "Sesquicentennial blog: Rabindranath and Yeats (quotes the letter via Rathindranath)", "url": U["blog_yeats"]}]
 },
 {
  "id": "monroe", "short": "Monroe", "name": "Harriet Monroe", "life": "1860–1936",
  "role": "Chicago poet and editor, aged 52; founder of Poetry: A Magazine of Verse (first issue October 1912)",
  "side": "American little-magazine world",
  "where": "Poetry's office, Chicago",
  "lat": 41.88, "lon": -87.63,
  "vantage": 2, "vantage_label": "the editor who printed him first in America",
  "form": "magazine issues (as editor); memoir (written later)",
  "language": "English",
  "authenticity": "Her record here is what she printed: Tagore's poems in Poetry in December 1912, June 1913 and December 1913. Her autobiography A Poet's Life (1938) is a later recollection and is not used for dates.",
  "bio": "Monroe had founded Poetry two months before Pound sent the Tagore poems. Printing them in the third issue gave a new Chicago magazine an international scoop, and she kept printing Tagore through the year of the prize.",
  "sources": [
   {"title": "Poetry, December 1912: table of contents", "url": U["poetry1912"]},
   {"title": "'Poetry and Rabindranath Tagore' (lists the 1912–13 issues)", "url": U["bdnovels"]}
  ]
 },
 {
  "id": "sturgemoore", "short": "Sturge Moore", "name": "Thomas Sturge Moore", "life": "1870–1944",
  "role": "English poet, wood-engraver and book designer, aged 42–43; Fellow of the Royal Society of Literature",
  "side": "London literary world; friend of Yeats",
  "where": "London",
  "lat": 51.52, "lon": -0.13,
  "vantage": 2, "vantage_label": "the nominator",
  "form": "nomination letter (1913); correspondence",
  "language": "English",
  "authenticity": "His nomination survives in the Swedish Academy's Nobel archive; it was the only nomination Tagore received in 1913. His correspondence with Tagore is at Senate House Library, London. The exact date of the letter has not been checked here.",
  "bio": "Sturge Moore is usually listed among those who heard the poems in Hampstead in 1912. As a Fellow of the Royal Society of Literature he was entitled to nominate, and he put Tagore's name forward while the Society as a body was backing Thomas Hardy.",
  "sources": [
   {"title": "The Daily Star: Stories behind 1913 Nobel award (quotes the nomination's opening)", "url": U["dailystar"]},
   {"title": "1913 Nobel Prize in Literature (nominations summary)", "url": U["wiki1913"]}
  ]
 },
 {
  "id": "hallstrom", "short": "Hallström", "name": "Per Hallström", "life": "1866–1960",
  "role": "Swedish writer and translator, aged 47; member of the Swedish Academy (from 1908) and its Nobel Committee",
  "side": "Swedish Academy",
  "where": "Stockholm",
  "lat": 59.33, "lon": 18.07,
  "vantage": 3, "vantage_label": "the committee's reader",
  "form": "committee report; enquiries",
  "language": "Swedish",
  "authenticity": "His report on Tagore is in the Nobel archive of the Swedish Academy and was summarised by Gunnar Ahlström and Anders Österling. A much-repeated English rendering compares Tagore with Goethe; it comes from secondary sources and is not quoted here.",
  "bio": "Hallström wrote the committee's assessment of Tagore, working from the English Gitanjali and whatever else he could find. In May 1913 he had the Nobel Library ask London for more. His report is the institutional reading of the book.",
  "sources": [{"title": "Sesquicentennial blog: more on the recommendation (Hallström, Hjärne, Österling)", "url": U["blog_rec"]}]
 },
 {
  "id": "heidenstam", "short": "Heidenstam", "name": "Verner von Heidenstam", "life": "1859–1940",
  "role": "Swedish poet and novelist, aged 54; member of the Swedish Academy from 1912; Nobel laureate in 1916",
  "side": "Swedish Academy",
  "where": "Sweden",
  "lat": 59.33, "lon": 18.07,
  "vantage": 3, "vantage_label": "the academician who swung the vote",
  "form": "dated letter to the Academy",
  "language": "Swedish",
  "authenticity": "His statement of 18 October 1913 to the Academy's permanent secretary is in the Nobel archive and is cited in Ahlström's and Österling's accounts; only paraphrase is used here, since English renderings are modern translations.",
  "bio": "Heidenstam had joined the Academy only the year before. His letter in support of Tagore, written when the committee was still leaning towards Émile Faguet, is regularly credited with turning the Academy's vote.",
  "sources": [{"title": "Frontier: Nobel Laurel – The Centenary (Heidenstam letter, committee dates)", "url": U["frontier"]}]
 },
 {
  "id": "academy", "short": "Swedish Academy", "name": "Swedish Academy and its Nobel Committee (minutes, ballots and ceremony record)", "life": "1913",
  "role": "The body that awards the Nobel Prize in Literature; committee chaired by the historian Harald Hjärne, with Erik Axel Karlfeldt as permanent secretary",
  "side": "Institution",
  "where": "Stockholm (the Academy met in the Börshuset, Stortorget)",
  "lat": 59.325, "lon": 18.071,
  "vantage": 3, "vantage_label": "the judges",
  "form": "committee minutes, nomination archive, ceremony records",
  "language": "Swedish",
  "authenticity": "Nomination and committee papers are closed for fifty years and have since been opened; the 1913 deliberations are known chiefly through Gunnar Ahlström's and Anders Österling's published accounts. The presentation speech of 10 December 1913 is published by the Nobel Foundation.",
  "bio": "The committee received 32 nominations for 28 writers in 1913. Its chairman doubted how much of Tagore's poetry was his own and how much came from classical Indian tradition, and the committee favoured the French critic Émile Faguet. The full Academy overruled it.",
  "sources": [
   {"title": "Nobel Prize: 1913 award ceremony speech", "url": U["nobelspeech"]},
   {"title": "Sesquicentennial blog: Rabindranath won Nobel Prize (quotes Ahlström on the vote)", "url": U["blog_won"]}
  ]
 },
 {
  "id": "thompson", "short": "E. J. Thompson", "name": "Edward John Thompson", "life": "1886–1946",
  "role": "Wesleyan Methodist educational missionary at Bankura College, Bengal, aged 27; later Tagore's English biographer",
  "side": "British missionaries in Bengal",
  "where": "Bankura; visiting Santiniketan 13–14 November 1913",
  "lat": 23.68, "lon": 87.68,
  "waypoints": [
   {"lat": 23.23, "lon": 87.07, "label": "Bankura"},
   {"lat": 23.68, "lon": 87.68, "label": "Santiniketan, 13–14 Nov 1913"}
  ],
  "vantage": 1, "vantage_label": "a guest on the day the news came",
  "form": "private written account (dated 17 November 1913)",
  "language": "English",
  "authenticity": "His account of the visit, dated 17 November 1913 and written for a few friends, was published by his son E. P. Thompson in the London Review of Books (vol. 8 no. 9, 1986) and in Alien Homage (1993). First published after 1928, so paraphrased only.",
  "bio": "Thompson had come to Santiniketan by train to talk poetry. He spent the morning of 13 November improving the diction of new translations with Tagore under the trees, and was still there the next afternoon when the telegrams began to arrive. He later wrote two books on Tagore.",
  "sources": [{"title": "E. P. Thompson, 'Memories of Tagore' (London Review of Books, 1986)", "url": U["lrb"]}]
 },
 {
  "id": "press", "short": "The press", "name": "Newspapers in London, New York and Los Angeles (Reuters reports and editorials)", "life": "1913",
  "role": "Daily papers reporting and judging the award",
  "side": "British and American press",
  "where": "London, New York, Los Angeles",
  "lat": 51.514, "lon": -0.107,
  "vantage": 4, "vantage_label": "news only",
  "form": "newspaper reports and editorials",
  "language": "English",
  "authenticity": "Quotations are from reports of 13–15 November 1913 as reproduced in centenary studies and anthologies of press reaction; the original issues have not been checked here.",
  "bio": "Reuters carried the news from Stockholm on 13 November. Papers on both sides of the Atlantic mixed delight, puzzlement and open racial hostility, and some of them registered that the prize had for the first time gone to someone who was not white.",
  "sources": [
   {"title": "Sesquicentennial blog: Rabindranath won Nobel Prize (quotes Evening Post and Los Angeles Times)", "url": U["blog_won"]},
   {"title": "1913 Nobel Prize in Literature (press reactions)", "url": U["wiki1913"]}
  ]
 }
]

E = []
def e(date_iso, date_display, precision, eye, place, headline, digest, quote, confidence, source_note):
    E.append(dict(date_iso=date_iso, date_display=date_display, precision=precision, eye=eye, place=place,
                  headline=headline, digest=digest, quote=quote, confidence=confidence, source_note=source_note))

e("1911-01", "Winter 1910–11", "range", "rothenstein", "Jorasanko, Calcutta",
  "A visiting painter asks to see the poet's work",
  "On his Indian tour Rothenstein visited the Tagore house in Calcutta, where the poet's nephews Abanindranath and Gaganendranath were leading a new school of Indian painting. He was struck by their uncle and asked for translations. A few prose versions, some made by the Santiniketan teacher Ajit Kumar Chakravarty, reached him in London in 1911. The account of the meeting comes largely from Rothenstein's memoir, written two decades later.",
  "", "approx", "Rothenstein, Men and Memories vol. 2 (1932), as summarised in Subhayu Bandyopadhyay (Scots Tagore) and Open University, Making Britain; memoir written later.")

e("1912-03", "March 1912", "month", "tagore", "Calcutta",
  "Illness cancels the voyage to England",
  "Tagore was booked to sail for England in March 1912, but his doctors would not let him travel and the passage was given up. He went to the family estate at Shilaida on the Padma river to rest. The voyage he had planned for health and for his son's sake would become a literary journey instead.",
  "", "approx", "Jawhar Sircar, 'Gitanjali, Tagore and London' (he was not permitted to travel in March 1912 and rested at Shilaida).")

e("1912-04", "April–May 1912", "range", "tagore", "Shilaida, on the Padma (now Kushtia, Bangladesh)",
  "Too weak to write new poems, he translates old ones",
  "At Shilaida Tagore began putting songs from the Bengali Gitanjali and other recent books into English prose in an exercise book. He later told his niece Indira Devi that he lacked the energy for new work and turned to translation as a quiet occupation, without expecting anything to come of it. By the time he reached England the notebook held 83 translations drawn from Gitanjali, Gitimalya, Naivedya, Kheya and the play Achalayatan.",
  "", "approx", "Tagore's Bengali letter to Indira Devi of 6 May 1913 (paraphrased); William Radice, Seminar 623 (2011), on the Rothenstein manuscript at the Houghton Library.")

e("1912-05-27", "Monday 27 May 1912", "day", "tagore", "Bombay",
  "He sails from Bombay with his son and daughter-in-law",
  "Tagore left Bombay for England aboard the City of Glasgow with Rathindranath and Pratima. He kept translating on the voyage in a second notebook, which has not survived.",
  "", "verified", "Sesquicentennial blog, 'Rabindranath welcomed at Calcutta' (left Bombay 27 May 1912); Scots Tagore (ship City of Glasgow); Radice on the lost second notebook.")

e("1912-06-16", "Sunday 16 June 1912", "day", "tagore", "London",
  "Arrival in London with two notebooks of English prose",
  "After about three weeks at sea Tagore reached London on 16 June. Within days he moved to lodgings that Rothenstein found for him at 3 Villas on the Heath, in the Vale of Health, Hampstead, close to Rothenstein's own house.",
  "", "verified", "Open University, Making Britain (in Britain from 16 June 1912; 3 Heath Villas June–July 1912); English Heritage blue plaque page.")

e("1912-06", "June 1912, the day after arrival (exact day not recorded)", "month", "rathindranath", "London Underground",
  "The manuscript is left behind on the Underground",
  "Rathindranath later wrote that he and his father left an attaché case containing the English translations on an Underground train and did not notice until the next day. He went to the Left Luggage office expecting the worst and found it there. Versions differ on the station: Sircar's summary of the memoir gives Charing Cross, other retellings Baker Street.",
  "", "approx", "Rathindranath Tagore, On the Edges of Time (1958), as summarised by Jawhar Sircar; Scots Tagore (Baker Street). Memoir written later; station disputed.")

e("1912-06", "Late June 1912", "month", "rothenstein", "Oak Hill Park, Hampstead",
  "Rothenstein reads the notebook and sends copies out",
  "Tagore gave Rothenstein the exercise book of translations. Rothenstein had copies typed and sent them to Yeats, the critic A. C. Bradley and the preacher Stopford Brooke. He urged Tagore to add the later translations from the voyage. The notebook itself stayed with Rothenstein and is now at Harvard.",
  "", "approx", "William Radice, Seminar 623 (2011); English Heritage blue plaque page; Rothenstein's memoir (1932, written later) for the details of his reaction.")

e("1912-06", "Summer 1912, before the reading", "month", "yeats", "London",
  "Yeats carries the typescript everywhere for days",
  "Yeats read the translations in London and found that he could not stop. In his introduction he described carrying them about in railway trains, on the tops of omnibuses and in restaurants, and having to close the manuscript so that strangers would not see how they moved him.",
  "carried the manuscript of these translations about with me for days", "approx", "Yeats, Introduction to Gitanjali (India Society, 1912), dated September 1912; the period described is June–July 1912.")

e("1912-07-07", "Sunday 7 July 1912, evening", "day", "rothenstein", "11 Oak Hill Park, Hampstead",
  "A Tagore evening in a painter's drawing room",
  "Rothenstein invited a select company to hear the translations: among those named are Ernest Rhys, Alice Meynell, Evelyn Underhill, Henry Nevinson, May Sinclair, Charles Trevelyan, Arthur Fox Strangways, C. F. Andrews, Ezra Pound and Thomas Sturge Moore. Yeats read and Tagore sat listening. The house has since been demolished. One reference work dates the reading to 30 June; most accounts, and the poet's son, give 7 July.",
  "", "verified", "English Heritage blue plaque page (7 July 1912); Hurwitz 1964; sesquicentennial blog citing Rathindranath for the guest list; Reading Experience Database 3457 (gives 30 June, after Waller 2006).")

e("1912-07-07", "Sunday 7 July 1912, evening", "day", "yeats", "11 Oak Hill Park, Hampstead",
  "Yeats introduces the poems, then reads them aloud",
  "Before reading, Yeats spoke about the poems. According to Andrews he set their religious feeling beside The Imitation of Christ and their feeling for nature beside Keats, Shelley and Wordsworth. Then he read a selection to a room that included the poet himself.",
  "", "verified", "Andrews, 'An Evening with Rabindra', Modern Review, August 1912, as quoted in the sesquicentennial blog.")

e("1912-07-07", "Sunday 7 July 1912, evening", "day", "andrews", "11 Oak Hill Park, Hampstead",
  "A missionary on leave hears Bengal in an English room",
  "Andrews met Tagore that night for the first time. He noted the poems Yeats chose, including the one that became no. 95, about crossing the threshold of life and death, and no. 22, set in the deep shadows of a rainy July. He wrote that the verses brought the scenery of Bengal before his eyes and judged them entirely their own.",
  "singularly and wholly original", "verified", "Andrews, 'An Evening with Rabindra', Modern Review (Calcutta), August 1912, as quoted in the sesquicentennial blog.")

e("1912-07-07", "Sunday 7 July 1912, evening", "day", "rathindranath", "11 Oak Hill Park, Hampstead",
  "Silence after the reading, then letters",
  "Rathindranath remembered the silence after Yeats stopped reading as almost painful, and that the guests left with little said. The next day letters of thanks began to arrive at Hampstead, and he kept them.",
  "", "approx", "Rathindranath Tagore, On the Edges of Time (1958), as quoted in the sesquicentennial blog; memoir written later.")

e("1912-07-07", "Sunday 7 July 1912, evening", "day", "pound", "11 Oak Hill Park, Hampstead",
  "Pound hears the poems for the first time",
  "Pound was among the guests at Rothenstein's. Within weeks he had made up his mind that the Bengali poet was the literary discovery of the season and set about securing poems for the Chicago magazine he was advising.",
  "", "approx", "Harold M. Hurwitz, 'Ezra Pound and Rabindranath Tagore', American Literature 36 (1964), reprinted in the Fortnightly Review.")

e("1912-07-08", "Monday 8 July 1912", "day", "sinclair", "London",
  "A novelist cannot find words, so she writes them",
  "May Sinclair wrote to Tagore the morning after the reading. She explained that she had not been able to say anything to him about the poems the night before and tried to put her response in a letter instead. The poet Margaret Radford wrote on the same day.",
  "", "verified", "Letters of 8 July 1912 quoted in Rathindranath Tagore, On the Edges of Time (1958), via the sesquicentennial blog. Paraphrased; first published after 1928.")

e("1912-08", "August 1912", "month", "andrews", "Calcutta (publication)",
  "Andrews reports the evening to Indian readers",
  "The Modern Review, Calcutta's leading English-language monthly, printed Andrews's account of the Hampstead evening. It told Bengali readers, before any English book existed, that their poet had been read aloud by Yeats to a room of London writers.",
  "", "verified", "Modern Review, August 1912, 'An Evening with Rabindra' (sesquicentennial blog).")

e("1912-08-02", "Friday 2 August 1912", "day", "tagore", "London",
  "Tagore tells Santiniketan that a book is coming",
  "In a Bengali letter to Ajit Kumar Chakravarty, the Santiniketan teacher who had made some of the first English versions of his poems, Tagore reported that the India Society would publish Gitanjali and that Yeats would write the introduction. The decision had been taken at a dinner for the poet at the Trocadero restaurant.",
  "", "approx", "Tagore to Ajit Kumar Chakravarty, 2 August 1912 (Bengali; paraphrased), as cited in the sesquicentennial blog, 'Printing of Gitanjali'.")

e("1912-09-07", "Saturday 7 September 1912", "day", "yeats", "Normandy",
  "Yeats asks for a paragraph of plain facts",
  "Yeats had taken the edited manuscript to Normandy to write the introduction. He wrote to Rothenstein that his essay contained no facts beyond the conversations it quoted, and asked for a short biographical note with dates to follow it.",
  "", "verified", "Yeats to Rothenstein, 7 September 1912 (Collected Letters; paraphrased), cited in the sesquicentennial blog, 'Printing of Gitanjali'.")

e("1912-09", "September 1912", "month", "yeats", "Normandy / London",
  "The introduction: a dreamed-of world",
  "Yeats's introduction, signed September 1912, quoted conversations with Indian visitors about Tagore's fame in Bengal and presented the poems as the voice of a culture where poetry and religion were still undivided. He wrote that the lyrics showed him a world he had long imagined.",
  "a world I have dreamed of all my life long", "approx", "Yeats, Introduction to Gitanjali (India Society, 1912; Macmillan, 1913). Dating of the signature not checked against a facsimile.")

e("1912-10-19", "Saturday 19 October 1912", "day", "tagore", "England",
  "Tagore leaves England for America",
  "Before the book appeared, Tagore left Britain for the United States, where Rathindranath was to take graduate courses at the University of Illinois. He would hear of the book's reception by letter.",
  "", "verified", "Open University, Making Britain (in Britain 16 June to 19 October 1912).")

e("1912-11-01", "Friday 1 November 1912 (16 Kartik 1319 BS)", "day", "rothenstein", "London",
  "Seven hundred and fifty copies in cream silk",
  "The India Society issued Gitanjali (Song Offerings): 103 prose poems, 53 from the Bengali Gitanjali and the rest from ten other books. It was printed at the Chiswick Press in 750 copies, 250 for sale, with Rothenstein's portrait drawing of Tagore as a photogravure frontispiece and Yeats's introduction.",
  "", "approx", "Sesquicentennial blog, 'Printing of Gitanjali' (1 Nov, 16 Kartik); Saffronart lot description (750 copies, 250 for sale, Chiswick Press, Rothenstein frontispiece); Radice on contents.")

e("1912-11-17", "Sunday 17 November 1912", "day", "tagore", "Unitarian Church, Urbana, Illinois",
  "In a prairie college town, a lecture on the Upanishads",
  "Tagore gave the first of a series of talks at the Unitarian church in Urbana, on the Upanishads. He followed it with talks on religion in ancient India (23 November) and on Hindu thought and the problem of evil (27 November). He stayed with the electrical engineering professor Morgan Brooks and read his poems to a group that met at 909 West Nevada Street. These talks grew into the book Sadhana.",
  "", "verified", "University of Illinois Archives, Student Life and Culture: Tagore in Urbana.")

e("1912-11", "Late 1912", "range", "rathindranath", "University of Illinois, Urbana",
  "Back at his old university",
  "Rathindranath took graduate courses at Illinois for a few months, lodging with the Spanish professor Arthur R. Seymour and his wife Mayce, while his father lectured in town. Mrs Seymour wrote the introduction to a selection of Tagore's work in the student Illinois Magazine that December.",
  "", "verified", "University of Illinois Archives: Tagore in Urbana (Illinois Magazine IV:3, December 1912).")

e("1912-12", "December 1912", "month", "pound", "London / Chicago",
  "Six poems and a note in Poetry",
  "Poetry's third issue printed six of the Gitanjali poems with Pound's note, 'Tagore's Poems'. Pound explained that they had been picked from a hundred lyrics about to come out as a book and presented the poet as both modern and ancient.",
  "The six poems now published were chosen from a hundred lyrics", "verified", "Poetry 1:3 (December 1912); Poetry Foundation issue page and article page; wording as quoted in 'Poetry and Rabindranath Tagore'.")

e("1912-12", "December 1912", "month", "monroe", "Chicago",
  "A three-month-old magazine prints the Bengali poet",
  "Monroe's December number put Tagore beside five new poems by Yeats and work by John Reed, George Sterling and Alice Corbin Henderson. It was Tagore's first appearance in print in America, a month after the London edition, and it came out while he was lecturing a hundred and forty miles south of her office.",
  "", "verified", "Poetry Foundation, December 1912 issue contents.")

e("1913-01", "January 1913", "month", "tagore", "Chicago",
  "Chicago, the university, and Harriet Moody's house",
  "Tagore spent time in Chicago, spoke at the University of Chicago and stayed with Harriet Vaughn Moody, the widow of the poet William Vaughn Moody, who became a lifelong friend. Her house was a meeting place for the city's writers.",
  "", "approx", "Dipesh Chakrabarty, 'Friendships in the Shadow of Empire', Modern Asian Studies 48:5 (2014), abstract; Olivia Howard Dunbar, A House in Chicago (1947), cited in 'Poetry and Rabindranath Tagore'.")

e("1913-01-09", "Thursday 9 January 1913", "day", "yeats", "London",
  "Yeats wants his sentence back",
  "Yeats complained that a change made to the last paragraph of poem no. 52 without his knowledge had removed the coyness and sweetness of the woman in it and spoiled the poem. He blamed the India Society's Fox Strangways and asked for the old sentence to be restored in the new edition.",
  "", "approx", "Yeats letter of 9 January 1913 (recipient as given in the sesquicentennial blog, 'Printing of Gitanjali'; paraphrased).")

e("1913-02-14", "Friday 14 February 1913", "day", "tagore", "United States",
  "From America, a promise to show Yeats the proofs",
  "Tagore wrote to Rothenstein that he knew Yeats was unhappy about corrections made without him, and promised that the proofs of the new edition would be sent to Yeats first. The letter shows the poet already treating the English text as partly someone else's book.",
  "", "approx", "Tagore to Rothenstein, 14 February [1913], in Imperfect Encounter (1972), as cited in the sesquicentennial blog; year inferred from context.")

e("1913-03", "March 1913", "month", "pound", "London",
  "Pound reaches for Dante",
  "In the Fortnightly Review Pound published a long essay on Tagore. He compared the poet to Dante and set him against what he saw as the weariness of modern European verse.",
  "", "approx", "Hurwitz 1964 (Fortnightly Review reprint).")

e("1913-03", "March 1913", "month", "yeats", "London",
  "Macmillan takes over the book",
  "Macmillan issued Gitanjali as a trade edition with Yeats's introduction. Demand was immediate, and it was reprinted many times over the next two years. The Gardener and The Crescent Moon followed later in 1913.",
  "", "verified", "Radice (Seminar 623); Caravan, 31 Oct 2022; Open University, Making Britain.")

e("1913-04", "April 1913", "month", "pound", "London",
  "In private, 'more theosophy'",
  "By April Pound was writing privately that Tagore's philosophy was only more theosophy. The public praise and the private mockery overlapped for some months, and by 1917 he was dismissing Tagore's reputation in print.",
  "", "approx", "Hurwitz 1964, summarising Pound's letters (The Letters of Ezra Pound, ed. Paige, 1950); paraphrased.")

e("1913-05-06", "Tuesday 6 May 1913", "day", "tagore", "London",
  "To his niece, why he translated",
  "Back in London since 19 April, Tagore wrote in Bengali to Indira Devi to explain how the English Gitanjali had come about. He described the translations as an expression of his innermost feelings and of his spiritual practice, made in weakness and without ambition. Among Bengali critics, rumours that someone else had made them were already spreading.",
  "", "verified", "Tagore to Indira Devi Chaudhurani, 6 May 1913 (Bengali; paraphrased), as cited by William Radice, Seminar 623 (2011); Open University for return date.")

e("1913-05-20", "Tuesday 20 May 1913", "day", "hallstrom", "Stockholm / London",
  "Stockholm asks London who this poet is",
  "To support Hallström's report, the Nobel Library in Stockholm asked the Times Book Club in Oxford Street for material on Tagore. Its secretary, G. F. James, passed the request to Fox Strangways, who sent press cuttings from The Times, the Fortnightly Review, The Nineteenth Century and other papers.",
  "", "approx", "Sesquicentennial blog, 'More on recommendation of Nobel Prize' (letter of 20 May 1913, G. F. James to Strangways).")

e("1913-07-18", "Friday 18 July 1913", "day", "academy", "Nobel Library, Stockholm",
  "Bengali books reach Stockholm",
  "The Nobel Library received three of Tagore's Bengali books, Naivedya, Kheya and Gitanjali, as well as English volumes such as The Gardener and Glimpses of Bengal Life. The orientalist Esaias Tegnér was the one Academy member able to read the originals; the rest worked from translations.",
  "", "approx", "Frontier, 'Nobel Laurel – The Centenary' (2012); The Daily Star (Tegnér the only Bengali reader).")

e("1913-09-27", "Saturday 27 September 1913", "day", "tagore", "Bombay, then Calcutta",
  "Home to garlands he thought were for someone else",
  "Tagore left Britain on 3 September and landed at Bombay on the City of Lahore on 27 September. Two days later a crowd met his train at Howrah. He wrote afterwards to Edward Thompson that he had assumed the people with garlands at Bombay were waiting for some official.",
  "", "verified", "Sesquicentennial blog, 'Rabindranath welcomed at Calcutta' (Bombay 27 Sept, Howrah 29 Sept 1913; letter to Thompson); Open University (left 3 Sept 1913).")

e("1913-10-18", "Saturday 18 October 1913", "day", "heidenstam", "Sweden",
  "An academician writes that he has found a great poet",
  "Heidenstam wrote to the Academy's permanent secretary in support of Tagore. He argued that the poems revealed one of the very greatest poets of the age and that the Academy had a rare chance to honour a great name before the rest of the world knew it.",
  "", "approx", "Frontier, 'Nobel Laurel – The Centenary' (date and gist); Ahlström and Österling as summarised in centenary studies. Paraphrased from modern translations.")

e("1913-10", "Autumn 1913", "month", "hallstrom", "Stockholm",
  "Hallström's report argues for Tagore",
  "Hallström completed his written assessment, the second part dealing with Gitanjali. He judged the poetry to rank with the greatest of modern European lyric verse. It did not change the mind of the committee chairman, Harald Hjärne, who doubted how much of what he read was Tagore's own and how much came from ancient Indian tradition.",
  "", "approx", "Sesquicentennial blog, 'More on recommendation' (Österling's account); Wikipedia, 1913 Nobel Prize in Literature (report summary). Month not fixed.")

e("1913-10-24", "Friday 24 October 1913", "day", "academy", "Stockholm",
  "The committee still prefers a French critic",
  "Until the committee meeting of 24 October the leading name on the list was Émile Faguet, the French literary historian. Thomas Hardy, nominated by 97 Fellows of the Royal Society of Literature, had been set aside as too pessimistic for Nobel's will, and Anatole France as too sceptical.",
  "", "approx", "Frontier, 'Nobel Laurel – The Centenary'; Wikipedia, 1913 Nobel Prize in Literature.")

e("1913-11-13", "Thursday 13 November 1913", "day", "academy", "Stockholm",
  "The full Academy overrules its committee",
  "At the Academy's plenary meeting the committee's recommendation of Faguet was rejected. According to Gunnar Ahlström, of the thirteen members who voted, twelve voted for Tagore. The prize was announced the same day.",
  "", "verified", "Ahlström, quoted in the sesquicentennial blog, 'Rabindranath won Nobel Prize'; Wikipedia, 1913 Nobel Prize in Literature (announced 13 November).")

e("1913-11-13", "Thursday 13 November 1913", "day", "thompson", "Bolpur and Santiniketan",
  "Polishing new translations under the trees",
  "Thompson arrived at Bolpur about 11.30 in the morning and walked to the ashram with some of the boys. He found Tagore sitting under thick bushes with manuscripts of new translations on a little table, and was asked to improve their diction and rhythm. They also talked about Sister Nivedita, whom Tagore disliked, and Annie Besant, whom he refused ever to meet. Neither man knew that the vote in Stockholm was taking place that same day.",
  "", "verified", "E. J. Thompson's account dated 17 November 1913, published by E. P. Thompson, London Review of Books 8:9 (1986). Paraphrased.")

e("1913-11-13", "Thursday 13 November 1913", "day", "press", "New York",
  "'Anybody but a white person'",
  "Reporting the cable from Stockholm, the New York Evening Post observed that this was the first time on record that the prize had gone to anyone who was not white. Reuters' report, carried in London that evening, gave the prize money and the list of earlier laureates.",
  "given to anybody but a white person", "approx", "Evening Post (New York), 13 Nov 1913, and Reuters report, as quoted in the sesquicentennial blog, 'Rabindranath won Nobel Prize'.")

e("1913-11-14", "Friday 14 November 1913, afternoon", "day", "tagore", "Santiniketan",
  "A telegram in the pocket",
  "In his Stockholm lecture of 1921 Tagore remembered being handed a telegram while walking with visitors and boys. He put it in his pocket unread until an English guest urged him to open it, and he first thought the telegraph clerks had made a mistake. A congratulatory wire from Calcutta friends reached the Bolpur post office at 4.43 that afternoon; the Academy's own cable, routed through Macmillan in London, reached Calcutta only on the 15th and Santiniketan on the 16th, which is why sources give dates from 13 to 16 November.",
  "possibly the telegraphic language was not quite correct", "approx", "Tagore, Nobel lecture, Stockholm, 26 May 1921 (recollection eight years later); sesquicentennial blog 'Rabindranath won Nobel Prize (19)' for the telegram times; Open University and Scots Tagore give 16 November.")

e("1913-11-14", "Friday 14 November 1913, about 4.30 p.m.", "day", "thompson", "Santiniketan",
  "Tea interrupted",
  "Thompson was having tea when Tagore came in and asked to be excused for a few hours because he had to go somewhere. By evening the ashram knew why. Thompson's private record of the two days was written three days later for a few friends.",
  "", "approx", "Thompson's account as quoted in the sesquicentennial blog, 'Rabindranath won Nobel Prize (19)'; E. P. Thompson, LRB 1986. Paraphrased.")

e("1913-11-14", "Friday 14 November 1913", "day", "press", "London",
  "A surprise, 'hailed as a very happy one'",
  "The Times correspondent in Stockholm reported that the choice had surprised people but was being welcomed. The Daily News and Leader called Tagore an uncontroversial winner whose themes were those of art everywhere. Other papers complained that Hardy or Anatole France had been passed over.",
  "hailed as a very happy one", "approx", "The Times, Nov 1913, as quoted in Wikipedia, 1913 Nobel Prize in Literature; Daily News and Leader, 14 Nov 1913, as summarised by Jawhar Sircar.")

e("1913-11-15", "Saturday 15 November 1913", "day", "press", "Los Angeles",
  "'The Ignoble Decision'",
  "The Los Angeles Times headlined its story 'The Ignoble Decision' and called Tagore unworthy of the prize. It sneered that he was a Hindu poet whose name few people could pronounce.",
  "a Hindu poet whose name few people can pronounce", "approx", "Los Angeles Times, 15 Nov 1913, as quoted in the sesquicentennial blog, 'Rabindranath won Nobel Prize'.")

e("1913-11-17", "Monday 17 November 1913", "day", "thompson", "Bankura",
  "Thompson writes it all down",
  "Back at Bankura, Thompson wrote out a private account of his two days at Santiniketan for a few friends. It records the poet at work and at ease on the last day before his fame, and Thompson's own unease at the gap between the Bengal he knew and the Bengal of Yeats's introduction.",
  "", "verified", "E. P. Thompson, 'Memories of Tagore', LRB 8:9 (1986), introduction and text (account dated 17 November 1913).")

e("1913-11-18", "Tuesday 18 November 1913", "day", "tagore", "Santiniketan",
  "Fame as a tin can tied to a dog's tail",
  "Writing to Rothenstein in English, Tagore said that the uproar since the prize had destroyed his peace. He compared it to a tin can tied to a dog's tail, making a noise wherever he went.",
  "a tin can at a dog's tail", "approx", "Tagore to Rothenstein, 18 November 1913, Imperfect Encounter (1972), as cited by Nandan Datta, Outlook, 15 April 2004.")

e("1913-11-23", "Sunday 23 November 1913", "day", "tagore", "Santiniketan",
  "To the Calcutta deputation: an honour he cannot drink",
  "A trainload of Calcutta notables, among them the scientist Jagadish Chandra Bose, came to Santiniketan to congratulate him. Tagore's reply startled them. He said he could not accept their honour without hesitation, because many of those now praising him had scorned his work until Europe praised it. Reports say he left in a dog-cart while the crowd followed on foot. Later recollections give the party as only thirty or forty, and they say he afterwards apologised.",
  "", "approx", "Nandan Datta, Outlook (2004), citing Nirad C. Chaudhuri and Pramathanath Bishi; Sri Chinmoy, Rabindranath Tagore: The Moon of Bengal's Heart (2011), section 105 (late recollection). Date 23 November from standard biographies; not checked against the Calcutta papers.")

e("1913-12", "December 1913", "month", "monroe", "Chicago",
  "Poetry prints him again as a laureate",
  "A month after the prize, Poetry printed five more Tagore poems, among them 'The Gift' and 'Union'. The magazine that had printed him before he was famous now printed him as a Nobel laureate.",
  "", "approx", "'Poetry and Rabindranath Tagore' (December 1913 group); Poetry Foundation poem pages.")

e("1913-12-10", "Wednesday 10 December 1913", "day", "academy", "Grand Hôtel and Academy, Stockholm",
  "A ceremony without the laureate",
  "Harald Hjärne gave the presentation speech, saying the Academy was glad to honour a work that matched Nobel's will. At the banquet the British chargé d'affaires, Robert Clive, accepted the medal and diploma for Tagore and read his telegram thanking the Academy.",
  "", "verified", "Nobel Foundation: 1913 award ceremony speech; Caravan, 31 Oct 2022; Outlook, 2004.")

e("1913-12-10", "Wednesday 10 December 1913", "day", "tagore", "Santiniketan (telegram read in Stockholm)",
  "One line for Stockholm",
  "Tagore did not travel to Sweden. His telegram, read aloud at the banquet, thanked the Academy for understanding him across the distance. He received the medal and diploma from the Governor of Bengal, Lord Carmichael, in Calcutta on 29 January 1914, and gave his Nobel lecture in Stockholm only in May 1921.",
  "the breadth of understanding which has brought the distant near", "verified", "Banquet telegram, 10 December 1913 (Les Prix Nobel; Nobel Foundation); Scots Tagore (Calcutta presentation 29 Jan 1914; Stockholm 26 May 1921).")

claims = [
 {"date_iso": "1912-04", "date_display": "April–May 1912", "eye": "tagore", "claim": "Begins English prose versions of his Bengali songs at Shilaida, in an exercise book", "form": "begun", "evidence": "Tagore to Indira Devi, 6 May 1913; Radice 2011", "confidence": "approx"},
 {"date_iso": "1912-06", "date_display": "June 1912", "eye": "rothenstein", "claim": "Receives the notebook of 83 translations (now Houghton Library) and circulates typed copies to Yeats, Bradley and Stopford Brooke", "form": "other", "evidence": "Radice 2011; English Heritage", "confidence": "approx"},
 {"date_iso": "1912-07-07", "date_display": "7 July 1912", "eye": "yeats", "claim": "Reads the translations aloud at Rothenstein's Hampstead house (one source gives 30 June)", "form": "performed", "evidence": "Andrews, Modern Review Aug 1912; English Heritage; RED 3457", "confidence": "verified"},
 {"date_iso": "1912-08-02", "date_display": "2 August 1912", "eye": "tagore", "claim": "Reports that the India Society will publish, with an introduction by Yeats", "form": "commissioned", "evidence": "Tagore to Ajit Kumar Chakravarty (Bengali)", "confidence": "approx"},
 {"date_iso": "1912-09", "date_display": "September 1912", "eye": "yeats", "claim": "Completes the introduction in Normandy. How heavily he edited Tagore's text is contested: Radice argues for substantial changes to selection, order and wording", "form": "completed", "evidence": "Introduction dated Sept 1912; Yeats to Rothenstein 7 Sept 1912; Radice 2011", "confidence": "approx"},
 {"date_iso": "1912-09-09", "date_display": "9 September 1912 (24 Bhadra 1319)", "eye": "tagore", "claim": "Manuscript sent to the Chiswick Press; Tagore reads proofs with Yeats", "form": "other", "evidence": "Bengali chronology via sesquicentennial blog", "confidence": "approx"},
 {"date_iso": "1912-11-01", "date_display": "1 November 1912 (16 Kartik 1319)", "eye": "rothenstein", "claim": "India Society edition of Gitanjali (Song Offerings) published, 750 copies (250 for sale), Rothenstein frontispiece", "form": "published", "evidence": "Sesquicentennial blog; Saffronart lot notes; Open University", "confidence": "approx"},
 {"date_iso": "1912-12", "date_display": "December 1912", "eye": "pound", "claim": "Six Gitanjali poems and Pound's note printed in Poetry 1:3, Tagore's first American publication", "form": "published", "evidence": "Poetry Foundation issue page", "confidence": "verified"},
 {"date_iso": "1913-01-09", "date_display": "9 January 1913", "eye": "yeats", "claim": "Protests an unauthorised change to poem 52 and asks for the original sentence to be restored", "form": "other", "evidence": "Yeats letter, cited in sesquicentennial blog", "confidence": "approx"},
 {"date_iso": "1913-01", "date_display": "By 1 February 1913 (the nomination deadline)", "eye": "sturgemoore", "claim": "Nominates Tagore for the Nobel Prize, the only nomination he receives in 1913", "form": "other", "evidence": "Nobel nomination archive, as reported in Wikipedia and The Daily Star", "confidence": "approx"},
 {"date_iso": "1913-03", "date_display": "March 1913", "eye": "pound", "claim": "Essay 'Rabindranath Tagore' in the Fortnightly Review, comparing him to Dante", "form": "reviewed", "evidence": "Hurwitz 1964", "confidence": "approx"},
 {"date_iso": "1913-03", "date_display": "March 1913", "eye": "yeats", "claim": "Macmillan trade edition published with Yeats's introduction; many reprints follow", "form": "published", "evidence": "Radice 2011; Caravan 2022", "confidence": "verified"},
 {"date_iso": "1913-10-18", "date_display": "18 October 1913", "eye": "heidenstam", "claim": "Writes to the Academy urging the prize for Tagore", "form": "other", "evidence": "Nobel archive, via Frontier (2012)", "confidence": "approx"},
 {"date_iso": "1913-10-24", "date_display": "24 October 1913", "eye": "academy", "claim": "Nobel Committee still favours Émile Faguet", "form": "decided", "evidence": "Frontier (2012); Österling via sesquicentennial blog", "confidence": "approx"},
 {"date_iso": "1913-11-13", "date_display": "13 November 1913", "eye": "academy", "claim": "Academy in plenary session awards the 1913 prize to Tagore (12 of 13 voting, per Ahlström)", "form": "decided", "evidence": "Ahlström; Nobel Foundation", "confidence": "verified"},
 {"date_iso": "1913-12-10", "date_display": "10 December 1913", "eye": "academy", "claim": "Prize presented in absentia; Tagore's telegram read at the banquet", "form": "other", "evidence": "Nobel Foundation ceremony speech and banquet record", "confidence": "verified"}
]

convergences = [
 {"date": "1912-07-07", "label": "The Hampstead reading", "eyes": ["rothenstein", "yeats", "tagore", "andrews", "pound", "rathindranath", "sinclair", "sturgemoore"],
  "note": "Eight of the chapter's eyes were in one drawing room. Rothenstein saw a triumph for his protégé, Yeats a confirmation of his ideas about an undivided ancient culture, Andrews the landscape of Bengal, and Pound a scoop for Chicago. Rathindranath remembered only the silence. Tagore listened to his own poems read in another poet's voice."},
 {"date": "1912-11", "label": "The book appears while its author is in Illinois", "eyes": ["rothenstein", "yeats", "tagore", "rathindranath"],
  "note": "The India Society edition came out on 1 November in London. Its author was in Urbana preparing lectures on the Upanishads for a Unitarian congregation, and his son was back in the classrooms of his old university."},
 {"date": "1912-12", "label": "One issue of Poetry", "eyes": ["pound", "monroe", "yeats", "tagore"],
  "note": "The December Poetry carried Yeats's new poems and Tagore's translations in the same pages, with Pound's note as the link. Monroe printed it in Chicago while Tagore was a short train ride away in Urbana."},
 {"date": "1913-05", "label": "Spring 1913: the book judged at both ends", "eyes": ["tagore", "hallstrom", "pound"],
  "note": "In the same month Tagore wrote privately in Bengali about what the translations meant to him, and Stockholm was asking London for press cuttings so that it could assess him. Meanwhile Pound had begun to sneer in his private letters."},
 {"date": "1913-10", "label": "Stockholm divides", "eyes": ["heidenstam", "hallstrom", "academy"],
  "note": "The committee chairman doubted that the poems were Tagore's own, and his committee preferred a French critic. Hallström's report and Heidenstam's letter of 18 October pushed the other way. Hardly anyone in the room could read the original language."},
 {"date": "1913-11-13", "label": "The vote, and an ordinary morning in Bengal", "eyes": ["academy", "thompson", "tagore", "press"],
  "note": "While the Academy voted in Stockholm, Tagore and Thompson sat under the trees at Santiniketan adjusting the rhythm of new English translations. In New York the Evening Post was already noting that the prize had gone to someone who was not white."},
 {"date": "1913-11-14", "label": "The news reaches Santiniketan", "eyes": ["tagore", "thompson", "press"],
  "note": "Tagore remembered a telegram he nearly did not open, and Thompson remembered a tea he left halfway through. The London papers that morning were weighing the choice against Hardy. The conflicting dates (13–16 November) come from three different telegrams."},
 {"date": "1913-12", "label": "December 1913: a ceremony without the poet", "eyes": ["academy", "tagore", "monroe"],
  "note": "In Stockholm a diplomat read Tagore's one-sentence thanks while Poetry printed five more of his poems in Chicago. At Santiniketan Tagore was still trying to get back the quiet he had lost."}
]

ties = [
 {"a": "tagore", "b": "rathindranath", "kind": "relative", "note": "Father and son travelled together in 1912–13. Rathindranath's later memoir is the source of the lost-manuscript story."},
 {"a": "rothenstein", "b": "tagore", "kind": "met", "note": "They met in Calcutta in 1910–11. Rothenstein found Tagore's London lodgings, hosted the reading, and drew the portrait used as the frontispiece. Their letters of 1911–1914 were edited as Imperfect Encounter."},
 {"a": "rothenstein", "b": "yeats", "kind": "influenced", "note": "Rothenstein sent Yeats the typed translations, and Yeats wrote to him from Normandy about the introduction."},
 {"a": "yeats", "b": "tagore", "kind": "read each other", "note": "Yeats edited the translations, read them aloud and wrote the introduction. He argued with the India Society over single sentences of Tagore's text."},
 {"a": "pound", "b": "yeats", "kind": "met", "note": "Pound was Yeats's friend and, from the winter of 1913–14, his secretary at Stone Cottage. Both men's poems appeared in the December 1912 Poetry."},
 {"a": "pound", "b": "monroe", "kind": "influenced", "note": "As Poetry's foreign correspondent Pound sent Monroe the six Tagore poems that she printed in December 1912."},
 {"a": "andrews", "b": "tagore", "kind": "met", "note": "They met for the first time at the reading on 7 July 1912. Andrews went to live at Santiniketan in 1914."},
 {"a": "sinclair", "b": "tagore", "kind": "mentioned", "note": "Sinclair wrote to Tagore the morning after hearing his poems."},
 {"a": "sturgemoore", "b": "academy", "kind": "influenced", "note": "Sturge Moore's was the only nomination of Tagore in 1913. The Academy chose him over the 97 Fellows of the same Royal Society of Literature who had backed Hardy."},
 {"a": "sturgemoore", "b": "yeats", "kind": "met", "note": "Sturge Moore was a close friend of Yeats and designed covers for his books. Their correspondence was later published."},
 {"a": "hallstrom", "b": "heidenstam", "kind": "met", "note": "Both were members of the Swedish Academy and argued on the same side, against their committee's preference for Faguet."},
 {"a": "thompson", "b": "tagore", "kind": "met", "note": "Thompson revised translations with Tagore on 13 November 1913 and later wrote two books about him. Tagore wrote to him about the welcome he received on returning home in 1913."},
 {"a": "press", "b": "academy", "kind": "opposite sides", "note": "Some papers welcomed the Academy's decision, while others, such as the Los Angeles Times, attacked it in racial terms."}
]

threads_out = [
 {"to": "v1:ww1", "note": "Wilfred Owen carried Tagore's poems at the front. After his death in November 1918 his mother Susan Owen wrote to Tagore in 1920 that the words of Gitanjali's farewell poem, beginning 'When I go from hence', were in her son's pocket book in his handwriting."},
 {"to": "v2:partition-1947", "note": "Tagore wrote 'Amar Shonar Bangla' in 1905 during the protests against the first partition of Bengal, and composed 'Jana Gana Mana' in 1911. After the partition of 1947, the second became India's national anthem and the first, in 1972, Bangladesh's."},
 {"to": "bauhaus", "note": "In December 1922 works by Bauhaus artists, including Klee and Kandinsky, were shown in Calcutta beside paintings by Tagore's nephews Gaganendranath and Abanindranath at the Indian Society of Oriental Art. The link is usually traced to Tagore's visit to Germany in 1921 and to the art historian Stella Kramrisch, who was then teaching at Santiniketan."},
 {"to": "harlem", "note": "W. E. B. Du Bois, who read Tagore's work, asked him for a message to Black Americans, and The Crisis printed Tagore's reply in 1929. In 1913 the New York press had noted that the prize was the first to go to someone who was not white."}
]

images = [
 {"url": U["eh"], "title": "Blue plaque, 3 Villas on the Heath, Hampstead", "caption": "The London County Council plaque (1961) on the Vale of Health house where Tagore lodged in the summer of 1912, a short walk from Rothenstein's house in Oak Hill Park, where the reading took place.", "date": "plaque 1961; stay 1912", "credit": "English Heritage"},
 {"url": U["saffron"], "title": "Gitanjali (Song Offerings), India Society, 1912", "caption": "A copy of the first edition, one of 750 printed at the Chiswick Press in cream silk with red initials, with Rothenstein's portrait of Tagore as a photogravure frontispiece. Shown in an auction listing, not a museum.", "date": "November 1912", "credit": "Saffronart, Passages to India sale, July 2024"},
 {"url": U["poetry1912"], "title": "Poetry: A Magazine of Verse, December 1912", "caption": "The contents page of the issue in which Tagore's six poems and Pound's note first appeared in America, alongside new poems by Yeats.", "date": "December 1912", "credit": "Poetry Foundation"},
 {"url": U["illinois"], "title": "Tagore in Urbana, 1912–13", "caption": "University of Illinois Archives feature on Tagore's months in Urbana: the Unitarian church lectures, the Cosmopolitan Club reception and Rathindranath's graduate study.", "date": "1912–1913", "credit": "University of Illinois Archives, Student Life and Culture Archives"},
 {"url": U["hathi"], "title": "Gitanjali (song offerings), digitised", "caption": "A library scan of the English Gitanjali with Yeats's introduction, so the 1912–13 text and its prefatory matter can be read in full.", "date": "1912–1913", "credit": "HathiTrust Digital Library"}
]

further = [
 {"title": "William Radice, 'The universal is personal' (Seminar, 2011), on the Rothenstein manuscript", "url": U["radice"]},
 {"title": "Harold M. Hurwitz, 'Ezra Pound and Rabindranath Tagore' (1964)", "url": U["hurwitz"]},
 {"title": "Dipesh Chakrabarty, 'Friendships in the Shadow of Empire: Tagore's Reception in Chicago' (2014)", "url": U["chakrabarty"]},
 {"title": "E. P. Thompson, 'Memories of Tagore' (London Review of Books, 1986)", "url": U["lrb"]},
 {"title": "Open University, Making Britain: Rabindranath Tagore", "url": U["ou"]},
 {"title": "Nobel Prize: 1913 award ceremony speech", "url": U["nobelspeech"]},
 {"title": "University of Illinois Archives: Tagore in Urbana", "url": U["illinois"]}
]

intro = [
 "In the spring of 1912 Rabindranath Tagore was fifty-one, the most famous poet in Bengal and almost unknown outside it. Illness had stopped him sailing for England in March. While he recovered on the family estate at Shilaida, on the Padma, he began writing out English prose versions of songs from his Bengali Gitanjali (1910) and other recent books in an exercise book. He did not, by his own account, expect much to come of it. Eighteen months later the Swedish Academy gave him the Nobel Prize in Literature, the first time it had gone to a writer from outside Europe.",
 "This chapter follows the book between those two points: a notebook nearly lost on the London Underground, a painter's drawing room in Hampstead where Yeats read the poems aloud on 7 July 1912, a limited edition of 750 copies in cream silk, six poems in a three-month-old Chicago magazine, lectures to a Unitarian congregation in Urbana, Illinois, a trade edition from Macmillan, and a committee in Stockholm that could not read the original language and did not want to give him the prize. The full Academy overruled the committee on 13 November 1913. The next afternoon, at his school at Santiniketan, Tagore put a telegram in his pocket and did not open it.",
 "The record is mostly letters, published articles, committee papers and memoirs written later, with very few diaries. The most immediate eyewitness accounts are C. F. Andrews's report of the Hampstead evening, printed in Calcutta a month later, and Edward Thompson's account of the two days at Santiniketan, written on 17 November 1913. Rothenstein's Men and Memories (1932) and Rathindranath Tagore's On the Edges of Time (1958) supply much of the familiar story but were written decades afterwards, and they are flagged. Tagore's Bengali letters are paraphrased. English texts printed before 1929, such as Yeats's introduction, Pound's notes and the newspapers, supply the few short quotations.",
 "Laid side by side, these eyes show how a book was made by more than one person. Tagore translated, Rothenstein circulated, Yeats selected, reordered and introduced, and the India Society's officers changed words that both poets then fought over. Whether the English Gitanjali is Tagore's book, Yeats's or both is still argued, and the chapter reports the positions. The same pages show the reception moving outward, from the drawing room to Calcutta, Chicago, Stockholm and finally the press, which mixed delight with open racial contempt.",
 "The chapter ends with a deputation from Calcutta. A trainload of notables came to Santiniketan to congratulate the poet whose Bengali work many of them had disparaged, and Tagore told them he could not accept their praise. Five days earlier he had written to Rothenstein that fame had been tied to him like a tin can to a dog's tail."
]

chapter = {
 "id": "gitanjali-1912",
 "title": "The Gitanjali Year: Calcutta, London, Stockholm, 1912–1913",
 "short_title": "The Gitanjali Year",
 "subtitle": "Tagore's English Gitanjali from the Padma to the Nobel Prize, 1912–1913",
 "span": "1912–1913",
 "intro": intro,
 "calendar_note": "All dates are Gregorian. Two dates for the printing of Gitanjali come from Bengali chronologies and are given in the Bengali calendar as well: 24 Bhadra 1319 BS (Monday 9 September 1912) and 16 Kartik 1319 BS (Friday 1 November 1912). Sources give anything from 13 to 16 November 1913 for the day Tagore heard of the prize. The dates belong to different messages: the Academy's decision and Reuters' report (13 November), a congratulatory wire from Calcutta friends that reached Bolpur on the afternoon of 14 November, and the Academy's own cable through Macmillan, received in Calcutta on the 15th and wired on to Santiniketan on the 16th.",
 "eyes": eyes,
 "entries": sorted(E, key=lambda x: x["date_iso"]),
 "claims": claims,
 "convergences": convergences,
 "ties": ties,
 "threads_out": threads_out,
 "images": images,
 "further": further,
 "vantage_key": "0 = the poet and the book's makers (Tagore, Rothenstein, Yeats); 1 = in the room, at the Hampstead reading or at Santiniketan; 2 = editors and advocates who carried the poems into print or to Stockholm; 3 = the Swedish judges, reading in translation; 4 = newspapers, news only."
}

json.dump(chapter, open(OUT, "w"), ensure_ascii=False, indent=1)
print(len(eyes), len(E), len(claims), len(convergences), len(ties), len(threads_out), len(images), len(further))
ids = {x["id"] for x in eyes}
for x in E:
    assert x["eye"] in ids, x
    if x["quote"]:
        assert len(x["quote"].split()) <= 12, x["quote"]
for c in convergences:
    for i in c["eyes"]: assert i in ids, i
for t in ties: assert t["a"] in ids and t["b"] in ids
for c in claims: assert c["eye"] in ids
for x in eyes: assert len(x["short"]) <= 16, x["short"]
