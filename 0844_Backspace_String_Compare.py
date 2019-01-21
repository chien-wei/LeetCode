class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        i, j = len(S)-1, len(T)-1
        skip_i, skip_j = 0, 0
        while True:
            while i >= 0:
                if S[i] == '#':
                    skip_i += 1
                elif skip_i > 0:
                    skip_i -= 1
                else:
                    break
                i -= 1
            while j >= 0:
                if T[j] == '#':
                    skip_j += 1
                elif skip_j > 0:
                    skip_j -= 1
                else:
                    break
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i -= 1
            j -= 1