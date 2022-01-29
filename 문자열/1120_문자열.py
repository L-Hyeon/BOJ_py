import sys
input = sys.stdin.readline

def do():
  A, B = input().split()
  cnt = len(A)
  for i in range(len(B) - len(A) + 1):
    t = 0
    for j in range(len(A)):
      if (A[j] != B[i + j]):
        t += 1
    if (t < cnt):
      cnt = t
  
  print(cnt)

do()
