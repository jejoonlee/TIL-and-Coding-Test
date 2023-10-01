# 20230925 [Java] 문제풀이 





## [프로그래머스] 주식가격




#### 그냥 2중 for문을 사용하여, prices에 있는 원소들을 서로 비교하면 되는 문제다

- 크거나 같으면 다음 prices 원소를 순회한다
- 작으면 바로 break



```java
class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        for (int i = 0; i < prices.length; i++) {
            int count = 0;
            
            for (int j = i + 1; j < prices.length; j++) {
                count ++;
                if (prices[i] > prices[j]) break;
            }
            answer[i] = count;
        }
        
        return answer;
    }
}
```





## [프로그래머스] 다리를 지나는 트럭



#### 다리 길이만큼 queue에 0 을 넣어준다



#### 임시로 다리 위에 있는 트럭들의 무게를 구해줄 trucksWeight를 만든다



#### 그렇게 다리 위에 있는 트럭들과 다리에 들어올 트럭의 무게를 비교하면서, 트럭이 다리에 들어올 수 있을지 없을지 결정을 한다



#### 무게가 오버가 되면 0을 넣어주면서, 앞에 있는 0 또는 트럭을 queue에서 빼준다



```java
import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        
        Queue<Integer> bridge = new LinkedList<>();
        int trucksWeight = 0;
        
        for (int i = 0; i < bridge_length; i++) bridge.offer(0);
        
        int index = 0;
        
        while (index < truck_weights.length) {
            answer ++;
            trucksWeight -= bridge.poll();
            
            if (trucksWeight + truck_weights[index] <= weight) {
                bridge.offer(truck_weights[index]);
                trucksWeight += truck_weights[index];
                index ++;
            } else {
                bridge.offer(0);
            }
        }
        
        return answer + bridge.size();
    }
}
```







## [프로그래머스] 캐시



#### LRU 알고리즘을 사용하는 문제다 (Least Recently Used)

- 즉 캐시에 저장하는 데이터는, 제일 최근 사용한 데이터를 기준으로 캐시에 저장을 한다



#### 큐를 이용하여 캐시를 만들었다



#### 캐시 사이즈가 0일 때에는, 바로 도시 개수에 5를 곱해서 답을 리턴한다



#### 그것이 아니면 캐시 안에 데이터를 저장하며, 캐시 안에 다음 데이터가 있는지 없는지 확인한다

- 캐시 안에 데이터가 있으면, 그 데이터를 다시 queue 맨 뒤로 보내준다 (최근 사용된 데이터, +1)
- 캐시 안에 데이터가 없으면, 데이터를 캐시 안에 넣어주면 된다 ( +5)
  - 여기서 캐시 사이즈를 초과하면, 제일 앞에 있는 데이터를 없애준다



```java
import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        
        Queue<String> cache = new LinkedList<>();
        
        if (cacheSize == 0) return cities.length * 5;
        
        
        for (String c : cities) {
            String city = c.toLowerCase();
            
            if (cache.contains(city)) {
                answer ++;
                cache.remove(city);
            } else {
                if (cache.size() >= cacheSize) {
                    cache.poll();
                }
                answer += 5;
            }
            cache.offer(city);
        }
        
        return answer;
    }
}
```

