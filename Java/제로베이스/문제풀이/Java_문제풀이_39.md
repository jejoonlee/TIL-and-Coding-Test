# 20230819 [Java] 문제풀이 







## [프로그래머스] 할인 행사



#### HashMap에 원하는 제품과, 그 수량을 넣는다



#### 그리고 10일 단위로, Discount를 순회하면서, HashMap에 있는 제품과 동일한 제품이 있으면 하나씩 빼준다

- 즉 10일 단위로 갱신이 될 때마다 새로운 HashMap을 가지고 와야 한다
- 그래서 copy 라는 메서드를 따로 만들었다



#### 그렇게 10개를 모두 살 수 있으면 answer에다가 1을 누적시키면 된다

- 제발 문제를 잘 읽자!!!!!!!



```java
import java.util.*;
class Solution {
    public static HashMap<String, Integer> copy(HashMap<String, Integer> list) {
        
        HashMap<String, Integer> newList = new HashMap<>();
        
        for (String key : list.keySet()) {
            newList.put(key, list.get(key));
        }
        
        return newList;
    }
    
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        HashMap<String, Integer> list = new HashMap<>();
        
        for (int i = 0; i < want.length; i++) { 
            list.put(want[i], number[i]);
        }
        
        for (int j = 0; j <= discount.length - 10; j++) {
            HashMap<String, Integer> tempList = copy(list);
            int tempAns = 0;

            for (int k = j; k < j + 10; k++) {
                if (tempList.containsKey(discount[k]) && tempList.get(discount[k]) != 0) {
                    tempList.put(discount[k], tempList.get(discount[k]) - 1);
                    tempAns ++;
                }    
            }
            
            if (tempAns == 10) {
                answer += 1;
            }
        }
        
        return answer;
    }
}
```

