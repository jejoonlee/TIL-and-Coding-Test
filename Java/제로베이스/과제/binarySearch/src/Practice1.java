import java.util.Arrays;

public class Practice1 {
    public static int solution(int[] array, int target) {

        if (array == null || array.length == 0) {
            return -1;
        }

        int left = 0;
        int right = array.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (target == array[mid]) {
                return mid;
            } else if (target > array[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -left - 1;

    }
    public static void main(String[] args) {
        int[] array = {1, 2, 5, 10, 20, 30, 40, 50, 60};

        System.out.println(solution(array, 30));
        System.out.println(solution(array, 3));
        System.out.println(solution(array, 11));
        System.out.println(solution(array, 35));

    }
}
