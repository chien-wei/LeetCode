class Solution:
    def findDiagonalOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        res = []
        cur = [0, 0]
        def update(cur):
            a, b = cur[0], cur[1]

            if (a + b) % 2 == 0:
                if a - 1 < 0 and b + 1 >= len(matrix[0]):
                    return [a+1, b]
                elif a - 1 < 0:
                    return [a, b+1]
                elif b + 1 >= len(matrix[0]):
                    return [a+1, b]
                else:
                    return [a-1, b+1]
            else:
                if a + 1 >= len(matrix) and b - 1 < 0:
                    return [a, b+1]
                elif a + 1 >= len(matrix):
                    return [a, b+1]
                elif b - 1 < 0:
                    return [a+1, b]
                else:
                    return [a+1, b-1]
            
            
        for _ in range(len(matrix)):
            for _ in range(len(matrix[0])):
                #print(cur)
                res.append(matrix[cur[0]][cur[1]])
                cur = update(cur)
        return res