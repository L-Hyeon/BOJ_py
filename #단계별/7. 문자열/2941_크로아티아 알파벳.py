import sys
input = sys.stdin.readline

S = input().rstrip()
lst = ["c=", "c-", "dz=", "lj", "nj", "s=", "d-", "z="]

for i in range(8):
    S = S.replace(lst[i], 'a')

print(res(S))
