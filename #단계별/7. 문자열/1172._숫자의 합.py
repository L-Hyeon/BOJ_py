import sys
input = sys.stdin.readline

N = int(input())
query = list(map(int, list(input().rstrip())))

print(sum(query))
