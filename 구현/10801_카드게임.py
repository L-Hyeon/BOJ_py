import sys
input = sys.stdin.readline

def do():
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  win = [0, 0]
  for i in range(10):
    if (A[i] > B[i]):
      win[0] += 1
    elif (A[i] < B[i]):
      win[1] += 1
  
  if (win[0] > win[1]):
    print('A')
  elif (win[0] < win[1]):
    print('B')
  else:
    print("D")

do()
