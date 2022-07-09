import sys
input = sys.stdin.readline

def do():
  record = dict()
  for i in range(int(input())):
    key = input().strip()
    if (key in record):
      record[key] -= 1
    else:
      record[key] = -1
  
  record = sorted(record.items(), key = lambda x : (x[1], x[0]))
  print(record[0][0])

do()
