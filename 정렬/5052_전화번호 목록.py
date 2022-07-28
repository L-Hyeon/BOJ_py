import sys
input = sys.stdin.readline

class Node:
  def __init__(self, data):
    self.data = data
    self.children = dict()
    self.fin = False

class Trie:
  def __init__(self):
    self.head = Node(None)
  
  def insert(self, string):
    cur = self.head
    for e in string:
      if (e not in cur.children):
        cur.children[e] = Node(e)
      cur = cur.children[e]
    cur.fin = True

  def isConsistent(self, string):
    cur = self.head
    for e in string:
      if (cur.fin):
        return False
      cur = cur.children[e]
    return True

def slow():
  for _ in range(int(input())):
    trie = Trie()
    lst = list()
    for i in range(int(input())):
      s = input().strip()
      lst.append(s)
      trie.insert(s)
    
    flag = True
    for e in lst:
      if (not trie.isConsistent(e)):
        flag = False
        break
    
    print("YES" if (flag) else "NO")

def do():
  for _ in range(int(input())):
    N = int(input())
    lst = list(input().strip() for i in range(N))
    lst.sort()
    isConsistent = True
    for i in range(N - 1):
      if (lst[i] == lst[i + 1][:len(lst[i])]):
        isConsistent = False
        break
    
    print("YES" if (isConsistent) else "NO")

do()
