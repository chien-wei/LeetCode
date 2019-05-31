public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        // arithmetic shift is only different when performing right shift to signed integer
        // java >>> perform right logical shift, which means fill 0 at the front
        int res = 0;
        for (int i=0; i < 32; i++) {
            res = (res << 1) + (n & 1);
            n >>>= 1;
        }
        return res;
    }
}