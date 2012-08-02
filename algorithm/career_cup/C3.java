

public class C3{
    public static void main(String[] args){
        Queue q = new Queue();
        System.out.println(stk.top().value);
        System.out.println(stk.size());
    }
}

class Queue{
    private int size;
    private Node front;
    private Node rear;

    public Queue(){
        front = new Node(-1);
        rear = front;
        size = 0;
    }

    public Node enqueue(int data){
        rear.next = new Node(data);
        rear = rear.next;
        ++size;
        return rear;
    }

    public Node dequeue(){
        if(size <= 0) return null;
        Node ret = front;
        front = front.next;
        --size;
        return ret;
    }
}

class Stack{
    private int size;
    private Node top;

    public Stack(){
        top = new Node(-1);
        size = 0;
    }

    public Node push(int data){
        Node node = new Node(data);
        node.next = top;
        top = node;
        ++size;
        return Node;
    }

    public Node pop(){
        if(size <= 0) return null;
        Node ret = top;
        top = top.next;
        --size;
        return ret;
    }

    public Node top(){
        if(size <= 0) return null;
        return top;
    }

    public int size(){
        return size;
    }
}
