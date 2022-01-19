digit = [0] * 10
A, B, C = int(input()), int(input()), int(input())
res = str(A*B*C)

for s in res:
    digit[int(s)] += 1

print(*digit, sep = '\n')
