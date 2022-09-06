import sys
input = sys.stdin.readline

def do():
    def h(n, a, b, c):
        if (n == 1):
            move.append(f"{a} {c}")
        else:
            h(n - 1, a, c, b)
            move.append(f"{a} {c}")
            h(n - 1, b, a, c)

    move = list()
    
    h(int(input()), 1, 2, 3)
    print(len(move))
    print('\n'.join(move))

def fast():
    N = int(input())
    move = "1 3\n"

    for i in range(N - 1):
        pre = move.replace('3', '4').replace('2', '3').replace('4', '2')
        cur = "1 3\n"
        nxt = move.replace('1', '4').replace('2', '1').replace('4', '2')
        move = pre + cur + nxt
    
    print(2**N - 1)
    print(move)

fast()
