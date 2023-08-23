# 20230822 [Java] 문제풀이 







## [프로그래머스] 혼자 놀기의 달인



#### 상자에 카드를 넣고 무작위로 섞어 일렬로 나열한다



#### 그리고 상자를 1번부터 순차적으로 증가하는 번호를 붙인다



<img src="Java_문제풀이_41.assets/image-20230822215032434.png" alt="image-20230822215032434" style="zoom:50%;" />

- 상자 번호에서, 카드 번호를 보고, 카드 번호에 대한 상자 번호를 여는 것이다



#### 인덱스를 상자 번호라고 생각하면 카드 번호에 1을 항상 빼야한다



```java
import java.util.*;

class Solution {
    
    public int solution(int[] cards) {
        ArrayList<Integer> group = new ArrayList<>();
        
        int[] visited = new int[cards.length];
        
        for (int i = 0; i < cards.length; i ++) {
            int tempCount = 0;
            
            if (visited[i] == 0) {
                Stack<Integer> stack = new Stack<>();
                stack.add(i);
                visited[i] = 1;
                
                while (!stack.isEmpty()) {
                    tempCount ++;
                    int current = stack.pop();
                    
                    if (visited[cards[current] - 1] == 0) {
                        stack.add(cards[current] - 1);
                        visited[cards[current] - 1] = 1;
                    }
                }
            }
            group.add(tempCount);
        }
        
        Collections.sort(group, (x1, x2) -> x2 - x1);
        
        return group.get(0) * group.get(1);
    }
}
```

