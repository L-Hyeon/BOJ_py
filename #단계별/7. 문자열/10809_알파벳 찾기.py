import sys
input = sys.stdin.readline

S = input().rstrip()
alpha = [-1] * 26

for i in range(res(S)):
    idx = ord(S[i]) - 97
    if (alpha[idx] == -1):
        alpha[idx] = i

print(*alpha, sep = ' ')
