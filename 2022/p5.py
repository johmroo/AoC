from aocd import submit
from collections import deque

P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def p5_1(f):
    S = []
    for i in range(9):
        S.append(deque())
    for l in f:
        l = l.rstrip()
        if l[1] == '1':
            break
        for i, idx in enumerate(range(1, len(l), 4)):
            if l[idx] in P:
                S[i].append(l[idx])

    for l in f:
        l = l.rstrip()
        if len(l) > 1:
            q = l.split(' ')
            n, f, t = int(q[1]),int(q[3]),int(q[5])
            for i in range(n):
                e = S[f - 1].popleft()
                S[t - 1].appendleft(e)
    return "".join(a[0] for a in S)


def p5_2(f):
    S = []
    for i in range(9):
        S.append(deque())
    for l in f:
        l = l.rstrip()
        if l[1] == '1':
            break
        for i, idx in enumerate(range(1, len(l), 4)):
            if l[idx] in P:
                S[i].append(l[idx])
    for l in f:
        l = l.rstrip()
        if len(l) > 1:
            q = l.split(' ')
            n, f, t = int(q[1]),int(q[3]),int(q[5])
            S2 = deque()
            for i in range(n):
                x = S[f - 1].popleft()
                S2.appendleft(x)
            S[t - 1].extendleft(S2)
    return "".join(a[0] for a in S)

day = 5

data = f"day{day:02}.txt"
f = open(data, 'r')
res = p5_1(f)
print(res)
submit(res)
