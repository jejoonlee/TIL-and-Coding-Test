# 20230906 [Java] 문제풀이 





## [프로그래머스] 메뉴 리뉴얼



#### 문자열을 리스트로 잘 만들고, 2중 리스트에서, 리스트 크기에 따라서 정렬을 한다



#### {2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}

- 2 를 answer에 제일 앞 부분에 넣는다 (2)
- {2} 와 {2, 1} 을 비교하여, 없는 숫자를 answer에 넣는다 (1)
- {2, 1}와 {2, 1, 3} 을 비교하여, 없는 숫자를 answer에 넣는다 (3)
- {2, 1, 3}와 {2, 1, 3, 4} 을 비교하여, 없는 숫자를 answer에 넣는다 (4)



```java
import java.util.*;
class Solution {
    public ArrayList<Integer> solution(String s) {
        
        ArrayList<Integer> answer = new ArrayList<>();
        
        // 앞에 {{ 와 뒤의 }} 빼기
        s = s.substring(2, s.length() - 2);
        
        s = s.replace("},{", "/");
        
        String[] stringArray = s.split("/");
        
        // 문자열 길이를 오름차순으로 정렬
        Arrays.sort(stringArray, (x1, x2) -> x1.length() - x2.length());
        
        answer.add(Integer.parseInt(stringArray[0].split(",")[0]));

        for (int i = 1; i < stringArray.length; i++) {
            
            String[] tempArray = stringArray[i].split(",");
            
            for (String temp : tempArray) {
                int tempNum = Integer.parseInt(temp);
                if(!answer.contains(tempNum)) {
                    answer.add(tempNum);
                }
            }
        }

        
        return answer;
    }
}
```

