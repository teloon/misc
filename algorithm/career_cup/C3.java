

public class C3{
    public static void main(String[] args){
        Stack stk = new Stack(5);
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
    private int curr_idx;
    private int capacity;
    private int[] arr;

    public Stack(int capacity){
        this.capacity = capacity;
        this.arr = new int[capacity];
        this.curr_idx = -1;
    }

    public boolean push(int data){
        if(curr_idx+1 >= capacity) return false;
        ++curr_idx;
        arr[curr_idx] = data;
        return true;
    }

    public int pop(){
        if(curr_idx < 0) return -1;
        --curr_idx;
        return arr[curr_idx+1];
    }

    public int top(){
        if(curr_idx < 0) return -1;
        return arr[curr_idx];
    }

    public int size(){
        return curr_idx+1;
    }
}
