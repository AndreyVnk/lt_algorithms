'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
'''

class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]

        curr['*'] = {}

    def search(self, word):
        return self.dfs(self.root, word)

    def dfs(self, node, word):
        for idx, char in enumerate(word):
            if char == '.':
                for val on node.values():
                    if self.dfs(val, word[idx + 1:]):
                        return True
                return False
            else:
                if chat not in node:
                    return False
            node = node[char]
        return '*' in node

# Time: O(n), Space: O(n)

