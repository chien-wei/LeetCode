class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return list(map(lambda x: int(x), sorted(list(map(lambda x: str(x), range(1, n+1))))))