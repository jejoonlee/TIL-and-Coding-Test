# 20230829 [Java] 문제풀이 





## [프로그래머스] 양궁대회



#### 아직 백트래킹, 완전 탐색이 많이 약한 것 같다 (그래도 전보다 어느 정도 생각을 할 수 있게 되었다)



#### 먼저 shoot을 통해서 n번 동안 라이언이 쏠 수 있는 모든 경우를 배열로 구한다



#### 그리고 compare을 통해서 라이언과 아파치가 맞춘 과녁을 비교하면서, 두 명의 점수를 비교해준다



```java
import java.util.*;

class Solution {
    
    public static int[] answer;
    public static int maxDif = 0;
    public static int[] lionArrow = new int[11];
    
    public void shoot(int s, int limit, int[] info) {
        if (s == limit) {
            int dif = compare(info);
            if (dif >= maxDif) {
                maxDif = dif;
                answer = lionArrow.clone();
            }
            return;
        }
        
        for (int i = 0; i < info.length && lionArrow[i] <= info[i]; i++) {
            lionArrow[i] ++;
            shoot(s+1, limit, info);
            lionArrow[i] --;
        }
        
    }
    
    public int compare(int[] info) {
        int apeach = 0;
        int lion = 0;
        
        for (int i = 0; i < info.length; i++) {
            if (info[i] == 0 && lionArrow[i] == 0) continue;
            if (info[i] >= lionArrow[i]) {
                apeach += (10 - i);
            } else {
                lion += (10 - i);
            }
        }
        
        return lion - apeach;
    }
    
    
    public int[] solution(int n, int[] info) {
        
        shoot(0, n, info);
        
        if(maxDif == 0) {
            answer = new int[1];
            answer[0] = -1;
        }
        
        return answer;
    }
}
```
