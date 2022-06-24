import sys
input = sys.stdin.readline

def do():
  for _ in range(int(input())):
    N = int(input())
    lst = list(list(map(int, input().split())) for j in range(2))
    memo = list(list(lst[j][i] for i in range(N)) for j in range(2))

    for i in range(1, N):
      if (i == 1):
        memo[0][1] += memo[1][0]
        memo[1][1] += memo[0][0]
        continue
      memo[0][i] += max(memo[1][i - 1], memo[1][i - 2])
      memo[1][i] += max(memo[0][i - 1], memo[0][i - 2])
    
    print(max(memo[0][N - 1], memo[1][N - 1]))

do()
