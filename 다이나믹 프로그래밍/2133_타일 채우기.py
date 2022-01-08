import sys
input = sys.stdin.readline

def do():
  N = int(input())
  memo = [0]*(31)
  memo[2] = 3
  for i in range(4, N + 1):
    if (i % 2 == 0):
      memo[i] = 3*memo[i - 2] + 2*sum(memo[0:i - 2:2]) + 2
  print(memo[N])

do()
