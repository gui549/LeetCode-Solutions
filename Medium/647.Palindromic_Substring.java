package Medium;


// better solution
class Solution {

    public int countSubstrings(String s) {
        int ans = 0, n = s.length();
        boolean[][] dp = new boolean[n + 1][n + 1];
    
        for (int d = 0; d < n; d++) {
            for (int i = 0; i + d < n; i++) {
                int j = i + d;
                if (s.charAt(i) == s.charAt(j)){
                    dp[i][j] = (i + 1 >= j - 1) ? true : dp[i + 1][j - 1];
                    if (dp[i][j]) ans++; 
                }
            }
        }

        return ans;
    } 
}

// first solution
// class Solution {

//     boolean[][] dp;

//     public int countSubstrings(String s) {
//         int n = s.length();
//         dp = new boolean[n + 1][n + 1];
    
//         int ans = 0;
//         for (int i = 0; i < n; i++) {
//             for (int j = i; j < n; j++) {
//                 if (checkPalindrome(s, i, j)){
//                     ans++;
//                 }
//             }
//         }

//         return ans;
//     } 

//     private boolean checkPalindrome(String s, int start, int end) {
//         if (dp[start][end] || start >= end) {
//             return true;
//         }

//         if (s.charAt(start) == s.charAt(end)){
//             dp[start][end] = checkPalindrome(s, start + 1, end - 1);
//         }

//         return dp[start][end];
//     }
// }