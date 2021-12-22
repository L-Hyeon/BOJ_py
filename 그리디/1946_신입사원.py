import sys
input = sys.stdin.readline

def do():
    for _ in range(int(input())):
        N = int(input())
        lst = sorted(list(tuple(map(int, input().split())) for i in range(N)), key = lambda x : x[0])
        
        cnt = 1
        t = lst[0][1]
        for i in range(1, N):
            if (lst[i][1] < t):
                cnt += 1
                t = lst[i][1]
        
        print(cnt)

def fast():
    tt = int(input())
    res = [0]*tt
    for _ in range(tt):
        N = int(input())
        lst = [0]*(N + 1)
        for i in range(N):
            a, b = map(int, input().split())
            lst[a] = b
        
        cnt = 1
        t = lst[1]
        for x in lst[2:]:
            if (x < t):
                cnt += 1
                t = x
        res[_] = cnt
    
    sys.stdout.write('\n'.join(map(str, res)))

fast()
