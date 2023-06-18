
class NodeDouble{
    int data;
    NodeDouble prev;
    NodeDouble next;

    NodeDouble (int data, NodeDouble prev, NodeDouble next) {
        this.data = data;
        this.prev = prev;
        this.next = next;
    }
}

class DoublyLinkedList {
    NodeDouble head;
    NodeDouble tail;

    DoublyLinkedList(NodeDouble node) {
        this.head = node;
        this.tail = node;
    }

    public boolean isEmpty() {
        if (this.head == null) {
            return true;
        }
        return false;
    }

    public void addData(int data, Integer beforeData) {
        if (this.head == null) {
            this.head = new NodeDouble(data, null, null);
            this.tail = this.head;
        } else if (beforeData == null) {
            this.tail.next = new NodeDouble(data, this.tail, null);
            this.tail= this.tail.next;
        } else {
            NodeDouble current = this.head;
            NodeDouble currentPrev = current;

            while (current != null) {

                if (current.data == beforeData) {
                    // 제일 앞 부분이면?
                    if (current == this.head) {
                        this.head = new NodeDouble(data, null, this.head);
                        this.head.next.prev = this.head;
                    } else {
                        currentPrev.next = new NodeDouble(data, currentPrev, current);
                        current.prev = currentPrev.next;
                    }
                    break;
                }

                currentPrev = current;
                current = current.next;
            }

        }
    }

    public void removeData(int data) {
        if (isEmpty()) {
            System.out.println("This list is Empty");
            return;
        }

        NodeDouble current = this.head;
        NodeDouble prevNode = current;

        while (current != null) {
            if (current.data == data) {
                if (current == this.head && current == this.tail) {
                    this.head = null;
                    this.tail = null;
                } else if (current == this.head) {
                    this.head = current.next;
                    this.head.prev = null;
                } else if (current == this.tail) {
                    this.tail = this.tail.prev;
                    this.tail.next = null;
                } else {
                    prevNode.next = current.next;
                    current.next.prev = prevNode;
                }
                break;
            }
+
            prevNode = current;
            current = current.next;
        }
    }
}

public class Practice2 {
    public static void main(String[] args) {


    }
}
