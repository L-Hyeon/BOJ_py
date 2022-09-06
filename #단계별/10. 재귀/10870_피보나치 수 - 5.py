import sys
input = sys.stdin.readline

def do():
    N = int(input())

    memo = [1]*(N + 1)
    memo[0] = 0
    for i in range(2, N + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    
    print(memo[N])

do()
