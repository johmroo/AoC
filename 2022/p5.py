from collections import Counter


def p1(f):
    fish = [int(x) for x in f.read().strip().split(",")]
    for i in range(80):
        for j, a in enumerate(fish[:]):
            if a == 0:
                fish.append(8)
                fish[j] = 6
            else:
                fish[j] -= 1
    return len(fish)


def p2(f):
    fish = Counter(map(int, f.read().split(",")))
    for i in range(256):
        fish = Counter({(k - 1): v for k, v in fish.items()})
        fish[6] += fish[-1]
        fish[8] += fish[-1]
        del fish[-1]
    return sum(fish.values())

year = 2022
day = 5
path =f"day{day:02}.txt"
print(path)

from aocd import submit
#f = open('day05.txt', 'r')
#submit(p1(f),part="a",day=day,year=year)
#f = open('day05.txt', 'r')
#submit(p2(f),part="b",day=day,year=year)

