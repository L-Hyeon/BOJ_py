from re import L
import sys
input = sys.stdin.readline

def do():
  ball = 1
  for i in range(int(input())):
    a, b = map(int, input().split())
    if (ball == a):
      ball = b
    elif (ball == b):
      ball = a
  
  print(ball)

do()
