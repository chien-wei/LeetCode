class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        common = {}
        occur = {}
        first_flag = True
        for string in A:
            for c in string:
                if first_flag:
                    common[c] = common.get(c, 0) + 1
                else:
                    occur[c] = occur.get(c, 0) + 1
            if not first_flag:
                for letter in common:
                    occur_number = occur.get(letter, 0)
                    if common[letter] > occur_number:
                        common[letter] = occur_number
            else:
                first_flag = False
            occur = {}
                
        result = []
        for letter in common:
            for _ in range(common[letter]):
                result.append(letter)
        return result