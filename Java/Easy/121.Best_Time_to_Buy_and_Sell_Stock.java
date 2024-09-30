package Easy;

class Solution {
    public int maxProfit(int[] prices) {
        int buyPrice = Integer.MAX_VALUE;
        int ans = 0;
        for (int price : prices) {
            if (price < buyPrice) {
                buyPrice = price;
            } 

            ans = Math.max(ans, price - buyPrice);
        }
        return ans;
    }
}