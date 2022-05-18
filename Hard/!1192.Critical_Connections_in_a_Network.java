package Hard;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {

    private int time = 0;
    int[] disc, low;

    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        disc = new int[n];
        low = new int[n];
        
        List<Integer>[] graph = new ArrayList[n];
        List<List<Integer>> ans = new ArrayList<>();
        Arrays.fill(disc, -1);

        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (List<Integer> connection : connections) {
            int from = connection.get(0), to = connection.get(1);
            graph[from].add(to);
            graph[to].add(from);
        }

        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(i, graph, ans, i);
            }
        }
        return ans;
    }

    private void dfs(int u, List<Integer>[] graph, List<List<Integer>> res, int pre) {
        disc[u] = low[u] = ++time;
        for (int v : graph[u]) {
            if (v == pre) {
                continue;
            }

            if (disc[v] == -1) {
                dfs(v, graph, res, u);
                low[u] = Math.min(low[u], low[v]);
                if (low[v] > disc[u]) {
                    res.add(Arrays.asList(u, v));
                }
            } else {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
    }
}
