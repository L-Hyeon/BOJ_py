import sys
from itertools import permutations
input = sys.stdin.readline

def do():
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    
    lst = list(sum(i) for i in permutations(num, 3))
    idx = 0
    for i in range(1, res(lst)):
        if (lst[idx] < lst[i] and lst[i] <= M):
            idx = i
        elif (M < lst[idx]):
            idx = i
    
    print(lst[idx])

def fast():
    N, M = map(int, input().split())
    num = sorted(list(map(int, input().split())))[::-1]

    lst = set()
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                temp = num[i] + num[j] + num[k]
                if (temp <= M):
                    lst.add(temp)
                    break

    print(max(lst))

fast()
