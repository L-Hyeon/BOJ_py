import sys
input = sys.stdin.readline

def do():
  N = int(input())
  lst = list(list(map(int, input().split())) for i in range(N))
  memo = [0]*N
  for i in range(N):
    if (N < i + lst[i][0]):
      continue
    memo[i] += lst[i][1]
    for j in range(i + lst[i][0], N):
      memo[j] = max(memo[j], memo[i])
  print(max(memo))

do()
