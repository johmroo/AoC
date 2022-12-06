from aocd import submit
import sys 

def p6_1(f):
    l = f.read()
    q = 4
    ans = q
    while len(set(l[ans - q :ans])) != q: ans+=1
    return ans

def p6_2(f):
    l = f.read()
    q = 14
    ans = q
    while len(set(l[ans - q :ans])) != q: ans+=1
    return ans

day = int(sys.argv[0][1])
data = f"day{day:02}.txt"
f = open(data, 'r')
res = p6_1(f)
submit(res)
