import sys
input = sys.stdin.readline

def do():
  lst = list()
  for _ in range(int(input())):
    S = input().strip()
    temp = ''
    for s in S:
      if (s.isdigit()):
        temp += s
      elif(temp != ''):
        lst.append(int(temp))
        temp = ''
    if (temp != ''):
      lst.append(int(temp))
  print(*sorted(lst), sep = '\n')

do()
