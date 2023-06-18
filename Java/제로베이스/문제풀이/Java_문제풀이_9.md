# 20230614 Java 문제풀이 





## [백준] 1158 요세푸스 문제

#### 1부터 N까지의 숫자를 배열 안에 넣는다



#### 그리고 K번째 마다, 배열에서 숫자를 빼며, 다른 리스트에 넣는다

- 마지막 숫자에 도달하면 다시 제일 첫 번째 숫자로 돌아온다

#### String을 사용하여 <> 안에 정답 숫자들을 넣어주었다



#### Count를 사용하며 K번째를 찾았다



**index = (index + 1) % list.size();**

- 리스트 안에 있는 인덱스를 초과할 때에 0으로 다시 돌려 보내준다





```java
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
```





