import sys
input = sys.stdin.readline

for _ in range(int(input())):
    query = list(input().split())
    res = ''

    for s in query[1]:
        for i in range(int(query[0])):
            res += s

    print(res)
