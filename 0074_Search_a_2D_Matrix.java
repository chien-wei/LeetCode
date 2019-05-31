class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0) return false;
        int N = matrix[0].length;
        int lo = 0, hi = matrix.length * N;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            int x = matrix[mid/N][mid%N];
            if (x < target) {
                lo = mid + 1;
            } else if (x > target) {
                hi = mid;
            } else {
                return true;
            }
        }
        return false;
    }
}