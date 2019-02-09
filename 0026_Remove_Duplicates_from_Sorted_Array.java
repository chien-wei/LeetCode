class Solution {
    public int removeDuplicates(int[] nums) {
        int N = 1;
        int i = N;
        while (i < nums.length) {
            if (nums[i] != nums[i-1]) {
                nums[N++] = nums[i];
            }
            i++;
        }
        return N;
    }
}