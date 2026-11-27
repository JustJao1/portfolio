// SHA-256 on raw bytes; no external packages.
function sha256(bytes) {
 const K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
 const H=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
 const L=bytes.length, padded=new Uint8Array(Math.ceil((L+9)/64)*64);padded.set(bytes);padded[L]=128;
 const view=new DataView(padded.buffer);view.setUint32(padded.length-8,Math.floor(L/0x20000000));view.setUint32(padded.length-4,L*8>>>0);
 const r=(x,n)=>(x>>>n)|(x<<(32-n)),w=new Uint32Array(64);
 for(let off=0;off<padded.length;off+=64){for(let j=0;j<16;j++)w[j]=view.getUint32(off+j*4);for(let j=16;j<64;j++){const a=w[j-15],b=w[j-2];w[j]=(w[j-16]+(r(a,7)^r(a,18)^(a>>>3))+w[j-7]+(r(b,17)^r(b,19)^(b>>>10)))>>>0}
 let [a,b,c,d,e,f,g,h]=H;
 for(let j=0;j<64;j++){const x=(h+(r(e,6)^r(e,11)^r(e,25))+((e&f)^(~e&g))+K[j]+w[j])>>>0,y=((r(a,2)^r(a,13)^r(a,22))+((a&b)^(a&c)^(b&c)))>>>0;h=g;g=f;f=e;e=(d+x)>>>0;d=c;c=b;b=a;a=(x+y)>>>0}
 [a,b,c,d,e,f,g,h].forEach((v,j)=>H[j]=(H[j]+v)>>>0)}
 return H.map(x=>x.toString(16).padStart(8,'0')).join('')
}
function utf8(s){return Uint8Array.from(unescape(encodeURIComponent(s)),x=>x.charCodeAt(0))}
function decode64(s){s=s.replace(/\s/g,'');if(!/^[A-Za-z0-9+/]*={0,2}$/.test(s)||s.length%4)throw Error('Invalid base64');const C='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/',a=[];for(let i=0;i<s.length;i+=4){let n=C.indexOf(s[i])<<18|C.indexOf(s[i+1])<<12|Math.max(0,C.indexOf(s[i+2]))<<6|Math.max(0,C.indexOf(s[i+3]));a.push(n>>>16&255);if(s[i+2]!=='=')a.push(n>>>8&255);if(s[i+3]!=='=')a.push(n&255)}return Uint8Array.from(a)}
