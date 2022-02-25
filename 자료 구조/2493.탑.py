import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def do():
  N = int(input())
  lst = list(map(int, input().split()))

  res = [0]*N
  heap = [(lst[N - 1], N - 1)]
  for i in range(N - 2, -1, -1):
    while (heap):
      if (heap[0][0] < lst[i]):
        res[heap[0][1]] = i + 1
        heappop(heap)
      else:
        break

    heappush(heap, (lst[i], i))

  print(*res)

def fast():
  N = int(input())
  lst = [100000001] + list(map(int, input().split()))

  stk = [0]
  res = list()

  for i in range(1, N + 1):
    while (True):
      if (lst[i] > lst[stk[-1]]):
        stk.pop()
      else:
        break
    
    stk.append(i)
    res.append(stk[-2])
  
  print(*res)

fast()
