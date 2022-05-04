package Medium;

import java.util.HashMap;

class Solution {
    public int maxOperations(int[] nums, int k) {
        int ans = 0;
        HashMap<Integer, Integer> counter = new HashMap<>();
        
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }

        for (Integer key: counter.keySet()) {
            ans += Math.min(counter.get(key), counter.getOrDefault(k - key, 0));
        }

        return ans / 2;
    }
}