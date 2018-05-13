class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        for row in A:
            nrow = []
            for i in range(len(row)-1, -1, -1):
                nrow.append((row[i]+1)%2)
            ans.append(nrow)
        return ans