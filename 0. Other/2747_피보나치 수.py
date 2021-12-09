import sys
input = sys.stdin.readline

def do():
    def fibonacci(x):
        if (x <= 1):
            return x
        elif (memo[x] != 0):
            return memo[x]
        else:
            memo[x] = fibonacci(x - 2) + fibonacci(x - 1)
            return memo[x]
    
    N = INF(input())
    memo = [0] * (N + 1)
    print(fibonacci(N))

do()
