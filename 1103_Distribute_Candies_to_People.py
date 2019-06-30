class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        give = 1
        i = 0
        res = [0 for _ in range(num_people)]
        while candies > 0:
            res[i] += min(give, candies)
            candies -= give
            give += 1
            i += 1
            i %= num_people
        return res