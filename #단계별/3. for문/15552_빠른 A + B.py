import sys

buf = sys.stdin.read().split('\n')

x = int(buf[0])
del buf[0]

for i in range(x):
    a, b = buf[i].split()
    buf[i] = (f"{int(a) + int(b)}\n")

sys.stdout.write(''.join(buf))
