from aocd import submit
from os.path import exists
import sys 
from collections import Counter

def p1(f):
    path = []
    dirs = Counter()
    for line in f.read().splitlines():
        match line.split():
            case ["dir",d] : pass
            case ["$", 'ls']: pass 
            case ["$", "cd", '/']: path = [] 
            case ["$", "cd", '..']: path.pop()
            case ["$", "cd", d]: path.append(d)
            case [size,d]: 
                dirs['/'] += int(size)
                prefixes = [path[:i + 1] for i in range(len(path))]
                for i in prefixes: dirs['/'.join(i)] += int(size)
    return sum(x for x in dirs.values() if x < 100000)
def p2(f):
    path = []
    dirs = Counter()
    for line in f.read().splitlines():
        match line.split():
            case ["dir",d] : pass
            case ["$", 'ls']: pass 
            case ["$", "cd", '/']: path = []
            case ["$", "cd", '..']: path.pop()
            case ["$", "cd", d]: path.append(d)
            case [size,d]:
                dirs['/'] += int(size)
                prefixes = [path[:i + 1] for i in range(len(path))]
                for i in prefixes: dirs['/'.join(i)] += int(size)
    return min(x for x in dirs.values() if dirs['/'] - x <= 40000000)

x = sys.argv[0].split('/')
year = int(x[0])
day = int(x[1].split('.')[0][1:])
data = f"{year}/day{day:02}.txt"
if not exists(data):
    from aocd import get_data
    with open(data, "w") as f:
        f.write(get_data(day=day, year=year))

f = open(data, 'r')
submit(p1(f))
f = open(data, 'r')
submit(p2(f))
