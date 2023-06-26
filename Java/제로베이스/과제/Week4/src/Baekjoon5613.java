import java.util.*;

public class Baekjoon5613 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int answer = 0;
        int calculate = 0;

        while (true) {
            String command = scanner.next();

            if (command.equals("=")) {
                break;
            } else if (command.equals("+")) {
                calculate = 0;
            } else if (command.equals("-")) {
                calculate = 1;
            } else if (command.equals("*")) {
                calculate = 2;
            } else if (command.equals("/")) {
                calculate = 3;
            } else {
                if (calculate == 0) {
                    answer += Integer.parseInt(command);
                } else if (calculate == 1) {
                    answer -= Integer.parseInt(command);
                } else if (calculate == 2) {
                    answer *= Integer.parseInt(command);
                } else if (calculate == 3) {
                    answer /= Integer.parseInt(command);
                }
            }
        }

        System.out.println(answer);
    }
}
