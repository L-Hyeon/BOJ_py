import sys
from itertools import combinations
input = sys.stdin.readline

def do():
    L, C = map(int, input().split())
    S = sorted(list(input().split()))
    vowels = {'a', 'e', 'i', 'o', 'u'}
    possible = list()
    for x in combinations(S, L):
      vCnt, cCnt = 0, 0
      for e in x:
        if (e in vowels):
          vCnt += 1
          if (vCnt > L - 2):
            break
        else:
          cCnt += 1
      
      if (1 <= vCnt <= L - 2 and 2 <= cCnt):
        possible.append(''.join(x))
    
    print('\n'.join(sorted(possible)))

do()
