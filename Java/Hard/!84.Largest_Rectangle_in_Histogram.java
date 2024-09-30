package Hard;

import java.util.Stack;

// easy to understand solution 
class Solution {
    public int largestRectangleArea(int[] heights) {
        if (heights == null || heights.length == 0) return 0;
        int[] lessFromLeft = new int[heights.length];
        int[] lessFromRight = new int[heights.length];

        lessFromLeft[0] = -1;
        lessFromRight[heights.length - 1] = heights.length;

        for (int i = 1; i < heights.length; i++) {
            int p = i - 1;

            while (p >= 0 && heights[p] >= heights[i]) {
                p = lessFromLeft[p];
            }

            lessFromLeft[i] = p;
        }

        for (int i = heights.length - 2; i >= 0; i--) {
            int p = i + 1;

            while (p <= heights.length - 1 && heights[p] >= heights[i]) {
                p = lessFromRight[p];
            }

            lessFromRight[i] = p;
        }

        int ans = 0;
        for (int i = 0; i < heights.length; i++) {
            ans = Math.max(ans, heights[i] * (lessFromRight[i] - lessFromLeft[i] - 1));
        }

        return ans;
    }
}


// more compact solution
// class Solution {
//     public int largestRectangleArea(int[] heights) {
//         if (heights == null || heights.length == 0) return 0;
//         Stack<Integer> stack = new Stack<>();
//         int ans = 0;

//         for (int i = 0; i < heights.length + 1; i++) {
//             int height = (i == heights.length ? 0 : heights[i]);
//             if (stack.isEmpty() || height >= heights[stack.peek()]) {
//                 stack.push(i);
//             } else {
//                 int tp = stack.pop();
//                 int width = (stack.isEmpty() ? i : i - 1 - stack.peek());
//                 ans = Math.max(ans, heights[tp] * width);
//                 i--;
//             }
//         }

//         return ans;
//     }
// }


