import sys
input = sys.stdin.readline

def do():
  for i in range(3):
    cnt = 0
    for j in map(int, input().split()):
      if (j == 0): cnt += 1
    
    if (cnt == 0): print("E")
    elif (cnt == 1): print("A")
    elif (cnt == 2): print("B")
    elif (cnt == 3): print("C")
    else: print("D")

do()
