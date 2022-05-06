package Medium;

import java.util.ArrayList;
import java.util.Stack;

class Solution {
    public int evalRPN(String[] tokens) {
        ArrayList<Integer> stack = new ArrayList<>(tokens.length);

        for (String token : tokens) {
            if (token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
                int num2 = stack.remove(stack.size() - 1);
                int num1 = stack.remove(stack.size() - 1);
                int result = 0;
                switch (token) {
                    case "+": result = num1 + num2;
                              break;
                    case "-": result = num1 - num2;
                              break;
                    case "*": result = num1 * num2;
                              break;
                    case "/": result = num1 / num2;
                              break;
                }
                stack.add(result);
            } else {
                int num = Integer.parseInt(token);
                stack.add(num);
            }
        }
        return stack.get(0);
    }
}
