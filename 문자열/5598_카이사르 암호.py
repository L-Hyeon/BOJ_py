import sys
input = sys.stdin.readline

def do():
  s = input().strip()
  res = ''
  for e in s:
    res += chr(((ord(e) - 68)%26) + 65)
  print(res)

do()
