x = 1
t = 0
s = 0

def cycle(t,s,n):
    for _ in range(n):
        if t % 40 in (x - 1, x, x + 1):
            print("#", end="")
        else:
            print(".", end="")
        t += 1
        if (t+20)%40==0:
            s += t * x
        if t % 40 == 0:
            print()
    return t,s

f = open("2022/day10.txt", 'r')
m = f.read().splitlines()

for i in m:
    match i.split():
        case ["addx", v]:
            t,s = cycle(t,s,2)
            x += int(v)
        case ["noop"]:
            t,s = cycle(t,s,1)

print(s)
