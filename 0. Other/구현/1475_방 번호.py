import sys
input = sys.stdin.readline

def do():
  cnt = [0]*9
  for i in input().strip():
    if (i == '9'):
      cnt[6] += 1
    else:
      cnt[int(i)] += 1
  
  if (cnt[6] & 1):
    cnt[6] = cnt[6]//2 + 1
  else:
    cnt[6] //= 2
  print(max(cnt))

do()
