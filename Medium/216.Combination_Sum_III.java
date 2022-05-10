package Medium;

import java.util.ArrayList;
import java.util.List;


// better solution
class Solution {

    List<List<Integer>> ans = new ArrayList<>();

    public List<List<Integer>> combinationSum3(int k, int n) {
        combination(new ArrayList<>(), k, 1, n);
        return ans;
    }

    public void combination(List<Integer> comb, int k, int start, int n) {
        if (comb.size() == k && n == 0) {
            List<Integer> res = new ArrayList<>(comb);
            ans.add(res);
            return;
        }

        if (comb.size() == k || n < 0) {
            return;
        }

        for (int i = start; i <= 9; i++) {
            comb.add(i);
            combination(comb, k, i + 1, n - i);
            comb.remove(comb.size() - 1);
        }
    }   
}

// first solution
// class Solution {
//     public List<List<Integer>> combinationSum3(int k, int n) {
//         List<List<Integer>> candidates = combination(9, k, n);
//         List<List<Integer>> ans = new ArrayList<>();
//         for (List<Integer> sublist : candidates) {
//             if (sublist.stream().mapToInt(Integer::intValue).sum() == n) {
//                 ans.add(sublist);
//             }
//         }
//         return ans;
//     }

//     public List<List<Integer>> combination(int n, int k, int target) {
//         List<List<Integer>> res = new ArrayList<>();
//         if (k == 0) {
//             res.add(new ArrayList<>());
//             return res;
//         }
        
//         for (int i = n - 1; i >= 1; i--) {
//             for (List<Integer> sublist : combination(i, k - 1, target)) {
//                 sublist.add(i);
//                 if (sublist.stream().mapToInt(Integer::intValue).sum() <= target) {
//                     res.add(new ArrayList<>(sublist));
//                 }
//             }
//         }
       
//         return res;
//     }   
// }