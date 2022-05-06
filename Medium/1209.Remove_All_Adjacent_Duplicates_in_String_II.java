package Medium;

import java.util.Stack;

// better solution
class Solution {
    public String removeDuplicates(String s, int k) {
        int[] count = new int[s.length()];
        StringBuffer sb = new StringBuffer();
        for (char c : s.toCharArray()) {
            sb.append(c);
            int last = sb.length() - 1;
            count[last] = 1 + (last > 0 && sb.charAt(last) == sb.charAt(last - 1) ? count[last - 1] : 0);
            if (count[last] >= k) sb.delete(sb.length() - k, sb.length());
        }
        return sb.toString();
    }
}

// first solution
// class Solution {
//     public String removeDuplicates(String s, int k) {
//         StringBuffer sb = new StringBuffer(s);
//         Stack<Integer> startIndices = new Stack<>();
//         char currentChar = '#';
//         int count = 0;

//         for (int i = 0; i < sb.length(); i++) {
//             if (currentChar != sb.charAt(i)) {
//                 currentChar = sb.charAt(i);
//                 startIndices.add(i);
//                 count = 1;
//             } else {
//                 if (k == ++count) {
//                     int idx = startIndices.pop();
//                     for (int j = 0; j < k; j++) {
//                         sb.deleteCharAt(idx);
//                     }
//                     if (!startIndices.isEmpty()) {
//                         i = startIndices.pop() - 1;
//                     } else {
//                         i = 0;
//                     }
//                 }
//             }
//         }

//         return sb.toString();
//     }
// }