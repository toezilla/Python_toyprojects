class TreeNode:
    
    """
    Author: Seunghyun Hwang <innuendobeat@gmail.com>
    Date: 2022-09-08
    Purpose: Implementation of Node for Binary Search Tree
    """
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    """
    Author: Seunghyun Hwang <innuendobeat@gmail.com>
    Date: 2022-09-08
    Purpose: Implementation of Binary Search Tree
    """

    def __init__(self):
        self.root = TreeNode(None)

    def insert(self, data):
        current_node = self.insert_node(self.root, data)
        return current_node is not None

    def insert_node(self, node, data):
        if node.data is None:
            return TreeNode(data)

        if data < node.data:
            node.left = self.insert_node(node.data.left, data)

        if data == node.data:
            print("Error: data duplicated!")
            return

        if data > node.data:
            node.right = self.insert_node(node.data.right, data)

    def find(self, data):
        current_node = self.find_node(self.root, data)
        return current_node

    def find_node(self, node, data):
        if data == node.data:
            return node

        if data < node.data:
            node.left = self.find_node(node.left, data)

        if data > node.data:
            node.right = self.find_node(node.right, data)

    def find_parent(self, node, data):
        if data == node.left.data:
            return node

        if data == node.right.data:
            return node

        if data < node.data:
            node.left = self.find_parent(node.left, data)

        if data > node.data:
            node.right = self.find_parent(node.right, data)

    # finding minimum value in a subtree
    def find_minimum(self, node):
        result = 2147000000
        while node:
            if node.data < result:
                result = node.data
            node = node.left
        return result

    #finding maximum value in a subtree
    def fine_maximum(self, node):
        result = -2147000000
        while node:
            if node.data > result:
                result = node.data
            node = node.right
        return result

    def delete(self, data):
        current_node = self.find_node(self.root, data)

        if not current_node:
            print("Error: There is no such value in the Tree.")
            return

        parent_node = self.find_parent(self.root, data)
        if not current_node.left and not current_node.right:
            if parent_node.left.data == data:
                parent_node.left = None
            elif parent_node.right.data == data:
                parent_node.right = None

        elif (current_node.left and not current_node.right) or (not current_node.left and current_node.right):
            if parent_node.left.data == data:
                parent_node.left = current_node.left
            elif parent_node.right.data == data:
                parent_node.right = current_node.right

        else:
            minimum = self.find_minimum(parent_node.right)
            min_node = self.find_node(self.root, minimum)
            min_parent_node = self.find_parent(self.root, node.data)

            if min_parent_node.left.data == min_node:
                min_parent_node.left.data = None
            elif min_parent_node.right.data == min_node:
                min_parent_node.right.data = None

            current_node.data = minimum