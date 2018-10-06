class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        class Trie:
            def __init__(self):
                self.child = {}
                self.isend = False

            def insert(self, word):
                if word[0] not in self.child:
                    self.child[word[0]] = Trie()
                if len(word) == 1:
                    self.child[word[0]].isend = True
                elif len(word) > 1:
                    self.child[word[0]].insert(word[1:])

            def get_depth(self, cur):
                return max([cur] + [self.child[c].get_depth(cur+1) for c in self.child])

        def dfs_trie(board, r, c, visited, T, word):
            res = []
            if board[r][c] in T.child:
                cur = board[r][c]
                word += cur
                if T.child[cur].isend:
                    res.append(word)
                v = visited
                for (x, y) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if x >= 0 and y >= 0 and x < len(board) and y < len(board[0]) and not v[x][y]:
                        v[r][c] = True
                        res += dfs_trie(board, x, y, v, T.child[cur], word)
                        v[r][c] = False
            return res

        T = Trie()
        for word in words:
            T.insert(word)

        res = []
        M, N = len(board), len(board[0])
        for r in range(M):
            for c in range(N):
                visited = [[False for _ in range(N)] for _ in range(M)]
                res = res + dfs_trie(board, r, c, visited, T, '')
        return list(set(res))