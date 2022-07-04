import sys
input = sys.stdin.readline

def do():
  A, B = input().split()
  A = A[::-1]
  B = int(B)
  res = 0
  for i in range(len(A) - 1, -1, -1):
    e = (ord(A[i]) - 55) if (A[i].isalpha()) else int(A[i])
    res += e*(B**i)
  print(res)

do()
