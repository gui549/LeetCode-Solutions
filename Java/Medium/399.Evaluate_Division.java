package Medium;

import java.util.HashMap;
import java.util.List;

// better solution
class Solution {
    
    HashMap<String, String> root = new HashMap<>();
    HashMap<String, Double> vals = new HashMap<>();
    HashMap<String, HashMap<String, Double>> edges = new HashMap<>();

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        int n = equations.size(), m = queries.size();
        for (int i = 0; i < n; i++) {
            String x = equations.get(i).get(0), y = equations.get(i).get(1);
            if (!edges.containsKey(x))
                edges.put(x, new HashMap<>());
            if (!edges.containsKey(y))
                edges.put(y, new HashMap<>());
            edges.get(x).put(y, values[i]);
            edges.get(y).put(x, 1 / values[i]);
        }

        for (String x : edges.keySet()) {
            if (!vals.containsKey(x)) dfs(x, x, 1);
        }
        double[] ans = new double[m];
        for (int i = 0; i < m; i++) {
            String x = queries.get(i).get(0), y = queries.get(i).get(1);
            String px = root.getOrDefault(x, x), py = root.getOrDefault(y, y);
            if (px != py) 
                ans[i] = -1.0;
            else
                ans[i] = vals.get(x) / vals.get(y);
        }
        return ans;
    }
    
    private void dfs(String x, String p, double v) {
        vals.put(x, v);
        root.put(x, p);
        for (String y : edges.get(x).keySet()) {
            if (!vals.containsKey(y)) 
                dfs(y, p, v * edges.get(y).get(x));
        }
    }
}


// first solution
// class Solution {
    
//     private HashMap<String, List<String>> adjacentMap = new HashMap<>();;
//     private HashMap<String, Double> valueMap = new HashMap<>();;
//     private HashMap<String, Double> absValueMap = new HashMap<>();;
//     private HashMap<String, String> parentMap = new HashMap<>();;


//     public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
//         double[] ans = new double[queries.size()];

//         for (int i = 0; i < equations.size(); i++) {
//             List<String> eq = equations.get(i);
//             if (!adjacentMap.containsKey(eq.get(0))) {
//                 adjacentMap.put(eq.get(0), new ArrayList<>());  
//             }
//             if (!adjacentMap.containsKey(eq.get(1))) {
//                 adjacentMap.put(eq.get(1), new ArrayList<>());  
//             }
//             adjacentMap.get(eq.get(0)).add(eq.get(1));
//             adjacentMap.get(eq.get(1)).add(eq.get(0));
     
//             valueMap.put(eq.get(0) + ":" + eq.get(1), values[i]);
//             valueMap.put(eq.get(1) + ":" + eq.get(0), 1 / values[i]);
//         }

//         for (String var : adjacentMap.keySet()) {
//             if (absValueMap.containsKey(var)) continue;
//             parentMap.put(var, var);
//             absValueMap.put(var, 1.0);
//             dfs(var, 1.0, var);
//         }
        
//         for (int i = 0; i < queries.size(); i++) {
//             List<String> query = queries.get(i);
//             if (!absValueMap.containsKey(query.get(0)) || !absValueMap.containsKey(query.get(1))) {
//                 ans[i] = -1.0;
//             } else if (parentMap.get(query.get(0)) != parentMap.get(query.get(1))) {
//                 ans[i] = -1.0;
//             } else {
//                 ans[i] = absValueMap.get(query.get(1)) / absValueMap.get(query.get(0));                 }
//         }

//         return ans;
//     }
    
//     private void dfs(String var, double currentAbsValue, String parent) {
//         for (String nextVar : adjacentMap.get(var)) {
//             if (absValueMap.containsKey(nextVar)) continue;
//             double nextAbsValue = currentAbsValue * valueMap.get(var + ":" + nextVar);
//             absValueMap.put(nextVar, nextAbsValue);
//             parentMap.put(nextVar, parent);
//             dfs(nextVar, nextAbsValue, parent);
//         }
//     }
// }
