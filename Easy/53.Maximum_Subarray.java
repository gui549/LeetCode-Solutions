package Medium;


class Solution {
    public int maxSubArray(int[] nums) {
        int sum = 0, ans = -10000;
        
        for(int i = 0; i < nums.length; i++) {
            sum = sum + nums[i];
            ans = Math.max(sum, ans);
        
            if (sum < 0) sum = 0;
        }

        return ans;
    }
}