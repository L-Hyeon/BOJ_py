import sys
input = sys.stdin.readline

def do():
  N, K = map(int, input().split())
  lst = list(map(int, input().split()))
  l, r = 0, K - 1
  mx = sum(lst[:K])
  s = mx
  while (r < N - 1):
    r += 1
    s += lst[r]
    s -= lst[l]
    l += 1
    if (mx < s):
      mx = s
  print(mx)

do()
