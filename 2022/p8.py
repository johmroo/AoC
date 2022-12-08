f = open(("day08.txt"), 'r')
m = f.read().splitlines()

rows = len(m)
cols = len(m[0])

ans = 0 
for i in range(rows):
    for j in range(cols):
        sc = 1
        for a,b in [(-1,0),(1,0),(0,-1),(0,1)]:
            found = 1
            c = 0
            while found>0:
                c += 1
                x,y = i+a*c,j+b*c
                if x>=0 and x < rows and y>=0 and y<cols:
                    if m[x][y] >= m[i][j]: found = 0
                else:
                    break
            if found: 
                ans += 1
                break

ans2 = 0
for i in range(0,rows):
    for j in range(0,cols):
        sc = 1
        for a,b in [(-1,0),(1,0),(0,-1),(0,1)]:
            c = 0
            x,y = i+a,j+b
            while x>=0 and x < rows and y>=0 and y<cols:
                c += 1
                if m[x][y] >= m[i][j]: break
                x,y = i+a*(c+1),j+b*(c+1)
            sc *= c
        ans2 = max(ans2,sc)

print(ans)
print(ans2)
