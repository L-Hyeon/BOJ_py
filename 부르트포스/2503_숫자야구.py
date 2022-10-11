import sys
from itertools import permutations
input = sys.stdin.readline

def do():
  possible = list(permutations(range(1, 10), 3))
  for _ in range(int(input())):
    q, strike, ball = input().split()
    q, strike, ball = list(map(int, q)), int(strike), int(ball)
    temp = list()
    for e in possible:
      s, b = 0, 0
      for i in range(3):
        if (q[i] == e[i]):
          s += 1
          if (strike < s):
            break
        elif (q[i] in e):
          b += 1
          if (ball < b):
            break
      if (strike == s and ball == b):
        temp += [e]
    possible = temp

  print(len(possible))

do()
