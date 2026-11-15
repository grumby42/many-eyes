import json,glob
LBL={}
try: LBL=json.load(open('labels.json'))
except Exception: pass
out={}
for f in sorted(glob.glob('ch-*.json')):
    cid=f[3:-5]; c=json.load(open(f))
    for e in c['eyes']:
        if e.get('lat') is None: continue
        k=f"{cid}:{e['id']}"
        out[k]={"lat":e['lat'],"lon":e['lon'],"label":LBL.get(k) or e.get('where','').split(';')[0].split(',')[0][:22],"waypoints":e.get('waypoints') or []}
json.dump(out,open('coords.json','w'),indent=1,ensure_ascii=False); print(len(out))
