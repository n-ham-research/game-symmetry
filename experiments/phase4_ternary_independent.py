"""Independent cell-permutation/union-find ternary certificate review."""
import itertools,collections
from matching_audit import bijections
W=list(bijections((3,)*3)); profiles=list(itertools.product(range(3),repeat=3));cells=[(s,i) for s in profiles for i in range(3)]; idx={c:i for i,c in enumerate(cells)}
def perm(g):
 p,f=g;ans=[]
 for s,i in cells:
  t=[None]*3
  for j in range(3):t[p[j]]=f[j][s[j]]
  ans.append(idx[tuple(t),p[i]])
 return tuple(ans)
P=[perm(g) for g in W];ids={p:i for i,p in enumerate(P)};identity=tuple(range(81));r=perm(((1,2,0),((0,1,2),)*3))
def mul(a,b):return tuple(a[b[i]] for i in range(81))
def group(g):
 seen={identity};todo=[identity]
 while todo:
  a=todo.pop()
  for t in (r,g):
   b=mul(a,t)
   if b not in seen:seen.add(b);todo.append(b)
 return frozenset(seen)
H={group(P[i]) for i,g in enumerate(W) if g[0] not in ((0,1,2),(1,2,0),(2,0,1))}; hist=collections.Counter(map(len,H));bad=[]
# A group is strategytrivial/fullimage iff its stabilizer of eachplayer acts
# trivially on allcells' focal action. Test all sectionpairs withoutmatching API.
for h in H:
 parent=list(range(81))
 def find(x):
  while parent[x]!=x:x=parent[x]
  return x
 for t in h:
  for i in range(81):parent[find(i)]=find(t[i])
 cl={t for t in P if all(find(i)==find(t[i]) for i in range(81))}
 # Full matching corresponds conjugate bareS3 by independent localstrategylabels.
 full=False
 for f1 in itertools.permutations(range(3)):
  for f2 in itertools.permutations(range(3)):
   f=((0,1,2),f1,f2); inv=tuple(tuple(x.index(a) for a in range(3)) for x in f)
   lifts=[]
   for p in itertools.permutations(range(3)):
    maps=tuple(tuple(f[p[i]][inv[i][a]] for a in range(3)) for i in range(3))
    lifts.append(perm((p,maps)))
   if all(t in cl for t in lifts):full=True;break
  if full:break
 if not full:bad.append({W[ids[t]] for t in h})
print(hist,'exceptional',len(bad),[len(h) for h in bad])
assert hist=={6:4,18:3,24:6,54:3,162:1,648:2}
assert len(bad)==3
for h in bad:
 odd=[g for g in h if g[0] in ((0,2,1),(1,0,2),(2,1,0))]
 assert len(odd)==3 and len({g[1] for g in odd})==1
 assert all(len(set(g[1]))==1 for g in odd)
