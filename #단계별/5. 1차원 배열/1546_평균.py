N = int(input())
lst = list(map(int, input().split()))
mx = max(lst)

res = 0
for i in range(N):
    res += 100*lst[i] / mx

print(res / N)
