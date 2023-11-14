# 20231018 [Java] 문제풀이



## 사전식으로 숫자 정렬하기



#### 1부터 n 까지의 숫자를 문자열로 정렬하는 것



#### 그냥 문자열로 해서 정렬을 하면 정렬은 되지만, 너무 큰 숫자 n이 들어오면 시간이 초과된다

```java
import java.util.*;

class Solution {
    public int[] solution(int n) {
        String[] answer = new String[n];
        int[] result = new int[n];

        for (int i = 1; i <= n; i ++) answer[i - 1] = String.format("%d", i);

        Arrays.sort(answer);

        for (int i = 0; i < n; i++) result[i] = Integer.parseInt(answer[i]);


        return result;
    }
}
```



#### DFS 사용

```java
public class DictArray {

    static List<Integer> result;

    public static void dfs(int num, int limit) {

        if (num > limit) return;

        if (num > 0) result.add(num);

        // 자식 노드에 유효한 숫자가 있는지 0부터 9까지 확인
        for (int i = 0; i < 10; i ++) {
			
            // 자식 노드의 값은 부모 노드에 값에 10을 곱한 것
            int tempNum = num * 10 + i;
			
            // 0 자체가 있으면 안 됨
            if (tempNum == 0) continue;

            dfs(tempNum, limit);
        }
    }

    public static void main(String[] args) {
        int n = 15;

        result = new ArrayList<Integer>();

        dfs(0, 15);

        System.out.println(result);
    }

}
```



