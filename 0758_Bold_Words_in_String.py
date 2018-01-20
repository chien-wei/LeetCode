class Solution:
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        if len(words) == 0:
            return S
        tuples = []
        for w in words:
            #print(w)
            head = 0
            result = S.find(w, head)
            while result != -1:
                tuples.append([result, result + len(w)])
                head = result +1 
                result = S.find(w, head)

        tuples = sorted(tuples, key=lambda element: (element[0], element[1]))
        
        print(tuples)
        
        if len(tuples) == 0:
            return S
        
        newTuples = []
        head = -1
        tail = tuples[0][1]
        for i in range(len(tuples)):
            if head == -1:
                head = tuples[i][0]
                tail = tuples[i][1]
            if tuples[i][0] <= tail:
                tail = max(tail, tuples[i][1])
                continue
                
            newTuples.append([head, tail])
            head = tuples[i][0]
            tail = tuples[i][1]
        newTuples.append([head, tail])
            
        print(newTuples)
        
        newTuples = sorted(newTuples, key=lambda element: (-element[0]))
        
        for t in newTuples:
            S = S[0:t[0]] + "<b>" + S[t[0]:t[1]] + "</b>" + S[t[1]:]
        
        return S