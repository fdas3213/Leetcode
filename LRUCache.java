import java.util.HashMap;

public class LRUCache {

    private class Node{
        int key;
        int val;
        Node pre;
        Node next;
        Node(int key, int val){
            this.key = key;
            this.val = val;
        }
    }

    class DList {
        Node dummyHead;
        Node dummyTail;

        DList(){
            dummyHead = new Node(0,0);
            dummyTail = new Node(0,0);
            dummyHead.next = dummyTail;
            dummyTail.pre = dummyHead;
        }

        private void addToHead(Node node){
            Node temp = dummyHead.next;
            dummyHead.next = node;
            node.next = temp;
            temp.pre = node;
            node.pre = dummyHead;
        }

        private void moveToHead(Node node){
            node.pre.next = node.next;
            node.next.pre = node.pre;
            addToHead(node);
        }

        private void removeTail(){
            Node newtail = dummyTail.pre.pre;
            newtail.next = dummyTail;
            dummyTail.pre = newtail;
        }

        private Node getTail(){
            return dummyTail.pre;
        }
    }

    private DList list;
    private HashMap<Integer, Node> cache;
    private int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        list = new DList();
        cache = new HashMap<>();
    }

    public int get(int key) {
        Node node = cache.get(key);
        if(node == null) return -1;
        list.moveToHead(node);
        return node.val;
    }

    public void put(int key, int value) {
        Node node = cache.get(key);
        if(node != null){
            list.moveToHead(node);
            node.val = value;
        }else{
            Node newNode = new Node(key,value);
            cache.put(key, newNode);
            list.addToHead(newNode);

            if(cache.size() > capacity){
                Node tail = list.getTail();
                list.removeTail();
                cache.remove(tail.key);
            }
        }
    }

    public static void main(String[] args){
        LRUCache obj = new LRUCache(2);
        obj.put(1,1);
        obj.put(2,2);
        System.out.println(obj.get(1));
        obj.put(3,3);
        System.out.println(obj.get(2));
        obj.put(4,4);
        System.out.println(obj.get(1));
        System.out.println(obj.get(3));
        System.out.println(obj.get(4));
    }
}
