import sys
input = sys.stdin.readline

def timeOut():
  S = list(input().strip())
  cur = len(S)
  for _ in range(int(input())):
    q = list(input().split())
    if (q[0] == 'L'):
      if (cur == 0): continue
      cur -= 1
    elif (q[0] == 'D'):
      if (cur == len(S)): continue
      cur += 1
    elif (q[0] == 'B'):
      if (cur == 0): continue
      S.pop(cur - 1)
      cur -= 1
    elif (q[0] == 'P'):
      S.insert(cur, q[1])
      cur += 1
  
  print(''.join(S))

def do():
  pre = list(input().strip())
  post = list()

  for i in range(int(input())):
    q = list(input().split())
    if (q[0] == 'L'):
      if (not pre): continue
      post.append(pre.pop())
    elif (q[0] == 'D'):
      if (not post): continue
      pre.append(post.pop())
    elif (q[0] == 'B'):
      if (not pre): continue
      pre.pop()
    elif (q[0] == 'P'):
      pre.append(q[1])
  
  pre.extend(post[::-1])
  print(''.join(pre))

do()
