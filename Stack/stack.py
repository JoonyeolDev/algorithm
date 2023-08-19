class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedListStack:
    def __init__(self):
        self.head = None
        
    def push(self, value):
        self.head = Node(value, self.head)
    
    def pop(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        return node.data
    
    def top(self):
        if self.head is None:
            return None
        return self.head.data
    
    def is_empty(self):
        return self.head is None

stack = LinkedListStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(len(stack))