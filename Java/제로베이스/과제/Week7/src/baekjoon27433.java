import java.util.*;
public class baekjoon27433 {

    public static long factorial(long num) {
        if (num == 0 || num == 1) {
            return 1;
        }

        return num * factorial(num-1);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        long answer = factorial(scanner.nextLong());

        System.out.println(answer);

    }

}