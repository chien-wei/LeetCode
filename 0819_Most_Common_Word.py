class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        h = {}
        words = paragraph.replace('!', '').replace('?', '').replace('\'', '').replace(',', '').replace(';', '').replace('.', '').split(' ')
        for word in words:
            w = word.lower()
            if w not in h:
                h[w] = 1
            else:
                h[w] += 1
        for cand in sorted(h, key=h.get)[::-1]:
            if cand not in banned:
                return cand
        return ''