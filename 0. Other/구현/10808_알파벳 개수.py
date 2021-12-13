import sys
input = sys.stdin.readline

def do():
  cnt = [0]*26
  for s in input().strip():
    cnt[ord(s) - 97] += 1
  
  print(*cnt)

do()
