class MyCircularQueue {
    int[] arr;
    int front;
    int size;

    public MyCircularQueue(int k) {
        arr = new int[k];
        front = 0;
        size = 0;
    }
    
    public boolean enQueue(int value) {
        if(isFull()) return false;
        
        arr[(front + size) % arr.length] = value;
        ++size;
        return true;
    }
    
    public boolean deQueue() {
        if(isEmpty()) return false;
        front = (front + 1) % arr.length;
        --size;
        return true;
    }
    
    public int Front() {
        if(isEmpty()) return -1;
        return arr[front];
    }
    
    public int Rear() {
        if(isEmpty()) return -1;
        return arr[(front + size - 1) % arr.length];
    }
    
    public boolean isEmpty() {
        return size == 0;
    }
    
    public boolean isFull() {
        return size == arr.length;
    }
}
