import sys
input = sys.stdin.readline

def do():
  res = 0
  for _ in range(int(input())):
    stk = list()
    for e in input().strip():
      if (stk and stk[-1] == e):
        stk.pop()
      else:
        stk.append(e)
    if (not stk):
      res += 1
  print(res)

def fast():
  res = 0
  for _ in range(int(input())):
    word, t = input().strip(), ""
    while (word != t):
      t = word
      word = word.replace("AA", "").replace("BB", "")
    if (not word):
      res += 1
  print(res)

fast()
