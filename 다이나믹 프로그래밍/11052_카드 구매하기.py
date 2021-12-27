import sys
input = sys.stdin.readline

def do():
  N = int(input())
  lst = [0] + list(map(int, input().split()))
  memo = [0]*(N + 1)
  memo[1] = lst[1]
  for i in range(2, N + 1):
    for j in range(1, i + 1):
      if (memo[i] < memo[i - j] + lst[j]):
        memo[i] = memo[i - j] + lst[j]
  
  print(memo[N])

do()
