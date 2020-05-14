'''
232 ms
'''
class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
    
    def _find(self, word, startsWith = False, insert = False):
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            
            if insert and not node.children[idx]:
                node.children[idx] = TrieNode()
                
            node = node.children[idx]
            if not node:
                return False
        
        if insert:
            node.end = True
        else:
            return node.end or startsWith

    def insert(self, word):
        self._find(word, insert = True)
        
    def search(self, word):
        return self._find(word)    

    def startsWith(self, prefix):
        return self._find(prefix, startsWith = True)
        
        
'''
Fastest 104 ms
'''
class Trie:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        root = self.trie
        for c in word:
            if c not in root:
                root[c]={}
            root = root[c]
        root['#'] = '#'

    def search(self, word: str) -> bool:
        # start = self.trie
        # for c in word:
        #     if c not in start:
        #         return False
        #     start = start[c]
        # if '#' in start:
        #     return True
        # return False
        return self.startsWith(word + '#')

    def startsWith(self, prefix: str) -> bool:
        start = self.trie
        for c in prefix:
            if c not in start:
                return False
            start = start[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)

'''
fast 108 ms using dictionary
'''

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'
        
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True
