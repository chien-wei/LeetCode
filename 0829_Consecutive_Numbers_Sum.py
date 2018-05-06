class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 3:
            return 1
        base = 3
        i = 2
        result = 1
        while N >= base:
            #print(base, i)
            if i % 2 == 1 and N % i == 0:
                result += 1
                #print("a")
            elif i % 2 == 0 and N % i == i // 2:
                result += 1
                #print("b")
            base += i
            i += 1
        return result