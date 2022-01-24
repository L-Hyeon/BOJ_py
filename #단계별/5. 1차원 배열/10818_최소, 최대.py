import sys
input = sys.stdin.readline

N = input()
lst = list(map(int, input().split()))

print(min(lst), max(lst))
