import sys
input = sys.stdin.readline

def do():
    M, D = map(int, input().split())
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    acc = D - 1
    for i in range(M - 1):
        acc += month[i]
    print(date[acc % 7])

do()
