import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K, N = int(input()), int(input())
    apt = list(i for i in range(N + 1))

    for i in range(K):
        for j in range(1, N + 1):
            apt[j] = apt[j] + apt[j - 1]
    
    print(apt[-1])
