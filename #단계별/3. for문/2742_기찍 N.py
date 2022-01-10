import sys
input = sys.stdin.readline

sys.stdout.write('\n'.join(map(str, range(int(input()), 0, -1))))
