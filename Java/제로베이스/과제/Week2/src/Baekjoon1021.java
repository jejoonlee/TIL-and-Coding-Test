import java.util.ArrayDeque;
import java.util.Scanner;
import java.util.Deque;
public class Baekjoon1021 {

    static int findIndex(int num, Deque<Integer> queue) {
        int index = 0;

        for (int number : queue) {
            if (number == num) {
                break;
            };
            index += 1;
        }

        return index;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Deque<Integer> list = new ArrayDeque<Integer>();
        Deque<Integer> queue = new ArrayDeque<Integer>();

        int n = Integer.parseInt(scanner.next());
        int m = Integer.parseInt(scanner.next());

        for (int i = 0; i < m ; i ++) {
            list.addLast(Integer.parseInt(scanner.next()));
        }

        for (int i = 1; i <= n; i ++) {
            queue.addLast(i);
        }

        int result = 0;
        while (list.size() > 0) {
            if (list.peek() == queue.peekFirst()) {
                list.removeFirst();
                queue.removeFirst();
            } else {
                int index = findIndex(list.peek(), queue);

                if (queue.size() / 2 >= index) {
                    while (list.peek() != queue.peekFirst()) {
                        int num1 = queue.removeFirst();
                        queue.addLast(num1);
                        result += 1;
                    }
                } else {
                    while (list.peek() != queue.peekFirst()) {
                        int num2 = queue.removeLast();
                        queue.addFirst(num2);
                        result += 1;
                    }
                }
            }

        }

        System.out.println(result);
    }
}
