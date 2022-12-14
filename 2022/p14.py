def solve(c,b,n):
    t = 0
    while True:
        x,y = 500,0
        while True:
            if (x,y+1) not in c: y = y+1
            elif (x-1,y+1) not in c: x,y = x-1,y+1
            elif (x+1,y+1) not in c: x,y = x+1,y+1
            else: break  
        t += 1
        if y+1>=b and n == 0: return t-1
        if x == 500 and y == 0: return t
        c.add((x,y))

f = open("2022/day14.txt").read().strip().split('\n')
cave = set()
for i in f:
    last = None
    for j in i.split('->'):
        x,y = j.split(',')
        x,y = int(x),int(y)
        if last is not None:
            nx,ny = x-last[0],y-last[1]
            l = max(abs(nx),abs(ny))
            dx = 1 if nx>0 else (-1 if nx<0 else 0)
            dy = 1 if ny>0 else (-1 if ny<0 else 0)
            for i in range(l+1): cave.add((last[0]+i*dx,last[1]+i*dy))
        last = (x,y)

cave_floor = 2+max(x[1] for x in cave)
minx,maxx = min(x[0] for x in cave)-500,max(x[0] for x in cave)+500
for i in range(minx, maxx): cave.add((i,cave_floor))
cave2 = cave.copy()
print(solve(cave,cave_floor,0))
print(solve(cave2,cave_floor,1))
