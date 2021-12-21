import sys
input = sys.stdin.readline

def do():
  N = int(input())
  words = list(input().strip() for i in range(N))
  res = ""
  for i in range(len(words[0])):
    temp = words[0][i]
    for j in range(1, N):
      if (temp != words[j][i]):
        temp = "?"
    res += temp
  
  print(res)

do()
