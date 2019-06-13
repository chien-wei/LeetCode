class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # bfs
        color = image[sr][sc]
        if color == newColor:
            return image
        que = [[sr, sc]]
        M, N = len(image), len(image[0])
        while len(que) > 0:
            i, j = que.pop()
            print(i, j)
            image[i][j] = newColor
            for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if x >= 0 and x < M and y >= 0 and y < N and image[x][y] == color:
                    que.append([x, y])
        return image