import sys
input = sys.stdin.readline

def do():
  for s in input():
    if (s.isupper()):
      sys.stdout.write(chr(65 + (ord(s) - 52) % 26))
    elif (s.islower()):
      sys.stdout.write(chr(97 + (ord(s) - 84) % 26))
    else:
      sys.stdout.write(s)

do()
