def p4_1(f):
    ans = 0
    for line in f:
        l = line.split(',')
        l1,l2 = l[0].split('-'),l[1].split('-')
        a1,b1 = int(l1[0]),int(l1[1])
        a2,b2 = int(l2[0]),int(l2[1])
        A,B = set(range(a1,b1+1)),set(range(a2,b2+1))
        if len(A - B) == 0 or len(B - A) == 0:
            ans += 1
    return ans

def p4_2(f):
    ans = 0
    for line in f:
        l = line.split(',')
        l1,l2 = l[0].split('-'),l[1].split('-')
        a1,b1 = int(l1[0]),int(l1[1]),
        a2,b2 = int(l2[0]),int(l2[1])
        A,B = set(range(a1,b1+1)),set(range(a2,b2+1))
        if len(A & B) > 0:
            ans += 1
    return ans

f = open('2022/day04.txt', 'r')
print(p4_1(f))
f = open('2022/day04.txt', 'r')
print(p4_2(f))
