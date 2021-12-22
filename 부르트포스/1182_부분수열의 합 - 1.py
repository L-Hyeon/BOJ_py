import sys
from itertools import combinations
input = sys.stdin.readline

def do():
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    cnt = 0
    for i in range(1, N + 1):
        for x in combinations(lst, i):
            if (sum(x) == K):
                cnt += 1
    
    print(cnt)

def fast():
    def cal(n, s, l, r):
        if (n == len(l)):
            r[s] = r.get(s, 0) + 1
            return
        cal(n + 1, s, l, r)
        cal(n + 1, s + l[n], l, r)

    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    left = lst[:N//2]
    right = lst[N//2:]
    resLeft, resRight = dict(), dict()

    cal(0, 0, left, resLeft)
    cal(0, 0, right, resRight)
    resLeft[0] -= 1
    resRight[0] -= 1

    res = resLeft.get(K, 0) + resRight.get(K, 0)
    for i in resLeft:
        if (K - i in resRight):
            res += resRight[K - i]*resLeft[i]
    
    print(res)

fast()
