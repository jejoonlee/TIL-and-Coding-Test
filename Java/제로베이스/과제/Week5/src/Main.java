import java.util.HashMap;

public class Main {
    private static boolean isPairSum(int[] array, int target) {
        int left = 0;
        int right = array.length - 1;
        while (left < right) {
            if (array[left] + array[right] == target) return true;
            else if (array[left] + array[right] > target) right--;
            else left++;
        }
        return false;
    }
    public static void main(String[] args) {
        int[] array = {1, 4, 7, 8, 9, 10, 11, 17, 18, 21, 26, 27};

        System.out.println(isPairSum(array, 17));

        HashMap<Integer, Integer> map = new HashMap<>();

        map.put

    }
}