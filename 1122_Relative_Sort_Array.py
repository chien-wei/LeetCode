class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict1 = {}
        for n in arr1:
            dict1[n] = dict1.get(n, 0) + 1
        
        res = []
        for n in arr2:
            if n in dict1:
                res = res + [n] * dict1[n]
                dict1.pop(n)
        
        for k in sorted(dict1.keys()):
            res = res + [k] * dict1[k]
        return res