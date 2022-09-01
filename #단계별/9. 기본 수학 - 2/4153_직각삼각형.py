import sys
input = sys.stdin.readline

def do():
    q = list(map(int, input().split()))
    while (q[0] != 0 and q[1] != 0 and q[2] != 0):
        q.sort()

        if (q[2]**2 == q[1]**2 + q[0]**2):
            print("right")
        else:
            print("wrong")
        
        q = list(map(int, input().split()))

do()
