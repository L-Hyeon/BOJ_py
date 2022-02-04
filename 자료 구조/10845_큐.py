import sys
input = sys.stdin.readline

def do():
  q = list()
  for i in range(int(input())):
    query = input().split()
    if (query[0] == "push"):
      q.append(query[1])
    elif (query[0] == "pop"):
      print(q.pop(0) if (q) else -1)
    elif (query[0] == "size"):
      print(len(q))
    elif (query[0] == "empty"):
      print(0 if (q) else 1)
    elif (query[0] == "front"):
      print(q[0] if (q) else -1)
    elif (query[0] == "back"):
      print(q[-1] if (q) else -1)

do()
