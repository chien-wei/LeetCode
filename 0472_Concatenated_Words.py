class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        class Trie():
            def __init__(self):
                self.child = {}
                self.isend = False
            
            def insert(self, word):
                if len(word) < 1:
                    return
                if word[0] not in self.child:
                    self.child[word[0]] = Trie()
                if len(word) == 1:
                    self.child[word[0]].isend = True
                elif len(word) > 1:
                    self.child[word[0]].insert(word[1:])
        
        words = list(set(words))
        T = Trie()
        for word in words:
            T.insert(word)
            
        res = []
        for word in words:
            if word == '':
                continue
            stack = [word]
            seen = {}
            flag = False # if found, no need to continue
            while len(stack) > 0:
                tmp = T
                cur = stack.pop(0)
                word_length = 0
                # find sub-word
                while cur[0] in tmp.child:
                    if len(cur) == 1 and tmp.child[cur[0]].isend and word_length != len(word)-1:
                        res.append(word)
                        flag = True
                        break
                    elif len(cur) == 1:
                        break
                    elif tmp.child[cur[0]].isend and cur[1:] not in seen:
                        stack.append(cur[1:])
                        seen[cur[1:]] = 1
                    
                    tmp = tmp.child[cur[0]]
                    cur = cur[1:]
                    word_length += 1
                    #print(cur, word_length, stack)
                if flag:
                    break
        return list(set(res))