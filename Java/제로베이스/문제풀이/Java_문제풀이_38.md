# 20230818 [Java] 문제풀이 







## [프로그래머스] 택배상자



#### 스택에 상자를 넣으면서 order에 있는 숫자와 비교했다



#### 스택에 있는 숫자의 제일 위에 있는 숫자가 현재 order와 같으면, while문을 통해서 하나씩 꺼내면서, 다음 순서로 넘어가고, answer에다 1을 누적시켰다



```java
import java.util.*;

class Solution {
    public int solution(int[] order) {
        int answer = 0;
        
        Stack<Integer> reserve = new Stack<>();
        
        int box = 1;
        int idx = 0;
        
        while (box <= order.length) {
            reserve.add(box);
            
            while (!reserve.isEmpty() && reserve.peek() == order[idx]) {
                reserve.pop();
                answer ++;
                idx ++;
            }
            
            box ++;
        }
        
        return answer;
    }
}
```

