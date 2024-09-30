package Medium;


class Solution {
    public int findPeakElement(int[] nums) {
        int n = nums.length, lo = 0, hi = n - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            boolean isLargerThanLeft = false, isLargerThanRight = false;
            
            if (mid == 0 || nums[mid - 1] < nums[mid]) {
                isLargerThanLeft = true;
            }

            if (mid == n - 1 || nums[mid + 1] < nums[mid]) {
                isLargerThanRight = true;
            }

            if (isLargerThanLeft && isLargerThanRight) {
                return mid;
            } else if (isLargerThanLeft) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        
        return -1;
    }  
}