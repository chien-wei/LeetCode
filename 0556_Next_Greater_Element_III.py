class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = list(str(n))
        a = b = -1
        for i in range(len(n)-2, -1, -1):
            if n[i] < n[i+1]:
                a = i
                break
        if a == -1:
            return -1
        for i in range(len(n)-1, -1, -1):
            if n[i] > n[a]:
                b = i
                break
        #print(a,b)
        n[a], n[b] = n[b], n[a]
        #print(n)
        n = n[:a+1] + n[a+1:][::-1]
        res = int(''.join(n))
        return res if res < 2**31 - 1 else -1