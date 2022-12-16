from collections import defaultdict
from functools import cache
import re

p = {}
dist  = defaultdict(lambda: 10000)
pnodes = []

f = open("2022/day16.txt")
REGEX = r"^Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w ,]+)$"
for vid, flow, b in re.findall(REGEX, f.read(), re.MULTILINE):
    flow = int(flow)
    p[vid] = flow
    if flow > 0: pnodes.append(vid)
    for i in b.split(", "): dist[(i, vid)] = 1

n = len(p)
for k in p:
    for i in p:
        for j in p:
            dist[(i,j)] = min(dist[(i,j)], dist[(i,k)] + dist[(k,j)])
@cache
def solve2(i,t,im):
    best,m = 0,1
    for next in  pnodes:
        if m & im:
            if (tn := t-dist[(i,next)] - 1) >= 0:
                best = max(best, solve2(next,tn,im - m) + tn * p[next])
        m <<=1
    return best

M = (1<<len(pnodes))-1

print(solve2("AA",30,M))
print(max(solve2("AA",26,iM) + solve2("AA", 26, M-iM) for iM in range(M+1)))
