# 20230918 [Java] 문제풀이 





## [프로그래머스] 프로세스



#### 우선순위 큐를 사용해서 프로세스의 우선순위를 찾는다

- 여기서 우선순위 큐는 내림차순으로 만들어야 한다



#### 그리고 큐에 priorities를 프로세스의 인덱스와 프로세스의 우선순위를 배열로 넣어준다



#### 큐를 돌면서 우선순위가 같은 프로세스를 result 리스트에 넣어주고 우선순위 큐에서 해당 우선순위는 빼주고, 큐에서도 빼준다



#### 큐를 돈다는 것은, 우선순위가 같지 않으면 큐의 맨 뒤로 돌아가게 된다



```java
import java.util.*;

class Solution {
    
    public int solution(int[] priorities, int location) {

        ArrayList<Integer> result = new ArrayList<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>((x1, x2) -> x2 - x1);
        Queue<int[]> queue = new LinkedList<>();
        
        for (int i = 0 ; i < priorities.length; i ++) {
            pq.offer(priorities[i]);
            
            // 큐에는 인덱스와, 우선순위를 넣는다
            queue.offer(new int[]{i, priorities[i]});
        }
        
        while (!queue.isEmpty()) {
            
            int[] current = queue.poll();
            
            if (pq.peek() > current[1]) {
                queue.offer(current);
            } else {
                result.add(current[0]);
                pq.poll();
            }
        }
        
        
        return result.indexOf(location) + 1;
    }
}
```





## [프로그래머스] 기능개발



#### 첫 번째 for문은, 남은 작업을 끝내기 위한 날을 센다



#### 두 번째 for문에서 그 날들을 순회하면서, 앞에 날짜가 크면, 뒤에 더 큰 날짜가 올 때까지, 한 그룹으로 묶어서 count해준다



```java
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public ArrayList<Integer> solution(int[] progresses, int[] speeds) {
        int[] leftOver = new int[progresses.length];
        
        for (int i = 0; i < progresses.length; i++) {
            
            // 0 이 아니면, 작업을 끝내려면 하루가 더 필요하다는 것
            if ((100 - progresses[i]) % speeds[i] != 0) {
                leftOver[i] = (100 - progresses[i]) / speeds[i] + 1;
            } else {
                leftOver[i] = (100 - progresses[i]) / speeds[i];
            }
            
        }
        
        ArrayList<Integer> answer = new ArrayList<Integer> ();
        int count = 1;
        
        for (int i = 1; i < progresses.length; i++) {
            if (leftOver[i - 1] >= leftOver[i]) {
                count += 1;
            } else {
                answer.add(count);
                count = 1;
            }

        }
        
        answer.add(count);
        
        return answer;
    }
}
```

