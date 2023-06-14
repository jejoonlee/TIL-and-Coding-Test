import java.util.Scanner;

public class Baekjoon10818 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        int[] array = new int[n];

        int maximum = -1000000;
        int minimum = 1000000;

        for (int i = 0; i < n ; i ++) {
            array[i] = Integer.parseInt(scanner.next());

            if (array[i] > maximum) {
                maximum = array[i];
            }

            if (array[i] < minimum) {
                minimum = array[i];
            }
        }

        System.out.printf("%d %d", minimum, maximum);

    }
}
