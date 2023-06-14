# Java 문제풀이 





## [백준] 1021번 회전하는 큐

#### 1부터 N번의 숫자가 큐 안에 있다

#### 큐 안에서 꺼내야 할 숫자들이 주어진다

- 큐에서는 제일 앞에 숫자를 꺼낼 수 있다
- 제일 앞에, 원하는 숫자가 없으면 왼쪽으로 한칸씩 또는 오른쪽으로 한칸씩 움직여야 한다



#### Deque를 활용했다

- 만약 queue 안에, 꺼내야 할 숫자의 인덱스가 queue 안에 있는 숫자를 반으로 나눴을 때, 인덱스가 그 이하일 때에는 왼쪽으로 한칸씩 움직여준다

```java
import java.util.ArrayDeque;
import java.util.Scanner;
import java.util.Deque;
public class Main {

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
```

