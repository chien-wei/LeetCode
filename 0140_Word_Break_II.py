# Prefix tree + backtracking: TLE on full of "a", "aa" in wordDict which make the Trie useless...
class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
    def insert(self, word):
        children = self.children
        if len(word) == 1:
            children[word] = children.get(word, Trie())
            children[word].isEnd = True
        else:
            children[word[0]] = children.get(word[0], Trie())
            children[word[0]].insert(word[1:])
            
    def search(self, word):
        children = self.children
        if len(word) == 1 and word in children and children[word].isEnd:
            return True
        elif len(word) > 1 and word[0] in children:
            return children[word[0]].search(word[1:])
        else:
            return False
        
    def prefix(self, word):
        res = []
        acc = ""
        cur = self
        for i in range(len(word)):
            if word[i] in cur.children:
                acc = acc + word[i]
                cur = cur.children[word[i]]
            else:
                break
            if cur.isEnd:
                res.append(acc)
        return res

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
            
        def backtrack(s, i, acc, res):
            if i == len(s):
                res.append(acc)
            prefixes = trie.prefix(s[i:])
            for prefix in prefixes:
                acc.append(prefix)
                backtrack(s, i+len(prefix), acc[:], res)
                acc.pop()
            
        result = []
        backtrack(s, 0, [], result)
        for i in range(len(result)):
            result[i] = " ".join(result[i])
        return result
                
