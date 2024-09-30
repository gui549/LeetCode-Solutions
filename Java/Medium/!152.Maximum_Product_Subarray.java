package Medium;


class Solution {
    public int maxProduct(int[] nums) {
        int ans = Integer.MIN_VALUE, n = nums.length, l = 1, r = 1;
        for (int i = 0; i < n; i++) {
            l = (l == 0 ? 1 : l) * nums[i];
            r = (r == 0 ? 1 : r) * nums[n - i - 1];
            ans = Math.max(ans, Math.max(l, r));
        }
        return ans;
    }
}