from collections import defaultdict
from functools import cache

p = {} 
nidx  = {}
dist  = defaultdict(lambda: 10000)
pnodes = []

def get_node(node: str):
    if node in nidx: return nidx[node]
    nidx[node] = len(nidx)
    return nidx[node]

f = open("2022/day16.txt")

for l in f:
    l = l.strip()
    l = l.replace("Valve ","")
    l = l.replace(" has flow rate","")
    l = l.replace(" tunnels lead to valve ","")
    l = l.replace(" tunnels lead to valves ","")
    l = l.replace(" tunnel leads to valve ","")
    l = l.replace(" tunnel leads to valves ","")
    l = l.replace(" ","")
        
    s,b = l.split(";")
    vid,flow= s.split("=")
    flow = int(flow)
    b = b.split(',')
    src = get_node(vid)
    for i in b: dist[(get_node(i), src)] = 1
    p[src] = flow
    if flow > 0: pnodes.append(src)

n = len(nidx)
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[(i,j)] = min(dist[(i,j)], dist[(i,k)] + dist[(k,j)])

@cache
def solve2(i,t,im):
    best,m = 0,1
    for next in  pnodes:
        if m & im:
            if (tn := t-dist[(i,next)] - 1) >= 0:
                best = max(best, solve(next,tn,im - m) + tn * p[next])
        m <<=1
    return best

M = (1<<len(pnodes))-1
print(solve(nidx["AA"],30,M))
print(max(solve(nidx["AA"],26,iM) + solve(nidx["AA"], 26, M-iM) for iM in range(M+1)))
