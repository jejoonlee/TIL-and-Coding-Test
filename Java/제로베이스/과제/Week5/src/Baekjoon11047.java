import java.util.*;
public class Baekjoon11047 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.next());
        int k = Integer.parseInt(scanner.next());

        int[] money = new int[n];

        for(int i = 0; i < n; i++) money[i] = Integer.parseInt(scanner.next());

        int answer = 0;

        for(int i = n - 1; i >= 0; i--) {
            if (k >= money[i]) {
                answer += k / money[i];
                k -= (k / money[i]) * money[i];

                if (k == 0) {
                    break;
                }
            }
        }

        System.out.println(answer);

    }
}
