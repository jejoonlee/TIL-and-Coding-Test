import java.util.Arrays;

public class Main {
    public static int binarySearch(int[] array, int target) {
        int left = 0;
        int right = array.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (array[mid] == target) {
                return mid;
            } else if (target > array[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }

    public static int binarySearchRe(int[] array, int target, int left, int right) {
        if (left > right) {
            return -1;
        }

        int mid = (left + right) / 2;
        if (target > array[mid]) {
            return binarySearchRe(array, target, mid + 1, right);
        } else if (target < array[mid]) {
            return binarySearchRe(array, target, left, mid - 1);
        } else {
            return mid;
        }
    }

    public static void main(String[] args) {
        int[] array = {1, 2, 7, 8, 9, 11, 17, 21, 26, 27, 70, 77};


        System.out.println(Arrays.binarySearch(array,7));
        System.out.println(Arrays.binarySearch(array,10));

    }
}