from collections import deque
import re

def solve(bp, T):
    _,c1,c2,c3,c32,c4,c43 = bp
    maxco = max([c1,c2,c3,c4])
    best = 0
    d = deque([(0,0,0,0,1,0,0,0,T)])
    skip = set()
    while d:
        o1,o2,o3,o4,r1,r2,r3,r4,t = d.popleft()
        best = max(best, o4)
        if t==0: continue

        # for state comparison purposes dont store more stuff than we will ever need
        if o1>=t*maxco-r1*(t-1): o1 = t*maxco-r1*(t-1)
        if o2>=t*c32-r2*(t-1): o2 = t*c32 - r2*(t-1)
        if o3>=t*c43-r3*(t-1): o3 = t*c43 - r3*(t-1)
        ns = (o1,o2,o3,o4,r1,r2,r3,r4,t)
        if ns in skip: continue
        skip.add(ns)
        
        o1,o2,o3,o4 = o1+r1,o2+r2,o3+r3,o4+r4
        d.append((o1,o2,o3,o4,r1,r2,r3,r4,t-1))
        if o1>=c1+r1 and r1<maxco: d.append((o1-c1,o2,o3,o4,r1+1,r2,r3,r4,t-1))
        if o1>=c2+r1 and r2<c32: d.append((o1-c2,o2,o3,o4,r1,r2+1,r3,r4,t-1))
        if o1>=c3+r1 and o2>=c32+r2 and r3<c43: d.append((o1-c3,o2-c32,o3,o4,r1,r2,r3+1,r4,t-1))
        if o1>=c4+r1 and o3>=c43+r3: d.append((o1-c4,o2,o3-c43,o4,r1,r2,r3,r4+1,t-1))
    return best

f = open("2022/day19.txt")
ans1,ans2 = 0,1
for i,l in enumerate(f):
    l = l.strip()
    l = re.findall(r'\b\d+\b',l)
    bp = [int(x) for x in l]
    ans1 += bp[0]*solve(bp,24)
    if i<3: ans2 *= solve(bp,32)
print(ans1)
print(ans2)
