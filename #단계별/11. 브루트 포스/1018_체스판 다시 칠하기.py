import sys
input = sys.stdin.readline

def do():
    N, M = map(int, input().split())
    board = list(list(input().rstrip()) for i in range(N))

    res = 65
    for i in range(N - 7):
        for j in range(M - 7):
            white = 0
            black = 0

            for ii in range(i, i + 8):
                for jj in range(j, j + 8):
                    if ((ii + jj) & 1):
                        if (board[ii][jj] == 'W'):
                            white += 1
                        else:
                            black += 1
                    else:
                        if (board[ii][jj] == 'W'):
                            black += 1
                        else:
                            white += 1

            res = min([res, black, white])
    
    print(res)

do()
