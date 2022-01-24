for i in range(int(input())):
    ans = input()
    res = 0
    score = 0
    for s in ans:
        if (s == 'O'):
            score += 1
            res += score
        else:
            score = 0

    print(res)
    