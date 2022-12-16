from collections import defaultdict
from functools import cache
import re

p = {} 
nidx  = {}
dist  = defaultdict(lambda: 10000)
pnodes = []

def get_node(node: str):
    if node in nidx: return nidx[node]
    nidx[node] = len(nidx)
    return nidx[node]

f = open("2022/day16.txt")
REGEX = r"^Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w ,]+)$"
for vid, flow, b in re.findall(REGEX, f.read(), re.MULTILINE):
    src = get_node(vid)
    flow = int(flow)
    p[src] = flow
    if flow > 0: pnodes.append(src)
    for i in b.split(", "): dist[(get_node(i), src)] = 1

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
