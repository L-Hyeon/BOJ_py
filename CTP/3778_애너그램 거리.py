import sys
input = sys.stdin.readline

def do():
  for _ in range(int(input())):
    A = input().strip()
    B = input().strip()

    alpha = [0]*26
    temp = ord('a')

    for s in A:
      alpha[ord(s) - temp] += 1
    for s in B:
      alpha[ord(s) - temp] -= 1
    
    res = 0
    for x in alpha:
      if (x != 0):
        res += abs(x)
    
    print(f'Case #{_ + 1}: {res}')

do()