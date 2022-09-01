import sys
input = sys.stdin.readline

def do():
    for _ in range(int(input())):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        d = (abs(x1 - x2)**2 + abs(y1 - y2)**2)**0.5
        if (r2 < r1):
            r2, r1 = r1, r2
        
        if (d == 0):
            if (r1 == r2):
                print(-1)
            else:
                print(0)
        else:
            if (d == r1 + r2 or d + r1 == r2):
                print(1)
            elif (d < r1 + r2 and d + r1 > r2):
                print(2)
            else:
                print(0)

do()
