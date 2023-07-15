# 20230714 [Java] 문제풀이 





## [백준 17478 Silver - 5] 재귀함수가 뭔가요?

#### 재귀는 함수가, 자기 자신을 호출하는 것이다 (아는데 아직도 어려움...)



#### 일단 count를 1씩 더하면서 num과 같아지면 return을 해준다 (break point)



#### 그 이후에는 System.out.printf("%s라고 답변하였지.", under).println(); 이 파트가 실행이 되는 것이다



```
어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
"재귀함수가 뭔가요?"
"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
____"재귀함수가 뭔가요?"
____"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
____마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
____그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
________"재귀함수가 뭔가요?"	 <-- 여기서부터는 count와 num이 같아진 것
________"재귀함수는 자기 자신을 호출하는 함수라네"
________라고 답변하였지. 
____라고 답변하였지.	<-- return 후 System.out.printf("%s라고 답변하였지.", under).println(); 부분
라고 답변하였지.


```



```java
import java.util.*;
public class baekjoon17478 {

    public static void ask(int count, int num, String under) {

        System.out.printf("%s\"재귀함수가 뭔가요?\"", under).println();

        if (count == num) {
            System.out.printf("%s\"재귀함수는 자기 자신을 호출하는 함수라네\"", under).println();
            System.out.printf("%s라고 답변하였지.", under).println();
            return;
        }

        System.out.printf("%s\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.", under).println();
        System.out.printf("%s마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.", under).println();
        System.out.printf("%s그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"", under).println();
        ask(count + 1, num, under + "____");

        System.out.printf("%s라고 답변하였지.", under).println();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();

        System.out.println("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.");
        ask(0, num, "");
    }
}

```

