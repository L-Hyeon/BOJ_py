import sys
input = sys.stdin.readline

def do():
  word = ''
  flag = False
  for c in input().strip():
    if (flag):
      sys.stdout.write(c)
      if (c == '>'):
        flag = False
    elif (c == ' '):
      sys.stdout.write(word[::-1] + ' ')
      word = ''
    elif (c == '<'):
      flag = True
      sys.stdout.write(word[::-1] + '<')
      word = ''
    else:
      word += c
  if (word):
    sys.stdout.write(word[::-1])

do()
