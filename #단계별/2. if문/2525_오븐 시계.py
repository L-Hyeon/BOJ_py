A, B = map(int, input().split())
C = int(input())
B += C
if (B > 59):
  A += B//60
  B %= 60
if (A > 23):
  A %= 24
print(A, B)