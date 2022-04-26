package Medium;

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int minCostConnectPoints(int[][] points) {
        PriorityQueue<Edge> pq = new PriorityQueue<>(); 
        int[] parent = new int[points.length];
        Arrays.setAll(parent, p -> p);
        
        for (int i = 0; i < points.length - 1; i++) {
            for (int j = i + 1; j < points.length; j++) {
                int dist = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                pq.add(new Edge(dist, i, j));
            }
        }

        int ans = 0;
        int numEdges = 0;
        UnionFind uf = new UnionFind(points.length);
        while (numEdges < points.length - 1) {
            Edge edge = pq.poll();
            if (uf.find(edge.startNode) != uf.find(edge.endNode)) {
                ans += edge.weight;
                numEdges++;
                uf.union(edge.startNode, edge.endNode);
            }
        }
        return ans;
    }
}

class UnionFind {
    int[] parent;

    UnionFind(int n) {
        this.parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    public void union(int a, int b) {
        parent[find(a)] = parent[find(b)];
    }

    public int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
}

class Edge implements Comparable<Edge>{
    
    int weight;
    int startNode;
    int endNode;

    Edge(int weight, int startNode, int endNode) {
        this.weight = weight;
        this.startNode = startNode;
        this.endNode = endNode;
    }

    @Override
    public int compareTo(Edge o) {
        return this.weight - o.weight;
    }
}