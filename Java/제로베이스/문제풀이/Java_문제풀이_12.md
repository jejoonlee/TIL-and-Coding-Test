# 20230627 [Java] 문제풀이 





## [프로그래머스] 안전지대

#### 행렬이 주어진다



#### 1은 지뢰가 있는 곳 그리고 0은 지뢰가 없는 곳이다

- 지뢰 기준으로 8방면 (위, 아래, 좌, 우, 대각선) 모두 위험 지역이다



#### 위험 지역이 아닌 곳의 개수를 찾으면 된다



#### 1) 델타 탐색 (dr, dc) 를 통해 1을 발견하면 8방면을 2로 만들어 준다 



#### 2) 그렇게 위험 지역을 1과 2로 표시하고, 다시 2중 for문을 통해 안전 지역인 0을 세준다



```java
class Solution {
    public int solution(int[][] board) {
        int answer = 0;
        
        int[] dr = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dc = {-1, 0, 1, -1, 1, -1, 0, 1};
        
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board.length; c++) {
                if (board[r][c] == 1) {
                    for (int i = 0; i < 8; i++) {
                        int sr = dr[i] + r;
                        int sc = dc[i] + c;
                        
                        if ((0 <= sr && sr < board.length) && (0 <= sc && sc < board.length)) {
                            if (board[sr][sc] == 0) {
                                board[sr][sc] = 2;
                            }
                        }
                    }
                }
            }
        }
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                if (board[i][j] == 0) {
                    answer += 1;
                }
            }
        }
        
        return answer;
    }
}
```





## 최빈값 구하기

#### 배열이 주어지고, 배열 안에 정수 중에, 제일 많이 나온 정수를 출력하는 것이다



#### 제일 많이 나온 정수의 개수가 1을 초과할 때에, -1을 출력한다



#### Collections.max(map.values()); 를 통해서 최대 값을 가지고 온다

- 여기서 최대 값은, 제일 큰 개수를 뜻한다



#### 그리고 map을 순회하면서, 최대 개수와 동일한 값을 가진 key를 numbers 리스트에 넣는다



#### numbers 리스트가 1을 초과하면 -1 을 출력하고, 한 개면, 그 하나의 정수만 출력해준다



```java
import java.util.*;

class Solution {
    public int solution(int[] array) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        int value;
        
        for (int num : array) {
            if (!map.containsKey(num)) {
                map.put(num, 1);
            } else {
                value = map.get(num);
                map.put(num, value + 1);
            }
        }
        
        int maxVal = Collections.max(map.values());
        
        System.out.println(maxVal);
        
        for (int num : map.keySet()) {
            if (map.get(num) == maxVal) {
                numbers.add(num);
            }
        }
        
        if (numbers.size() > 1) {
            return -1;
        } else {
            return numbers.get(0);
        }
    }
}
```



