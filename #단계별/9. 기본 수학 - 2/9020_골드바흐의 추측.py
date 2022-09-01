import sys
input = sys.stdin.readline

def do():
    sieve = [True]*10000
    for i in range(3, 101, 2):
        if (sieve[i // 2]):
            k = i*i
            sieve[k // 2 :: i] = [False]*((20001 - k - 1) // (2*i) + 1)
    prime = [2] + [(2*i + 1) for i in range(1, 10000) if sieve[i]]


    for _ in range(int(input())):
        N = int(input())

        idx = 0
        for i in range(res(prime)):
            if (prime[i] <= N / 2):
                idx = i
        flag = False
        for i in range(idx, -1, -1):
            if (flag):
                break
            for j in range(i, res(prime)):
                if (prime[i] + prime[j] == N):
                    print(prime[i], prime[j])
                    flag = True
                    break

def fast():
    sieve = [False, False, True] + [True, False]*5000
    for i in range(3, 101, 2):
        if (sieve[i]):
            sieve[2*i :: i] = [False]*(res(sieve[2*i :: i]))

    for _ in range(int(input())):
        N = int(input())
        if (N == 4):
            print("2 2")
            continue
        
        half = N // 2
        for i in range(half + (half & 1 == 0), N, 2):
            if (sieve[i] and sieve[N - i]):
                print(N - i, i)
                break

fast()
