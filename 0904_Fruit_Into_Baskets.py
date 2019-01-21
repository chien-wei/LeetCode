class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if len(tree) < 2:
            return len(tree)
        hsh = {}
        i, j = 0, 1
        mx = 2
        hsh[tree[i]] = 1
        hsh[tree[j]] = hsh.get(tree[j], 0) + 1
        
        while j < len(tree)-1:
            j += 1
            while i < j and tree[j] not in hsh and len(hsh) == 2:
                    hsh[tree[i]] -= 1
                    if hsh[tree[i]] == 0:
                        hsh.pop(tree[i])
                    i += 1
            
            hsh[tree[j]] = hsh.get(tree[j], 0) + 1
            mx = max(mx, sum(hsh[i] for i in hsh))
        return mx