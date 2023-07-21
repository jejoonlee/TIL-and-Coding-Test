# 20230720 [Java] 문제풀이 



## [백준] 27433 팩토리얼



#### 20! 은 int를 훨씬 넘어서 int가 아니라 long을 사용해야 한다



```java
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
```

