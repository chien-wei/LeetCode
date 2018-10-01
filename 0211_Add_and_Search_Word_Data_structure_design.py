class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = {}
        self.isend = False
        
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word[0] not in self.child:
            self.child[word[0]] = WordDictionary()
        if len(word) > 1:
            self.child[word[0]].addWord(word[1:])
        elif len(word) == 1:
            self.child[word[0]].isend = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if word[0] == '.' and len(word) > 1:
            ans = False
            for c in self.child:
                ans = ans or self.child[c].search(word[1:])
            return ans
        elif word[0] == '.' and len(word) == 1:
            ans = False
            for c in self.child:
                ans = ans or self.child[c].isend
            return ans
        elif word[0] not in self.child:
            return False
        elif len(word) > 1:
            return self.child[word[0]].search(word[1:])
        elif len(word) == 1:
            return self.child[word[0]].isend