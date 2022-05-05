package Hard;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Objects;

// better solution
class Solution {

    public int maxPoints(int[][] points) {
        if (points == null) return 0;
        if (points.length <= 2) return points.length;

        int ans = 0;
        for (int i = 0; i < points.length; i++) {
            HashMap<String, Integer> map = new HashMap<>();

            int max = 0;
            for (int j = i + 1; j < points.length; j++) {
                int dx = points[i][0] - points[j][0];
                int dy = points[i][1] - points[j][1];
                int gcd = gcd(dx, dy);
                
                String slope = dx / gcd + "/" + dy / gcd;
                map.put(slope, map.getOrDefault(slope, 0) + 1);
                max = Math.max(max, map.get(slope));
            }
            ans = Math.max(ans, max + 1);
        }

        return ans;
    }

    private int gcd(int a, int b) {
        if (b == 0) return a;
        else return gcd(b, a % b);
    }
}


// first solution
// class Solution {

//     public int maxPoints(int[][] points) {
//         HashMap<Double, HashMap<Double, HashSet<Point>>> map = new HashMap<>();

//         if (points.length <= 2) return points.length;

//         for (int i = 0; i < points.length; i++) {
//             for (int j = i + 1; j < points.length; j++) {
//                 Point point1 = new Point(points[i][0], points[i][1]);
//                 Point point2 = new Point(points[j][0], points[j][1]);
                
//                 double slope, yIntercept;
//                 if (point1.x == point2.x) {
//                     slope = Double.NaN;
//                     yIntercept = point1.x; // In this case, yIntercept means x-intercept
//                 } else {
//                     slope = (point1.y - point2.y) / (double) (point1.x - point2.x);
//                     yIntercept = point1.y - point1.x * slope;  
//                 }

//                 if (!map.containsKey(slope)) {
//                     map.put(slope, new HashMap<>());
//                 }

//                 if (!map.get(slope).containsKey(yIntercept)) {
//                     map.get(slope).put(yIntercept, new HashSet<>());
//                 }

//                 map.get(slope).get(yIntercept).add(point1);
//                 map.get(slope).get(yIntercept).add(point2);
//             }
//         }

//         int ans = 0;
//         for (double slope : map.keySet()) {
//             for (double yIntercept : map.get(slope).keySet()) {
//                 int count = map.get(slope).get(yIntercept).size();
//                 ans = Math.max(ans, count);
//             }
//         }

//         return ans;
//     }
// }

// class Point {
//     int x;
//     int y;

//     Point(int x, int y) {
//         this.x = x;
//         this.y = y;
//     }

//     @Override
//     public boolean equals(Object o) {
//         if (this == o) return true;
//         if (o == null || getClass() != o.getClass()) return false;
//         Point p = (Point) o;
//         return this.x == p.x && this.y == p.y;
//     }

//     @Override
//     public int hashCode() {
//         return Objects.hash(x, y);
//     }

// }