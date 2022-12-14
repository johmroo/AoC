def solve(c,b,n):
    t = 0
    while (500,0) not in c:
        x,y = 500,0
        while True:
            if y>=b: break
            if (x,y+1) not in c: y = y+1
            elif (x-1,y+1) not in c: x,y = x-1,y+1
            elif (x+1,y+1) not in c: x,y = x+1,y+1
            else: break  
        t += 1
        if y+1>=b and n == 0: return t-1
        c.add((x,y))
    return t

f = open("2022/day14.txt")
cave = set()
for line in open("2022/day14.txt"):
    x = [list(map(int, p.split(","))) for p in line.split(" -> ")]
    for (x1, y1), (x2, y2) in zip(x, x[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                cave.add((x,y))

cave_floor = 1+max(x[1] for x in cave)
cave2 = cave.copy()
print(solve(cave,cave_floor,0))
print(solve(cave2,cave_floor,1))
