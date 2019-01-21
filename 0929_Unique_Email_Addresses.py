class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        dist = set()
        for e in emails:
            ind = e.index('@')
            new = ''.join(e[:ind].split('.')) + e[ind:]
            ind1 = new.index('+')
            ind2 = new.index('@')
            dist.add(new[:ind1] + new[ind2:])
        
        return len(list(dist))