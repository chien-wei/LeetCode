class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        zipped = list(zip(difficulty, profit))
        zipped.sort(key = lambda x: x[1])
        zipped = zipped[::-1]
        #print(zipped)
        worker.sort()
        worker = worker[::-1]
        #print(worker)
        i = 0
        result = 0
        for w in worker:
            while i < len(zipped) and w < zipped[i][0]:
                i += 1
            if i == len(zipped):
                pass
            else:
                result += zipped[i][1]
        return result