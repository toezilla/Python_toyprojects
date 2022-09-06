from collections import deque

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

class Queue:
    def __init__(self, size):
        self.queue = deque()
        self.space = size

    def init(self):
        self.queue = deque()
        print("Initiation completed!")

    def enque(self, number):
        if self.space == 0:
            print("Error: Queue is Full!")
        else:
            self.queue.append(number)
            self.space -= 1
            print(f"{number} successfully enqued!")

    def dequeue(self):
        if self.queue:
            print(f"{(tmp:=self.queue.popleft())} successfully dequeued!")
            return tmp
        else:
            print("Error: Queue is Empty!")

    def isEmpty(self):
        if self.queue:
            print("Empty!")
        else:
            print("Not empty!")

    def peek(self):
        if self.queue:
            print(f"{(tmp:=self.queue[0])} will be dequed next!")
            return tmp
        else:
            print("Error: Queue is Empty!")

    def is_full(self):
        if self.space == 0:
            print("Full!")
        else:
            print("Not FUll!")

    def size(self):
        print(f"Currently {(length:=len(self.queue))} items in queue")
        return length