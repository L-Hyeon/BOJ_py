import sys
input = sys.stdin.readline

def do():
  N = int(input())
  tree = dict()
  for i in range(N - 1):
    a, b = map(int, input().split())
    if (a in tree): tree[a] += [b]
    else: tree[a] = [b]
    if (b in tree): tree[b] += [a]
    else: tree[b] = [a]
  
  leaf = list()
  stk = [(1, 0)]
  visited = [False]*(N + 1)
  visited[1] = True
  while (stk):
    cur, dep = stk.pop()
    if (cur != 1 and len(tree[cur]) == 1):
      leaf.append(dep)
      continue

    for e in tree[cur]:
      if (not visited[e]):
        stk.append((e, dep + 1))
        visited[e] = True
  
  print("Yes" if (sum(leaf) & 1) else "No")

do()
