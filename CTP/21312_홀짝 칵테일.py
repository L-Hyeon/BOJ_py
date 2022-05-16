import sys
input = sys.stdin.readline

def do():
  lst = list(map(int, input().split()))
  odd = list(lst[i] & 1 for i in range(3))
  cnt = odd.count(1)
  if (cnt == 2):
    if (odd[0] == 0):
      print(lst[1]*lst[2])
    elif (odd[1] == 0):
      print(lst[0]*lst[2])
    else:
      print(lst[0]*lst[1])
  elif (cnt == 1):
    if (odd[0] == 1):
      print(lst[0])
    elif (odd[1] == 1):
      print(lst[1])
    else:
      print(lst[2])
  else:
    print(lst[0]*lst[1]*lst[2])

do()
