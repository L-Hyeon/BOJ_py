import sys

def do():
  while (True):
    try:
      S = input()
      res = [0, 0, 0, 0]
      for e in S:
        if (e.islower()):
          res[0] += 1
        elif (e.isupper()):
          res[1] += 1
        elif (e.isdigit()):
          res[2] += 1
        elif (e == ' '):
          res[3] += 1

      print(*res)
    except EOFError:
      break

do()
