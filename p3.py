import itertools

def p3_1(f):
    ans = 0
    P = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in f:
        a = i.rstrip()
        l = len(a)//2
        q1,q2 = set(a[:l]),set(a[l:])
        q = q1 & q2
        for k in q:
            ans += P.index(k)
    return ans

def p3_2(f):
    ans = 0
    P = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for q1,q2,q3 in itertools.zip_longest(*[f]*3):
        q1,q2,q3 = q1.rstrip(),q2.rstrip(),q3.rstrip()
        q = set(q1) & set(q2) & set(q3)
        for k in q:
            ans += P.index(k)
    return ans

f = open('data3', 'r')
print(p3_1(f))
f = open('data3', 'r')
print(p3_2(f))