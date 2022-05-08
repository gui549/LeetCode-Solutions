package Medium;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

interface NestedInteger {

    // @return true if this NestedInteger holds a single integer, rather than a nested list.
    public boolean isInteger();
    
    // @return the single integer that this NestedInteger holds, if it holds a single integer
    // Return null if this NestedInteger holds a nested list
    public Integer getInteger();
    
    // @return the nested list that this NestedInteger holds, if it holds a nested list
    // Return empty list if this NestedInteger holds a single integer
    public List<NestedInteger> getList();
}


class NestedIterator implements Iterator<Integer> {

    int idx = 0;
    List<Integer> list;

    public NestedIterator(List<NestedInteger> nestedList) {
        list = unpack(nestedList);
    }

    private List<Integer> unpack(List<NestedInteger> nestedList) {
        List<Integer> res = new ArrayList<>();
        for (NestedInteger ele : nestedList) {
            if (ele.isInteger()) {
                res.add(ele.getInteger());
            } else {
                res.addAll(unpack(ele.getList()));
            }
        }

        return res;
    }

    @Override
    public Integer next() {
        return list.get(idx++);        
    }

    @Override
    public boolean hasNext() {
        return list.size() >= idx;
    }
}
