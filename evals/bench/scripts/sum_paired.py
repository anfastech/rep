import json,os,sys
# usage: python3 scripts/sum_paired.py r3 r4 ...  (reads scores/<id>-paired.json and blind/MAPPING.txt)
B=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M={}
for line in open(f"{B}/blind/MAPPING.txt"):
    if ":" in line:
        k,v=line.split(":",1); M[k.strip()]=dict(p.split("=") for p in v.split())
def prec(items):
    items=[i for i in items if i["label"] in("grounded","incidental","wrong")]
    return (sum(i["label"]=="grounded" for i in items),len(items))
tot={}
for id in sys.argv[1:]:
    d=json.load(open(f"{B}/scores/{id}-paired.json")); G=d["g_rules"]
    vis=[g for g in G if g["visible"] in("yes","partly")]
    for k in "XY":
        v=M[id][k]; R=d[k]["r_items"]
        rv=sum({"full":1,"partial":.5}.get(g[k],0) for g in vis)/len(vis)
        ra=sum({"full":1,"partial":.5}.get(g[k],0) for g in G)/len(G)
        core=prec([i for i in R if i["section"] in("rules","template")]); allp=prec(R)
        wrong=sum(i["label"]=="wrong" for i in R)
        print(f"{id} {v}: recall_visible {rv:.2f} recall_all {ra:.2f} prec_rules {core[0]}/{core[1]} prec_all {allp[0]}/{allp[1]} wrong {wrong}")
        t=tot.setdefault(v,[0,0,0,0,0,0,0]); t[0]+=rv; t[1]+=core[0]; t[2]+=core[1]; t[3]+=allp[0]; t[4]+=allp[1]; t[5]+=wrong; t[6]+=1
for v,t in sorted(tot.items()):
    print(f"MEAN {v}: recall_visible {t[0]/t[6]:.2f} prec_rules {t[1]/t[2]:.2f} prec_all {t[3]/t[4]:.2f} wrong {t[5]}")
