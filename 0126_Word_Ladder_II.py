# DFS: get TLE
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        def nextTrans(s: str) -> set:
            res = set()
            for i in range(len(s)):
                for j in range(26):
                    res.add(s[:i] + chr(ord('a') + j) + s[i+1:])
            res.remove(s)
            return res
        
        def dfs(cur: str, wordSet: set(), acc: List[str], res: List[List[str]]):
            acc.append(cur)
            if cur == endWord:
                if len(res) > 0 and len(res[0]) > len(acc):
                    res.clear()
                res.append(acc)
                return
            
            if len(res) > 0 and len(acc) >= len(res[0]):
                return
            
            trans = nextTrans(cur)
            nextSet = wordSet.intersection(trans)
            for nxt in list(nextSet):
                wordSet.remove(nxt)
                dfs(nxt, wordSet, acc[:], res)
                wordSet.add(nxt)
            
        res = []
        dfs(beginWord, set(wordList), [], res)
        return res

# BFS: get TLE because using intersection, but is more readable
# TODO: change to generator
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        def nextTrans(s: str) -> set:
            res = set()
            for i in range(len(s)):
                for j in range(26):
                    res.add(s[:i] + chr(ord('a') + j) + s[i+1:])
            res.remove(s)
            return res
        
        wordSet = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            print(layer)
            newlayer = defaultdict(list)
            for w in layer:
                if w == endWord: 
                    res.extend(k for k in layer[w])
                else:
                    trans = nextTrans(w)
                    nextSet = wordSet.intersection(trans)
                    for nxt in list(nextSet):
                        newlayer[nxt] += [j + [nxt] for j in layer[w]]

            wordSet -= nextSet
            layer = newlayer

        return res

# Accepted
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        def nextTrans(s: str) -> set:
            res = set()
            for i in range(len(s)):
                for j in range(26):
                    res.add(s[:i] + chr(ord('a') + j) + s[i+1:])
            res.remove(s)
            return res
        
        wordSet = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = defaultdict(list)
            for w in layer:
                if w == endWord: 
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for j in range(26):
                            nxt = w[:i] + chr(ord('a') + j) + w[i+1:]
                            if nxt in wordSet:
                                newlayer[nxt] += [j + [nxt] for j in layer[w]]

            wordSet -= set(newlayer.keys())
            layer = newlayer

        return res

