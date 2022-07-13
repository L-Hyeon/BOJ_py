import sys
input = sys.stdin.readline

def do():
  N = int(input())
  M = int(input())
  S = input().strip()
  pat = 'I' + 'OI'*N
  res = 0

  for i in range(len(pat), M):
    temp = S[i - len(pat) : i]
    if (temp == pat):
      res += 1
  
  print(res)

def fast():
  N = int(input())
  M = int(input())
  S = input().strip()
  res, cnt, i = 0, 0, 0
  while (i < M - 1):
    if (S[i: i + 3] == "IOI"):
      i += 2
      cnt += 1
      if (cnt == N):
        res += 1
        cnt -= 1
    else:
      i += 1
      cnt = 0
  
  print(res)

fast()
