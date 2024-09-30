package Hard;

import java.util.Collections;
import java.util.PriorityQueue;
import java.util.TreeSet;

// use TreeSet
class SORTracker {

    private TreeSet<Location> locations;
    private Location lastReturned;

    public SORTracker() {
        locations = new TreeSet<>();
        lastReturned = new Location("", Integer.MAX_VALUE);
    }
    
    public void add(String name, int score) {
        Location location = new Location(name, score);
        locations.add(location);

        if (location.compareTo(lastReturned) > 0) {
            lastReturned = locations.higher(lastReturned);
        }
    }
    
    public String get() {
        lastReturned = locations.lower(lastReturned);

        return lastReturned.name;
    }
}

// use two heap
// class SORTracker {

//     private PriorityQueue<Location> maxHeap;
//     private PriorityQueue<Location> minHeap;

//     public SORTracker() {
//         maxHeap = new PriorityQueue<>(Collections.reverseOrder());
//         minHeap = new PriorityQueue<>();
//     }
    
//     public void add(String name, int score) {
//         Location newLocation = new Location(name, score);
//         Location tmp = minHeap.poll();
//         if (tmp == null) {
//             maxHeap.add(newLocation);
//             return;
//         }

//         if (newLocation.compareTo(tmp) > 0) {
//             minHeap.add(newLocation);
//             maxHeap.add(tmp);
//         } else {
//             minHeap.add(tmp);
//             maxHeap.add(newLocation);
//         }

//     }
    
//     public String get() {
//         Location res = maxHeap.poll();
//         if (res == null) {
//             throw new IllegalStateException();
//         }
//         minHeap.add(res);

//         return res.name;
//     }
// }

class Location implements Comparable<Location> {

    String name;
    int score;

    Location(String name, int score) {
        this.name = name;
        this.score = score;
    }

    @Override
    public int compareTo(Location o) {
        if (this.score != o.score) {
            return Integer.compare(this.score, o.score);
        }
        return -this.name.compareTo(o.name);
    }
}