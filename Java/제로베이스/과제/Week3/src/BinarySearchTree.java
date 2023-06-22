
import java.util.*;

class Node {
    int value;
    Node left;
    Node right;

    Node (int value, Node left, Node right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}
public class BinarySearchTree {
    Node head;

    BinarySearchTree(int value) {
        this.head = new Node(value, null, null);
    }

    public void addNode(int value) {

        if (this.head == null) {
            this.head = new Node(value, null, null);
        } else {
            Node current = this.head;

            while (true) {
                if (value == current.value) {
                    break;
                } else if (value < current.value) {
                    if (current.left == null) {
                        current.left = new Node(value, null, null);
                        break;
                    }
                    current = current.left;
                } else if (value > current.value) {
                    if (current.right == null) {
                        current.right = new Node(value, null, null);
                        break;
                    }
                    current = current.right;
                }
            }
        }
    }

    public void removeNode(int value) {
        Node parent = null;
        Node child = null;
        Node changeNode = null; // 삭제할 노드의 자식 노드가 2개일 때에, 삭제할 노드와 바꿀 하단 노드
        Node tempNode = null; // changeNode를 찾기 위해, 임시적으로 만든 노드

        Node current = this.head;

        while (current != null) {
            if (value == current.value) {
                break;
            }

            parent = current; // 부모 노드 저장하기
            if (value < current.value) {
                current = current.left;
            } else {
                current = current.right;
            }
        }

        if (parent == null) {
            System.out.println("There is no node");
            return;
        }

        if (current.left == null && current.right == null) { // leaf 노드인 경우
            if (this.head == current) { // root 노드가 current이면, 값이 하나 밖에 없다는 것
                this.head = null;
            } else {
                if (parent.left == current) {
                    parent.left = null;
                } else {
                    parent.right = null;
                }
            }
        } else if ((current.left != null && current.right == null) || (current.left == null && current.right != null)) {
            if (current.left != null) { // current는 삭제할 값이고, child와 parent는 연결해야 하는 노드들이다
                child = current.left;
            } else {
                child = current.right;
            }

            if (parent == null) { // parent가 null이면, 삭제하는 값이 루트 노드라는 것이다
                this.head = child;
            } else {
                if (parent.left == current) {
                    parent.left = child;
                } else {
                    parent.right = child;
                }
            }
        } else  {
            tempNode = current;
            changeNode = current.left; // 왼쪽 기준은, 제일 큰 숫자를 찾고 || 오른쪽으로 가면, 제일 작은 숫자를 찾아야 한다

            // 왼쪽으로 changeNode를 먼저 가져갔기 때문에, 오른쪽에 있는 자식 노드를 찾으면 된다
            while (changeNode.right != null) {
                tempNode = changeNode;
                changeNode = changeNode.right;
            }

            tempNode.right = changeNode.left;
            changeNode.left = current.left;
            changeNode.right = current.right;

            if (parent == null) {
                this.head = changeNode;
            } else {
                if (parent.left == current) {
                    parent.left = changeNode;
                } else {
                    parent.right = changeNode;
                }
            }

        }
    }

    public void levelOrder(Node node) {
        Queue<Node> queue = new LinkedList();
        queue.add(node);
        while (!queue.isEmpty()) {
            Node current = queue.poll();

            System.out.print(current.value + " ");

            if (current.left != null) {
                queue.offer(current.left);
            }
            if (current.right != null) {
                queue.offer(current.right);
            }
        }
        System.out.println();
    }
    public static void main(String[] args) {
        BinarySearchTree bst = new BinarySearchTree(20);

        bst.addNode(10);
        bst.addNode(30);
        bst.addNode(1);
        bst.addNode(15);
        bst.addNode(25);
        bst.addNode(13);
        bst.addNode(35);
        bst.addNode(27);
        bst.addNode(40);
        bst.levelOrder(bst.head);

        bst.removeNode(40);
        bst.levelOrder(bst.head);
        bst.removeNode(25);
        bst.levelOrder(bst.head);
        bst.removeNode(20);
        bst.levelOrder(bst.head);

    }
}
