class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        # split the text
        # from words[2] to words[n-1], check words[x-1] == second and words[x-2] == first
        # if yes, append to the result
        
        result = []
        words = text.split()
        for i in range(2, len(words)):
            if first == words[i-2] and second == words[i-1]:
                result.append(words[i])
        return result