# 20230707 [Java] 문제풀이 



## [프로그래머스] 완주하지 못한 선수

#### 완주하지 못 한 선수를 찾는 것이다



#### 참여는 했지만, 끝내지 못 한, 한 사람을 찾으면 된다



#### 참여한 사람들의 이름을 marathon 이라는 HashMap에 넣고, value는 +1을 해준다

- 같은 이름이 있을 수 있다



#### completion에서, 이름이 나올때마다, value에 -1을 해준다

- 동명인이 없으면 모든 value는 하나 빼고 0일 것이다
- 동명인이 있을 수 있어 -1만 해주는 것이다
- 0이 아니면 그 사람이 완주를 못 한 선수다



```java
import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> marathon = new HashMap<String, Integer>();
        
        for (String runner : participant) {
            if (!marathon.containsKey(runner)) {
                marathon.put(runner, 1);
            } else {
                int num = marathon.get(runner);
                marathon.put(runner, num + 1);
            }
            
        }
        
        for (String runner : completion) {
            int num = marathon.get(runner);
            marathon.put(runner, num - 1);
        }
        
        for (String run : marathon.keySet()) {
            if (marathon.get(run) > 0) {
                return run;
            }
        }
        
        return "None"
    }
}
```

