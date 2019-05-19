class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # a dictionary that has words as key, number of chain as value
        # sort the words by the length of word
        # for each word in words, find word missing one letter in dictionary
        # if found, plus one in value
        
        WORDS = sorted(words, key=lambda w: len(w))
        num_chain = {}
        mx = 0
        if len(WORDS) > 0:
            mx = 1
        for word in WORDS:
            num_chain[word] = 1
            for i in range(len(word)):
                mis = word[:i] + word[i+1:] # miss i character
                if mis in num_chain:
                    num_chain[word] = max(num_chain[word], num_chain[mis] + 1)
                    mx = max(mx, num_chain[word])
        return mx