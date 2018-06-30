class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        la, lb = len(A), len(B)
        if la != lb:
            return False
        diffs = []
        char_count = {}
        isbuddy = False
        has_same = False
        for a, b in zip(A, B):
            # first different char
            if a != b and len(diffs) == 0 and not isbuddy:
                diffs = [a, b]
            # second different char
            elif a != b and not isbuddy:
                if a == diffs[1] and b == diffs[0]:
                    isbuddy = True
            # third different char
            elif a != b and isbuddy:
                isbuddy = False
                break
            # when the char are the same, count the number of same char
            elif not has_same:
                if a in char_count:
                    has_same = True
                else:
                    char_count[a] = 1
        # if no different char but have same one in each
        if len(diffs) == 0 and has_same:
            isbuddy = True
        return isbuddy
            