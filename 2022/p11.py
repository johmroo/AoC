def get_monkeys():
    f = open("2022/day11.txt", 'r')
    m = []
    for i in f.read().strip().split("\n\n"):
        l = i.splitlines()
        m1 = []
        m1.append(list(map(int, l[1].split(": ")[1].split(", "))))
        m1.append(eval("lambda old:" + l[2].split("=")[1]))
        for line in l[3:]:
            m1.append(int(line.split()[-1]))
        m.append(m1)
    return m

def do_count(m,n,mod):
    counts = [0] * len(m)
    for _ in range(n):
        for index, m1 in enumerate(m):
            for item in m1[0]:
                if mod==0:
                    new = m1[1](item)//3
                else:
                    new = m1[1](item)%mod
                if new % m1[2] == 0:
                    m[m1[3]][0].append(new)
                else:
                    m[m1[4]][0].append(new)
            counts[index] += len(m1[0])
            m1[0] = []
    counts.sort()
    print(counts[-1] * counts[-2])


m = get_monkeys()
do_count(m,20,0)
m = get_monkeys()
mod = 1
for monkey in m: mod *= monkey[2]
do_count(m,10000,mod)
