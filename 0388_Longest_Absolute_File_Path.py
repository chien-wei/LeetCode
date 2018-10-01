class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if len(input) == 0:
            return 0
        paths = input.split('\n')
        i = 0
        cur_path = []
        res = []
        for path in paths:
            level = path.split('\t')
            N = len(cur_path)
            L = len(level)
            if L > N:
                cur_path.append(level[-1])
            else:
                for _ in range(N-L+1):
                    cur_path.pop()
                cur_path.append(level[-1])
            if '.' in path:
                res.append('/'.join(cur_path))
                cur_path.pop()
        if len(res) == 0:
            return 0
        return max(len(r) for r in res)