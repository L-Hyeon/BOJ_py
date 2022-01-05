import sys
input = sys.stdin.readline

def do():
  N = int(input())
  lst = list(map(int, input().split()))
  memo = [0]*N
  for i in range(N):
    for j in range(i):
      if (lst[i] < lst[j]) and (memo[i] < memo[j]):
        memo[i] = memo[j]
    memo[i] += 1
  
  print(max(memo))

def oth():
  N = int(input())
  lst = list(map(int, input().split()))
  memo = [lst[0]]
  for i in range(1, N):
    if (lst[i] < memo[-1]):
      memo.append(lst[i])
    else:
      for j in range(len(memo)):
        if (memo[j] <= lst[i]):
          memo[j] = lst[i]
          break
  print(len(memo))

oth()
