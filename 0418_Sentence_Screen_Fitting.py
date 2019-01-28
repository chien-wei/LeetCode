class Solution:
    def wordsTyping(self, rows, cols, sentence):
        self.i = -1
        def getNext():
            self.i += 1
            if self.i >= len(sentence):
                self.i = 0
            return sentence[self.i]
        
        if len(sentence) == 0:
            return [('-' * cols) for i in range(rows)]

        res = []
        next = getNext()
        for _ in range(rows):
            line = ""
            while len(line) != cols:
                if len(line) == 0:
                    line += next
                    next = getNext()
                elif len(line) + len(next) + 1 <= cols:
                    line += '-' + next
                    next = getNext()
                else:
                    line += '-' * (cols - len(line))
            res.append(line)
        return res

s = Solution()
print(s.wordsTyping(rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]))
print(s.wordsTyping(rows = 3, cols = 6, sentence = ["a", "bcd", "e"]))
print(s.wordsTyping(rows = 2, cols = 8, sentence = ["hello", "world"]))
print(s.wordsTyping(rows = 2, cols = 8, sentence = []))