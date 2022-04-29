package Medium;

import java.util.LinkedList;
import java.util.Queue;


// DFS solution
class Solution {
    public boolean isBipartite(int[][] graph) {
        int[] colors = new int[graph.length];

        for (int i = 0; i < graph.length; i++) {
            if (colors[i] == 0 && !dfs(graph, colors, i, 1)) // ✅
                return false; 
        }
    
        return true;
    }

    public boolean dfs(int[][] graph, int[] colors, int curr, int color) {
        colors[curr] = color;
        for (int next : graph[curr]) {
            if (colors[next] == -color) continue;
            if (colors[next] == color || dfs(graph, colors, next, -color)) return false;
        }
        return true;
    }
}



// BFS solution
// class Solution {
//     public boolean isBipartite(int[][] graph) {
//         int[] color = new int[graph.length];

//         for (int i = 0; i < graph.length; i++) {
//             if (color[i] != 0) continue;
//             Queue<Integer> queue = new LinkedList<>();
//             color[i] = 1;
//             queue.add(i);

//             while (!queue.isEmpty()) {
//                 int currentNode = queue.poll();
//                 for (int nextNode : graph[currentNode]) {
//                     if (color[nextNode] == 0) {
//                         color[nextNode] = -color[currentNode];
//                         queue.add(nextNode);
//                     } else if (color[nextNode] != -color[currentNode]) {
//                         return false;
//                     }
//                 }
//             }
//         }
//         return true;
//     }
// }
