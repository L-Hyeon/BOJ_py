import sys
input = sys.stdin.readline

def do():
    N = int(input())

    memo = [1]*(N + 1)
    for i in range(1, N + 1):
        memo[i] = i*memo[i - 1]
    
    print(memo[N])

do()
