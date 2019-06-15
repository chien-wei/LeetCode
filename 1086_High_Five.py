from collections import defaultdict
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list) # [scores]
        for student, score in items:
            scores[student].append(score)
        
        scoresList = list(scores.items())
        avgs = list(map(lambda x: [x[0], sum(sorted(x[1])[::-1][:5]) // 5], scoresList))
        
        return sorted(avgs, key=lambda x: x[0])