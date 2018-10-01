class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = {}
        self.isend = False
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if word[0] not in self.child:
            self.child[word[0]] = Trie()
        if len(word) > 1:
            self.child[word[0]].insert(word[1:])
        elif len(word) == 1:
            self.child[word[0]].isend = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word[0] not in self.child:
            return False
        if len(word) > 1:
            return self.child[word[0]].search(word[1:])
        elif len(word) == 1:
            return self.child[word[0]].isend
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if prefix[0] not in self.child:
            return False
        if len(prefix) > 1:
            return self.child[prefix[0]].startsWith(prefix[1:])
        elif len(prefix) == 1:
            return self.child[prefix[0]].isend or len(self.child[prefix[0]].child) > 0
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)