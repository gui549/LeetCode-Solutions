package Medium;

import java.util.HashMap;
import java.util.HashSet;

class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) set.add(num);
        int best = 0;
        for (int n : set) {
            if (!set.contains(n - 1)) {
                int m = n + 1;
                while (set.contains(m)) m++;
                best = Math.max(best, m - n);
            }
        }
        return best;
    }
}

// class Solution {
//     public int longestConsecutive(int[] nums) {
//         int ans = 0;
//         HashMap<Integer, Integer> map = new HashMap<>();
//         for (int n : nums) {
//             if (!map.containsKey(n)) {
//                 int left = map.containsKey(n - 1) ? map.get(n - 1) : 0;
//                 int right = map.containsKey(n + 1) ? map.get(n + 1) : 0;

//                 int sum = left + right + 1;
//                 map.put(n, sum);

//                 ans = Math.max(ans, sum);

//                 map.put(n - left, sum);
//                 map.put(n + right, sum);
//             }
//         }
//         return ans;
//     }
// }