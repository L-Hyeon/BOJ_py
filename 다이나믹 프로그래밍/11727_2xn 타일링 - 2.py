import sys
input = sys.stdin.readline

def do():
  N = int(input())
  if (N == 1):
    print(1)
    return
  memo = [0]*(N + 1)
  memo[1] = 1
  memo[2] = 3
  for i in range(3, N + 1):
    memo[i] = (memo[i - 1] + 2*memo[i - 2]) % 10007
  
  print(memo[N])

do()
