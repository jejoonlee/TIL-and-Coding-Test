# 20230820 [Java] 문제풀이 







## [프로그래머스] 두 큐 합 같게 만들기



#### 이 문제는 두 큐가 주어지고, 서로의 원소를 주고 받으면서, 서로의 원소들의 값이 같을 수 있도록 만드는 것이다

- 제일 주의해야할 점은, 두 개의 큐가 있다는 것이다
- 서로 원소를 주고 받을 때에, 제일 먼저 큐에 들어온 원소를, 다른 큐에게 전달할 수 있다는 점이다



#### 각 두 큐의 값을 구하고, 그 값에 따라, 값이 더 큰 큐에서, 더 작은 큐에게 원소를 주는 방식으로 로직을 짜면 된다



#### while문이 무한 루프에 빠질 수 있는 상황이 있어서, answer가 나올 수 있는 최대의 수를 정해준다

- (answer > queue1.length * 4)



#### 두 개의 큐의 합이 같으면, 바로 answer를 출력해준다

- answer는 원소의 움직임의 개수다





```java
import java.util.*;

class Solution {
    public long solution(int[] queue1, int[] queue2) {
        long answer = 0;
        long queue1Sum = 0;
        long queue2Sum = 0;
        
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        
        for (int i = 0; i < queue1.length; i ++) {
            queue1Sum += queue1[i];
            q1.add(queue1[i]);
            queue2Sum += queue2[i];
            q2.add(queue2[i]);
        }
        
        if ((queue1Sum + queue2Sum) % 2 != 0) return -1;
        
        long target = (queue1Sum + queue2Sum) / 2;
        boolean notPossible = true;
        
        while(!q1.isEmpty() && !q2.isEmpty()) {
            if (queue1Sum > queue2Sum) {
                int num = q1.poll();
                queue1Sum -= num;
                queue2Sum += num;
                q2.add(num);
                answer += 1;
            } else if (queue2Sum > queue1Sum) {
                int num = q2.poll();
                queue2Sum -= num; 
                queue1Sum += num;
                q1.add(num);
                answer += 1;
            } else {
                notPossible = false;
                break;
            }
            
            if (answer > queue1.length * 4) {
                return -1;
            }
        }
        
        if (notPossible) return -1;
        
        return answer;
    }
}
```

