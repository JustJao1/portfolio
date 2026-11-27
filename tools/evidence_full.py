#!/usr/bin/env python3
"""Generate complete SHA-256 file manifests for the preserved public snapshots.
No dependencies beyond Python 3 and Git. Never executes repository source.
Optional --archives writes local ZIP backups; never uploads them.
"""
import argparse, hashlib, json, os, pathlib, subprocess, tempfile, zipfile
SNAPSHOTS = {
 "meu-ritmo": "a0cfcc5ec9e585bf3abb7c12ffe1e9e7e78a2d37",
 "meu-ritmo-app": "4885932f7905724672cabc9c2b1dfbf28e522fab",
 "traincore": "867e5397630e7e971c7e74d69227833b667e5512",
 "imovance": "bd2c47cfd074f903c4daa2ff62c740623643aed9",
 "doc-intelligence": "f1d28ae6cb3587d729c0a04825e3f78da6f4c645",
 "flow-engine": "39f11f598c0757daa564383fc0981309a5e1f297",
 "pulse-monitor": "6b56894d481f321cefb7ea677e19d0064dfa1503",
 "freight-connect": "f44df2a464249993e2a9d7d04e38b152dfa5eaca",
 "api-studio": "d674987f2f980a3fe6b58e69400eadf8d7ce474a",
 "linkpilot": "a4aad7be70e37526e6e38fca84b759c3d4919213",
 "portfolio": "3a55c4d8ccd35dcbf9d9d481b908e6e1c82f8078",
}
def git(cwd, *args):
    return subprocess.check_output(["git","-C",str(cwd),*args])
def digest(data): return hashlib.sha256(data).hexdigest()
def canonical(v): return json.dumps(v,ensure_ascii=False,separators=(",",":")).encode("utf-8")
def make_manifest(repo, commit, out, archives):
    with tempfile.TemporaryDirectory() as tmp:
        git(tmp,"init","--quiet")
        git(tmp,"fetch","--quiet","--no-tags","--depth=1",f"https://github.com/JustJao1/{repo}.git",commit)
        actual=git(tmp,"rev-parse","FETCH_HEAD").decode().strip()
        if actual!=commit: raise RuntimeError(f"Unexpected commit: {repo}")
        tree=git(tmp,"rev-parse",commit+"^{tree}").decode().strip()
        records=[]; inventory=[]; files=[]
        for raw in git(tmp,"ls-tree","-r","-z",commit).split(b"\0"):
            if not raw: continue
            head,path=raw.split(b"\t",1);mode,kind,oid=head.decode("ascii").split()
            path=path.decode("utf-8")
            if kind!="blob":
                inventory.append([path,mode,kind,oid,None])
                records.append({"path":path,"mode":mode,"git_object":oid,"type":kind,"sha256":None})
                continue
            data=git(tmp,"cat-file","blob",oid)
            # Verify original Git object bytes as well.
            if hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()!=oid:
                raise RuntimeError(f"Object mismatch: {repo}/{path}")
            inventory.append([path,mode,kind,oid,len(data)])
            records.append({"path":path,"mode":mode,"git_object":oid,"bytes":len(data),"sha256":digest(data),"lfs_pointer":data.startswith(b"version https://git-lfs.github.com/spec/v1\n")})
            if archives: files.append((path,data,mode))
        inventory.sort(key=lambda x:x[0]);records.sort(key=lambda x:x["path"])
        manifest={"schema":1,"repository":"JustJao1/"+repo,"commit":commit,"git_tree":tree,"sha256_git_inventory":digest(canonical(inventory)),"sha256_file_manifest":digest(canonical(records)),"files":records,"scope":"Exact tracked Git blob bytes; excludes untracked files, external services/media, LFS content and submodule content. LinkPilot snapshot contains documentation only."}
        (out/f"{repo}.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        if archives:
            with zipfile.ZipFile(out/f"{repo}-{commit[:12]}.zip","w",compression=zipfile.ZIP_DEFLATED) as z:
                for path,data,mode in sorted(files):
                    p=pathlib.PurePosixPath(path)
                    if p.is_absolute() or ".." in p.parts or "\\" in path: raise RuntimeError("Unsafe path")
                    info=zipfile.ZipInfo(path,date_time=(2026,11,26,0,0,0));info.create_system=3;info.external_attr=int(mode,8)<<16;info.compress_type=zipfile.ZIP_DEFLATED
                    z.writestr(info,data)
                z.writestr("_EVIDENCE_MANIFEST.json",json.dumps(manifest,ensure_ascii=False,indent=2))
        print(f"{repo}: {len(records)} entries | {manifest['sha256_file_manifest']}")
def main():
    p=argparse.ArgumentParser();p.add_argument("--out",default="evidencias-completas");p.add_argument("--archives",action="store_true");args=p.parse_args()
    out=pathlib.Path(args.out);out.mkdir(parents=True,exist_ok=True)
    for repo,commit in SNAPSHOTS.items(): make_manifest(repo,commit,out,args.archives)
if __name__=="__main__": main()
