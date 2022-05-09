package Easy;

class Solution {
    public int titleToNumber(String columnTitle) {
        int ans = 0;
        for (int i = columnTitle.length() - 1; i >= 0; i--) {
            ans += (columnTitle.charAt(i) - '@') * (int) Math.pow(26, columnTitle.length() - 1 - i);
        }
        return ans;
    }
}