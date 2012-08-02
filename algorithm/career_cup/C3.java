

public class C3{
    public static void main(String[] args){
        Stack stk = new Stack();
        stk.push(1);
        stk.pop();
        stk.pop();
        stk.push(1);
        stk.push(2);
        stk.push(3);
        stk.push(4);
        stk.push(5);
        stk.push(6);
        System.out.println(stk.top());
        System.out.println(stk.size());
    }
}

class Stack{
    private int size;
    private Node top;

    public Stack(){
        top = new Node(-1);
        size = 0;
    }

    public boolean push(int data){
        Node node = new Node(data);
        node.next = top;
        top = node;
        ++size;
        return true;
    }

    public int pop(){
        if(size <= 0) return -1;
        int ret = top.data;
        top = top.next;
        --size;
        return ret;
    }

    public int top(){
        if(size <= 0) return -1;
        return top.data;
    }

    public int size(){
        return size;
    }
}
