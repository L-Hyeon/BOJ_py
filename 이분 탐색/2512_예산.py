import sys
input = sys.stdin.readline

def do():
  N = int(input())
  lst = list(map(int, input().split()))
  K = int(input())

  left, right = 0, max(lst)
  while (left <= right):
    mid = (left + right)//2
    s = 0
    for e in lst:
      if (e < mid):
        s += e
      else:
        s += mid
    
    if (s <= K):
      left = mid + 1
    else:
      right = mid - 1
  
  print(right)

do()
