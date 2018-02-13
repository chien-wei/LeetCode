
# This one got TLE, but I think it is good solution.
# class Solution:
#     def palindromePairs(self, words):
#         """
#         :type words: List[str]
#         :rtype: List[List[int]]
#         """
#         candidates = list(enumerate(map(lambda w: w[::-1], words)))
#         result = []
#         print(candidates)
#         for i in range(len(words)):
#             N = len(words[i])
#             for cand in candidates:
#                 # front case
#                 if len(cand[1]) >= N and cand[1][:N] == words[i] and cand[1][N:] == cand[1][N:][::-1]:
#                     if i != cand[0]: result.append([i, cand[0]])
#                 # back case
#                 NC = len(cand[1])
#                 if NC > N and cand[1][NC-N:] == words[i] and cand[1][:NC-N] == cand[1][:NC-N][::-1]:
#                     if i != cand[0]: result.append([cand[0], i])
#         return result

# Butter: use hash to reduce one iteration

class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
            
        cand = dict([(w[::-1], i) for i, w in enumerate(words)])
        res = []
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                prefix, postfix = w[:j], w[j:]
                if prefix in cand and i != cand[prefix] and postfix == postfix[::-1]:
                    res.append([i, cand[prefix]])
                if j>0 and postfix in cand and i != cand[postfix] and prefix == prefix[::-1]:
                    res.append([cand[postfix], i])
        return res
