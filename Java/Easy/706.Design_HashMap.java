package Easy;

import java.util.LinkedList;
import java.util.List;

class MyHashMap {

    List<Integer[]>[] hashMap;
    int capacity = 1000;
    double loadFactor = 0.75;
    int count = 0;

    public MyHashMap() {
        hashMap = new LinkedList[capacity];
    }
    
    public void put(int key, int value) {
        if (count == capacity * loadFactor) {
            count = 0;
            capacity *= 2;
            List<Integer[]>[] oldHashMap = hashMap;
            hashMap = new LinkedList[capacity];
            for (int i = 0; i < oldHashMap.length; i++) {
                for (Integer[] item : hashMap[i]) {
                    this.put(item[0], item[1]);
                }
            }
        }
        int hash = key % capacity;
        if (hashMap[hash] == null) {
            hashMap[hash] = new LinkedList<>();
        }
        for (Integer[] item : hashMap[hash]) {
            if (item[0] == key) {
                item[1] = value;
                return;
            }
        }
        Integer[] newItem = { Integer.valueOf(key), Integer.valueOf(value) }; 
        hashMap[hash].add(newItem);
    }
    
    public int get(int key) {
        int hash = key % capacity;
        List<Integer[]> hashElements = hashMap[hash];
        if (hashElements != null) {
            for (Integer[] item : hashElements) {
                if (item[0] == key) return item[1];
            }
        }
        return -1; 
    }
    
    public void remove(int key) {
        int hash = key % capacity;
        List<Integer[]> hashElements = hashMap[hash];
        if (hashElements != null) {
            for (int i = 0; i < hashElements.size(); i++) {
                if (hashElements.get(i)[0] == key) {
                    hashElements.remove(i);
                    break;
                }
            }
        }
    }
}