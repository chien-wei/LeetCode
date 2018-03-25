class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        h = {}
        for word in words:
            tmp = ''
            for c in word:
                tmp += morse[ord(c) - ord('a')]
            h[tmp] = 1
        return len(h)