class MaxHeap:
    
    """
    Author: Seunghyun Hwang <innuendobeat@gmail.com>
    Date: 2022-09-08
    Purpose: Implementation of Max Heap
    """
    
    def __init__(self, size):
        self.size = size
        self.array = [None] * self.size
        self.leaf = 0

    def show(self):
        print(self.array)

    def is_full(self):
        for i in range(1, self.size):
            if self.array[i] is None:
                print("Max Heap is not full!")
                return False
        print("Max Heap is Full!")
        return True

    def is_empty(self):
        for i in range(1, self.size):
            if self.array[i]:
                print("Max Heap is not empty!")
                return False
        print("Max Heap is empty!")
        return True

    def insert(self, data):
        if self.is_full is True:
            print(self.is_full)
            return

        if self.leaf == 0:
            self.array[1] = data
            self.leaf = 1
            return data

        self.array[(index := self.leaf+1)] = data
        self.leaf += 1

        while index > 1:
            if self.array[index] > self.array[index//2]:
                self.array[index], self.array[index//2] = self.array[index//2], self.array[index]
                index = index//2
        return data

    # noinspection PyMethodMayBeStatic
    def change_node(self, index, array):
        current = array[index]
        left = array[index*2]
        right = array[index*2+1]

        # if node has 0 children
        if not left and not right:
            return

        # if node has 1 child
        ## if there is only left node
        if left and not right:
            if left > current:
                array[index], array[index*2] = array[index*2], array[index]
                return self.change_node(index*2, array)
        ## if there is only right node
        if right and not left:
            if right > current:
                array[index], array[index*2+1] = array[index*2+1], array[index]
                return self.change_node(index*2+1, array)

        # if node has 2 children
        if left and right:
            if left >= right:
                if left > current:
                    array[index], array[index * 2] = array[index * 2], array[index]
                    return self.change_node(index * 2, array)
            if right >= left:
                if right > current:
                    array[index], array[index * 2 + 1] = array[index * 2 + 1], array[index]
                    return self.change_node(index * 2 + 1, array)


    def pop(self):
        self.array[1], self.array[self.leaf] = self.array[self.leaf], None
        self.change_node(1, self.array)
        self.leaf -= 1
