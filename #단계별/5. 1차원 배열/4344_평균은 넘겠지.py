for _ in range(int(input())):
    N, *lst = map(int, input().split())
    avg = sum(lst) / N
    aboveAvg = 0
    for i in range(N):
        if (avg < lst[i]):
            aboveAvg += 1
    
    print(f"{100*aboveAvg / N:.3f}%")
