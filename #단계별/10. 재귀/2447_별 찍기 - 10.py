import sys
input = sys.stdin.readline

def do():
    def makeStarList(N):
        if (N == 3):
            return ["***", "* *", "***"]
        
        x = makeStarList(N // 3)
        y = list(zip(x, x, x))

        for i in range(len(y)):
            y[i] = ''.join(y[i])
        z = list(zip(x, [' '*(N // 3)]*(N // 3), x))

        for i in range(len(z)):
            z[i] = ''.join(z[i])
        return y + z + y

    N = int(input())
    print('\n'.join(makeStarList(N)))

do()
