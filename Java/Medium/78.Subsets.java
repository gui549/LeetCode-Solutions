package Medium;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < Math.pow(2, nums.length); i++) {
            List<Integer> element = new ArrayList<>();
            int binary = i, digit = 0;
            while (binary > 0) {
                if (binary % 2 == 1) element.add(nums[digit]);
                binary /= 2; digit++;
            }
            ans.add(element);
        }
        return ans;
    }
}