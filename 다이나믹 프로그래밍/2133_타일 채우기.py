import sys
input = sys.stdin.readline

def do():
  N = int(input())
  if (N == 1):
    print(1)
    return
  memo = [0]*(N + 1)
  memo[2] = 3
  for i in range(4, N + 1, 2):
    memo[i] = 3*memo[i - 2] + 2*sum(memo[0:i - 2:2]) + 2
  print(memo[N])

do()
