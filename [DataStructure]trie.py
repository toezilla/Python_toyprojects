from typing import List

class TrieNode:
    
    """
    Author: Seunghyun Hwang <innuendobeat@gmail.com>
    Date: 2022-09-15
    Purpose: Implementation of Node for Trie
    """
    
    def __init__(self):
        self.key = None
        self.data = None
        self.child = {} # number of alphabets
        self.is_end = False

class Trie:
    
    """
    Author: Seunghyun Hwang <innuendobeat@gmail.com>
    Date: 2022-09-15
    Purpose: Implementation of Trie
    """
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, data: str) -> None:
        current_node = self.root
        for word in data:
            if word not in current_node.child:
                current_node.child[word] = TrieNode()
            current_node = current_node.child[word]

        current_node.is_end = True

        return current_node

    def find(self, data: str):
        node = self.root
        for word in data:
            if word not in node.child:
                return False
            node = node.child[word]
        return True
