import java.util.*;

public class Baekjoon2003 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.next());
        int m = Integer.parseInt(scanner.next());

        int[] array = new int[n];

        for (int i = 0; i < n; i++) array[i] = Integer.parseInt(scanner.next());

        int left = 0;
        int right = 0;
        int answer = 0;
        int tempAdd = array[left];

        while (left < n) {
            if (tempAdd <= m) {
                if (tempAdd == m) answer += 1;

                if (right + 1 < n) {
                    right ++;
                    tempAdd += array[right];
                } else {
                    tempAdd -= array[left];
                    left ++;
                }
            } else if (tempAdd > m) {
                tempAdd -= array[left];
                left ++;
            }
        }
        System.out.println(answer);

    }
}
