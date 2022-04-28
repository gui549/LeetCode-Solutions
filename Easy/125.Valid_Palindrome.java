package Easy;

// better solution
class Solution {
    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {

            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) left++;
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) right--;
            
            if (Character.toLowerCase(s.charAt(left++)) != Character.toLowerCase(s.charAt(right--))) 
                return false;
        }
        return true;
    }
}

// first solution
// class Solution {
//     public boolean isPalindrome(String s) {
//         StringBuffer sb = new StringBuffer();
//         for (int i = 0; i < s.length(); i++) {
//             char ch = s.charAt(i);
//             if (Character.isLetterOrDigit(ch)) 
//                 sb.append(Character.toLowerCase(ch));
//         }

//         for (int i = 0; i < sb.length() / 2; i++) {
//             if (sb.charAt(i) != sb.charAt(sb.length() - 1 - i)) return false;
//         }
//         return true;
//     }
// }