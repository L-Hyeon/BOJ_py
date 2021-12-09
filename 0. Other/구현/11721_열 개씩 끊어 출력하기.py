import sys
input = sys.stdin.readline

def do():
    Q = input().rstrip()
    for i in range(1, len(Q) + 1):
        sys.stdout.write(Q[i - 1])
        if (i % 10 == 0):
            sys.stdout.write('\n')

do()
