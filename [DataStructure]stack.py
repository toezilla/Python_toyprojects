class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]

    def show_stack(self):
        return self.stack

    def isEmpty(self):
        if self.stack:
            return 1
        else:
            return 0

    def push(self, number):
        self.stack.append(number)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return "Error: Stack is Empty!"