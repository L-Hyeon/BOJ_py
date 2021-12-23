import sys
input = sys.stdin.readline

def do():
  N = input().strip()
  while (N != '0'):
    isPalindrome = True
    for i in range(len(N)//2):
      if (N[i] != N[len(N) - 1 - i]):
        isPalindrome = False
        break
    print("yes" if (isPalindrome) else "no")
    N = input().strip()

do()
