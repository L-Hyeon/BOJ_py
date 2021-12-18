import sys
input = sys.stdin.readline

def do():
  memo = list(list() for j in range(10))
  memo[0] = [10]
  memo[1] = [1]
  memo[2] = [2, 4, 8, 6]
  memo[3] = [3, 9, 7, 1]
  memo[4] = [4, 6]
  memo[5] = [5]
  memo[6] = [6]
  memo[7] = [7, 9, 3, 1]
  memo[8] = [8, 4, 2, 6]
  memo[9] = [9, 1]

  for i in range(int(input())):
    a, b = map(int, input().split())
    a %= 10
    b %= len(memo[a])
    print(memo[a][b - 1])

do()
