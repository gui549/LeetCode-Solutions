package Medium;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

class Solution {

    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        permutation(ans, nums, 0);
        return ans;
    }

    public void permutation(List<List<Integer>> res, int[] nums, int index) {
        if (index == nums.length) {
            List<Integer> tmp = Arrays.stream(nums).boxed().collect(Collectors.toList());
            res.add(tmp);
            return;
        }
        Set<Integer> seen = new HashSet<>();
        for (int i = index; i < nums.length; i++) {
            if (seen.add(nums[i])) {
                swap(nums, i, index);
                permutation(res, nums, index + 1);
                swap(nums, i, index);
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
} 