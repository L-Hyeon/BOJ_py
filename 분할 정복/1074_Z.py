import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def do():
  def cal(n, r, c):
    if (n == 0):
      return 0
    return 2*(r%2) + (c%2) + 4*cal(n - 1, r//2, c//2)

  N, r, c = map(int, input().split())
  print(cal(N, r, c))

do()
