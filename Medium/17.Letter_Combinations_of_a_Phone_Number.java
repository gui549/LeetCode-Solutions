package Medium;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

class Solution {

    static final String[] letters = new String[] {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    
    public List<String> letterCombinations(String digits) {
        if (digits == null || digits.length() == 0) 
            return new LinkedList<>();
        
        LinkedList<String> ans = new LinkedList<>();
        ans.add("");
        
        for (int i = 0; i < digits.length(); i++) {
            int size = ans.size();
            for (int j = 0; j < size; j ++) {
                String prevString = ans.removeFirst();
                for (char letter : letters[digits.charAt(i) - '0'].toCharArray()) { 
                    ans.add(prevString + letter);
                }
            }
        }
        return ans;
    }
}