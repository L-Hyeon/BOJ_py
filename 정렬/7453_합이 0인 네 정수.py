import sys
input = sys.stdin.readline

def do():
    N = int(input())
    a, b, c, d = list(), list(), list(), list()
    for i in range(N):
        aa, bb, cc, dd = map(int, input().split())
        a += [aa]
        b += [bb]
        c += [cc]
        d += [dd]
    
    ab = dict()
    for aa in a:
        for bb in b:
            t = aa + bb
            ab[t] = ab.get(t, 0) + 1
    
    cnt = 0
    for cc in c:
        for dd in d:
            cnt += ab.get(-(cc + dd), 0)
    
    print(cnt)

def fast():
    N = int(input())
    a, b, c, d = list(), list(), list(), list()
    for i in range(N):
        aa, bb, cc, dd = map(int, input().split())
        a += [aa]
        b += [bb]
        c += [cc]
        d += [dd]
    
    a.sort()
    b.sort()
    ab = [i + j for i in a for j in b]
    ab.sort()
    ab.append((1 << 29) + 2)

    c.sort(reverse = True)
    d.sort(reverse = True)
    cd = [i + j for i in c for j in d]
    cd.sort(reverse = True)
    cd.append((1 << 29) + 1)

    i = j = 0
    k = N*N
    res = 0
    while (i < k and j < k):
        m = ab[i] + cd[j]
        if (m > 0):
            j += 1
        elif (m < 0):
            i += 1
        else:
            u, v = ab[i], cd[j]
            p = i
            q = j
            while(u == ab[i]):
                i += 1
            while(v == cd[j]):
                j += 1
            res += (i - p)*(j - q)
    
    print(res)

fast()
