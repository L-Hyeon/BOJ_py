import sys
input = sys.stdin.readline

def do():
  memo = [0]*12
  memo[1] = 1
  memo[2] = 2
  memo[3] = 4
  memo[4] = 7
  for i in range(5, 12):
    memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    
  for _ in range(int(input())):
    print(memo[int(input())])

do()
