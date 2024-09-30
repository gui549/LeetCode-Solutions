package Medium;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

// better soultion
class Solution {
    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        if (pairs == null) return s;
        
        UnionFind uf = new UnionFind(s.length());
        for (List<Integer> pair : pairs) {
            uf.union(pair.get(0), pair.get(1));
        }
        
        Map<Integer, PriorityQueue<Character>> map = new HashMap<>();
        char[] sChar = s.toCharArray();
        for(int i = 0; i < sChar.length; i++) {
            int parent = uf.find(i);
            map.putIfAbsent(parent, new PriorityQueue<>());
            map.get(parent).offer(sChar[i]);
        }
        
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < sChar.length; i++) {
            sb.append(map.get(uf.find(i)).poll());
        }
        
        return sb.toString();
    }
}



// first solution
// class Solution {
//     public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
//         if (pairs == null) return s;
//         StringBuffer sb = new StringBuffer();

//         UnionFind uf = new UnionFind(s.length());
//         for (List<Integer> pair : pairs) {
//             uf.union(pair.get(0), pair.get(1));
//         }

//         Map<Integer, List<Integer>> map = new HashMap<>();
//         for(int i = 0; i < uf.parent.length; i++) {
//             int parent = uf.find(i);
//             if (parent != i) {
//                 if (map.containsKey(parent)) {
//                     map.get(parent).add(i);
//                 } else {
//                     List<Integer> union = new ArrayList<>();
//                     union.add(parent);
//                     union.add(i);
//                     map.put(parent, union);
//                 }
//             }
//         }

//         Map<Integer, List<Integer>> mapWithSortedElements = new HashMap<>();
//         map.forEach((k, v) -> {
//             mapWithSortedElements.put(k, new ArrayList<>(v));
//         });

//         map.forEach((k, v) -> {
//             v.sort((i1, i2) -> Integer.compare(i1, i2));
//         });

//         mapWithSortedElements.forEach((k, v) -> {
//             v.sort((i1, i2) -> Character.compare(s.charAt(i1), s.charAt(i2)));
//         });

//         int[] indices = new int[s.length()];
//         for (int i = 0; i < indices.length; i++) indices[i] = i;

//         map.forEach((k, v) -> {
//             for (int i = 0; i < v.size(); i++) {
//                 indices[v.get(i)] = mapWithSortedElements.get(k).get(i);
//             }
//         });
        
//         for (int i = 0; i < indices.length; i++) {
//             sb.append(s.charAt(indices[i]));
//         }

//         return sb.toString();
//     }
// }

class UnionFind {

    int[] parent;

    public UnionFind(int n) {
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i; 
    }

    public int find(int x) {
        if (x != parent[x]) parent[x] = find(parent[x]);
        return parent[x];
    }

    public void union(int x, int y) {
        parent[find(x)] = parent[find(y)];
    }
}