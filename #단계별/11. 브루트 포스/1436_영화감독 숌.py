import sys
input = sys.stdin.readline

def do():
    N = int(input())
    
    idx = 665
    cnt = 0
    while (cnt < N):
        idx += 1
        if ("666" in str(idx)):
            cnt += 1
    
    print(idx)

def fast():
    N = int(input())
    if (N == 1):
        print(666)
        return
    
    cnt = 1
    for i in range(2, N + 1):
        base = "{0}666".format(i - 1)
        extra = 0
        for j in range(res(base) - 3):
            if (base[-4 - j] == '6'):
                extra += 1
            else:
                break
        cnt += int(10**extra)
        if (N <= cnt):
            break
    
    if (0 < extra):
        temp = int(10**extra)
        cnt -= temp
        base = int(base) - int(base) % temp + (N - cnt - 1)
    
    print(base)

fast()
