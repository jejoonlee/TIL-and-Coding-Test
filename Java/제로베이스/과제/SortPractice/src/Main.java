import java.util.*;

public class Main {

    public static void swap(int[] array, int from, int to) {

        int tempNum = array[from];
        array[from] = array[to];
        array[to] = tempNum;

    }

    public static void quickSort(int[] array, int left, int right) {
        if (left >= right) {
            return;
        }

        int pivot = partition(array, left, right);

        quickSort(array, left, pivot - 1);
        quickSort(array, pivot + 1, right);
    }

    public static int partition(int[] array, int left, int right) {
        int pivot = array[left];
        int l = left;
        int r = right;


        while (l < r) {

            while (array[r] > pivot && l < r) {
                r--;
            }

            while (array[l] <= pivot && l < r) {
                l ++;
            }

            swap(array, l, r);
        }

        swap(array, left, l);

        return r;
    }

    // 분할 하는 것
    public static void mergeSort(int[] array, int[] tempArray, int left, int right) {
        if (left < right) {
            int midIdx = (right + left) / 2;
            // 왼쪽 분할
            mergeSort(array, tempArray, left, midIdx);
            // 오른쪽 분할
            mergeSort(array, tempArray, midIdx + 1, right);

            // 모든 숫자들이 하나씩 분할이 된 상태면, 합치면 된다
            merge(array, tempArray, left, right, midIdx);
        }
    }

    // 합치는 것
    public static void merge(int[] array, int[] tempArray, int left, int right, int midIdx) {
        int l = left;
        int r = midIdx + 1;
        int idx = l;

        while (l <= midIdx || r <= right) {
            if (l <= midIdx && r <= right) {
                if (array[l] <= array[r]) {
                    tempArray[idx ++] = array[l ++];
                } else {
                    tempArray[idx ++] = array[r ++];
                }
            } else if (l <= midIdx && r > right) {
                tempArray[idx ++] = array[l ++];
            } else {
                tempArray[idx ++] = array[r ++];
            }
        }

        for (int i = left; i <= right; i++) {
            array[i] = tempArray[i];
        }
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
            int minIdx = i;
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

//        array = new int[]{7, 6, 2, 5, 1, 3, 4};
//        System.out.println(Arrays.sort(array, Collections.reverseOrder()));

        int[] array1 = new int[]{7, 6, 2, 4};
        int[] tempArray = new int[array1.length];
        mergeSort(array1, tempArray, 0, array1.length - 1);
        System.out.println(Arrays.toString(array1));

        array = new int[]{7, 6, 2, 5, 1, 3, 4};
        quickSort(array, 0, array.length - 1);
        System.out.println("퀵 정렬 - " + Arrays.toString(array));
    }
}