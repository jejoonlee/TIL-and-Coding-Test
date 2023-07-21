import java.util.*;
public class baekjoon25501 {
    static int count;

    public static int isPalindrom(String word, int i, int j) {
        if (i >= j) {
            return 1;
        } else if (word.charAt(i) != word.charAt(j)) {
            return 0;
        } else {
            count ++;
            return isPalindrom(word, i + 1, j - 1);
        }

    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int test = scanner.nextInt();

        for (int i = 0; i < test; i ++) {
            String word = scanner.next();

            count = 0;

            System.out.println(isPalindrom(word, 0, word.length() - 1) + " " + count);
        }
    }
}
