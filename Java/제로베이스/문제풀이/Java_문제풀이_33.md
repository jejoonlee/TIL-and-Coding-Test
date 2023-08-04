# 20230804 [Java] 문제풀이 







## [프로그래머스] 무인도 여행



#### DFS만 잘 구현하면 쉽게 풀 수 있는 내용이었다



#### 일단 방문처리를 하면서 섬을 탐색하면서 count에다가 maps에 있는 숫자들을 더해주면 된다



```java
import java.util.*;
class Solution {
    
    public static int[] dr = {-1, 0, 0, 1};
    public static int[] dc = {0, -1, 1, 0};
    public static String[][] realMap;
    public static int[][] visited;
    public static int count;
    
    public static int dfs(int row, int column) {
        
        for (int i = 0; i < 4; i++) {
            int sr = dr[i] + row;
            int sc = dc[i] + column;
            
            if (0 <= sr && sr < realMap.length && 0 <= sc && sc < realMap[0].length) {
                if (!realMap[sr][sc].equals("X") && visited[sr][sc] == 0) {
                    visited[sr][sc] = 1;
                    count += Integer.parseInt(realMap[sr][sc]);
                    dfs(sr, sc);
                }
            }
        }
        
        return count;
    }
    
    public ArrayList<Integer> solution(String[] maps) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        realMap = new String[maps.length][maps[0].length()];
        visited = new int[maps.length][maps[0].length()];
        
        boolean isIsland = false;
        for (int i = 0; i < maps.length; i++) {
            for (int j = 0; j < maps[i].length(); j++) {
                realMap[i][j] = Character.toString(maps[i].charAt(j));
                if (maps[i].charAt(j) != 'X') isIsland = true;
            }
        }
        
        if (!isIsland) {
            answer.add(-1);
            return answer;
        }
        
        for (int i = 0; i < realMap.length; i++) {
            for (int j = 0; j < realMap[i].length; j++) {
                if (!realMap[i][j].equals("X") && visited[i][j] == 0) {
                    visited[i][j] = 1;
                    count = Integer.parseInt(realMap[i][j]);
                    answer.add(dfs(i, j));
                }
            }
        }
        
        Collections.sort(answer);
        
        return answer;
    }
}
```
