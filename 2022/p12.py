from collections import deque

f = open("2022/day12.txt").read().strip()
m = f.splitlines() 
rows = len(m)
cols = len(m[0])

def elev(i,j):
    if m[i][j] == 'E':
        return ord('z')
    elif m[i][j] == 'S':
        return ord('a')
    else:
        return ord(m[i][j])
    
def solve(n):
    Q = deque()
    for i in range(rows):
        for j in range(cols):
            if m[i][j]=='S' or (n==1 and m[i][j] == 'a'):
                Q.append(((i,j), 0))

    S = set()
    while Q:
        (i,j),c = Q.popleft()
        if m[i][j]=='E':
            return c
        if (i,j) in S:
            continue
        S.add((i,j))
        for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0<=x<rows and 0<=y<cols and elev(x,y)<=1+elev(i,j):
                Q.append(((x,y),c+1))

print(solve(0))
print(solve(1))
