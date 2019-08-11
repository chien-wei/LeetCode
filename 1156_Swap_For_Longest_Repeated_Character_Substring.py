class Solution:
    def maxRepOpt1(self, text: str) -> int:
        nums = []
        chars = []
        i = 0
        counts = {}
        while i < len(text):
            char = text[i]
            counts[char] = counts.get(char, 0) + 1
            num = 1
            while i + 1 < len(text) and text[i+1] == text[i]:
                num += 1
                i += 1
            nums.append(num)
            chars.append(char)
            i += 1
        
        j = 0
        res = 0
        while j < len(chars):
            char = chars[j]
            if j + 2 < len(chars) and char == chars[j+2]:
                if nums[j+1] == 1 and counts[char] > 2:
                    res = max(res, nums[j] + nums[j+2] + 1)
                elif nums[j+1] == 1 and counts[char] == 2:
                    res = max(res, nums[j] + nums[j+2])
                elif counts[char] > 1:
                    res = max(res, nums[j] + 1)
            elif counts[char] > 1:
                res = max(res, nums[j] + 1)
            else:
                res = max(res, nums[j])
            j += 1
                
        return res