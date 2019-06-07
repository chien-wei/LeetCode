class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        HashMap<Integer, Integer> targets = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (targets.containsKey(nums[i])) {
                result[1] = i;
                result[0] = targets.get(nums[i]);
                break;
            }
            targets.put(target - nums[i], i);
        }
        return result;
    }
}