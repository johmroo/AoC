f = open("2022/day09.txt", 'r')
m = f.read().splitlines()
d = {"R": (1, 0), "L": (-1, 0),"U": (0, 1), "D": (0, -1),}

def p1(m,sz):
    tpos = set()
    H = [[0,0] for i in range(sz)]

    tpos.add(str(H[-1]))
    for i in m:
        a,b = i.split()
        b = int(b)
        for j in range(b):
            H[0][0] += d[a][0]
            H[0][1] += d[a][1]
            for q in range(sz-1):
                d1 = H[q][0] - H[q+1][0]
                d2 = H[q][1] - H[q+1][1]
                k1 = min(1, max(-1, d1))
                k2 = min(1, max(-1, d2))

                if abs(d1) > 1 or abs(d2) > 1::
                    H[q+1][0] += k1
                    H[q+1][1] += k2
            tpos.add(str(H[-1]))
    print(len(tpos))

p1(m,2)
p1(m,10)
