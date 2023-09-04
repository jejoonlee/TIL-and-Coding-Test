# 20230904 [Java] 문제풀이 





## [프로그래머스] 거리두기 확인하기



#### P들의 위치를 찾고, P들을 비교를 한다

- 먼저 맨해튼의 거리를 비교한다
- 2 이하면, 두 개의 P들이 가로 또는 세로 상에 있으면
  - 1맨해튼 거리가 1이면, 거리두기를 못 하는 것
  - 2맨해튼 거리인데, 중간에 패티션이 없으면 거리두기를 못 하는 것
- 대각선에 있으면, 반대쪽 대각선에 모두 패티션이 없으면 거리두기를 못 하는 것이





#### 아래 코드는 테스트 코드 5번이 계속 틀린다

```java
import java.util.*;
class Solution {
    
    public static boolean socialDistance(String[] places, ArrayList<int[]> pLocation) {
        
        boolean isPossible = true;
        
        for (int i = 0; i < pLocation.size() - 1; i ++) {
            if (!isPossible) break;
            
            for (int j = i + 1; j < pLocation.size(); j ++) {
                int[] from = pLocation.get(i);
                int[] to = pLocation.get(j);
                
                int manhattan = Math.abs(from[0] - to[0]) + Math.abs(from[1] - to[1]);
                
                if (manhattan <= 2) {
                    // 가로 상에 있으면
                    if (from[0] == to[0]) {
                        if (manhattan == 1) {   // 거리가 1이면 바로 옆에 있다는 것
                            isPossible = false;
                            break;
                        } else if (manhattan == 2) {    // 거리가 2이고 중간에 파티션 여부
                            char petition = places[from[0]].charAt(from[1] + 1);
                            if (petition == 'O') {
                                isPossible = false;
                                break;
                            }
                        }
                        // 세로 상에 있으면
                    } else if (from[1] == from[1]) {
                        if (manhattan == 1) {   // 거리가 1이면 바로 옆에 있다는 것
                            isPossible = false;
                            break;
                        } else if (manhattan == 2) {    // 거리가 2이고 중간에 파티션 여부
                            char petition = places[from[0] + 1].charAt(from[1]);
                            if (petition == 'O') {
                                isPossible = false;
                                break;
                            }
                        }
                        
                    }
                    // 대각선 위치
                    if (from[0] != to[0] && from[1] != to[1]) {
                        
                        if (from[1] < to[1]) {
                            // from 위치의 동쪽과 남쪽을 확인하고, 둘 중에 하나라도 패티션이 없으면 거리두기를 못 하고 있는 것
                            if (places[from[0] + 1].charAt(from[1]) != 'X' && places[from[0]].charAt(from[1] + 1) != 'X') {
                                isPossible = false;
                                break;
                            }
                            // from 위치의 서쪽과 남쪽을 확인하고, 둘 중에 하나라도 패티션이 없으면 거리두기를 못 하고 있는 것
                        } else if (from[1] > to[1]) {
                            if (places[from[0] + 1].charAt(from[1]) != 'X' && places[from[0]].charAt(from[1] - 1) != 'X') {
                                isPossible = false;
                                break;
                            }
                        }
                        
                    }
                }
            }
            
            if (!isPossible) break;
        }
        
        return isPossible;
    }
    
    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        
        
        for (int i = 0; i < 5; i ++) {
            ArrayList<int[]> pLocation = new ArrayList<>();
        
            for (int j = 0; j < 5; j ++) {
                for (int k = 0; k < 5; k ++) {
                    if (places[i][j].charAt(k) == 'P') {
                        pLocation.add(new int[]{j, k});
                    }
                }
            }
            
            Collections.sort(pLocation, (x1, x2) -> x1[0] - x2[0]);
            
            for (int[] pLoc : pLocation) System.out.print(Arrays.toString(pLoc));
            System.out.println();
            
            if (socialDistance(places[i], pLocation)) {
                answer[i] = 1;
            };
            
            
        }
        
        return answer;
    }
}
```
