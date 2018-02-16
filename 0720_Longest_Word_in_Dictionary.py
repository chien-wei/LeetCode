class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        d = {"":1}
        words = sorted(words)
        ans = ""
        for word in words:
            if word[:-1] in d:
                d[word] = 1
                if len(word) > len(ans):
                    ans = word
                elif len(word) == len(ans) and ans > word:
                    ans = word
            
        return ans


# There is a one liner solution
# def longestWord(self, W):
#     return min((set(itertools.accumulate(w))-set(W),-len(w),w)for w in W+[''])[2]