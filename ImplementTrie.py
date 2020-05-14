# 5/14 LeetCode May Challenge
# https://leetcode.com/explore/learn/card/trie/
class TreeNode:
    def __init__(self, v):
        self.val = v
        self.children = {} # use a hashmap to store children nodes
        self.endhere = False # use boolean to flag a word


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(None)


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i, v in enumerate(word):
            if v not in node.children: # not in the dictionary of children
                node.children[v] = TreeNode(v)
            node = node.children[v]
            if i == len(word) - 1:
                node.endhere = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for v in word:
            if v not in node.children: # not in the dictionary of children
                return False
            node = node.children[v] # move on to look for v's children
        return node.endhere # True if it is a word, False if it is prefix


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for v in prefix:
            if v not in node.children:
                return False
            node = node.children[v]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('word')
param_2 = obj.search('word')
param_3 = obj.startsWith('wo')
print(param_2, param_3)
obj.insert('apple')
param_4 = obj.search('app')
param_5 = obj.startsWith('app')
print(param_4, param_5)
obj.insert('app')
param_6 = obj.search('app')
print(param_6)
