class Deque:
    
    """
    Author: Seunghyun Hwang <innuendobeat@gmail.com>
    Date: 2022-09-13
    Purpose: Implementation of Deque
    """
    
    def __init__(self, MAX_SIZE):
        self.array = [None] * MAX_SIZE
        self.front = 0
        self.rear = 0
        self.size = 0
        self.max_size = MAX_SIZE

    # def show(self):
    #     print(self.array)

    def is_empty(self):
        if not self.size:
            print("Empty")
            return True

        print("Not Empty")
        return False

    def is_full(self):
        if self.size == self.max_size:
            print("Full")
            return

        print("Not Full")
        return False

    def size(self):
        print(f"Size of Deque is {self.size}.")
        return self.size

    def add_front(self, data):
        if self.front == 0:
            self.array[self.front] = data
            self.front = self.max_size-1
            self.size += 1
            return

        self.array[self.front] = data
        self.front -= 1
        self.size += 1
        return

    def add_rear(self, data):
        if self.rear == self.max_size-1:
            self.rear = 0
            self.array[self.rear] = data
            self.size += 1
            return

        self.rear += 1
        self.array[self.rear] = data
        self.size += 1
        return

    def delete_front(self):
        if self.front == self.max_size-1:
            self.front = 0
            self.array[self.front] = None
            self.size -= 1
            return

        self.front -= 1
        self.array[self.front] = None
        self.size -= 1
        return

    def delete_rear(self):
        if self.rear == 0:
            self.array[self.rear] = None
            self.rear = self.max_size - 1
            self.size -= 1
            return

        self.array[self.rear] = None
        self.rear += 1
        self.size -= 1
        return

    def get_front(self):
        if self.front == self.max_size-1:
            self.front = 0
            data = self.array[self.front]
            self.array[self.front] = None
            self.size -= 1
            return data

        self.front -= 1
        data = self.array[self.front]
        self.array[self.front] = None
        self.size -= 1
        return data

    def get_rear(self):
        if self.rear == 0:
            data = self.array[self.rear]
            self.array[self.rear] = None
            self.rear = self.max_size - 1
            self.size -= 1
            return data

        data = self.array[self.rear]
        self.array[self.rear] = None
        self.rear += 1
        self.size -= 1
        return data
