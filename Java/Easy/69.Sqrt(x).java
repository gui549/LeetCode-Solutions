package Easy;

class Solution {
    public int mySqrt(int x) {
        long y = 0L;
        while (y * y <= x) {
            y++;
        }
        return (int) y - 1; 
    }
}