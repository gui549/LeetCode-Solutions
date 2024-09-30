package Easy;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

// Better Solution
class MyHashSet {
    List<Integer>[] hashSet = null;
    int capacity = 1000;
    double loadFactor = 0.75;
    int count = 0;

    public MyHashSet() {
        hashSet = new LinkedList[capacity];
    }
    
    public void add(int key) {
        if (contains(key)) return;
        if (loadFactor * capacity == count) {
            count = 0;
            capacity *= 2;
            List<Integer>[] oldHashSet = hashSet;
            hashSet = new LinkedList[capacity];
            for (int i = 0; i < oldHashSet.length; i++) {
                List<Integer> hashElements = oldHashSet[i];
                if (hashElements != null) {
                    for (int element : hashElements) {
                        this.add(element);
                    }
                }
            }
        }
        int hash = key % capacity;
        if (hashSet[hash] == null) {
            hashSet[hash] = new LinkedList<>();
        }
        hashSet[hash].add(key);
        count++;
    }
    
    public void remove(int key) {
        int hash = key % capacity;
        List<Integer> hashElements = hashSet[hash];
        if (hashElements != null) {
            if (hashElements.remove(Integer.valueOf(key))) {
                count--;
            }
        }
    }
    
    public boolean contains(int key) {
        int hash = key % capacity;
        List<Integer> hashElements = hashSet[hash];
        if (hashElements != null) {
            return hashElements.contains(Integer.valueOf(key));
        }
        return false;
    }
}

// simple solution
// class MyHashSet {
//     boolean[] hashSet;

//     public MyHashSet() {
//         hashSet = new boolean[1000001];
//     }
    
//     public void add(int key) {
//         hashSet[key] = true;
//     }
    
//     public void remove(int key) {
//         hashSet[key] = false;
//     }
    
//     public boolean contains(int key) {
//         return hashSet[key];
//     }
// }