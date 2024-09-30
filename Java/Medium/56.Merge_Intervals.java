package Medium;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


class Solution {
	public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) {
            return intervals;
        }

        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));
        
        List<int[]> ans = new ArrayList<>();
        int[] newInterval = intervals[0];
        ans.add(newInterval);
        for (int[] interval : intervals) {
            if (interval[0] <= newInterval[1]) {
                newInterval[1] = Math.max(interval[1], newInterval[1]);
            } else {
                newInterval = interval;
                ans.add(newInterval);
            }
        }

        return ans.toArray(new int[ans.size()][]);
    }
}



/*
class Solution {
    public int[][] merge(int[][] intervals) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int[] interval : intervals) {
            map.put(interval[0], map.getOrDefault(interval[0], 0) + 1);
            map.put(interval[1], map.getOrDefault(interval[1], 0) - 1);
        }    

        List<Integer> keys = new ArrayList<>(map.keySet());
        keys.sort((s1, s2) -> s1.compareTo(s2));

        int count = 0;
        List<int[]> ans = new ArrayList<>();
        int[] tmp = new int[2];
        for (Integer key : keys) {
            if (count == 0) {
                tmp[0] = key;
            }
            count += map.get(key);

            if (count == 0) {
                tmp[1] = key;
                ans.add(tmp.clone());
            }
        }

        return ans.toArray(new int[ans.size()][]);
    }
}
*/