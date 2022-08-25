import sys
input = sys.stdin.readline

def do():
  A, B = 0, 0
  score = 0
  for _ in range(int(input())):
    t, time = input().split()
    m, s = map(int, time.split(':'))
    if (t == '1'):
      if (score == 0):
        A += 48*60 - (60*m + s)
      score += 1
      if (score == 0):
        if (0 < B):
          B = B - (48*60 - (60*m + s))
    else:
      if (score == 0):
        B += 48*60 - (60*m + s)
      score -= 1
      if (score == 0):
        if (0 < A):
          A = A - (48*60 - (60*m + s))
  print('{:0>2}:{:0>2}'.format(A//60,A % 60))
  print('{:0>2}:{:0>2}'.format(B//60,B % 60))

do()
