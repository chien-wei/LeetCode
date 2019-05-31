// this will get us stackoverflow
class Solution {
    private double helper(double x, int n, double res) {
        if (n == 0) {
            return res;
        } else if (n < 0) {
            return helper(1/x, -n, res);
        } else {
            return helper(x, n-1, res * x);
        }
    }
    
    public double myPow(double x, int n) {
        return helper(x, n, 1.0);
    }
}

// optimized with math and bit operation
// https://leetcode.com/problems/powx-n/discuss/19563/Iterative-Log(N)-solution-with-Clear-Explanation
class Solution {
    public double myPow(double x, int n) {
        double ans = 1;
        long absN = Math.abs((long)n);
        while(absN > 0) {
            if((absN&1)==1) ans *= x;
            absN >>= 1;
            x *= x;
        }
        return n < 0 ?  1/ans : ans;
    }
}