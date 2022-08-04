import sys
input = sys.stdin.readline

def do():
  for _ in range(int(input())):
    print(sorted(list(map(int, input().split())), reverse = True)[2])

do()
