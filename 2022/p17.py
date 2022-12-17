f = open("2022/day17.txt")
wind = f.read().strip()

rocks = [
    [(2,0),(3,0),(4,0),(5,0)],
    [(3,2),(2,1),(3,1),(4,1),(3,0)],
    [(2,0),(3,0),(4,0),(4,1),(4,2)],
    [(2,0),(2,1),(2,2),(2,3)],
    [(2,1),(2,0),(3,1),(3,0)],
]

def left(rock):
    if any([x==0 for (x,_) in rock]): return rock
    return set([(x-1,y) for (x,y) in rock])

def right(rock):
    if any([x==6 for (x,_) in rock]): return rock
    return set([(x+1,y) for (x,y) in rock])

cave = set([(x,0) for x in range(7)])
hist = {}
top,w,t,ex = 0,0,0,0
mt = 1000000000000
while t<mt:
    # look for rock pattern
    rockid = (t%5,w) 
    if t>2022 and rockid in hist:
        topx,tx = hist[rockid]
        dy,dt = top-topx,t-tx
        skip = (mt-t)//dt
        t += skip*dt  # just step fwd in time, top remains the same
        ex += skip*dy # remember how many we skipped, to be added at the end
    hist[rockid] = (top,t)
    
    rock = set([(a,top+4+b) for a,b in rocks[t%5]])
    while True:
        nrock = right(rock) if wind[w]=='>' else left(rock)
        if not nrock & cave: rock = nrock
        w = (w+1)%len(wind)
        nrock = set([(x,y-1) for (x,y) in rock]) 
        if nrock & cave:
            top = max(top,max([y for (_,y) in rock]))
            cave |= rock
            break
        else: rock = nrock
    t += 1
    if t==2022: print(top)
print(top+ex)
