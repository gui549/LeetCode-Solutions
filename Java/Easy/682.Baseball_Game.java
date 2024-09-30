package Medium;

import java.util.Stack;

class Solution {
    public int calPoints(String[] ops) {
        int sum = 0;
        Stack<Integer> stack = new Stack<>();
        
        for (String op : ops) {
            if (op.equals("C")) {
                sum -= stack.pop();

            } else if (op.equals("D")) {
                Integer item = stack.peek() * 2;
                sum += item;
                stack.push(item);

            } else if (op.equals("+")) {
                Integer item1 = stack.get(stack.size() - 1);
                Integer item2 = stack.get(stack.size() - 2);                
                sum += item1 + item2;
                stack.push(item1 + item2);

            } else {
                sum += Integer.parseInt(op);
                stack.push(Integer.valueOf(op));
            }

        }
        return sum;
    }
}