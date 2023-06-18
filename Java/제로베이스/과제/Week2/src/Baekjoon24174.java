import java.util.Scanner;
import java.util.Arrays;

public class Baekjoon24174 {
    static int count = 0;
    static int cut;

    public static void heapSort(int[] array) {
        int n = array.length - 1;

        buildMinHeap(array, n);

        for (int i = n; i > 1; i--) {
            int tempNum = array[1];
            array[1] = array[i];
            array[i] = tempNum;

            count ++;

            if (count == cut) {
                System.out.println(Arrays.toString(array));
                return;
            }

            heapify(array, 1, i - 1);
        }
    }

    public static void buildMinHeap(int[] array, int size){
        for (int i = size/2 ; i > 0 ; i--) {
            heapify(array, i, size);
        }
    }

    public static void heapify(int[] array, int target, int size) {
        int left = target * 2;
        int right = target * 2 + 1;
        int smaller = 0;

        if (right <= size) {
            if (array[left] < array[right]) {
                smaller = left;
            } else {
                smaller = right;
            }
        } else if (left <= size) {
            smaller = left;
        } else {
            return;
        }

        if (array[smaller] < array[target]) {
            int tempTarget = array[target];
            array[target] = array[smaller];
            array[smaller] = tempTarget;

            count ++;

            if (count == cut) {
                System.out.println(Arrays.toString(array));
                return;
            }

            heapify(array, smaller, size);
        }

    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.next());
        cut = Integer.parseInt(scanner.next());

        int[] array = new int[N + 1];

        for (int i = 1 ; i <= N ; i++) {
            array[i] = Integer.parseInt(scanner.next());
        }

        heapSort(array);

        if (count < cut) {
            System.out.println(-1);
        }

    }
}
