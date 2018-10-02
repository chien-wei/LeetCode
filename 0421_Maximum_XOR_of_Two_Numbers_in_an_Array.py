class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        class BinaryTrie:
            def __init__(self):
                self.left = None
                self.right = None
                self.depth = -1
                self.value = ''
            
            def insert(self, num_str):
                if len(num_str) == 0:
                    return
                if num_str[0] == '0':
                    if self.left == None:
                        self.left = BinaryTrie()
                        self.left.depth = self.depth + 1
                        self.left.value = self.value + '0'
                    self.left.insert(num_str[1:])
                else:
                    if self.right == None:
                        self.right = BinaryTrie()
                        self.right.depth = self.depth + 1
                        self.right.value = self.value + '1'
                    self.right.insert(num_str[1:])
            def find_max(self, nums):
                res = 0
                for num in nums:
                    cur = self
                    for n in '{0:032b}'.format(num):
                        if n == '0' and cur.right:
                            cur = cur.right
                        elif n == '0' and cur.left:
                            cur = cur.left
                        elif n == '1' and cur.left:
                            cur = cur.left
                        elif n == '1' and cur.right:
                            cur = cur.right
                    res = max(res, int(cur.value, 2) ^ num)
                return res
                
        
        trie = BinaryTrie()
        for num in nums:
            trie.insert('{0:032b}'.format(num))
        return trie.find_max(nums)


#Another solution using just bit operation:
class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ans = 0
        for i in range(32)[::-1]:
            ans <<= 1
            prefixes = {num >> i for num in nums}
            ans += any(ans ^ 1 ^ p in prefixes for p in prefixes)
        return ans