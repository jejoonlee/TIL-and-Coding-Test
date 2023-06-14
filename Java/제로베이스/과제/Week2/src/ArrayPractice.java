import java.util.Arrays;

public class ArrayPractice {

    static void oddEvenAverage(double[] array) {
        double even = 0;
        double evenCount = 0;
        double odd = 0;
        double oddCount = 0;

        for (double num: array) {
            if (num % 2 == 0) {
                even += num;
                evenCount += 1;
            } else {
                odd += num;
                oddCount += 1;
            }
        }

        System.out.printf("짝수 평균: %.1f", even / evenCount).println();
        System.out.printf("홀수 평균: %.1f", odd / oddCount).println();
    }

    static void target(int[] array, int target) {
        int answer = 0;

        for (int i = 0; i < array.length; i++) {
            if (array[i] == target) {
                answer = i;
            }
        }

        System.out.println("결과: " + answer);
    }

    static void reverseArray(int[] array) {
        for (int i = 0; i < array.length / 2; i ++) {
            int tempNum = array[i];
            array[i] = array[array.length - 1 - i];
            array[array.length - 1 - i] = tempNum;
        }

        System.out.println(Arrays.toString(array));
    }

    static void findPeek(int[] height) {

        for (int i = 0; i < height.length; i ++) {
            if (i == 0 || i == height.length - 1) {
                if (height[0] > height[1] || height[height.length - 1] > height[height.length - 2]) {
                    System.out.print(height[i] + " ");
                }
            } else {
                if (height[i] > height[i + 1] && height[i] > height[i - 1]) {
                    System.out.print(height[i] + " ");
                }
            }

        }
    }
    public static void main(String[] args) {
        oddEvenAverage(new double[]{1, 2, 3, 4, 5, 6, 7, 8, 9});
        target(new int[]{1, 1, 100, 1, 1, 1, 100}, 100);
        reverseArray(new int[]{1, 3, 5, 7, 9});
        findPeek(new int[]{3, 1, 2, 6, 2, 2, 5, 1, 9, 10, 1, 11});
    }
}
