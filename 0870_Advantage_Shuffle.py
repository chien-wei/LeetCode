class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        def bs(array, l, r, val):
            while l <= r:
                mid = l + (r-l)//2
                if array[mid] == val:
                    return mid
                elif array[mid] < val:
                    l = mid + 1
                else:
                    r = mid - 1 
            return l
        
        res = []
        A.sort()
        for b in B:
            i = bs(A, 0, len(A) - 1, b)
            while i < len(A) and A[i] == b:
                i += 1
            if i >= len(A):
                res.append(A.pop(0))
            else:
                res.append(A.pop(i))
            
        return res