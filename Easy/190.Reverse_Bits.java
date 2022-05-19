package Easy;

class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {
            int bitmask = 1 << i;
            if ((n & bitmask) != 0) {
                ans |= 1 << (31 - i);
            }
        }
        return ans;
    }
}