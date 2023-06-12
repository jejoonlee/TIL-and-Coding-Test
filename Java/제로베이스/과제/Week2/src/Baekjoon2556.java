import java.util.Stack;
import java.util.Scanner;
import java.util.ArrayList;

public class Baekjoon2556{

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Stack<Integer> stack1 = new Stack<Integer>();
        Stack<Integer> stack2 = new Stack<Integer>();
        Stack<Integer> stack3 = new Stack<Integer>();
        Stack<Integer> stack4 = new Stack<Integer>();

        int n = scanner.nextInt();
        ArrayList <Integer> list = new ArrayList<Integer> ();

        for (int i = 0 ; i < n ; i ++) {
            list.add(Integer.parseInt(scanner.next()));
        }

        boolean isPossible = true;
        for (int num : list) {
            if (stack1.empty() || stack1.peek() < num) {
                stack1.push(num);
            } else if (stack2.empty() || stack2.peek() < num) {
                stack2.push(num);
            } else if (stack3.empty() || stack3.peek() < num) {
                stack3.push(num);
            } else if (stack4.empty() || stack4.peek() < num) {
                stack4.push(num);
            } else {
                isPossible = false;
                System.out.println("NO");
                break;
            }
        }

        if (isPossible) {
            System.out.println("YES");
        }
    }


}
