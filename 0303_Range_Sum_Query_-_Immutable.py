class NumArray:

    def __init__(self, nums: List[int]):
        self.acc = [0] + nums[:]
        for i in range(1, len(self.acc)):
            self.acc[i] += self.acc[i-1]
        

    def sumRange(self, i: int, j: int) -> int:
        return self.acc[j+1] - self.acc[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
