package Medium;

import java.security.DrbgParameters.NextBytes;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.PriorityQueue;

class Solution {

    public int networkDelayTime(int[][] times, int n, int k) {
        HashMap<Integer, HashMap<Integer, Integer>> graph = new HashMap<>();
        for (int[] time : times) {
            if (!graph.containsKey(time[0])) {
                graph.put(time[0], new HashMap<>());
            }
            graph.get(time[0]).put(time[1], time[2]);
        }

        PriorityQueue<Integer[]> pq = new PriorityQueue<>((o1, o2) -> Integer.compare(o1[0], o2[0]));
        HashMap<Integer, Integer> cost = new HashMap<>();
        pq.add(new Integer[]{0, k});
        while (!pq.isEmpty() && cost.size() < n) {
            Integer[] edge = pq.poll();
            int weight = edge[0];
            int node = edge[1];
            
            if (cost.containsKey(node)) {
                continue;
            }

            cost.put(node, weight);

            if (graph.containsKey(node)) {
                for (Integer nextNode : graph.get(node).keySet()) {
                    pq.add(new Integer[] {weight + graph.get(node).get(nextNode), nextNode});
                }
            }
        }
        
        if (cost.size() < n) {
            return -1;
        }

        return cost.values().stream().mapToInt(s -> (int) s).max().getAsInt();        
    }
}