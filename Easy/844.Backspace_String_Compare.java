package Easy;

// better solution
class Solution {
    public boolean backspaceCompare(String s, String t) {
        int i = s.length() - 1, j = t.length() - 1, back;
        while (true) {
            back = 0;
            while (i >= 0 && (back > 0 || s.charAt(i) == '#')) {
                back += s.charAt(i) == '#' ? 1 : -1; // ✅
                i--; 
            }
            back = 0;
            while (j >= 0 && (back > 0 || t.charAt(j) == '#')) {
                back += t.charAt(j) == '#' ? 1 : -1; // ✅
                j--; 
            }
            if (i >= 0 && j >= 0 && s.charAt(i) == t.charAt(j)) {
                i--;
                j--;
            } else {
                break;
            }
        }
        return i == -1 && j == -1;
    }
}

// first solution
// class Solution {
//     public boolean backspaceCompare(String s, String t) {
//         int pt1 = s.length() - 1, pt2 = t.length() - 1;
//         int back1 = 0, back2 = 0;
//         while (pt1 >= 0 && pt2 >= 0) {
//             while (pt1 >= 0 && (s.charAt(pt1) == '#' || back1 > 0)) {
//                 if (s.charAt(pt1) == '#') back1++;
//                 else if (back1 > 0) back1--;
//                 pt1--;
//             }
            
//             while (pt2 >= 0 && (t.charAt(pt2) == '#' || back2 > 0)) {
//                 if (t.charAt(pt2) == '#') back2++;
//                 else if (back2 > 0) back2--;
//                 pt2--;
//             }

//             if (pt1 >= 0 && pt2 >= 0 && s.charAt(pt1) != t.charAt(pt2)) {
//                 System.out.println(s.charAt(pt1) + " " + t.charAt(pt2));
//                 return false;
//             }
            
//             if (pt1 >= 0 && pt2 >= 0) {
//                 pt1--; pt2--;
//             }
//         }

//         while (pt1 >= 0 && (s.charAt(pt1) == '#' || back1 > 0)) {
//             if (s.charAt(pt1) == '#') back1++;
//             else if (back1 > 0) back1--;
//             pt1--;
//         }
        
//         while (pt2 >= 0 && (t.charAt(pt2) == '#' || back2 > 0)) {
//             if (t.charAt(pt2) == '#') back2++;
//             else if (back2 > 0) back2--;
//             pt2--;
//         }
        
//         return pt1 < 0 && pt2 < 0;
//     }
// }