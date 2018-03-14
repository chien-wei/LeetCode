from collections import Counter
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        new = []

        for row in wall:
            flag = 0
            last = 0
            sum = 0
            for i in row:
                sum += i
            for i in row:
                if flag == 1:
                    i = last + i
                flag = 1
                if i == sum:
                    continue
                new.append(i)
                last = i
        if new == []:
            return len(wall)
        else:
            from collections import Counter
            data = Counter(new)
            #print data.most_common()   # Returns all unique items and their counts
            return len(wall) - data.most_common(1)[0][1]  # Returns the highest occurring item
S = Solution()
S.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]])
