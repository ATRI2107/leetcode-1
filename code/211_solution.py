#    root
#    |  |
#    b  d
#    |  |
#    a  a
#    |  |
#    d* d*

# N = length of word
# Insert O(N) T/S
# Search with out . O(N)~T O(1)~S
# Search with . O(#total nodes in DS)~T O(#total nodes in DS)~S

class WordDictionary:
    class TrieNode(defaultdict):
        def __init__(self):
            super().__init__(WordDictionary.TrieNode)
            self.terminal = False
    
    def __init__(self):
        """ Initialize your data structure here."""
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        """ Adds a word into the data structure. """
        node = self.root
        for char in word: node = node[char]
        node.terminal = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. 
        A word could contain the dot character '.' to represent any one letter.
        """
        n = len(word)
        
        def dfs(node, i):
            if i == n: return node.terminal
            char = word[i]
            if char == '.':
                for key in node:
                    if dfs(node[key], i+1): return True
                return False
            elif char not in node: return False
            else: return dfs(node[char], i+1)
            
        return dfs(self.root, 0)
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)