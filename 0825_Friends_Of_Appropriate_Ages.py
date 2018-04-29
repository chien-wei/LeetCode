class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages.sort()
        i = 1
        j = 0
        result = 0
        while i < len(ages):
            same_age_count = 1
            if i == 1 and ages[0] == ages[i]:
                same_age_count += 1
            while i+1 < len(ages) and ages[i+1] == ages[i]:
                i += 1
                same_age_count += 1
            while j < i and ages[j] <= 0.5 * ages[i] + 7:
                j += 1
                
            result += (i-j) * same_age_count
            print(i, j)
            i += 1
        return result