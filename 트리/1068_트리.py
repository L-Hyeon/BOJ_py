import sys
input = sys.stdin.readline

def do():
  def dfs(k, lst):
    lst[k] = -2
    for i in range(len(lst)):
      if (k == lst[i]):
        dfs(i, lst)

  N = int(input())
  tree = list(map(int, input().split()))
  K = int(input())

  dfs(K, tree)
  cnt = 0
  for i in range(len(tree)):
    if (tree[i] != -2 and i not in tree):
      cnt += 1
  print(cnt)

do()
