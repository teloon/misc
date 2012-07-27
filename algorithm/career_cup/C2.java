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
        System.out.print("head");
        while(curr.next != null){
            System.out.format("-->%d", curr.next.data);
            curr = curr.next;
        }
        System.out.println();
    }

    public void p2(Node head){
        if(head == null) return;
        Node curr_node = head.next;
        Node seen_node = head;
        Node last_seen_node = head;
        boolean is_dup = false;
        while(curr_node != null){
            for(seen_node=head.next; seen_node!=curr_node; seen_node=seen_node.next){
                if(seen_node.data == curr_node.data){
                    is_dup = true;
                    break;
                }
            }
            if(is_dup){
                is_dup = false;
                last_seen_node.next = curr_node.next;
            }else{
                last_seen_node = curr_node;
            }
            curr_node = curr_node.next;
        }
    }

    public static void main(String[] args){
        C2 c2 = new C2();
        Node splList = c2.genLinkedList(15, 15);
        c2.printList(splList);
        c2.p2(splList);
        c2.printList(splList);
    }
}
