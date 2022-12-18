from collections import deque
f = open("2022/day18.txt")

m = set()
for l in f:
    x,y,z = l.split(',')
    m.add((int(x),int(y),int(z)))

def solve1():
    c = 0
    for (x,y,z) in m:
        q = set([((x+1,y,z)),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)])
        c += 6-len(q&m)
    print(c)

lim = 1500
def count_void(a,s):
    d = deque([a])
    while d:
        q = d.popleft()
        if q in m or q in s: continue
        s.add(q)
        if len(s) > lim: return
        x,y,z = q
        for q in [((x+1,y,z)),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]: d.append(q)

def solve2():
    c = 0
    bubbles = set()
    void = set()
    for (x,y,z) in m:
        for q in [((x+1,y,z)),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]:
            if q in m or q in bubbles: continue
            if q in void: c += 1
            else:
                s = set()
                count_void(q,s)
                if len(s)>lim:
                    c += 1
                    void |= s
                else: bubbles |= s
    print(c)

solve1()
solve2()
