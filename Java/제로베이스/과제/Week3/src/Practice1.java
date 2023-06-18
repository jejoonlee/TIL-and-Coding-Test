
class BinaryTree {
    char[] array;

    BinaryTree(char[] array) {
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
        char[] array = new char[10];
        for(int i = 0; i < array.length; i++) {
            array[i] = (char)('A' + i);
        }

        BinaryTree binaryTree = new BinaryTree(array);

        System.out.println("==PreOrder==");
        binaryTree.preOrder(0);
        System.out.println();

        System.out.println("==Inorder==");
        binaryTree.inOrder(0);
        System.out.println();

        System.out.println("==PostOrder==");
        binaryTree.postOrder(0);
        System.out.println();

        System.out.println("==LevelOrder==");
        binaryTree.levelOrder(0);
        System.out.println();
    }
}
