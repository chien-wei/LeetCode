# interesting discussion: https://discuss.leetcode.com/topic/117050/na%C3%AFve-solution-accepted-with-a-proof-wrong-difficulty/14
# proof of why greedy works: https://discuss.leetcode.com/topic/117202/formal-proof-of-the-optimality-of-greedy-algorithm/2

class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        couples = [int(_/2) for _ in row]
        swap = 0
        while couples:
            a,b = couples.pop(),couples.pop()
            if a!=b:
                couples[couples.index(a)] = b
                swap+=1
        return swap