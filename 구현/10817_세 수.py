import sys
input = sys.stdin.readline

def do():
    print(sorted(list(map(int, input().split())))[1])

do()
