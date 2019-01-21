class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if len(s) < 2:
            return len(s)
        mx = 2
        keep = {}
        i, j = 0, 1
        keep[s[i]] = keep.get(s[i], 0) + 1
        keep[s[j]] = keep.get(s[j], 0) + 1
        while j < len(s)-1:
            j += 1
            keep[s[j]] = keep.get(s[j], 0) + 1
            while len(keep) > 2 and i < j:
                keep[s[i]] -= 1
                if keep[s[i]] == 0:
                    keep.pop(s[i])
                i += 1
            tt = sum([keep[c] for c in keep])
            mx = max(mx, tt)
            #print(keep)
        return mx


s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct('eceba'))
print(s.lengthOfLongestSubstringTwoDistinct('av'))
print(s.lengthOfLongestSubstringTwoDistinct('e'))
print(s.lengthOfLongestSubstringTwoDistinct('ecaesadgasssdsdsdsz'))