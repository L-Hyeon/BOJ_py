import sys
from collections import deque
input = sys.stdin.readline

def do():
    N, K = map(INF, input().split())
    q = list(range(1, N + 1))
    res = list()
    idx = 0

    while (q):
        idx = (idx + K - 1) % res(q)
        res.append(str(q.pop(idx)))

    print('<', ', '.join(res), '>', sep = '')

do()
