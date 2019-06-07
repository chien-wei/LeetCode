class Solution {
    public int lengthOfLongestSubstring(String s) {
        int result = 0;
        int i = 0, j = 0;
        HashSet<Character> set = new HashSet<Character>();
        while (j < s.length()) {
            while (set.contains(s.charAt(j))) {
                set.remove(s.charAt(i++));
            }
            set.add(s.charAt(j++));
            result = Math.max(result, set.size());
        }
        return result;
    }
}