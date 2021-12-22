import sys
input = sys.stdin.readline

def do():
    N = int(input())
    lst = sorted(list(int(input()) for i in range(N)), reverse = True)
    res = 0
    for i in range(N):
        lst[i] = lst[i]*(i + 1)
        if (res < lst[i]):
            res = lst[i]
    
    print(res)

do()
