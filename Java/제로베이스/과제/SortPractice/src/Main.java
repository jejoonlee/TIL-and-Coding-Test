import java.util.*;

public class Main {

    public static void swap(int[] array, int from, int to) {

        int tempNum = array[from];
        array[from] = array[to];
        array[to] = tempNum;

    }
    public static void bubbleSort(int[] array) {
        for(int i = 1; i < array.length - 1; i++) {
            for (int j = 0; j < array.length - i; j++) {
                if (array[j] > array[j + 1]) {
                    swap(array, j, j+1);
                }
            }
        }
    }

    public static void insertionSort(int[] array) {
        for (int i = 1; i < array.length; i ++) {
            for (int j = i ; j > 0; j--) {
                if (array[j] < array[j - 1]) {
                    swap(array, j, j-1);
                } else {
                    break;
                }
            }
        }
    }

    private static void selectionSort(int[] array) {
        for (int i = 0; i < array.length; i++) {
            int minNum = array[i];
            int minIdx = -1;
            for (int j = i; j < array.length; j ++) {
                if (array[j] < minNum) {
                    minNum = array[j];
                    minIdx = j;
                }
            }

            swap(array, minIdx, i);
        }
    }

    public static void main(String[] args) {
        int[] array = {7, 6, 2, 5, 1, 3, 4};
        bubbleSort(array);
        System.out.println("버블 정렬 - " + Arrays.toString(array));

        array = new int[]{7, 6, 2, 5, 1, 3, 4};
        insertionSort(array);
        System.out.println("삽입 정렬 - " + Arrays.toString(array));

        array = new int[]{7, 6, 2, 5, 1, 3, 4};
        selectionSort(array);
        System.out.println("선택 정렬 - " + Arrays.toString(array));

        array = new int[]{7, 6, 2, 5, 1, 3, 4};
        System.out.println(Arrays.sort(array, Collections.reverseOrder()));
    }
}