public class LinkedList2 extends LinkedList{

    LinkedList2(Node node) {
        super.head = node;
    }

    // 연결 리스트에 데이터 추가
    // Before_data가 null인 경우, 가장 뒤에 추가
    public void addData(int data, Integer beforeData) {
        if (super.head == null) {
            super.head = new Node(data, null);
        } else if (beforeData == null) {
            Node current = super.head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = new Node(data, null);
        } else {
            Node current = super.head;
            Node prev = current;

            while (current != null) {
                if (current.data == beforeData) {
                    if (current == super.head) {
                        super.head = new Node(data, super.head);
                    } else {
                        prev.next = new Node(data, current);
                    }
                    break;
                }
                prev = current;
                current = current.next;
            }
        }
    }

    public void removeData(int data) {
        if (super.isEmpty()) {
            super.head = new Node(data, null);
            return;
        }

        Node current = super.head;
        Node prev = super.head;

        while (current != null) {
            if (current.data == data) {
                if (current == super.head) {
                    super.head = current.next;
                } else {
                    prev.next = current.next;
                }
                break;
            }

            prev = current;
            current = current.next;
        }
    }

}
