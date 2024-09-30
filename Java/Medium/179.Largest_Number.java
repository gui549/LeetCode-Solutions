package Medium;

import java.util.Arrays;
import java.util.Comparator;

// better solution
class Solution {
    public String largestNumber(int[] nums) {
        if (Arrays.stream(nums).sum() == 0) {
            return "0";
        }

        StringBuffer sb = new StringBuffer();
        Comparator<String> comparator = (s1, s2) -> (s2 + s1).compareTo(s1 + s2);

        Arrays.stream(nums).mapToObj(Integer::toString).sorted(comparator).forEach(sb::append);
        return sb.toString();
    }
}


// first solution
// class Solution {
//     public String largestNumber(int[] nums) {
//         if (Arrays.stream(nums).sum() == 0) {
//             return "0";
//         }

//         StringBuffer sb = new StringBuffer();
//         Comparator<String> comparator = (s1, s2) -> {
//             int pt1 = 0, pt2 = 0;

//             // compare s1 and s2 until both reaches the end
//             while (pt1 != s1.length() - 1 || pt2 != s2.length() - 1) {
//                 if (s1.charAt(pt1) != s2.charAt(pt2)) {
//                     return s2.charAt(pt2) - s1.charAt(pt1);
//                 }

//                 pt1 = (pt1 + 1) % s1.length();
//                 pt2 = (pt2 + 1) % s2.length();
//             }
//             return s2.charAt(pt2) - s1.charAt(pt1);
//         };

        
//         Arrays.stream(nums).mapToObj(Integer::toString).sorted(comparator).forEach(sb::append);
//         return sb.toString();
//     }
// }