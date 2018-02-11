class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        ans = 0
        s = set(answers)
        for i in s:
            tmp = 0
            number = answers.count(i) 
            #print(number)
            while number - tmp > i + 1:
                tmp += i+1
            ans += i+1
            ans += tmp
        return ans