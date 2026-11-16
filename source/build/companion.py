"""Build the Many Eyes companion: Long Chains, chain explorer, one-day-many-volumes, on this day, master index.
Usage: python3 companion.py <out.html> <utc stamp>"""
import json, sys, datetime
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from companion_data import load, chains, same_days

out, stamp = sys.argv[1], sys.argv[2]
dt = datetime.datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ")
BUILD = "EYESC-" + dt.strftime("%Y%m%d-%H%MZ")
vols, chapters, eyes, entries, edges = load()
grand, chs = chains(chapters, edges)
sd = same_days(entries, chapters)[:40]
DATA = {"vols": vols, "ch": chapters, "eyes": eyes, "en": entries, "edges": edges, "grand": grand, "chains": chs, "sd": sd}

HTML = r"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Many Eyes Companion</title>
<style>
:root{--bg:#f4eee3;--card:#fbf8f1;--ink:#2a2420;--ink2:#5b5148;--ink3:#8b7f72;--rule:#e1d5c2;--acc:#9a6a2a;--hi:#efe3cc;
--v1:#8c3b2e;--v2:#2f6f5e;--v3:#2d5a8c;--v4:#7a4c9a;--v5:#b5602b;--v6:#5c6b2e;--v7:#2b7a8a;--v8:#3c4f8f;--v9:#2f7a6a;--v10:#7a2f5a;--v11:#4a5a6a;--v13:#8a6a1f;--v14:#9a5b2e;--v15:#6b4f8a}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#1b1815;--card:#24201b;--ink:#ece4d6;--ink2:#c3b8a6;--ink3:#93887a;--rule:#3a342c;--acc:#d7a65e;--hi:#33291c;
--v1:#d9826f;--v2:#6cc0a6;--v3:#7fb0e6;--v4:#bf96e0;--v5:#eaa06c;--v6:#b3c470;--v7:#6fc6d6;--v8:#9fb0ee;--v9:#7fd1bf;--v10:#e39cc4;--v11:#a9b8c8;--v13:#e0bf6a;--v14:#e3a477;--v15:#c2a6e6}}
:root[data-theme="dark"]{--bg:#1b1815;--card:#24201b;--ink:#ece4d6;--ink2:#c3b8a6;--ink3:#93887a;--rule:#3a342c;--acc:#d7a65e;--hi:#33291c;
--v1:#d9826f;--v2:#6cc0a6;--v3:#7fb0e6;--v4:#bf96e0;--v5:#eaa06c;--v6:#b3c470;--v7:#6fc6d6;--v8:#9fb0ee;--v9:#7fd1bf;--v10:#e39cc4;--v11:#a9b8c8;--v13:#e0bf6a;--v14:#e3a477;--v15:#c2a6e6}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 Georgia,"Iowan Old Style",serif}
.sans{font-family:system-ui,-apple-system,"Segoe UI",sans-serif}
header.bar{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--rule);display:flex;gap:10px;align-items:center;padding:8px 16px}
header.bar b{font:700 13px/1 system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;margin-right:auto}
header.bar nav{display:flex;gap:4px;flex-wrap:wrap}header.bar nav a{font:13px system-ui,sans-serif;color:var(--ink2);text-decoration:none;padding:6px 8px;border-radius:6px}
header.bar nav a:hover{background:var(--hi)}
button.t{font:13px system-ui,sans-serif;background:var(--card);color:var(--ink);border:1px solid var(--rule);border-radius:6px;padding:6px 10px;cursor:pointer}
main{max-width:980px;margin:0 auto;padding:28px 16px 80px}
h1{font-size:clamp(36px,7vw,56px);margin:.1em 0}h2{font-size:28px;margin:56px 0 6px;padding-top:12px;border-top:1px solid var(--rule)}
.kicker{font:600 12px/1 system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--acc)}
.lede{color:var(--ink2);max-width:42em}.note{font:13px/1.5 system-ui,sans-serif;color:var(--ink3)}
.vb{display:inline-block;font:700 11px/1 system-ui,sans-serif;color:#fff;border-radius:4px;padding:3px 5px;vertical-align:2px;min-width:26px;text-align:center}
.card{background:var(--card);border:1px solid var(--rule);border-radius:10px;padding:16px 18px;margin:14px 0}
.chain ol{list-style:none;margin:10px 0 0;padding:0 0 0 14px;border-left:2px solid var(--rule)}
.chain li{position:relative;padding:6px 0 10px 12px}.chain li:before{content:"";position:absolute;left:-21px;top:13px;width:10px;height:10px;border-radius:50%;background:var(--c,var(--acc))}
.chain .yr{font:600 13px system-ui,sans-serif;color:var(--ink3);margin-right:6px}
.chain .hop{font-size:14.5px;color:var(--ink2);margin:2px 0 0;max-width:46em}
.chain summary{cursor:pointer;font-weight:600}.chain summary::marker{color:var(--acc)}
a.chl{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--rule)}a.chl:hover{border-color:var(--acc)}
.go{font:12px system-ui,sans-serif;color:var(--acc);text-decoration:none;margin-left:6px;white-space:nowrap}
.grid2{display:grid;align-items:start;grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr));gap:14px}
#tlwrap{overflow-x:auto;border:1px solid var(--rule);border-radius:10px;background:var(--card)}
#tl text{font:11px system-ui,sans-serif;fill:var(--ink3)}#tl .dot{cursor:pointer}#tl .dot:hover{stroke:var(--ink);stroke-width:2}
.ex-now{font-size:22px;margin:0}.ex-list{display:grid;gap:8px;margin-top:10px}
.ex-item{display:block;text-align:left;width:100%;background:var(--bg);border:1px solid var(--rule);border-radius:8px;padding:10px 12px;cursor:pointer;color:var(--ink);font:inherit}
.ex-item:hover{border-color:var(--acc)}.ex-item .hop{font-size:14px;color:var(--ink2);display:block;margin-top:2px}
.crumbs{font:13px system-ui,sans-serif;color:var(--ink3);margin-top:8px}.crumbs a{color:var(--acc);cursor:pointer}
select,input[type=search],input[type=date]{font:15px system-ui,sans-serif;padding:8px 10px;border:1px solid var(--rule);border-radius:8px;background:var(--card);color:var(--ink);max-width:100%}
table.ix{width:100%;border-collapse:collapse;font-size:15px}table.ix td,table.ix th{border-bottom:1px solid var(--rule);padding:7px 6px;vertical-align:top;text-align:left}
table.ix th{font:600 12px system-ui,sans-serif;color:var(--ink3);text-transform:uppercase;letter-spacing:.06em}
.day h3{margin:0 0 4px;font-size:19px}.day ul{margin:6px 0 0;padding-left:18px}.day li{margin:4px 0;font-size:15px}
.pill{font:12px system-ui,sans-serif;color:var(--ink3)}
.approx{font:11px system-ui,sans-serif;color:var(--ink3);border:1px solid var(--rule);border-radius:4px;padding:0 4px;margin-left:4px}
.more{font:14px system-ui,sans-serif;margin-top:8px}
footer{margin-top:60px;border-top:1px solid var(--rule);padding-top:14px;font:13px system-ui,sans-serif;color:var(--ink3)}
@media (max-width:640px){header.bar nav{display:none}table.ix td:nth-child(4),table.ix th:nth-child(4){display:none}}
</style></head><body>
<header class="bar"><b>Many Eyes · Companion</b><nav><a href="#chains">Long Chains</a><a href="#explore">Explorer</a><a href="#map">All chapters</a><a href="#days">One day</a><a href="#onthisday">On this day</a><a href="#index">Index</a></nav><button class="t" id="theme">☾ Night</button></header>
<main>
<p class="kicker">A synoptic reader · the whole series</p><h1>The Long Chains</h1>
<p class="lede" id="lede"></p>

<h2 id="chains">The Long Chains</h2>
<p class="note">Each chain follows threads that the chapters themselves record, always moving forward in time. Open one to read why each link holds; every chapter name opens that volume at the chapter (keep the volume files in the same folder).</p>
<div class="card chain" id="grand"></div>
<div class="grid2" id="chainlist"></div>

<h2 id="explore">Chain explorer</h2>
<p class="note">Start anywhere and walk the threads in either direction. Earlier links are marked ←, later ones →.</p>
<div class="card"><label class="sans note" for="exsel">Start from</label><br><select id="exsel"></select>
<div id="ex"></div><div class="crumbs" id="crumbs"></div></div>

<h2 id="map">All chapters on one line</h2>
<p class="note">Every chapter placed at its first dated entry, one lane per volume. Before 1500 the scale is compressed. Click a dot to open it in the explorer.</p>
<div id="tlwrap"><svg id="tl"></svg></div>

<h2 id="days">One day, many chapters</h2>
<p class="note">Exact dates (not approximate ones) recorded in two or more chapters, most volumes first.</p>
<div id="daylist"></div>

<h2 id="onthisday">On this day</h2>
<p class="note">Every exactly dated entry in the series for one day of the year.</p>
<div class="card"><input type="date" id="otd"> <span class="pill" id="otdn"></span><div id="otdl" class="day"></div></div>

<h2 id="index">Index of eyes</h2>
<p class="note">All the people whose records the seven volumes use. Search by name, place, role or chapter.</p>
<input type="search" id="q" placeholder="Search eyes, places, chapters…" style="width:100%">
<p class="pill" id="qn"></p>
<div style="overflow-x:auto"><table class="ix"><thead><tr><th>Eye</th><th>Chapter</th><th>Life</th><th>Where</th></tr></thead><tbody id="ixb"></tbody></table></div>
<p class="more" id="ixmore"></p>

<footer>Compiled by Ted Gransbury with Claude from the published volumes. Build <span id="bld"></span> · generated <span id="stp"></span>.</footer>
</main>
<script id="data" type="application/json">__DATA__</script>
<script>
const D=JSON.parse(document.getElementById('data').textContent), BUILD="__BUILD__", STAMP="__STAMP__";
const CH=Object.fromEntries(D.ch.map(c=>[c.k,c])), VOL=Object.fromEntries(D.vols.map(v=>[v.v,v]));
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const yr=y=>y==null?'':(y<0?(1-y)+' BC':String(y));
const vb=v=>`<span class="vb" style="background:var(--v${v})">${VOL[v].r}</span>`;
const href=(k,anchor)=>{const c=CH[k];return `${VOL[c.v].f}#${anchor||('ch-'+c.id)}`};
const chl=k=>{const c=CH[k];return `${vb(c.v)} <a class="chl" href="${href(k)}">${esc(c.t)}</a>`};
document.getElementById('bld').textContent=BUILD;document.getElementById('stp').textContent=STAMP;
document.getElementById('lede').textContent=`${D.ch.length} chapters, ${D.eyes.length.toLocaleString()} eyes and ${D.en.length.toLocaleString()} dated entries across ${D.vols.length} volumes, read as one connected web. The chains below follow the threads the chapters record from one event to the next, across centuries and volumes, as far as the record goes.`;
// theme
const root=document.documentElement,tb=document.getElementById('theme');
const dark=()=>root.dataset.theme? root.dataset.theme==='dark' : matchMedia('(prefers-color-scheme: dark)').matches;
const setT=()=>tb.textContent=dark()?'☀ Day':'☾ Night';setT();
try{const t=localStorage.getItem('me-theme');if(t){root.dataset.theme=t;setT()}}catch(e){}
tb.onclick=()=>{root.dataset.theme=dark()?'light':'dark';try{localStorage.setItem('me-theme',root.dataset.theme)}catch(e){};setT()};
// chains
function chainHTML(c,title,open){
  const a=CH[c[0].k],b=CH[c[c.length-1].k];
  return `<details ${open?'open':''}><summary>${esc(title||(a.t+' → '+b.t))} <span class="pill">${yr(a.y0)} → ${yr(b.y0)} · ${c.length} links · ${new Set(c.map(h=>CH[h.k].v)).size} volumes</span></summary><ol>${
   c.map(h=>{const x=CH[h.k];return `<li style="--c:var(--v${x.v})"><span class="yr">${yr(x.y0)}</span>${chl(h.k)}<a class="go" href="#explore" data-k="${h.k}">explore</a>${h.note?`<p class="hop">${esc(h.note)}</p>`:''}</li>`}).join('')}</ol></details>`}
document.getElementById('grand').innerHTML=chainHTML(D.grand,`The longest chain: ${D.grand.length} links from ${yr(CH[D.grand[0].k].y0)} to ${yr(CH[D.grand[D.grand.length-1].k].y0)}`,false);
document.getElementById('chainlist').innerHTML=D.chains.map(c=>`<div class="card chain">${chainHTML(c)}</div>`).join('');
document.addEventListener('click',e=>{const g=e.target.closest('[data-k]');if(g&&g.classList.contains('go')){explore(g.dataset.k,true)}});
// explorer
const NB={};D.edges.forEach(e=>{(NB[e.a]=NB[e.a]||[]).push({k:e.b,note:e.note});(NB[e.b]=NB[e.b]||[]).push({k:e.a,note:e.note})});
const sel=document.getElementById('exsel');
sel.innerHTML=D.vols.map(v=>`<optgroup label="Volume ${v.r} · ${esc(v.t)}">${D.ch.filter(c=>c.v===v.v).map(c=>`<option value="${c.k}">${esc(c.t)} (${yr(c.y0)})</option>`).join('')}</optgroup>`).join('');
let trail=[];
function explore(k,reset){if(reset)trail=[];trail.push(k);sel.value=k;const c=CH[k];
  const seen=new Set(),nb=(NB[k]||[]).filter(n=>!seen.has(n.k)&&seen.add(n.k)).sort((a,b)=>(CH[a.k].y0??0)-(CH[b.k].y0??0));
  document.getElementById('ex').innerHTML=`<p class="ex-now" style="margin-top:12px">${chl(k)}</p><p class="pill">${esc(c.s)} · ${c.ne} eyes · ${c.nn} entries · ${nb.length} threads</p><div class="ex-list">${
   nb.map(n=>{const x=CH[n.k],dir=(x.y0??0)<(c.y0??0)?'←':'→';return `<button class="ex-item" data-x="${n.k}"><span class="yr">${dir} ${yr(x.y0)}</span> ${vb(x.v)} ${esc(x.t)}<span class="hop">${esc(n.note)}</span></button>`}).join('')||'<p class="note">No threads recorded from this chapter yet.</p>'}</div>`;
  document.getElementById('crumbs').innerHTML=trail.length>1?'Path: '+trail.map((t,i)=>`<a data-i="${i}">${esc(CH[t].t)}</a>`).join(' › '):'';}
document.getElementById('ex').addEventListener('click',e=>{const b=e.target.closest('.ex-item');if(b)explore(b.dataset.x)});
document.getElementById('crumbs').addEventListener('click',e=>{const a=e.target.closest('a[data-i]');if(a){const i=+a.dataset.i,k=trail[i];trail=trail.slice(0,i);explore(k)}});
sel.onchange=()=>explore(sel.value,true);
explore(D.grand[0].k,true);
// timeline
(function(){const svg=document.getElementById('tl'),W=Math.max(900,document.getElementById('tlwrap').clientWidth),lane=34,top=26,H=top+lane*D.vols.length+28;
 const LN={};D.vols.forEach((v,i)=>LN[v.v]=i);const xs=y=>{const L=60,R=W-20,cut=1500,lo=-2600,hi=2000,f=.18;const span=R-L;return y<cut? L+(y-lo)/(cut-lo)*span*f : L+span*f+(y-cut)/(hi-cut)*span*(1-f)};
 let g=`<rect width="${W}" height="${H}" fill="transparent"/>`;
 [-2499,-499,500,1500,1600,1700,1800,1900,2000].forEach(y=>{g+=`<line x1="${xs(y)}" x2="${xs(y)}" y1="${top-8}" y2="${H-22}" stroke="var(--rule)"/><text x="${xs(y)}" y="${H-8}" text-anchor="middle">${yr(y)}</text>`});
 D.vols.forEach((v,i)=>{g+=`<text x="8" y="${top+i*lane+lane/2+4}">${v.r}</text>`});
 D.edges.forEach(e=>{const a=CH[e.a],b=CH[e.b];if(a.y0==null||b.y0==null)return;const ya=top+LN[a.v]*lane+lane/2,yb=top+LN[b.v]*lane+lane/2;g+=`<line x1="${xs(a.y0)}" y1="${ya}" x2="${xs(b.y0)}" y2="${yb}" stroke="var(--ink3)" stroke-opacity=".12"/>`});
 D.ch.forEach(c=>{if(c.y0==null)return;g+=`<circle class="dot" data-x="${c.k}" cx="${xs(c.y0)}" cy="${top+LN[c.v]*lane+lane/2}" r="6" fill="var(--v${c.v})"><title>${esc(c.t)} (${yr(c.y0)})</title></circle>`});
 svg.setAttribute('width',W);svg.setAttribute('height',H);svg.setAttribute('viewBox',`0 0 ${W} ${H}`);svg.innerHTML=g;
 svg.addEventListener('click',e=>{const d=e.target.closest('.dot');if(d){explore(d.dataset.x,true);location.hash='explore'}});})();
// one day
document.getElementById('daylist').innerHTML=D.sd.map(r=>{const items=r.i.map(i=>D.en[i]);const by={};items.forEach(x=>(by[x.k]=by[x.k]||[]).push(x));
 return `<div class="card day"><h3>${esc(items[0].dd||r.d)}</h3><span class="pill">${r.nc} chapters · ${r.nv} volume${r.nv>1?'s':''}</span><ul>${Object.entries(by).map(([k,xs])=>`<li>${chl(k)}: ${xs.map(x=>`<b>${esc(x.e)}</b> — ${esc(x.h)}`).join('; ')}</li>`).join('')}</ul></div>`}).join('');
// on this day
const otd=document.getElementById('otd');const now=new Date();otd.value=`2000-${String(now.getMonth()+1).padStart(2,'0')}-${String(now.getDate()).padStart(2,'0')}`;
function showOTD(){const md=otd.value.slice(5);const xs=D.en.filter(x=>/^-?\d{4}-\d\d-\d\d$/.test(x.d)&&x.d.slice(-5)===md&&!x.a).sort((a,b)=>parseInt(a.d)-parseInt(b.d));
 document.getElementById('otdn').textContent=`${xs.length} entries`;
 document.getElementById('otdl').innerHTML=xs.length?`<ul>${xs.map(x=>`<li><span class="yr">${yr(parseInt(x.d))}</span> ${chl(x.k)} — <b>${esc(x.e)}</b>: ${esc(x.h)}</li>`).join('')}</ul>`:'<p class="note">No exactly dated entries on this day of the year.</p>'}
otd.onchange=showOTD;showOTD();
// index
const IX=D.eyes.slice().sort((a,b)=>a.n.localeCompare(b.n));let lim=150;
const q=document.getElementById('q');
function showIX(){const t=q.value.trim().toLowerCase();const rows=t?IX.filter(e=>(e.n+' '+e.w+' '+e.r+' '+e.l+' '+CH[e.k].t).toLowerCase().includes(t)):IX;
 document.getElementById('qn').textContent=`${rows.length.toLocaleString()} of ${IX.length.toLocaleString()} eyes`;
 document.getElementById('ixb').innerHTML=rows.slice(0,lim).map(e=>`<tr><td><a class="chl" href="${href(e.k,'eye-'+CH[e.k].id+'-'+e.id)}">${esc(e.n)}</a>${e.p?` <i class="note">${esc(e.p)}</i>`:''}<br><span class="note">${esc(e.r)}</span></td><td>${chl(e.k)}</td><td class="note">${esc(e.l)}</td><td class="note">${esc(e.w)}</td></tr>`).join('');
 document.getElementById('ixmore').innerHTML=rows.length>lim?`<button class="t" id="mb">Show ${Math.min(300,rows.length-lim)} more</button>`:'';}
q.oninput=()=>{lim=150;showIX()};document.getElementById('ixmore').onclick=e=>{if(e.target.id==='mb'){lim+=300;showIX()}};showIX();
</script></body></html>"""
page = HTML.replace("__DATA__", json.dumps(DATA, ensure_ascii=False).replace("</", "<\\/")).replace("__BUILD__", BUILD).replace("__STAMP__", stamp)
open(out, "w", encoding="utf-8").write(page)
print("wrote", out, len(page) // 1024, "KB", BUILD)
