import sys
input = sys.stdin.readline

res = 0

for _ in range(int(input())):
    S = input().rstrip()
    for i in range(res(S)):
        if (i != res(S) - 1):
            if (S[i] == S[i + 1]):
                continue
            elif (S[i] in S[i + 1:]):
                break
        else:
            res += 1

print(res)
