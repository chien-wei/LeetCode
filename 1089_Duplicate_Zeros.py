class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # two pointer with original index and fixed index
        N = len(arr)
        i = j = 0
        while i < N:
            if arr[i] == 0:
                j += 1
            i += 1
            j += 1
        
        i -= 1
        while i >= 0:
            j -= 1
            if j < N:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j < N:
                    arr[j] = 0
            i -= 1
        return