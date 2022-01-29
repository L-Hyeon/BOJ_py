import sys
input = sys.stdin.readline

def do():
  S = input().strip()
  l = len(S)
  isPelindrome = True
  for i in range(l//2):
    if (S[i] != S[l - i - 1]):
      isPelindrome = False
      break
  
  print(1 if (isPelindrome) else 0)

do()
