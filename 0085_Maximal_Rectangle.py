# use largestRectangArea from Leetcode 84

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def largestRectangleArea(row_heights):
            stack = [-1]
            result = 0
            heights = row_heights[:]
            
            heights.append(0)
            for i in range(len(heights)):
                while len(stack) > 1 and heights[stack[-1]] > heights[i]:
                    rect_height = heights[stack.pop()]
                    rect_width = i - stack[-1] - 1
                    result = max(result, rect_height * rect_width)
                stack.append(i)
            return result
        
        mx_area = 0
        if len(matrix) < 1:
            return 0
        row_heights = [0] * len(matrix[0])
        for row in matrix:
            row = map(int, row)
            row_heights = list(map(lambda x, y: x * y + y, row_heights, row))
            mx_area = max(mx_area, largestRectangleArea(row_heights))
        
        return mx_area