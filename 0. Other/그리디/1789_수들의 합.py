import sys
input = sys.stdin.readline

def do():
    S = int(input())
    acc = 0
    cnt = 0
    while (acc <= S):
        cnt += 1
        acc += cnt
    print(cnt - 1)

do()
