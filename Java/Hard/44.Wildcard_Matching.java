package Hard;

import java.util.HashMap;
import java.util.Map;

// Advanced Solution
class Solution {
    public boolean isMatch(String s, String p) {
        int i = 0, j = 0;
        int m = s.length(), n = p.length();
        int matchIdx = -1, starIdx = -1;
        while (i < m) {
            if (j < n && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '?')) {
                i++; j++;
            } else if (j < n && p.charAt(j) == '*') {
                starIdx = j;
                j++;
                matchIdx = i;
            } else if(starIdx != -1) {
                j = starIdx + 1;
                i = ++matchIdx;
            } else {
                return false;
            }
        } 
        while (j < n && p.charAt(j) == '*') j++;
        return j == n;
    }
}


// Better Solution
// class Solution {
//     public boolean isMatch(String s, String p) {
//         boolean[][] dp = new boolean[s.length() + 1][p.length() + 1];
//         dp[0][0] = true;
//         for (int i = 1; i <= s.length(); i++) {
//             dp[i][0] = false;
//         }

//         for (int j = 1; j <= p.length(); j++) {
//             if (p.charAt(j - 1) == '*') dp[0][j] = true;
//             else break;
//         }

//         for (int i = 1; i <= s.length(); i++) {
//             for (int j = 1; j <= p.length(); j++) {
//                 if (p.charAt(j - 1) != '*')
//                     dp[i][j] = dp[i - 1][j - 1] && (s.charAt(i - 1) == p.charAt(j - 1) || p.charAt(j - 1) == '?');
//                 else
//                     dp[i][j] = dp[i - 1][j] || dp[i][j - 1];
//             }
//         }

//         return dp[s.length()][p.length()];
//     }
// }


// First Solution
// class Solution {
//     private Map<Integer, Map<Integer, Boolean>> cache = new HashMap<>();

//     public boolean isMatch(String s, String p) {
//         return isMatch(s, p, 0, 0);
//     }

//     private boolean isMatch(String s, String p, Integer i, Integer j) {
//         if (!cache.containsKey(i)) cache.put(i, new HashMap<>());
//         if (cache.get(i).containsKey(j))
//             return cache.get(i).get(j);
        
//         if (s.length() == i) {
//             if (p.length() == j) cache.get(i).put(j, true);
//             else if (p.charAt(j) == '*') cache.get(i).put(j, isMatch(s, p, i, j + 1));
//             else cache.get(i).put(j, false);
//         } else if (p.length() == j) {
//             cache.get(i).put(j, s.isEmpty());
//         } else if (p.charAt(j) == '*') {
//             cache.get(i).put(j, isMatch(s, p, i + 1, j) || isMatch(s, p, i, j + 1));
//         } else if (p.charAt(j) == '?' || s.charAt(i) == p.charAt(j)) {
//             cache.get(i).put(j, isMatch(s, p, i + 1, j + 1));
//         } else {
//             cache.get(i).put(j, false);
//         }
    
//         return cache.get(i).get(j);
//     }
// }
