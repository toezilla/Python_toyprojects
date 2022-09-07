class HashTable:
    def __init__(self, size):
        self.size = size
        self.bucket = [None]*(self.size)
        self.value_count = 0


    def show(self):
        print("-----Current Status of Bucket-----")
        print(f"There are {self.value_count} values in bucket.")
        print(self.bucket)


    # digit folding algorithm
    # noinspection PyMethodMayBeStatic
    def hash_function(self, key):
        code = 0
        for s in key:
            code += ord(str(s))
        return code

    # linear probing
    def collision_control(self, index):
        for idx in range(index+1, 2**31):
            if self.bucket[idx] is None:
                return idx


    def add(self, key, value):
        index = self.hash_function(key)
        if self.value_count == self.size:
            print("Error: Bucket is Full!")
            return

        if self.bucket[index] is not None:
            index = self.collision_control(index)

        self.bucket[index] = (key, value)
        self.value_count+=1


    def get(self, key):
        index = self.hash_function(key)
        if self.bucket[index][0] == key:
            return self.bucket[index][1]
        for idx in range(index+1, self.size):
            if self.bucket[idx][0] == key:
                return self.bucket[idx][1]
        else:
            print(f"Key {key} not found.")


    def contains_key(self, key):
        index = self.hash_function(key)
        if self.bucket[index][0] == key:
            return True
        for idx in range(index+1, self.size):
            if self.bucket[idx][0] == key:
                return True
        else:
            return False


    def contains(self, value):
        for i in range(self.size):
            if self.bucket[i] is not None:
                if self.bucket[i][1] == value:
                    print("Yes!")
                    return True
        else:
            print("No!")
            return False


    def remove(self, key):
        index = self.hash_function(key)
        if self.bucket[index][0] == key:
            self.bucket[index] = None
            self.value_count-=1
            return
        for idx in range(index+1, self.size):
            if self.bucket[idx][0] == key:
                self.bucket[idx] = None
                self.value_count-=1