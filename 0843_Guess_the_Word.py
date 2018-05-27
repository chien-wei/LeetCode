# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """
from random import randint
class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def compare(source, target, hits):
            num_hit = 0
            for i in range(len(source)):
                if source[i] == target[i]:
                    num_hit += 1
            if hits == 0 and num_hit > 0:
                return False
            if num_hit >= hits:
                return True
            return False
        
        wordlist = list(set(wordlist))
        for _ in range(10):
            #print(wordlist)
            if len(wordlist) == 1:
                return
            
            g = randint(0, len(wordlist)-1)
            #print(g)
            matches = master.guess(wordlist[g])
            tmp = wordlist[g]
            #print(tmp, matches)
            j = 0
            while j < len(wordlist):
                if not compare(wordlist[j], tmp, matches):
                    wordlist.pop(j)
                else:
                    j += 1