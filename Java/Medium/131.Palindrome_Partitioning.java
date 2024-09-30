package Medium;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

// better solution
class Solution {
    public List<List<String>> partition(String s) {
        if (s == null || s.length() == 0) return new ArrayList<>();
        
        List<List<String>> result = new ArrayList<>();
        helper(s, new ArrayList<>(), result);
        return result;
    }

    public void helper(String s, List<String> step, List<List<String>> result) {
        if (s == null || s.length() == 0) {
            result.add(new ArrayList<>(step));
            return;
        }

        for (int i = 1; i <= s.length(); i++) {
            String temp = s.substring(0, i);
            if (!isPalindrome(temp)) continue;
            
            step.add(temp);  // choose
            helper(s.substring(i, s.length()), step, result);
            step.remove(step.size() - 1);
        }

        return;
    }

    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        
        while (left <= right) {
            if (s.charAt(left) != s.charAt(right))
                return false;
            left++;
            right--;
        }

        return true;
    }
}

// first soultion
// class Solution {
//     public List<List<String>> partition(String s) {
//         List<List<String>> res = new ArrayList<>();
//         if (s == "") res.add(new LinkedList<>());
//         for (int i = 1; i < s.length() + 1; i++) {
//             String head = s.substring(0, i);
//             if (isPanlindrome(head)) {
//                 List<List<String>> tmp = partition(s.substring(i));
//                 tmp.forEach(li -> li.add(0, head));
//                 res.addAll(tmp);
//             }
//         }
//         return res;
//     }

//     private boolean isPanlindrome(String s) {
//         if (s == null) return false;
//         for (int i = 0; i < s.length() / 2; i++) {
//             if (s.charAt(i) != s.charAt(s.length() - 1 - i)) return false;
//         }
//         return true;
//     }
// }