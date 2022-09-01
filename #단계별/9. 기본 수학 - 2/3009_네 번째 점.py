import sys
input = sys.stdin.readline

def do():
    X, Y = list(), list()
    for i in range(3):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    
    res = [0, 0]
    for i in range(3):
        if (X.count(X[i]) == 1):
            res[0] = X[i]
        if (Y.count(Y[i]) == 1):
            res[1] = Y[i]
    
    print(*res)

do()
