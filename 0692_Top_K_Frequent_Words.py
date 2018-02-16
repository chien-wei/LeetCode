class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        ans = []
        [w, i] = list(zip(*collections.Counter(words).most_common()))
        j = 0
        while j < k:
            if j + 1 < len(i) and i[j+1] > i[j]:
                ans.append(w[j])
                j += 1
            else:
                tmp = []
                while j + 1 < len(i) and i[j+1] == i[j]:
                    tmp.append(w[j])
                    j += 1
                tmp.append(w[j])
                j += 1
                if j > k:
                    ans.extend(sorted(tmp)[:-(j-k)])
                else:
                    ans.extend(sorted(tmp))
        return ans