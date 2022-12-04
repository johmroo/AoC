
def p1_1(f):
    l = f.read().split("\n\n")
    q = [sum(int(i) for i in x.split()) for x in l]
    return max(q)

def p1_2(f):
    l = f.read().split("\n\n")
    q = [sum(int(i) for i in x.split()) for x in l]
    q.sort()
    return sum(q[-3:])

f = open('2022/day01.txt', 'r')
print(p1_1(f))
f = open('2022/day01.txt', 'r')
print(p1_2(f)) 
