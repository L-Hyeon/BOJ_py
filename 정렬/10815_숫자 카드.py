import sys
input = sys.stdin.readline

def do():
  N = int(input())
  A = set(map(int, input().split()))
  M = int(input())
  
  for e in map(int, input().split()):
    print(1 if (e in A) else 0, end = ' ')

do()
