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

    public void p1(Node head){
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

    public Node p2(Node head, int n){
        if(head==null || n<=0) return null;
        Node currNode = head.next;
        Node objNode = head.next;
        for( ; n>1; --n){ //n-1 moves
            if(currNode == null)
                return null;
            currNode = currNode.next;
        }
        while(currNode.next!=null){
            currNode = currNode.next;
            objNode = objNode.next;
        }
        return objNode;
    }

    public void p3(Node midNode){
		if(midNode == null || midNode.next == null) return;
		midNode.data = midNode.next.data;
		midNode.next = midNode.next.next;
    }

    public Node p4(Node head1, Node head2){
        if(head1==null || head2==null) return null;
        Node resHeadNode = new Node(-1);
        Node node1 = head1.next;
        Node node2 = head2.next;
        Node resNode = resHeadNode;
        int carry=0, addRes=0;
        while(node1!=null && node2!=null){
            addRes = node1.data + node2.data + carry;
            resNode.next = new Node(addRes%10);
            resNode = resNode.next;
            node1 = node1.next;
            node2 = node2.next;
            carry = addRes/10;
        }
        if(node1!=null || node2!=null) return null;
        return resHeadNode;

    }

    public static void main(String[] args){
        C2 c2 = new C2();
        Random ranObj = new Random();
        System.out.println("## Test p1");
        Node splList = c2.genLinkedList(15, 15);
        System.out.println("Initial List:");
        c2.printList(splList);
        c2.p1(splList);
        System.out.println("Result List:");
        c2.printList(splList);

        System.out.println("\n## Test p2");
        splList = c2.genLinkedList(15, 15);
        int last_idx = ranObj.nextInt(20);
        Node p2Ret = c2.p2(splList, last_idx);
        System.out.println("Initial List:");
        c2.printList(splList);
        if(p2Ret != null)
            System.out.format("%dth to last element: %d\n", last_idx, p2Ret.data);
        else
            System.out.format("%dth to last element: None\n", last_idx);

        System.out.println("\n## Test p3");
		splList = c2.genLinkedList(15, 15);
        System.out.println("Initial List:");
        c2.printList(splList);
        Node midNode = splList;
        for(int i=0; i<7; ++i) midNode = midNode.next;
        c2.p3(midNode);
        System.out.format("After remove midNode @pos 7, Result List:\n");
        c2.printList(splList);
        
        System.out.println("\n## Test p4");
		Node splList1 = c2.genLinkedList(15, 15);
		Node splList2 = c2.genLinkedList(15, 15);
        System.out.println("Initial List:");
        c2.printList(splList1);
        c2.printList(splList2);
        Node resList = c2.p4(splList1, splList2);
        System.out.format("Add result List:\n");
        c2.printList(resList);
    }
}
