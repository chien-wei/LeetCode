class Solution:
    def nextClosestTime(self, time):
        """
        :type time: string 
        :rtype: string
        """
        nums = sorted(list(set([time[0], time[1], time[3], time[4]])))
        [h, m] = time.split(':')
        # check minutes
        ind1 = nums.index(m[1])
        if ind1 != len(nums) - 1:
            return h + ':' + m[0] + nums[ind1+1]
        else:
            m = m[0] + nums[0]
        
        ind2 = nums.index(m[0])
        if ind2 != len(nums) - 1 and int(nums[ind2+1]) < 6:
            return h + ':' + nums[ind2+1] + m[1]
        else:
            m = nums[0] + m[1]

        # check hours
        ind3 = nums.index(h[1])
        if ind3 != len(nums) - 1:
            if int(h[0]) < 2:
                return h[0] + nums[ind3+1] + ':' + m
            elif h[0] == '2' and int(nums[ind3+1]) < 5:
                return h[0] + nums[ind3+1] + ':' + m
            else:
                h = h[0] + nums[0]

        ind4 = nums.index(h[0])
        if ind4 != len(nums) - 1 and int(nums[ind4+1]) < 3:
            return nums[ind4+1] + h[1] + ':' + m
        else:
            h = nums[0] + h[1]
        
        return h + ':' + m


s = Solution()
print(s.nextClosestTime('19:34'))
print(s.nextClosestTime('23:42'))
print(s.nextClosestTime('13:55'))
print(s.nextClosestTime('12:34'))
print(s.nextClosestTime('23:59'))