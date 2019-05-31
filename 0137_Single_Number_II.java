class Solution {
    public int singleNumber(int[] nums) {
        // need a cycle in three => need 2 bits
        // try to make 00 => 01 => 10 => 00
        int n1 = 0, n2 = 0;
        for (int i=0; i < nums.length; i++) {
            n1 = n1 ^ nums[i] & ~n2;
            n2 = n2 ^ nums[i] & ~n1;
        }
        return n1;
    }
}