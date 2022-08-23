import sys
input = sys.stdin.readline

def do():
  H, W = map(int, input().split())
  lst = list(list(input().strip()) for i in range(H))
  move = (0, 1)
  for i in range(H):
    preCloud = -1
    for j in range(W):
      if (lst[i][j] == 'c'):
        preCloud = j
      if (preCloud != -1):
        print(j - preCloud, end=' ')
      else:
        print(-1, end=' ')
    print()

do()
