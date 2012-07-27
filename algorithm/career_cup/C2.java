import java.util.HashSet;
import java.util.Random;

class Node{
    Node next = null;
    int data;
    public Node(int d) {this.data = d;}
    public void append(int d){
        Node curr_node = this;
        while(curr_node.next != null)
            curr_node = curr_node.next;
        curr_node.next = new Node(d);
    }
}

public class C2{
    public Node genLinkedList(int length, int max){
        Random ranObj = new Random();
        Node head = new Node(-1); //head node
        Node curr = head;
        for(int i=0; i<length; ++i){
            curr.next = new Node(ranObj.nextInt(max));
            curr = curr.next;
        }
        return head;
    }

    public void printList(Node head){
        Node curr = head;
        Systen.out.print("head")
        while(curr.next != null){
            System.out.format("-->%d", curr.next.data);
        }
    }

    public void p2(Node head){
        HashSet<int> seen_val_set = HashSet<int>();
        Node curr = head;
        while(curr.next != null){
            if(seen_val_set.contains(curr.next.data)){
                if(curr.next.next == null)
                    break;
                else
                    curr.next = curr.next.next;
            }else{
                seen_val_set.add(curr.next.data);
            }
        }
    }

    pubic static void main(String[] args){
        C2 c2 = new C2();
        Node splList = c2.genLinkedList(10, 20);
        c2.printList(splList);
    }
}