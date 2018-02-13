class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = B = 0
        c1 = collections.Counter(secret)
        c2 = collections.Counter(guess)
        for x, y in zip(secret, guess):
            if x == y:
                c1[x] -= 1
                c2[y] -= 1
                A += 1
        for c in c2:
            if c in c1:
                B += min(c1[c], c2[c])
        return str(A) + "A" + str(B) + "B"