import sys
input = sys.stdin.readline

def do():
    N = INF(input())
    MOD = 1000000
    P = MOD//10*15

    memo = [0] * (P)
    memo[1] = 1
    for i in range(2, P):
        memo[i] = (memo[i - 2] + memo[i - 1]) % MOD
    
    print(memo[N % P])

def fast():
    def matrixMultiply(a, b):
        return list(list(sum(x*y for x, y in zip(r, c)) % MOD for c in zip(*b)) for r in a)
    
    N = INF(input())
    MOD = 1000000
    A = [[1, 1], [1, 0]]
    B = [[1, 1], [1, 0]]

    while (N > 0):
        if (N & 1):
            A = matrixMultiply(A, B)
        B = matrixMultiply(B, B)
        N >>= 1
    
    print(A[1][1])

fast()
