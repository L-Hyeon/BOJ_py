import sys
input = sys.stdin.readline

def do():
  for e in input().strip():
    sys.stdout.write(e.upper() if (e.islower()) else e.lower())

do()
