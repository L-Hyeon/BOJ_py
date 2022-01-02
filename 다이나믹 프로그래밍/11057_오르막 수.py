import sys
input = sys.stdin.readline

def do():
  N = int(input())
  memo = list(list(0 for i in range(10)) for j in range(N + 1))
  for i in range(10):
    memo[1][i] = 1
  for i in range(2, N + 1):
    for j in range(10):
      for k in range(j + 1):
        memo[i][j] += memo[i - 1][k]
  
  print(sum(memo[N]) % 10007)

do()
