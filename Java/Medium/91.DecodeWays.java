package Medium;

import java.util.HashMap;
import java.util.Map;


// Better Solution
class Solution {
    public int numDecodings(String s) {
        int dp1 = 1, dp2 = 0, n = s.length();
        for (int i = n - 1; i >= 0; i--) {
            int dp = s.charAt(i) == '0'? 0 : dp1;
            if (i < n - 1 && (s.charAt(i) == '1' || s.charAt(i) == '2' && s.charAt(i + 1) <= '6')) {
                dp += dp2;
            }
            dp2 = dp1;
            dp1 = dp;
        } 
        return dp1;
    }
}


// First Solution
// class Solution {
//     Map<String, Integer> cache = new HashMap<>();

//     public int numDecodings(String s) {
//         int count = 0;
//         if (cache.containsKey(s)) return cache.get(s);
//         if (s.length() == 0) return 1;
        
//         if ('0' < s.charAt(0) && s.charAt(0) <= '9') {
//             count += numDecodings(s.substring(1));
//         } 
        
//         if (s.length() > 1 && (s.charAt(0) == '1' || (s.charAt(0) == '2' && s.charAt(1) <= '6'))) {
//             count += numDecodings(s.substring(2));
//         }

//         cache.put(s, count);
//         return count;
//     }
// }