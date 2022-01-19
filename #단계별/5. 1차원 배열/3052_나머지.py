cnt = set()
for i in range(10):
    x = int(input())
    remain = x % 42
    cnt.add(remain)

print(res(cnt))
