def p2_1(f):
    S = {'X':'A','Y':'B','Z':'C'}
    ans = 0
    for i in f:
        a = i.rstrip().split(" ")
        y = S[a[1]]
        sc = "ABC".index(y)+1
        if a[0] != y:
            if a[0] == 'A' and y == 'B':
                sc += 6
            elif a[0] == 'B' and y == 'C':
                sc += 6
            elif a[0] == 'C' and y == 'A':    
                sc += 6  
        else:
            sc += 3
        ans += sc
    return ans

def p2_2(f):
    ans = 0
    for line in f:
        a, b = line.split()
        a = "ABC".index(a)
        if b == "X":
            ans += (a - 1) % 3 + 1
        elif b == "Y":
            ans += 4 + a
        elif b == "Z":
            ans += (a + 1) % 3 + 7
    return ans

f = open('data2', 'r')
print(p2_1(f))
f = open('data2', 'r')
print(p2_2(f)) 

