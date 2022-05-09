package Medium;

class Solution {
    public int trailingZeroes(int n) {
        int ans = 0;

        while (n > 0) {
            n /= 5;
            ans += n;
        }

        return ans;
    }
}


// class Solution {
//     public int trailingZeroes(int n) {
//         int ans = 0;

//         for (int i = 1; i <= n; i++) {
//             int num = i;
//             while (num > 0 && num % 5 == 0) {
//                 ans += 1;
//                 num /= 5;
//             }
//         }

//         return ans;
//     }
// }


