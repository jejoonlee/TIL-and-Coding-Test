# 20230705 [Java] 문제풀이 



## 신고 결과 받기

#### k번 이상 신고를 받은 사람은 게시판 이용이 정지된다



#### 한 사람이, 특정한 사람 한 명을 계속 신고해도, 한번 신고한 것과 같다

- set을 이용하여, 한 사람이 특정 한 사람을 여러 번 신고 한 것을 없앤다



#### 각 유저가, 신고한 유저 ID 중, 정지된 ID의 개수를 구하는 것



```java
import java.util.*;

// 각 유저가, 신고한 유저 ID 중, 정지된 ID의 개수를 구하는 것

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        
        HashSet<String> set = new HashSet<String>();
        
        for (String string : report) set.add(string);
        
        HashMap<String, ArrayList<String>> map = new HashMap<>();
        
        ArrayList<String> reportList = new ArrayList<String>();
        
        // 각 id의 신고 당한 횟수
        int[] reported = new int[id_list.length];
        
        for (String s : set) {
            String[] fromTo = s.split(" ");
            
            reported[Arrays.asList(id_list).indexOf(fromTo[1])] += 1;
            
            if (!map.containsKey(fromTo[0])) {
                map.put(fromTo[0], new ArrayList<String>());
                reportList = map.get(fromTo[0]);
                reportList.add(fromTo[1]);
            } else {
                reportList = map.get(fromTo[0]);
                reportList.add(fromTo[1]);
            }
            
        }
        
        int[] answer = new int[id_list.length];
        
        for (int i = 0; i < id_list.length; i++) {
            ArrayList<String> reportedNames = map.get(id_list[i]);
            
            if (reportedNames != null) {
                for (String name : reportedNames) {
                    int index = Arrays.asList(id_list).indexOf(name);
                       
                    if (reported[index] >= k) {
                        answer[i] += 1;
                    }
                }
            }
        }
        
        
        return answer;
    }
}
```





## 없는 숫자 더하기

#### 0부터 9까지의 숫자 중에 배열에 없는 숫자를 더하는 것이다



#### HashMap에 0부터 9까지의 숫자를 key와 value에 저장한다

- 예) 0 = 0 / 1 = 1 / 2 = 2 / 3 = 3 / 4 = 4 / 5  = 5 / 6 = 6 / 7 = 7 / 8 = 8 / 9 = 9 


#### 배열을 순회하면서, 배열에 있는 숫자의 value를 0으로 만든다



#### 그리고 HashMap을 순회하면서, 모든 value를 더하면 된다

- 배열에 없는 숫자는 value에 그대로 있고, 있으면 0으로 바뀐 상태



```java
import java.util.*;
class Solution {  
    public int solution(int[] numbers) {
        int answer = 0;
        
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < 10; i++) map.put(i, i);
        
        for (int num : numbers) {
            if (map.containsKey(num)) {
                map.put(num, 0);
            }
        }
        
        for (int num : map.keySet()) answer += map.get(num);
        
        return answer;
    }
}
```

