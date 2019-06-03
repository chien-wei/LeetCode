class Solution:
    def compress(self, chars: List[str]) -> int:
        # in-place, use two index to push forward, one index to write
        N = len(chars)
        if N < 2:
            return
        w, i, j = 0, 0, 1
        while i < N:
            while j < N and chars[j] == chars[i]:
                j += 1
            chars[w] = chars[i]
            if j - i > 1:
                # handle ["a", "12"] to ["a", "1", "2"]
                num = str(j-i)
                for k in range(len(num)):
                    chars[w+1+k] = num[k]

                i, j = j, j+1
                w += 1 + len(num)
            else:
                i, j = j, j+1
                w += 1
        # remove extra space
        while len(chars) > w:
            chars.pop()