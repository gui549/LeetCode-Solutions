package Medium;

import java.util.Arrays;

// better solution
class Solution {
    public int countVowelStrings(int n) {
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) / 24; // combination(n+4, 4)
    }
}

// first solution
// class Solution {
//     public int countVowelStrings(int n) {
//         int[] count = new int[5];
//         count[0] = 1;
//         for (int i = 0; i < n; i++) {
//             for (int j = 1; j < 5; j++) {
//                 count[j] += count[j - 1];
//             }
//         }
//         return Arrays.stream(count).sum();
//     }
// }