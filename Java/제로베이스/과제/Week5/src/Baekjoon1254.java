import java.util.*;
public class Baekjoon1254 {
    public static boolean palindrom(String string) {
        if (string.length() == 1) {
            return false;
        }

        int i = 0;
        int j = string.length() - 1;

        while (i <= j) {
            if (string.charAt(i) != string.charAt(j)) {
                return false;
            }

            i ++;
            j --;
        }

        return true;
    }
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        String string = scanner.next();
        int palindromIdx = -1;
        int answer = 0;

        for (int i = 0; i < string.length(); i++) {
            if (palindrom(string.substring(i))) {
                palindromIdx = i;
                break;
            }
        }

        if (palindromIdx != -1) {
            answer += string.substring(palindromIdx).length() + (palindromIdx * 2);
        } else {
            answer += (string.length() * 2) - 1;
        }

        System.out.println(answer);
    }
}
