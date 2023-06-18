import java.util.LinkedList;
import java.util.Scanner;

public class Baekjoon1158 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.next());
        int K = Integer.parseInt(scanner.next());

        LinkedList<Integer> list = new LinkedList<Integer>();
        for (int num = 1; num <= N; num ++) {
            list.add(num);
        }

        String answer =  "<";

        int count = 1;
        int index = 0;

        while (true) {
            if (count == K) {
                answer += String.format("%d, ", list.get(index));
                count = 0;
                list.remove(index);

                if (list.size() == 0) {
                    answer = answer.substring(0, answer.length() - 2);
                    answer += ">";
                    break;
                }
                index -= 1;
            }

            count ++;
            index = (index + 1) % list.size();
        }

        System.out.println(answer);

    }
}
