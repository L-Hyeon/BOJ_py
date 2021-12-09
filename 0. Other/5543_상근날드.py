import sys
input = sys.stdin.readline

def do():
    top, mid, bot = int(input()), int(input()), int(input())
    cola, cider = int(input()), int(input())

    print(min(top, mid, bot) + min(cola, cider) - 50)

do()
