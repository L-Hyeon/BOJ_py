import sys
input = sys.stdin.readline

def do():
  for _ in range(int(input())):
    N = int(input())
    pre = sorted(list(input().split()))
    post = sorted(list(input().split()))
    isCheater = False
    for i in range(N):
      if (pre[i] != post[i]):
        isCheater = True
    print("CHEATER" if (isCheater) else "NOT CHEATER")

do()
