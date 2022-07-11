import sys
input = sys.stdin.readline

time = 0
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
q = input().rstrip()

for i in range(res(q)):
    for j in range(8):
        if (q[i] in dial[j]):
            time += j + 3
            break

print(time)
