# 20230614 Java 문제풀이 





## [백준] 10818 최소, 최대

#### 배열을 이용하여, 주어진 숫자들의 최소와 최대값을 찾으면 된다

- 파이썬을 이용할 때에 N개의 입력값을 공백으로 주어진 것을 한번에 리스트로 받아서, for문을 돌며 최소와 최대값을 찾았다
- 자바 같은 경우 **scanner.next();** 를 사용하여 하나의 for문에서, 입력값을 받으면서 최소와 최대값을 찾아냈다



#### 만약에 배열을 출력하고 싶을 때에는 Arrays 를 import 받고, Arrays.toString(배열이름) 으로 출력하면 된다

- import java.util.Arrays;



```java
import java.util.Scanner;

public class Baekjoon10818 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        int[] array = new int[n];

        int maximum = -1000000;
        int minimum = 1000000;

        for (int i = 0; i < n ; i ++) {
            array[i] = Integer.parseInt(scanner.next());

            if (array[i] > maximum) {
                maximum = array[i];
            }

            if (array[i] < minimum) {
                minimum = array[i];
            }
        }

        System.out.printf("%d %d", minimum, maximum);

    }
}
```





## 나누어 떨어지는 숫자 배열

#### 숫자로 이루어진 배열과, 해당 숫자들을 나누는 하나의 숫자 (divisor) 가주어진다

#### 배열에 들어간 숫자들과 divisor를 나누었을 때에, 0이 나누어 떨어지면, 그 숫자를 새로운 배열에 반환해준다

- 여기서 정답은 오름차순으로 정렬이 되어 있어야 한다



#### 정렬을 할 때에는 Collections를 사용했다

```java
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public ArrayList<Integer> solution(int[] arr, int divisor) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        
        for (int i = 0; i < arr.length; i ++) {
            if (arr[i] % divisor == 0) {
                answer.add(arr[i]);
            }
        }
        
        Collections.sort(answer);
        
        if (answer.size() == 0) {
            answer.add(-1);
        }
        return answer;
    }
}
```





