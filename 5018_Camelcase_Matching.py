class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        results = []
        for query in queries:
            i, j = 0, 0
            for p in pattern:
                while i < len(query) and p != query[i] and query[i].islower():
                    i += 1
                if i == len(query):
                    break
                if p != query[i]:
                    break
                i += 1
                j += 1
            if j == len(pattern) and (query[i:] == '' or query[i:].islower()):
                results.append(True)
            else:
                results.append(False)
        return results