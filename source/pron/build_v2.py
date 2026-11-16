import json, sys
K = {'P': 'person', 'L': 'place', 'T': 'term'}
C = {'s': 'sure', 'c': 'check'}
RAW = r"""
@merer
Merer|MEH-rer|P|Egyptian|c|Egyptological convention; vowels not written
Ankhhaf|AHNK-hahf|P|Egyptian|c|Egyptological convention
Dedi|DED-ee|P|Egyptian|c|Egyptological convention
sehedj|seh-HEJ|T|Egyptian|c|title 'inspector'; Egyptological convention
Khufu|KOO-foo|P|Egyptian|s|Egyptological convention
Akhet-Khufu|AH-khet KOO-foo|L|Egyptian|c|'Horizon of Khufu'
Ro-She Khufu|roh-SHAY KOO-foo|L|Egyptian|c|
Tura|TOO-rə|L|Arabic|s|
Giza|GEE-zə|L|Arabic|s|established English
Wadi al-Jarf|WAH-dee al-JARF|L|Arabic|s|
Zafarana|zah-fah-RAH-nə|L|Arabic|s|
Heliopolis|hee-lee-OP-ə-lis|L|Greek|s|established English
Suez|SOO-iz|L|Arabic|s|established English
Pierre Tallet|pyair ta-LAY|P|French|s|
Gregory Marouard|ma-roo-AR|P|French|c|
Sayed Mahfouz|SAY-yed mah-FOOZ|P|Arabic|s|
papyri|pə-PEYE-reye|T|Latin|s|
nome|NOHM|T|Greek|s|Egyptian province
@babylon-331
Esagila|e-sah-GEE-lə|L|Akkadian|c|
Marduk|MAR-dook|P|Akkadian|s|
Akkadian|ə-KAY-dee-ən|T|English|s|
Callisthenes of Olynthus|kə-LIS-thə-neez əv oh-LIN-thəs|P|Greek|s|English-Latin convention
Aristobulus of Cassandreia|a-ri-STOB-yuu-ləs əv ka-san-DREE-ə|P|Greek|c|
Lucius Flavius Arrianus (Arrian of Nicomedia)|LOO-shəs FLAY-vee-əs a-ree-AY-nəs|P|Latin|s|
Arrian|AR-ee-ən|P|Latin|s|
Nicomedia|nik-ə-MEE-dee-ə|L|Greek|s|
Plutarch of Chaeronea|PLOO-tark əv kair-ə-NEE-ə|P|Greek|s|
Quintus Curtius Rufus|KWIN-təs KUR-shee-əs ROO-fəs|P|Latin|s|
Diodorus Siculus|deye-ə-DOR-əs SIK-yuu-ləs|P|Latin|s|
Ephemerides|ef-ə-MER-i-deez|T|Greek|s|
Gaugamela|gaw-gə-MEE-lə|L|Greek|s|
Arbela|ar-BEE-lə|L|Greek|s|
Persepolis|pər-SEP-ə-lis|L|Greek|s|
Pasargadae|pə-SAR-gə-dee|L|Greek|s|
Sippar|SIP-ar|L|Akkadian|s|
Sikilla|si-KIL-ə|L|Akkadian|c|
Boeotia|bee-OH-shə|L|Greek|s|
Agyrium|ə-JIR-ee-əm|L|Latin|c|
@vesuvius-79
Gaius Plinius Caecilius Secundus|GEYE-əs PLIN-ee-əs see-SIL-ee-əs si-KUN-dəs|P|Latin|s|English-Latin convention
Pliny|PLIN-ee|P|Latin|s|
Lucius Caecilius Iucundus|LOO-shəs see-SIL-ee-əs yoo-KUN-dəs|P|Latin|s|
Sulpicii|sul-PISH-ee-eye|P|Latin|s|
Murecine|moo-reh-CHEE-neh|L|Italian|c|
Petronia Iusta|pi-TROH-nee-ə YUS-tə|P|Latin|s|
programmata|proh-GRAM-ə-tə|T|Latin|s|
Lucius Annaeus Seneca|LOO-shəs ə-NEE-əs SEN-i-kə|P|Latin|s|
Lucius Cassius Dio|LOO-shəs KAS-ee-əs DEE-oh|P|Latin|s|
Gaius Suetonius Tranquillus|GEYE-əs swi-TOH-nee-əs tran-KWIL-əs|P|Latin|s|
Philodemus|fil-ə-DEE-məs|P|Greek|s|
Puteoli|pyoo-TEE-ə-leye|L|Latin|s|
Herculaneum|hur-kyuu-LAY-nee-əm|L|Latin|s|
Misenum|meye-SEE-nəm|L|Latin|s|
Stabiae|STAY-bee-ee|L|Latin|s|
Pomponianus|pom-poh-nee-AY-nəs|P|Latin|s|
Via dell'Abbondanza|VEE-ah del-ab-bon-DAHN-tsah|L|Italian|s|
Vesuvius|vi-SOO-vee-əs|L|Latin|s|established English
aediles|EE-deyelz|T|Latin|s|
Tacitus|TAS-i-təs|P|Latin|s|
@black-death
John VI Kantakouzenos|kan-tə-koo-ZEE-nos|P|Greek|s|
Gabriele de' Mussi|gah-bree-EH-leh deh MOOS-see|P|Italian|s|
Louis Heyligen|HAY-lee-khən|P|Dutch|c|Flemish
Guy de Chauliac|GEE də shoh-LYAK|P|French|s|
Francesco Petrarca|fran-CHES-koh peh-TRAR-kah|P|Italian|s|
Petrarch|PET-rark|P|English|s|established English
Giovanni Boccaccio|joh-VAH-nee boh-KAH-choh|P|Italian|s|
Agnolo di Tura del Grasso|AHN-yoh-loh dee TOO-rah del GRAHS-soh|P|Italian|s|
Fritsche (Friedrich) Closener|FRIT-shə KLOH-zə-nər|P|German|c|
Zayn al-Din 'Umar ibn al-Wardi|ZAYN ad-DEEN OO-mar ib-nul-WAR-dee|P|Arabic|s|
Ibn Battuta|IB-ən ba-TOO-tə|P|Arabic|s|
al-Maqrizi|al-mak-REE-zee|P|Arabic|s|
Ibn Khatima|IB-ən KHAH-ti-mə|P|Arabic|c|
'Abd al-Rahman ibn Khaldun|AB-dur-rəkh-MAHN IB-ən khal-DOON|P|Arabic|s|
Avignon|a-veen-YON(H)|L|French|s|
Piacenza|pyah-CHEN-tsah|L|Italian|s|
Leicester|LES-tər|L|English|s|commonly mis-said
Drogheda|DROY-hə-də|L|English|s|Irish town; commonly mis-said
Qal'at ibn Salama|KAL-at ib-ən sə-LAH-mə|L|Arabic|c|
Yersinia pestis|yər-SIN-ee-ə PES-tis|T|Latin|s|
@constantinople-1453
Nicolò Barbaro|nee-koh-LOH BAR-bah-roh|P|Italian|s|
Leonard of Chios|KEYE-os|P|Greek|s|English for Chios
Leonardo Giustiniani|joo-stee-NYAH-nee|P|Italian|s|
Giacomo (Jacopo) Tetaldi|JAH-koh-moh teh-TAHL-dee|P|Italian|s|
Ubertino Pusculo|oo-ber-TEE-noh POOS-koo-loh|P|Italian|c|
George Sphrantzes|SFRAN-tseez|P|Greek|c|Greek SFRAN-dzis
Michael Kritoboulos of Imbros|kri-TOB-uu-ləs əv IM-bros|P|Greek|c|
Tursun Beg|toor-SOON BEG|P|Turkish|s|
Konstantin Mihailović of Ostrovica|kon-stan-TEEN mi-HEYE-lo-vich əv OS-tro-vi-tsah|P|Serbian|c|
Nestor Iskander|NES-tor is-kahn-DYER|P|Russian|c|
Doukas|DOO-kəs|P|Greek|s|
Mehmed|MEH-med|P|Turkish|s|
Palaiologos|pa-lay-OL-ə-gəs|P|Greek|s|English convention
Blachernae|blə-KUR-nee|L|Greek|s|
Kaligaria|ka-lee-GAH-ree-ə|L|Greek|c|
Hagia Sophia|HAH-yə soh-FEE-ə|L|Greek|s|
Galata|GAL-ə-tə|L|Turkish|s|
Mistra|MIS-trə|L|Greek|s|
Brescia|BRESH-ə|L|Italian|s|
Genoese|jen-oh-EEZ|T|English|s|
@first-contact
Cristoforo Colombo|krees-TOH-foh-roh koh-LOHM-boh|P|Italian|s|
Cristóbal Colón|krees-TOH-bahl koh-LOHN|P|Spanish|s|
Diego Álvarez Chanca|DYAY-goh AHL-vah-reth CHAHN-kah|P|Spanish|s|Castilian 'z' as th
Peter Martyr d'Anghiera|dahn-GYEH-rah|P|Italian|s|
Fray Ramón Pané|FREYE rah-MOHN pah-NAY|P|Spanish|s|
Amerigo Vespucci|ah-meh-REE-goh ves-POO-chee|P|Italian|s|
Hernán Cortés|er-NAHN kor-TES|P|Spanish|s|
Bernal Díaz del Castillo|ber-NAHL DEE-ahth del kahs-TEE-lyoh|P|Spanish|s|
Bernardino de Sahagún|ber-nar-DEE-noh deh sah-ah-GOON|P|Spanish|s|
Albrecht Dürer|AHL-brekht DYOOR-ər|P|German|s|ü approximated
Antonio Pigafetta|pee-gah-FET-tah|P|Italian|s|
Nahua|NAH-wah|T|Nahuatl|s|
Nahuatl|NAH-waht-əl|T|Nahuatl|s|
Tlatelolco|tlah-teh-LOHL-koh|L|Nahuatl|s|
Tenochtitlan|teh-noch-TEET-lahn|L|Nahuatl|s|
Moctezuma|mok-teh-SOO-mah|P|Nahuatl|s|Spanish-mediated
Toxcatl|TOHSH-kaht-əl|T|Nahuatl|s|
Taíno|teye-EE-noh|T|Spanish|s|
Coyoacán|koh-yoh-ah-KAHN|L|Nahuatl|s|
Mactan|mahk-TAHN|L|Cebuano|s|
@imjin-war
Yi Sun-sin|EE soon-sin|P|Korean|s|
Oh Hui-mun|OH hee-moon|P|Korean|c|
Ryu Seong-ryong|RYOO sung-nyong|P|Korean|s|
Toyotomi Hideyoshi|toh-yoh-toh-mee hee-deh-YOH-shee|P|Japanese|s|
Keinen|KAY-nen|P|Japanese|s|
Ōkōchi Hidemoto|OH-koh-chee hee-deh-moh-toh|P|Japanese|s|long vowels
Kang Hang|KAHNG HAHNG|P|Korean|s|
Gregorio de Céspedes|greh-GOH-ryoh deh THES-peh-dehs|P|Spanish|s|
Song Yingchang|sung ying-chahng|P|Mandarin|s|
Nanjung Ilgi|NAHN-joong IL-gee|T|Korean|s|
Swaemirok|SWEH-mee-rok|T|Korean|s|
Jingbirok|JING-bee-rok|T|Korean|s|
Seonjo|SUN-joh|P|Korean|s|
Jeolla|JUL-lah|L|Korean|s|
Namwon|NAHM-wun|L|Korean|s|
Myeongnyang|MYUNG-nyahng|L|Korean|s|
Gyeongsang|GYUNG-sahng|L|Korean|s|
Noryang|NOH-ryahng|L|Korean|s|
Hahoe|HAH-hweh|L|Korean|s|
Mimizuka|mee-mee-ZOO-kah|L|Japanese|s|
@ming-qing
Qi Biaojia (祁彪佳)|chee byow-jyah|P|Mandarin|s|
Wang Xiuchu (王秀楚)|wahng shyoh-choo|P|Mandarin|s|
Shi Kefa (史可法)|shur kuh-fah|P|Mandarin|s|
Dorgon|DOR-gon|P|Manchu|s|
Crown Prince Sohyeon (昭顯世子)|SOH-hyun|P|Korean|s|
Johann Adam Schall von Bell|YOH-hahn AH-dahm SHAHL fon BEL|P|German|s|
Martino Martini|mar-TEE-noh mar-TEE-nee|P|Italian|s|
Zhang Dai (張岱)|jahng deye|P|Mandarin|s|
Hayashi Gahō (林鵞峰, also Shunsai)|hah-YAH-shee GAH-hoh|P|Japanese|s|
Li Zicheng|lee dzuh-chung|P|Mandarin|s|
Wu Sangui|woo sahn-gway|P|Mandarin|s|
Qing|ching|T|Mandarin|s|
Yangzhou|yahng-joh|L|Mandarin|s|
Shaoxing|show-shing|L|Mandarin|s|
Shanhai Pass|shahn-heye|L|Mandarin|s|
Mukden|MUUK-dən|L|Manchu|s|
Shenyang|shun-yahng|L|Mandarin|s|
Jiangnan|jyahng-nahn|L|Mandarin|s|
Jiangyin|jyahng-yin|L|Mandarin|s|
Quekou Gate|chweh-koh|L|Mandarin|c|
@vienna-1683
teşrifatçı|tesh-ree-faht-CHUH|T|Turkish|s|master of ceremonies
Silahdar Fındıklılı Mehmed Ağa|see-lah-DAHR fuhn-duhk-luh-LUH meh-MET AH-ah|P|Turkish|s|ğ silent, lengthens vowel
Kara Mustafa Pasha|kah-RAH moos-tah-FAH pah-SHAH|P|Turkish|s|
Johann Peter von Vaelckeren|fon FEL-kə-rən|P|German|c|
Ernst Rüdiger von Starhemberg|ernst RUE-di-gər fon SHTAR-əm-berk|P|German|s|'ue' = German ü
Georg Franz Kolschitzky|GAY-ork frahnts kol-SHIT-skee|P|German|s|
Jerzy Franciszek Kulczycki|YEH-zhi fran-CHEE-shek kool-CHITS-kee|P|Polish|s|
Jan III Sobieski|YAHN so-BYES-kee|P|Polish|s|
Jakub Ludwik Sobieski|YAH-koob LOOD-veek so-BYES-kee|P|Polish|s|
Marco d'Aviano|MAR-koh dah-VYAH-noh|P|Italian|s|
Francis Taaffe|TAF|P|English|s|Irish surname
Mikołaj Dyakowski|mee-KOH-weye dyah-KOF-skee|P|Polish|s|
Löbel|LUR-bəl|L|German|s|
Kahlenberg|KAH-lən-berk|L|German|s|
Kraków|KRAH-koof|L|Polish|s|English often KRAK-ow
Heiligenstadt|HEYE-li-gən-shtaht|L|German|s|
Pötzleinsdorf|PURTS-leyens-dorf|L|German|s|
Thököly|TUR-kur-lee|P|Hungarian|s|
Kuruc|KOO-roots|T|Hungarian|s|
Evliya Çelebi|ev-lee-YAH cheh-leh-BEE|P|Turkish|s|
@lisbon-1755
Sebastião José de Carvalho e Melo|sə-bahsh-tee-OWN(H) zhoo-ZEH də kər-VAH-lyoo ee MEH-loo|P|Portuguese|s|European Portuguese
Pombal|pohm-BAHL|L|Portuguese|s|
Manuel da Maia|mə-NWEL də MEYE-ə|P|Portuguese|s|
Sir James Colquhoun of Luss|kə-HOON əv LUS|P|English|s|Scottish; commonly mis-said
Rev. William Borlase|BOR-ləs|P|English|c|Cornish surname
Reimarus|reye-MAH-ruus|P|German|s|
Voltaire (François-Marie Arouet)|vol-TAIR (fran(h)-SWAH ma-REE a-RWAY)|P|French|s|English for Voltaire
Königsberg|KUR-nikhs-berk|L|German|s|
Funchal|foon-SHAHL|L|Portuguese|s|
Cádiz|kə-DIZ|L|Spanish|s|Spanish KAH-deeth
Belém|bə-LAYN(H)|L|Portuguese|s|
Les Délices|lay day-LEES|L|French|s|
Rossdhu|ros-DOO|L|Scottish Gaelic|c|
Tetuan|tet-WAHN|L|Arabic|s|
Arzila|ar-ZEE-lə|L|Arabic|s|
Salé|sa-LAY|L|Arabic|s|
Meknes|mek-NES|L|Arabic|s|
Ludgvan|LUJ-ən|L|Cornish|c|
Tagus|TAY-gəs|L|English|s|
História da ruína da cidade de Lisboa|ish-TOR-yə də roo-EE-nə də see-DAHD də leezh-BOH-ə|T|Portuguese|s|
@tambora-1816
Benares|bə-NAR-iz|T|English|s|ship named for Varanasi
The Raja of Sanggar|RAH-jə əv SAHNG-gar|P|Malay|s|
Tambora|tam-BOR-ə|L|Indonesian|s|
Sumbawa|soom-BAH-wə|L|Indonesian|s|
John William Polidori|pol-i-DOR-ee|P|Italian|s|English usage
David Friedrich Lederer|LAY-də-rər|P|German|s|
Li Yuyang|lee yoo-yahng|P|Mandarin|c|
Monticello|mon-ti-CHEL-oh|L|English|s|
Villa Diodati|dee-oh-DAH-tee|L|Italian|s|
Geradstetten|gə-RAHT-shtet-ən|L|German|s|
Württemberg|VUER-təm-berk|L|German|s|'ue' = German ü
Yunnan|yoo-NAN|L|Mandarin|s|English approximation
Makassar|mə-KAS-ər|L|Indonesian|s|
Sulawesi|soo-lə-WAY-see|L|Indonesian|s|
Sumenep|soo-MEH-nep|L|Indonesian|s|
Bima|BEE-mə|L|Indonesian|s|
Sécheron|saysh-RON(H)|L|French|s|
Maison Chapuis|may-ZON(H) sha-PWEE|L|French|s|
Cologny|ko-lo-NYEE|L|French|s|
Mary Wollstonecraft Godwin|WUUL-stən-kraft|P|English|s|
@opium-war
Lin Zexu|lin dzuh-shyoo|P|Mandarin|s|
Daoguang Emperor|dow-gwahng|P|Mandarin|s|
Minning|min-ning|P|Mandarin|s|
Robert Jocelyn, Viscount Jocelyn|JOS-lin|P|English|s|
John Ouchterlony|ookh-tər-LOH-nee|P|English|c|Scottish surname
Zhu Shiyun|joo shur-yoon|P|Mandarin|s|
Yang Qi|yahng chee|P|Mandarin|s|
Granville Gower Loch|GOR LOKH|P|English|c|Gower as in Leveson-Gower
Qing|ching|T|Mandarin|s|
Chusan|choo-SAN|L|Mandarin|s|historic spelling of Zhoushan
Zhenjiang|jun-jyahng|L|Mandarin|s|
Humen|hoo-mun|L|Mandarin|s|
Macao|mə-KOW|L|English|s|
Dinghai|ding-heye|L|Mandarin|s|
Chuanbi|chwahn-bee|L|Mandarin|s|
Kowloon|kow-LOON|L|Cantonese|s|established English
Whampoa|wom-POH-ə|L|Cantonese|s|established English
Sanyuanli|sahn-ywen-lee|L|Mandarin|s|
Ili|EE-lee|L|Mandarin|s|
Nanking|nan-KING|L|English|s|old spelling of Nanjing
@irish-famine
Elizabeth Smith (née Grant of Rothiemurchus)|roth-ee-MUR-kəs|P|Scottish Gaelic|s|
Father Theobald Mathew|THEE-ə-bawld MATH-yoo|P|English|s|
Charles Edward Trevelyan|tri-VEL-yən|P|English|s|
Asenath Hatch Nicholson|AS-ə-nath|P|English|s|
James Mahony|MAH-hə-nee|P|Irish|c|
James Hack Tuke|TYOOK|P|English|s|
An Gorta Mór|ən GOR-tə MOHR|T|Irish|s|
Amhlaoibh Ó Súilleabháin|OW-leev oh SOOL-ə-vawn|P|Irish|s|
Callan|KAL-ən|L|English|s|
Baltiboys|bawl-tee-BOYZ|L|English|c|
Grosse Île|grohs EEL|L|French|s|
Belmullet|bel-MUL-it|L|Irish|s|
Erris|ER-is|L|Irish|s|
Kilrush|kil-RUSH|L|Irish|s|
Clonakilty|klon-ə-KIL-tee|L|Irish|s|
Skibbereen|skib-ə-REEN|L|Irish|s|
Moyarta|moy-AR-tə|L|Irish|c|
Connaught|KON-awt|L|English|s|
Choctaw|CHOK-taw|T|English|s|
Drogheda|DROY-hə-də|L|English|s|commonly mis-said
@black-ships
Matthew Calbraith Perry|KAL-brayth|P|English|s|
Peter Bernhard Wilhelm Heine|HEYE-nə|P|German|s|
Edward Yorke McCauley|mə-KAW-lee|P|English|s|
Luo Sen (Lo Sum)|lwaw sun|P|Mandarin|s|
Yoshida Shōin|yoh-shee-dah SHOH-een|P|Japanese|s|
Hibata Ōsuke|hee-bah-tah OHS-keh|P|Japanese|c|
Abe Masahiro|AH-beh mah-sah-hee-roh|P|Japanese|s|not 'Abe' as in Lincoln
Tokugawa Nariaki|toh-koo-GAH-wah nah-ree-AH-kee|P|Japanese|s|
Ii Naosuke|EE-ee nah-OHS-keh|P|Japanese|s|
Kawaji Toshiakira|kah-wah-jee toh-shee-ah-kee-rah|P|Japanese|s|
Ivan Aleksandrovich Goncharov|ee-VAHN ə-lyik-SAHN-drə-vyich gən-chə-ROF|P|Russian|s|
Putyatin|poo-TYAH-tin|P|Russian|s|
kurofune|koo-roh-FOO-neh|T|Japanese|s|
kawaraban|kah-wah-RAH-bahn|T|Japanese|s|
jōkisen|JOH-kee-sen|T|Japanese|s|'steamship'
Uraga|oo-RAH-gah|L|Japanese|s|
Kurihama|koo-ree-HAH-mah|L|Japanese|s|
Shimoda|shee-MOH-dah|L|Japanese|s|
Hakodate|hah-koh-DAH-teh|L|Japanese|s|
Denmachō|den-mah-CHOH|L|Japanese|s|
@delhi-1857
Mirza Asadullah Khan Ghalib|MEER-zah ə-sə-DUL-lah KHAHN GAH-lib|P|Urdu|s|Gh as a throaty g
Ghalib|GAH-lib|P|Urdu|s|
Munshi Jiwan Lal (Jeewan Lal)|MOON-shee JEE-vən LAHL|P|Hindi/Urdu|s|
Mainodin Hassan Khan (Mu'in al-Din Hasan Khan)|meye-noh-DEEN HAH-sən KHAHN|P|Urdu|c|
Syed Zahiruddin Hussain 'Zahir Dehlvi'|SAY-yəd zah-heer-ud-DEEN hu-SAYN ZAH-heer DEH-lə-vee|P|Urdu|s|
Maulvi Muhammad Baqar|MOWL-vee moo-HAM-mad BAH-kər|P|Urdu|s|
Dehli Urdu Akhbar|DEH-lee OOR-doo AKH-bar|T|Urdu|s|
Nanak Chand (Nanukchund)|NAH-nək CHUND|P|Hindi|s|
Vishnubhat Godse|VISH-noo-but GOHD-say|P|Marathi|s|
Bahadur Shah Zafar|bə-HAH-door SHAH ZUF-ər|P|Urdu|s|
Meerut|MEER-ət|L|Hindi|s|
Ballimaran|bul-lee-MAH-run|L|Urdu|s|
Paharganj|pə-HAR-gunj|L|Hindi|s|
kotwali|KOHT-wah-lee|T|Hindi/Urdu|s|police headquarters
Kanpur|KAHN-poor|L|Hindi|s|
Satichaura Ghat|sut-ee-CHOW-rah GAHT|L|Hindi|s|
Humayun's Tomb|hoo-MAH-yoon|L|Persian|s|
Secundra Bagh|si-KUN-drə BAHG|L|Urdu|s|
Jhansi|JAHN-see|L|Hindi|s|
Gali Qasim Jan|GUL-ee KAH-sim JAHN|L|Urdu|s|
@krakatoa-1883
Johanna Beyerinck|yoh-HAH-nah BEYE-ə-rink|P|Dutch|s|
Rogier Diederik Marius Verbeek|roh-KHEER DEE-də-rik MAH-ree-us vər-BAYK|P|Dutch|s|
Johannes Paulus van der Stok|yoh-HAH-nəs POW-lus vahn dər STOK|P|Dutch|s|
Schruit|SKHROWT|P|Dutch|c|Dutch 'ui' approximated
Edvard Munch|ED-vart MUUNK|P|Norwegian|s|
Krakatau|krah-kah-TOW|L|Indonesian|s|
Krakatoa|krak-ə-TOH-ə|L|English|s|established English
Sunda Strait|SUN-də|L|Indonesian|s|
Batavia|bə-TAY-vee-ə|L|Latin|s|
Ketimbang|kə-TIM-bahng|L|Indonesian|s|
Anjer|AHN-yər|L|Dutch|s|
Telok Betong|TEL-ok bə-TONG|L|Indonesian|s|
Lampung Bay|LAHM-poong|L|Indonesian|s|
Buitenzorg|BOWT-ən-zorkh|L|Dutch|s|now Bogor
Rodrigues|roh-DREEG|L|French|s|island's local usage
Kristiania|kris-tee-AH-nee-ə|L|Norwegian|s|
Prinses Marie|PRIN-ses ma-REE|T|Dutch|s|
@spain-1936
Manuel Azaña|mah-NWEL ah-THAH-nyah|P|Spanish|s|
Mikhail Koltsov|mee-khah-EEL kalt-SOF|P|Russian|s|
José Moscardó|hoh-SAY mos-kar-DOH|P|Spanish|s|
Alcázar|al-KAH-thar|L|Spanish|s|
Isidro Gomá y Tomás|ee-SEE-droh goh-MAH ee toh-MAHS|P|Spanish|s|
Wolfram von Richthofen|VOLF-rahm fon RIKHT-hoh-fən|P|German|s|
Carlos Morla Lynch|KAR-los MOR-lah LINCH|P|Spanish|s|Chilean
Galeazzo Ciano|gah-leh-AHT-tsoh CHAH-noh|P|Italian|s|
Saint-Jean-de-Luz|san(h)-zhahn(h)-də-LUEZ|L|French|s|
Burgos|BOOR-gos|L|Spanish|s|
Pamplona|pahm-PLOH-nah|L|Spanish|s|
Lopera|loh-PEH-rah|L|Spanish|s|
Vitoria|bee-TOH-ryah|L|Spanish|s|
Guernica|GWAIR-ni-kə|L|Spanish|s|English usage; Spanish gair-NEE-kah
Poliorama|poh-lyoh-RAH-mah|L|Catalan|s|
La Pobleta|lah poh-BLEH-tah|L|Valencian|s|
Móra d'Ebre|MOH-rə DAY-brə|L|Catalan|s|
Ajuntament|ə-zhoon-tə-MEN|T|Catalan|s|city hall
Gandesa|gən-DEH-zə|L|Catalan|s|
Collonges-sous-Salève|ko-LON(H)ZH soo sa-LEV|L|French|s|
@moscow-1937
Nina Sergeevna Lugovskaya|NEE-nə syir-GAY-yiv-nə loo-gəf-SKAH-yə|P|Russian|s|
Nina Alekseevna Kosterina|NEE-nə ə-lyik-SAY-yiv-nə KOS-tyi-ri-nə|P|Russian|c|
Andrei Stepanovich Arzhilovsky|ahn-DRAY styi-PAH-nə-vyich ar-zhi-LOF-skee|P|Russian|c|
Yulia Iosifovna Sokolova-Piatnitskaya|YOO-lyə ee-OH-si-fəv-nə sə-kə-LOH-və-pyat-NITS-kə-yə|P|Russian|s|
Maria Anisimovna Svanidze|mah-REE-yə ə-ni-SEE-məv-nə svah-NEE-dzeh|P|Georgian/Russian|s|
Alexander Nikolaevich Afinogenov|ni-kə-LAH-yi-vyich ə-fi-nə-GYEH-nəf|P|Russian|s|
Stepan Filippovich Podlubny|styi-PAHN fi-LEE-pə-vyich pəd-LOOB-nee|P|Russian|c|
Lyubov Vasilievna Shaporina|lyoo-BOF vah-SEE-lyiv-nə shə-POH-ri-nə|P|Russian|c|
Georgi Dimitrov|geh-OR-gee di-mi-TROF|P|Bulgarian|s|
Lion Feuchtwanger|LEE-on FOYKHT-vahng-ər|P|German|s|
Fitzroy Maclean|mə-KLAYN|P|English|s|
Tyumen|tyoo-MYEN|L|Russian|s|
Peredelkino|pyi-ryi-DYEL-ki-nə|L|Russian|s|
Zinoviev|zi-NOH-vee-ef|P|Russian|s|
Kamenev|KAH-myi-nyif|P|Russian|s|
Pyatakov|pyə-tah-KOF|P|Russian|s|
Bukharin|boo-KHAH-rin|P|Russian|s|
Rykov|RI-kəf|P|Russian|s|
Yagoda|YAH-gə-də|P|Russian|s|
Tukhachevsky|too-khah-CHEF-skee|P|Russian|s|
@partition-1947
Fikr Taunsvi (Ram Lal Bhatia)|FIK-ər TOWNS-vee|P|Urdu|c|
Mohandas Karamchand Gandhi|MOH-hən-dahs KUR-əm-chund GAHN-dee|P|Gujarati|s|
Jawaharlal Nehru|jə-WAH-hər-lahl NAY-roo|P|Hindi|s|
Muhammad Ali Jinnah|moo-HAM-mad AH-lee JIN-ah|P|Urdu|s|
Liaquat Ali Khan|lee-AH-kut AH-lee KHAHN|P|Urdu|s|
Baldev Singh|BUL-dayv SING|P|Punjabi|s|
Anis Kidwai|ə-NEES KID-weye|P|Urdu|s|
Margaret Bourke-White|BURK|P|English|s|
Beliaghata|bay-lee-ə-GAH-tah|L|Bengali|c|
Hydari Manzil|heye-DAH-ree MUN-zil|L|Urdu|s|
Purana Qila|poo-RAH-nah KI-lah|L|Hindi/Urdu|s|
Rahim Yar Khan|rə-HEEM YAHR KHAHN|L|Urdu|s|
Bahawalpur|bə-HAH-wəl-poor|L|Urdu|s|
Mussoorie|mə-SOOR-ee|L|Hindi|s|
Khalsa College|KHAHL-sah|L|Punjabi|s|
Amritsar|um-RIT-sər|L|Punjabi|s|
Karachi|kə-RAH-chee|L|Urdu|s|
Saadat Hasan Manto|SAH-dət HUS-ən MUN-toh|P|Urdu|s|
Khushwant Singh|KHOOSH-vunt SING|P|Punjabi|s|
Wavell|WAY-vəl|P|English|s|
@apollo-11
Edwin E. 'Buzz' Aldrin Jr.|AWL-drin|P|English|s|
Eugene F. 'Gene' Kranz|KRANZ|P|English|s|
H. R. (Harry Robbins) Haldeman|HAWL-də-mən|P|English|s|
Walter Cronkite|KRONG-keyet|P|English|s|
Sir Bernard Lovell|LUV-əl|P|English|s|
Jodrell Bank|JOD-rəl|L|English|s|
Nikolai Petrovich Kamanin|ni-kə-LEYE pyi-TROH-vyich kə-MAH-nin|P|Russian|s|
Cecil Beaton|SES-əl BEE-tən|P|English|s|
Cecil Harmsworth King|SES-əl HARMZ-wurth|P|English|s|
Broad Chalke|CHAWK|L|English|s|
Luna 15|LOO-nə|T|Russian|s|
@wall-1989
Mieczysław F. Rakowski|myeh-CHI-swahf rah-KOF-skee|P|Polish|s|
Li Peng|lee pung|P|Mandarin|s|
Zhao Ziyang|jow dzuh-yahng|P|Mandarin|s|
Anatoly Chernyaev|ə-nə-TOH-lee chir-NYAH-yif|P|Russian|s|
Wolfgang Schneider|VOLF-gahng SHNEYE-dər|P|German|s|
Christa Wolf|KRIS-tah VOLF|P|German|s|
Günter Schabowski|GUEN-tər shah-BOF-skee|P|German|s|'ue' = German ü
Horst Teltschik|HORST TEL-chik|P|German|s|
Václav Havel|VAHTS-lahf HAH-vel|P|Czech|s|
Ion Bucur|YON BOO-koor|P|Romanian|s|
Tiananmen|tyen-ahn-mun|L|Mandarin|s|
Deng Xiaoping|dung shyow-ping|P|Mandarin|s|
Zhongnanhai|jong-nahn-heye|L|Mandarin|s|
Jianguomenwai|jyen-gwaw-mun-weye|L|Mandarin|s|
Leipzig|LEYEP-tsikh|L|German|s|English LEYEP-sig
Alexanderplatz|ah-lek-SAHN-dər-plahts|L|German|s|
Hrádeček|HRAH-deh-chek|L|Czech|s|
Činoherní klub|CHI-no-her-nyee KLOOP|L|Czech|s|
Melantrich|MEH-lahn-trikh|L|Czech|s|
Imre Nagy|IM-reh NOJ|P|Hungarian|s|
"""
MANDARIN = 'Mandarin'
d = json.load(open(sys.argv[1]))
text = {c['chapter']: ' '.join(c['eyes'] + c['places'] + [c['intro']]) for c in d}
out, cur, bad = {}, None, []
for line in RAW.strip().splitlines():
    if line.startswith('@'):
        cur = line[1:]; out[cur] = []; continue
    t, p, k, lang, cf, note = line.split('|')
    if t not in text[cur]:
        bad.append((cur, t))
    it = {'t': t, 'p': p, 'kind': K[k], 'lang': lang, 'conf': C[cf]}
    if lang == MANDARIN:
        it['tone'] = True
    if note:
        it['note'] = note
    out[cur].append(it)
missing = set(text) - set(out)
print('bad', bad); print('missing chapters', missing)
json.dump(out, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
for k, v in out.items(): print(k, len(v))
