import sys
input = sys.stdin.readline

def do():
  def isPalindrome(x):
    if (str(x) == str(x)[::-1]):
      return True
    else:
      return False

  N = int(input())

  INF = 1003001
  sieve = [False, False] + [True]*(INF - 1)
  for i in range(2, int(INF**0.5) + 1):
    if (sieve[i]):
      for j in range(2*i, INF, i):
        sieve[j] = False

  while not (sieve[N] and isPalindrome(N)):
    N += 1
  print(N)

do()
