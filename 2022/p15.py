f = open("2022/day15.txt")
sensors = set()
beacons = set()
mind,maxd = 1000000000,0
y = 2000000
for l in f:
        l = l.replace("Sensor at ","")
        l = l.replace(" closest beacon is at ","")
        s,b = l.split(":")
        sx,sy = s.split(",")
        rx,ry = b.split(",")
        sxx,syy = int(sx.split("=")[1]),int(sy.split("=")[1])
        rxx,ryy = int(rx.split("=")[1]),int(ry.split("=")[1])
        mh = abs(sxx-rxx)+abs(syy-ryy)
        sensors.add((sxx,syy,mh))
        beacons.add((rxx,ryy))
        mhy = abs(syy-y) # mh distance to line
        if mh >= mhy:
            mind = min(mind,sxx-(mh-mhy))
            maxd = max(maxd,sxx+mh-mhy)

def in_range(x,y,s):
    for (sx,sy,d) in s:
        dxy = abs(x-sx)+abs(y-sy)
        if dxy<=d: return False
    return True

c = 0
for x in range(mind,maxd+1):
    if not in_range(x,y,sensors) and (x,y) not in beacons:
        c += 1
print(c)

# missing beacon must be just outside range of it closest sensor 
# otherwise another possible position would be one step closer
# and the position is not unique
maxv = 4000000
for (sx,sy,d) in sensors:
    for dx in range(d+2):
        dy = (d+1)-dx
        for x,y in [(sx-dx,sy-dy),(sx-dx,sy+dy),(sx+dx,sy-dy),(sx+dx,sy+dy)]:
            if not(0<=x<=maxv and 0<=y<=maxv): continue
            if in_range(x,y,sensors):
                print(x*maxv + y)
                exit(0)
