import sys
input = sys.stdin.readline

def do():
    N, K = map(INF,input().split())
    res = 0
    for i in range(1, N + 1):
        res = (res + K) % i
    print(res + 1)

do()
