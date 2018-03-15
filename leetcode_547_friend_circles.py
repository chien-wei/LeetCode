class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        x = len(M)
        y = len(M[0])

        reach = []
        ans = 0
        for i in range(x):
            for j in range(y):
                if j not in reach and M[i][j] == 1:
                    reach.append(j)

                    print i, j
                    print reach
                else:
                    pass



S = Solution()
S.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
