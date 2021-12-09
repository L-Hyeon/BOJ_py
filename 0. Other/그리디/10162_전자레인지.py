import sys
input = sys.stdin.readline

def do():
    N = int(input())
    if (N % 10):
        print(-1)
        return
    cnt = [0, 0, 0]

    cnt[0] = N//300
    N %= 300
    cnt[1] = N//60
    N %= 60
    cnt[2] = N//10
    N %= 10
    
    print(*cnt)

do()
