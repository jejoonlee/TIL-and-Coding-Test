# Java 문제풀이 (Programmers)



## 같은 숫자는 싫어

#### 배열이 주어진다

#### 배열 안에 숫자가 주어지는데, 연속으로 나열된 같은 숫자는 하나의 숫자로 반환한다

- 예) [1, 1, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7]  => [1, 3, 4, 5, 6, 7]
  - 1, 4, 6은 모두 연속으로 같은 숫자로 나열되어 있어, 하나로 줄인다



#### 간단하게, 먼저 제일 앞에 있는 숫자를 배열에 미리 넣는다



#### 그 다음은 인덱스 1로 시작하여, 전의 숫자와 비교하며, 전의 숫자와 다르면, answer 배열에 해당 숫자를 넣으면 된다

```java
import java.util.*;

public class Solution {
    public ArrayList<Integer> solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        
        answer.add(arr[0]);
        
        for (int i = 1; i < arr.length; i ++){
            if (arr[i] != arr[i - 1]) {
                answer.add(arr[i]);
            }
        }
        

        return answer;
    }
}
```

