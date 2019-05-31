class Solution {
    public int majorityElement(int[] nums) {
        // Boyer-Moore Majority Vote Algorithm
        int major = 0, count = 0;
        for (int i=0; i < nums.length; i++) {
            if (count == 0 && major != nums[i]) {
                major = nums[i];
            } else if (major == nums[i]) {
                count += 1;
            } else {
                count -= 1;
            }
        }
        return major;
    }
}