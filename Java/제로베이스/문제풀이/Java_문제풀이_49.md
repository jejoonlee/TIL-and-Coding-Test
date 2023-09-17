# 20230917 [Java] 문제풀이 





## [프로그래머스] 소수 찾기



#### isNotSuso 배열에 0부터 9999999까지 수소의 여부를 true 또는 false로 설정한다

- 수소이면 false / 아니면 true 이다



#### permutation, 순열을 통해서 주어진 숫자에서, 만들 수 있는 모든 숫자들을 만든다



#### 숫자들을 만들 때에 중복이 될 수 있기 때문에, set에 넣어준다



#### set에서 숫자들을 빼면서 수소인지 아닌지 인덱스를 통해서 개수를 센다



```java
import java.util.*;

class Solution {
    
    HashSet<Long> set = new HashSet<>();
    boolean[] isNotSuso = new boolean[10000000];
    int count = 0;
    
    
    
    public void permutation(String[] nums, boolean[] visited, int limit, int idx, String str) {
        
        if (idx == limit) {
            
            Long number = Long.parseLong(str);
            
            set.add(number);
            
            return;
        }
        
        
        for (int i = 0; i < nums.length; i ++) {
            
            if (!visited[i]) {
                visited[i] = true;
                permutation(nums, visited, limit, idx + 1, str + nums[i]);
                visited[i] = false;
            }
            
        }
        
    }
    
    public int solution(String numbers) {
        
        isNotSuso[0] = true;
        isNotSuso[1] = true;
        
        for (int i = 2; i < 10000000 / 4; i ++) {
            if (isNotSuso[i] == false) {
                for (int j = i + i; j < 10000000; j += i) {
                    isNotSuso[j] = true;
                }
            }
        }
          
        String[] nums = numbers.split("");
        boolean[] visited = new boolean[nums.length];
        
        for (int i = 1; i <= nums.length; i ++) {
            permutation(nums, visited, i, 0, "");
        }
        
        System.out.println(set);
        
        for (Long number : set) {
            if (!isNotSuso[number.intValue()]) count ++;
        }
        
        return count;
    }
}
```

