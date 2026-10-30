
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.value

    def display(self):
        current = self.top
        values = []
        while current is not None:
            values.append(current.value)
            current = current.next
        print("Stack (top to bottom):", values)


stack = LinkedStack()
stack.push("Apple")
stack.push("Banana")
stack.push("Mango")
stack.display()
print("Popped:", stack.pop())
print("Top value:", stack.peek())
stack.display()
