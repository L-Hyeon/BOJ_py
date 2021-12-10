class Node():
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None

class Linked_List():
    def __init__(self):
        head = None
        tail = None
        size = 0
    
    def isEmpty(self):
        if (size):
            return False
        else:
            return True
    
    def insertFront(self, x):
        if (self.isEmpty()):
            head = Node(x)
            size += 1
            tail = head
        else:
            t = Node(x)
            t.next = head
            head = t
            size += 1
    
    def removeFront(self):
        if (self.isEmpty()):
            return
        else:
            x = head
            head = x.next
            del x
            size -= 1
    
    def insertBack(self, x):
        if (self.isEmpty()):
            tail = Node(x)
            size += 1
            head = tail
        else:
            t = Node(x)
            t.prev = tail
            tail = t
            size += 1
    
    def removeBack(self):
        if (self.isEmpty()):
            return
        else:
            x = tail
            tail = x.prev
            del x
            size -= 1
