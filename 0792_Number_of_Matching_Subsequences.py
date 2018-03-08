# please read this discussion again:
# https://leetcode.com/problems/number-of-matching-subsequences/discuss/117634/Efficient-and-simple-go-through-words-in-parallel-with-explanation
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        waiting = collections.defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])