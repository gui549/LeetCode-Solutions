package Medium;

class Solution {
    public int minCost(String colors, int[] neededTime) {
        char ch = '#';
        int ans = 0, maxTime = 0;
        for (int i = 0; i < colors.length(); i++) {
            if (ch != colors.charAt(i)) {
                ch = colors.charAt(i);
                maxTime = neededTime[i];
            } else {
                ans += Math.min(maxTime, neededTime[i]);
                maxTime = Math.max(maxTime, neededTime[i]);
            }
        }

        return ans;
    }
}