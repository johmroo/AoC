def cmp(x, y):
    if type(x) == int:
        if type(y) == int: return x - y
        else: return cmp([x], y)
    else: 
        if type(y) == int: return cmp(x, [y])    
    for a, b in zip(x, y):
        v = cmp(a, b)
        if v: return v
    return len(x) - len(y)

f = open("2022/day13.txt")
p = [[eval(x) for x in cc.splitlines()] for cc in f.read().split("\n\n")]
c = 0
for i, (a, b) in enumerate(p):
    if cmp(a, b) < 0: c += i + 1
print(c)

f = open("2022/day13.txt")
p = [[eval(x) for x in cc.splitlines()] for cc in f.read().split()] + [[[2]], [[6]]]
d1,d2 = 1,1
for a in p:
    if cmp(a, [[2]]) < 0:
        d1 += 1
        d2 += 1
    elif cmp(a, [[6]]) < 0: d1 += 1
print(d1 * d2)
