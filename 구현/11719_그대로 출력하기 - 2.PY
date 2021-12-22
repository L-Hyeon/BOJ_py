import sys

def do():
    while True:
        try:
            print(input())
        except EOFError:
            break

do()
