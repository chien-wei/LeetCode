class Solution {
    public int removeElement(int[] nums, int val) {
        int N = nums.length;
        for (int i = N-1; i >=0; i--) {
            if (nums[i] == val) {
                nums[i] = nums[--N];
                nums[N] = val;
            }
        }
        return N;
    }
}