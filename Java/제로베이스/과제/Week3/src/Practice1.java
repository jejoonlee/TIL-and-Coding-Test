
import java.util.Scanner;
import java.util.Arrays;
class BinaryTree {
    int[] array;

    BinaryTree(int[] array) {
        this.array = array.clone();
    }

    public void preOrder(int idx){
        System.out.print(this.array[idx] + " ");

        // 자식 노드 확인하기
        int leftNode = 2 * idx + 1;
        int rightNode = 2 * idx + 2;

        // 왼쪽 자식 노드가 있는지 먼저 확인하기
        if (leftNode < this.array.length) {
            preOrder(leftNode);
        }

        if (rightNode < this.array.length) {
            preOrder(rightNode);
        }
    }

    public void inOrder(int idx) {
        // 자식 노드 확인하기
        int leftNode = 2 * idx + 1;
        int rightNode = 2 * idx + 2;

        // 왼쪽 자식 노드가 있는지 먼저 확인하기
        if (leftNode < this.array.length) {
            inOrder(leftNode);
        }

        System.out.print(this.array[idx] + " ");

        if (rightNode < this.array.length) {
            inOrder(rightNode);
        }
    }

    public void postOrder(int idx) {
        int leftNode = 2 * idx + 1;
        int rightNode = 2 * idx + 2;

        // 왼쪽 자식 노드가 있는지 먼저 확인하기
        if (leftNode < this.array.length) {
            postOrder(leftNode);
        }

        if (rightNode < this.array.length) {
            postOrder(rightNode);
        }

        System.out.print(this.array[idx] + " ");
    }

    public void levelOrder(int idx) {
        for (int i = 0 ; i < this.array.length; i ++) {
            System.out.println(array[i] + " ");
        }
        System.out.println();
    }

}


public class Practice1 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();

        int[] array = new int[num * num - 1];

        for (int i = 1; i < array.length ; i ++) {
            if (i % 2 == 0) {
                array[i] = 1;
            }
        }
        System.out.println(Arrays.toString(array));

        BinaryTree binaryTree = new BinaryTree(array);

        binaryTree.inOrder(0);

    }
}
