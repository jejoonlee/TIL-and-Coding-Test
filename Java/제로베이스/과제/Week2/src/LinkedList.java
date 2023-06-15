class Node {

    int data;
    Node next;

    Node () {}
    Node (int data, Node next) {
        this.data = data;
        this.next = next;
    }
}

public class LinkedList {
    Node head;

    LinkedList () {}
    LinkedList(Node node) {
        this.head = node;
    }

    // 연결 리스트 비어 있는지 확인
    public boolean isEmpty() {
        if (this.head == null) {
            return true;
        }
        return false;
    }

    // 연결 리스트의 맨 뒤에 데이터 추가
    public void addLast(int data) {
        if (isEmpty()) {
            this.head = new Node(data, null);
        } else {
            Node current = this.head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = new Node(data, null);
        }

    }

    // 연결 리스트의 맨 뒤의 데이터 삭제
    public void removeLast() {
        if (isEmpty()) {
            System.out.println("LinkedList is Empty");
            return;
        } else {
            Node current = this.head;
            Node prev = current;
            while (current.next != null) {
                prev = current;
                current = current.next;
            }

            if (current == this.head) {
                this.head = null;
            } else {
                prev.next = null;
            }
        }
    }

    // 연결 리스트에서 데이터 찾기
    public void findData(int data) {
        if (isEmpty()) {
            System.out.println("Empty List");
            return;
        } else {
            Node current = this.head;

            while (current != null) {
                if (current.data == data) {
                    System.out.println("Found the data");
                    return;
                }
                current = current.next;
            }
        }
        System.out.println("Data not found");
    }

    // 연결 리스트의 모든 데이터 출력
    public void printData() {
        if (isEmpty()) {
            System.out.println("Empty List");
            return;
        } else {
            Node current = this.head;
            while (current != null) {
                System.out.print(current.data + " ");
                current = current.next;
            }
        }
        System.out.println();
    }

}
