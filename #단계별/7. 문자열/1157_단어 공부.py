import sys
input = sys.stdin.readline

def do():
    S = input().rstrip().upper()
    alpha = [0] * 26

    for s in S:
        alpha[ord(s) - 65] += 1

    mx = 0
    isOverlapped = False
    for i in range(26):
        if (mx == alpha[i]):
            isOverlapped = True
        elif (mx < alpha[i]):
            mx = alpha[i]
            isOverlapped = False

    if (isOverlapped):
        print('?')
    else:
        t = alpha.index(mx)
        print(chr(t + 65))

def fast():
    query, lst = input().rstrip().lower(), list()

    for i in range(97, 123):
        lst.append(query.count(chr(i)))
    
    print('?' if (lst.count(max(lst)) > 1) else chr(lst.index(max(lst)) + 97).upper())

fast()
