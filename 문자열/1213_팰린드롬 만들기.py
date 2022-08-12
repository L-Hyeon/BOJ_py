import sys
input = sys.stdin.readline

def do():
  S = input().strip()
  alpha = [0]*26
  odd = 0
  for e in S:
    t = ord(e) - 65
    if (alpha[t] != 0 and alpha[t] & 1):
      odd -= 1
    elif (alpha[t] % 2 == 0):
      odd += 1
    alpha[t] += 1
  
  if (1 < odd):
    print("I'm Sorry Hansoo")
    return
  
  res = ""
  odd = -1
  for i in range(26):
    for j in range(0, alpha[i]//2):
      res += chr(65 + i)
    if (alpha[i] & 1):
      odd = i
  if (odd != -1):
    res += chr(65 + odd) + res[::-1]
  else:
    res += res[::-1]
  
  print(res)

do()
