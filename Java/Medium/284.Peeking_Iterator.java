package Medium;

import java.util.Iterator;

class PeekingIterator implements Iterator<Integer> {
	
    private Iterator<Integer> iterator;
    private Integer nextItem;
    private boolean isFininshed = false;

    public PeekingIterator(Iterator<Integer> iterator) {
        this.iterator = iterator;
        if (iterator.hasNext()) {
            nextItem = iterator.next();
        } else {
            isFininshed = true;
        }
	}
	
	public Integer peek() {
        return nextItem;
    }
	
	@Override
	public Integer next() {
        Integer res = nextItem;
        if (iterator.hasNext()) {
            nextItem = iterator.next();
        } else {
            isFininshed = true;
        }
        return res;
	}
	
	@Override
	public boolean hasNext() {
	    return! isFininshed;
	}
}