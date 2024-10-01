class Solution {
    fun isPalindrome(x: Int): Boolean {
        var num = x
        var reverse = 0
        while (num > 0) {
            reverse -= num % 10
            num = num / 10
        }

        return if (x + reverse == 0) true else false;
    }
}