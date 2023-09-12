# 20230913 [Java] 문제풀이 





## [프로그래머스] 문자열 압축



#### 입력되는 문자열을 압축하는 것이다

- 단 문자 단위는 같아야 하고, 연속되는 문자가 같으면 압축을 한다



```java
class Solution {
    public int solution(String s) {
        int answer = s.length();
        
        if (s.length() == 1) return 1;
        
        for (int i = 1; i <= s.length() / 2; i ++) {
            // cnt는 같은 문자열이 연속으로 있는지 카운트 해준다
            // cnt = 1은 아직 같은 문자열이 없다는 것
            int cnt = 1;
            String tempS = s.substring(0, i);
            String comString = "";
            int last = 1;
            
            for (int j = i; j < s.length(); j += i) {
                
                // Math.min(j+i, s.length())를 해서, 문자열 밖으로 안 나가게 한다
                String tempCompare = s.substring(j, Math.min(j + i, s.length())); 
                last = j;
                
                if (tempS.equals(tempCompare)) {
                    cnt ++;
                } else {
                    // cnt가 1이라는 것은, 연속되는 같은 단어가 없다는 것
                    // 즉 압축을 못 하는 것
                    if (cnt >= 2) {
                        comString += String.format("%d", cnt);
                    } 
                    
                    comString += tempS;
                    tempS = tempCompare;
                    cnt = 1;
                }
            }

            if (cnt > 1) comString += String.format("%d", cnt) + tempS;
            else comString += tempS;

            answer = Math.min(comString.length(), answer);
        }
        
        
        return answer;
    }
}
```

