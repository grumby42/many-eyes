import json,glob
DEF={"bandung":"Bandung","fatehpur-sikri":"Fatehpur Sikri","paris-1919":"Paris","philadelphia-1787":"State House","seneca-falls":"Seneca Falls","vienna-1815":"Vienna","worms-1521":"Worms","yalta":"Livadia"}
OVR={"bandung:malik":"Washington","bandung:dulles":"Washington","fatehpur-sikri:meherji":"Navsari","paris-1919:brockdorff":"Versailles",
"seneca-falls:douglass":"Rochester","seneca-falls:rochester-minutes":"Rochester","seneca-falls:bush":"Rochester","seneca-falls:emclintock":"Waterloo","seneca-falls:wright":"Auburn","seneca-falls:press":"New York",
"vienna-1815:louis18":"Paris","vienna-1815:wilberforce":"London","worms-1521:hutten":"Ebernburg","worms-1521:durer":"Antwerp",
"yalta:churchill":"Vorontsov Palace","yalta:cadogan":"Vorontsov Palace","yalta:moran":"Vorontsov Palace","yalta:sarah":"Vorontsov Palace","yalta:lunghi":"Vorontsov Palace","yalta:stalin":"Yusupov Palace","yalta:maisky":"Yusupov Palace","yalta:arciszewski":"London"}
out={}
for f in glob.glob('ch-*.json'):
    cid=f[3:-5]; c=json.load(open(f))
    for e in c['eyes']:
        k=f"{cid}:{e['id']}"; out[k]={"lat":e['lat'],"lon":e['lon'],"label":OVR.get(k,DEF[cid]),"waypoints":e.get('waypoints') or []}
out["fatehpur-sikri:monserrate"]["waypoints"]=[w for w in out["fatehpur-sikri:monserrate"]["waypoints"] if w["lon"]>60]
json.dump(out,open('coords.json','w'),indent=1,ensure_ascii=False); print(len(out))
