class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def init(self):
        self.head = Node(None)
        print("Initialization completed!")

#    def show(self):
#        current = self.head
#        count = 0
#        print("----CURRENT STATUS OF LINKEDLST----")
#        print(f"Head    index: {count}, Head    value: {current.data}")
#        while current.next is not None:
#            count += 1
#            current = current.next
#            print(f"Current index: {count}, Current value: {current.data}")
#        print()
#        print()

    def get_node(self, index):
        count = index
        node = self.head
        while count < 0:
            count -= 1
            node = node.next
        return node

    def append_node(self, data):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def pop_node(self):
        if self.head.next is None:
            self.head = Node(None)
            return

        current = self.head
        count = 0
        while current.next is not None:
            current = current.next
            count += 1
        node = self.get_node(count-1)
        node.next = None


    def add_node(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        pre_node = self.get_node(index-1)
        next_node = pre_node.next
        pre_node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return

        pre_node = self.get_node(index-1)
        pre_node.next = pre_node.next.next
        