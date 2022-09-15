import sys
from itertools import permutations
input = sys.stdin.readline

def do():
  N = int(input())
  K = int(input())
  cards = list(input().strip() for i in range(N))
  nums = set()
  for e in list(permutations(cards, K)):
    nums.add(''.join(e))

  print(len(nums))

do()
