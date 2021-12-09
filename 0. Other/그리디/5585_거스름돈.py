import sys
input = sys.stdin.readline

def do():
    N = 1000 - int(input())
    cnt = 0
    for x in [500, 100, 50, 10, 5, 1]:
        cnt += N//x
        N %= x
    
    print(cnt)

do()
