import sys
input = sys.stdin.readline

def do():
    N = int(input())
    lst = list(list(map(int, input().split())) for i in range(N))

    rank = [1]*N
    for i in range(N):
        for j in range(N):
            if (i == j):
                continue

            if (lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]):
                rank[i] += 1

    print(*rank)

do()
