import sys
from collections import Counter
input = sys.stdin.readline

def do():
    def cal(o, l):
        for x in l:
            t = list(x + e for e in o)
            o += t

    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    lstL = lst[:N//2]
    lstR = lst[N//2:]
    left, right = [0], [0]

    cal(left, lstL)
    cal(right, lstR)
    counter = Counter(right)

    cnt = 0 if (K != 0) else - 1
    for i in left:
        if (K - i in counter):
            cnt += counter[K - i]
    
    print(cnt)

do()
