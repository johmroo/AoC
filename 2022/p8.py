import sys
import itertools #permutations
from collections import defaultdict, Counter, deque

f = open(("day08.txt"), 'r')
m = []
for i in f:
	a = i.rstrip()
	m1 = [int(j) for j in a]
	m.append(m1)

rows = len(m)
cols = len(m[0])
print(rows)
print(cols)

ans = 0 
for i in range(rows):
    for j in range(cols):
        sc = 1
        for a,b in [(-1,0),(1,0),(0,-1),(0,1)]:
            found = True
            c = 0
            while found:
                c += 1
                x,y = i+a*c,j+b*c
                if x>=0 and x < rows and y>=0 and y<cols:
                    if m[x][y] >= m[i][j]: found = False
                else:
                    break
            if found: 
                ans += 1
                break
        
ans2 = 0
for i in range(0,rows):
    for j in range(0,cols):
        sc = 1
        for a,b in [(-1,0),(1,0),(0,-1),(0,1)]:
            c,v = 0,0
            while True:
                c += 1
                x,y = i+a*c,j+b*c
                if x>=0 and x < rows and y>=0 and y<cols:
                    v += 1
                    if m[x][y] >= m[i][j]: break
                else:
                    break
            sc *= v
        ans2 = max(ans2,sc)

print(ans)
print(ans2)
