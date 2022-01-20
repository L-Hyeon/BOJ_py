import sys, heapq
input = sys.stdin.readline

def do():
  N = int(input())
  cards = sorted(list(int(input()) for i in range(N)))
  heapq.heapify(cards)
  
  res = 0
  while (1 < len(cards)):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    res += a + b
    heapq.heappush(cards, a + b)
  
  print(res)

do()
