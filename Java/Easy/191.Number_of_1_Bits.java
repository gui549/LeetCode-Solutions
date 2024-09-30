package Easy;

// better solution
class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int ans = 0;
        while (n != 0) {
            ans += (n & 1);
            n >>= 1;
        }
        return ans;
    }
}

// first solution
// class Solution {
//     // you need to treat n as an unsigned value
//     public int hammingWeight(int n) {
//         int ans = 0;
//         for (int i = 0; i < 32; i++) {
//             int bitmask = 1 << i;
//             if ((n & bitmask) != 0) {
//                 ans ++;
//             }
//         }
//         return ans;
//     }
// }