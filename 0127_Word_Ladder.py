from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS
        # it seems there is no better way to check next words
        # nextTrans(): get all next transformation
        
        def nextTrans(s: str) -> set:
            res = set()
            for i in range(len(s)):
                for j in range(26):
                    res.add(s[:i] + chr(ord('a') + j) + s[i+1:])
            res.remove(s)
            return res
                
                
        wordSet = set(wordList)
        deq = deque()
        deq.append(beginWord)
        step = 0
        
        while len(deq) > 0:
            step += 1
            nxt = deque()
            while len(deq) > 0:
                cur = deq.popleft()
                if cur == endWord:
                    return step
                trans = nextTrans(cur)
                nextSet = wordSet.intersection(trans)
                wordSet -= nextSet # copy version: wordSet = wordSet.difference(nextSet)
                
                for n in list(nextSet):
                    nxt.append(n)
            deq = nxt
        return 0