# 20230709 [Java] 문제풀이 





## [프로그래머스] 요격 시스템

#### 미사일이 떨어지는 개구간이 targets라는 2차원 배열로 주어진다



#### 이 미사일을 요격하기 위해, 필요한 요격 미사일의 개수의 최솟값을 구하는 것이다



#### 일단 각 미사일의 개구간 중, 끝 부분을 기준으로 오름차순으로 정렬을 한다



#### 그렇게 정렬을 하고 난 후에, 현재 공격 받는 미사일의 개구간의 시작점과, 그 전의 공격 받았던 미사일의 개구간의 마지막 지점이 완전히 겹치면, 한번에 요격을 할 수 있다

- [3, 6] , [4, 7] : 두 미사일을 한번에 요격할 수 있음
- [3, 6], [6, 8] : 두 미사일을 요격하려면 두 개의 요격 미사일이 필요함
- [3, 6], [7, 9] : 두 미사일을 요격하려면 두 개의 요격 미사일이 필요함



```java
// ==== 내 첫 풀이 =====
import java.util.*;

class MTarget {
    int from;
    int to;
    
    MTarget(int from, int to) {
        this.from = from;
        this.to = to;
    }
}

class Solution {
    public int solution(int[][] targets) {
        int answer = 1;
        
        ArrayList<MTarget> targetList = new ArrayList<MTarget>();
        
        for (int[] t : targets) targetList.add(new MTarget(t[0], t[1]));
        
        Collections.sort(targetList, (MTarget t1, MTarget t2) -> t1.to > t2.to ? 1:-1);
        
        int attackTo = targetList.get(0).to;
        
        for (int i = 1; i < targetList.size(); i++) {
            int attackFrom = targetList.get(i).from;
            
            if (attackFrom >= attackTo) {
                answer ++;
                attackTo = targetList.get(i).to;
            }
        }
        
        return answer;
    }
}

// ==== 두번째 풀이 =====
class Solution {
    public int solution(int[][] targets) {
        int answer = 1;
        
        Arrays.sort(targets, (t1, t2) -> t1[1] >= t2[1] ? 1:-1);
        
        int attackTo = targets[0][1];
        for (int i = 1; i < targets.length; i++) {
            int attackFrom = targets[i][0];
            
            if (attackFrom >= attackTo) {
                answer ++;
                attackTo = targets[i][1];
            }
        }
        
        return answer;
    }
}
```





## 연속된 부분 수열의 합

#### 배열 안에서, 연속된 숫자들 중 합이 k가 되는 연속된 숫자들의 길이 중, 제일 작은 좌표를 구하는 문제다



#### 투 포인터를 통해서 k가 되는 길이를 구한다

- k가 만들어지면 i, j를 임시적으로 리스트에 저장을 하면 된다



### 그리고 리스트를 순회하면서, 제일 짧은 좌표를 출력하면 된다



```java
import java.util.*;
class Solution {
    public int[] solution(int[] sequence, int k) {
        ArrayList<int[]> answer = new ArrayList<int[]>();
        
        int i = 0;
        int j = 0;
        int minVal = Integer.MAX_VALUE;
        int tempAdd = sequence[0];
        
        while (i < sequence.length) {
            if (tempAdd <= k) {
                if (tempAdd == k) {
                    answer.add(new int[]{i, j});
                    minVal = Math.min(minVal, Math.abs(i - j));
                }
                if (j + 1 < sequence.length) {
                    tempAdd += sequence[++j];
                } else {
                    tempAdd -= sequence[i ++];
                }
            } else {
                tempAdd -= sequence[i ++];
            }
        }
        
        for (int[] numbers : answer) {
            if (numbers[1] - numbers[0] == minVal) {
                return numbers;
            }
        }
        
        return null;
        
    }
}
```

