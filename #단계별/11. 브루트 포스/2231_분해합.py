import sys
input = sys.stdin.readline

def do():
    N = int(input())

    res = -1
    for i in range(N + 1):
        temp = i + sum(map(int, list(str(i))))
        if (temp == N):
            res = i
            break
    
    if (res == -1):
        print(0)
    else:
        print(res)

def fast():
    N = int(input())
    idx = max(0, N - 9*res(str(N)))

    for i in range(idx, N):
        temp = i + sum(map(int, str(i)))
        if (temp == N):
            print(i)
            break
    else:
        print(0)

fast()
