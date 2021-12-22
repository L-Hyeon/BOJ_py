import sys
input = sys.stdin.readline

def do():
  def move(d):
      if d == 1:
          dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
      elif d == 2:
          dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
      elif d == 3:
          dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
      elif d == 4:
          dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

  def direction(d):
      if d == 1: return 0, 1
      elif d == 2: return 0, -1
      elif d == 3: return -1, 0
      elif d == 4: return 1, 0
  
  N, M, r, c, K = map(int, input().split())
  lst = list(list(map(int, input().split())) for i in range(N))
  dice = [0, 0, 0, 0, 0, 0, 0]
  for m in list(map(int, input().split())):
    a, b = direction(m)
    if (0 <= r + a < N and 0 <= c + b < M):
        r += a
        c += b
        move(m)
        if (lst[r][c] != 0):
            dice[1] = lst[r][c]
            lst[r][c] = 0
        else:
            lst[r][c] = dice[1]

        print(dice[6])

do()
