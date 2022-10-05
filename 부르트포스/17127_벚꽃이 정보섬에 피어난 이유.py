import sys
input = sys.stdin.readline

def do():
  N = int(input())
  lst = list(map(int, input().split()))
  a, res = 1, 0
  for i in range(N - 3):
    a *= lst[i]
    b = 1
    for j in range(i + 1, N - 2):
      b *= lst[j]
      c = 1
      for k in range(j + 1, N - 1):
        c *= lst[k]
        d = 1
        for l in range(k + 1, N):
          d *= lst[l]
        res = max(res, a + b + c + d)
  print(res)

do()
