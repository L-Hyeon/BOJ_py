import sys
input = sys.stdin.readline

def do():
  N = int(input())
  if (N == 1):
    print(1)
    return
  memo = [0]*(N + 1)
  sq = list(i**2 for i in range(1, 317))
  for i in range(1, N + 1):
    memo[i] = 100000
    for j in sq:
      if (i < j):
        break
      if (memo[i - j] + 1 < memo[i]):
        memo[i] = memo[i - j] + 1
  
  print(memo[i])

def fast():
  N = int(input())
  while (N % 4 == 0):
    N //= 4
  if (N % 8 == 7):
    print(4)
    return
  
  p, isSquare = 3, True
  if (N % 2 == 0):
    N /= 2
    isSquare = False
  
  while (p <= N):
    isDividedOddTimes = False
    while (N % p == 0):
      N /= p
      isDividedOddTimes = not isDividedOddTimes
    isSquare = isSquare and not isDividedOddTimes
    if (isDividedOddTimes) and (p % 4 == 3):
      print(3)
      return
    p += 2
  else:
    if (isSquare):
      print(1)
    else:
      print(2)

fast()
