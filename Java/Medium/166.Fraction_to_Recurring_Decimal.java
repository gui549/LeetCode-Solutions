package Medium;

import java.util.HashMap;

class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        
        StringBuffer sb = new StringBuffer();
        if ((numerator > 0) ^ (denominator > 0)) { // ✅
            sb.append('-');
        }
        
        long num = Math.abs((long) numerator);
        long den = Math.abs((long) denominator);

        sb.append(num / den);
        num %= den;
        if (num == 0) {
            return sb.toString();
        } 
        sb.append('.');
        
        HashMap<Long, Integer> indices = new HashMap<>();
        while (num != 0) {
            num *= 10;
            if (indices.containsKey(num)) {
                sb.insert((int) indices.get(num), '(');
                sb.append(')');
                return sb.toString();
            } 

            indices.put(num, sb.length());
            sb.append(num / den);
            num %= den;
        }

        return sb.toString();
    }
}