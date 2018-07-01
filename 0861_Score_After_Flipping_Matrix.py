class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        def flip(val):
            return (val+1)%2
        def flip_row(row):
            return [flip(col) for col in row]
        
        # first we flip all row to starting with 1
        for i, row in enumerate(A):
            if row[0] == 0:
                A[i] = flip_row(row)
        #print(A)
        # second we flip column if the result is number of 1 bigger than number of 0
        len_row = len(A)
        len_col = len(A[0])
        for j in range(len_col):
            number_of_0 = 0
            for i in range(len_row):
                if A[i][j] == 0:
                    number_of_0 += 1
            if number_of_0 > len_row / 2:
                for i in range(len_row):
                    A[i][j] = flip(A[i][j])
        result = 0
        for row in A:
            s = ''
            for col in row:
                s += str(col)
            result += int(s, 2)
        return result
                
                