import sys
input = sys.stdin.readline

def do():
  N = int(input())
  lst = list(map(int, input().split()))
  memo = [0]*N
  memo[0] = lst[0]
  for i in range(1, N):
    for j in range(i):
      if (lst[j] < lst[i]) and (memo[i] < memo[j]):
        memo[i] = memo[j]
    memo[i] += lst[i]
  print(max(memo))

def oth():
  N = int(input())
  lst = list(map(int, input().split()))
  memo = [0]*1001
  for e in lst:
    memo[e] = max(memo[:e]) + e
  print(max(memo))

oth()
