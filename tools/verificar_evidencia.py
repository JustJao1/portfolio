#!/usr/bin/env python3
"""Verify the recorded Git snapshot and compute SHA-256 of each tracked blob.
Run inside a local Git clone: python verificar_evidencia.py COMMIT [OUTPUT.json]
No network, no dependencies, no checkout or history modification.
"""
import hashlib, json, subprocess, sys
from pathlib import Path

if len(sys.argv) not in (2,3):
    raise SystemExit(__doc__)
commit=sys.argv[1]
def git(*args):
    return subprocess.check_output(["git", *args])
commit=git("rev-parse","--verify",commit+"^{commit}").decode().strip()
tree=git("rev-parse",commit+"^{tree}").decode().strip()
rows=[]
for item in git("ls-tree","-r","-l","-z",commit).split(b"\0"):
    if not item: continue
    info,path=item.split(b"\t",1)
    mode,kind,oid,size=info.decode().split()
    if kind!="blob": continue
    path=path.decode("utf-8")
    raw=git("cat-file","blob",oid)
    if len(raw)!=int(size): raise ValueError(path)
    rows.append(dict(path=path,mode=mode,git_blob=oid,size=int(size),sha256=hashlib.sha256(raw).hexdigest()))
rows.sort(key=lambda x:x["path"])
inventory="".join(f"{r['mode']}\t{r['git_blob']}\t{r['size']}\t{r['path']}\n" for r in rows)
output=dict(commit=commit,tree=tree,inventory_sha256=hashlib.sha256(inventory.encode("utf-8")).hexdigest(),files=rows)
dest=Path(sys.argv[2] if len(sys.argv)==3 else "SHA256-"+commit[:12]+".json")
if dest.exists(): raise SystemExit("Refusing to overwrite "+str(dest))
dest.write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("Files:",len(rows),"Inventory SHA-256:",output["inventory_sha256"],"Output:",dest)
