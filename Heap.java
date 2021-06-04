class Heap{
    public int[] heap;
    private int size;
    private int maxSize;
    private HeapType type;

    public enum HeapType {
        MAX,
        MIN
    }

    public Heap(int maxSize, HeapType type){
        heap = new int[maxSize+1];
        this.maxSize = maxSize;
        size = 0;
        this.type = type;
        if (type.equals(HeapType.MAX))
            heap[0] = Integer.MAX_VALUE;
        else
            heap[0] = Integer.MIN_VALUE;
    }

    public void insert(int val){
        heap[++size] = val;
        bubbleUp(size);
    }

    private int parent(int pos){
        return pos/2;
    }

    private int leftChild(int pos){
        return (2 * pos);
    }

    private int rightChild(int pos){
        return (2 * pos) + 1;
    }

    private void swap(int p0,int p1){
        int tmp = heap[p0];
        heap[p0] = heap[p1];
        heap[p1] = tmp;
    }

    private boolean isLeaf(int pos){
        return (pos > (size / 2) && pos <= size);
    }

    private void bubbleDown(int pos){
        if (isLeaf(pos))
            return;
        if(type.equals(HeapType.MAX)) {
            if (heap[pos] < heap[leftChild(pos)] || heap[pos] < heap[rightChild(pos)]) {
                if (heap[leftChild(pos)] > heap[rightChild(pos)]) {
                    swap(pos, leftChild(pos));
                    bubbleDown(leftChild(pos));
                } else {
                    swap(pos, rightChild(pos));
                    bubbleDown(rightChild(pos));
                }
            }
        }
        else{
            if (heap[pos] > heap[leftChild(pos)] || heap[pos] > heap[rightChild(pos)]) {
                if (heap[leftChild(pos)] < heap[rightChild(pos)]) {
                    swap(pos, leftChild(pos));
                    bubbleDown(leftChild(pos));
                } else {
                    swap(pos, rightChild(pos));
                    bubbleDown(rightChild(pos));
                }
            }
        }
    }

    private void bubbleUp(int pos){
        if(type.equals(HeapType.MAX)) {
            while (heap[pos] > heap[parent(pos)]) {
                swap(pos, parent(pos));
                pos = parent(pos);
            }
        }
        else{
            while (heap[pos] < heap[parent(pos)]) {
                swap(pos, parent(pos));
                pos = parent(pos);
            }
        }
    }

    public int pop(){
        int out = heap[1];
        heap[1] = heap[size--];
        bubbleDown(1);
        return out;
    }
}