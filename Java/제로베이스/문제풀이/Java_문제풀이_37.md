# 20230817 [Java] 문제풀이 







## [프로그래머스] 귤 고르기



#### 해쉬맵으로 문제를 풀었다



#### 해쉬맵에 귤 사이즈를 key, 사이즈에 대한 개수를 value로 넣었다



#### value기준으로 최소한의 종류를 구했다 (value를 배열에 넣고 내림차순으로 정렬했다)



```java
import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        
        HashMap<Integer, Integer> map = new HashMap<>();
        ArrayList<Integer> array = new ArrayList<>();
        
        for (int num : tangerine) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }
        
        for (Integer key : map.keySet()) array.add(map.get(key));
        
        Collections.sort(array, (x1, x2) -> x2 - x1);
        
        int tempAns = 0;
        
        for (int i = 0; i < array.size(); i++) {
            tempAns += array.get(i);
            if (tempAns >= k){
                answer = i + 1;
                break;
            }
        }
        
        
        return answer;
    }
}
```

