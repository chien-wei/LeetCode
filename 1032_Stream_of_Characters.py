class Trie:
    def __init__(self):
        self.childs = {}
        self.isEnd = False
    
    def insert(self, word):
        if len(word) == 0:
            self.isEnd = True
        elif word[0] in self.childs:
            self.childs[word[0]].insert(word[1:])
        else:
            self.childs[word[0]] = Trie()
            self.childs[word[0]].insert(word[1:])
    def prefix(self, word):
        cur = self
        i = 0
        while i < len(word) and word[i] in cur.childs:
            cur = cur.childs[word[i]]
            i += 1
            if cur.isEnd:
                return True
        return False

class StreamChecker:
    # just put the word reversely in our Trie
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.queue = []

    def query(self, letter: str) -> bool:
        self.queue.insert(0, letter)
        return self.trie.prefix(self.queue)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)