# 20230802 [Java] 문제풀이 







## [프로그래머스] 미로 탈출



#### start에서 lever로 갈 수 있는 최단 거리



#### lever에서 exit로 갈 수 있는 최단 거리를 구하는 것이다



#### 즉 bfs를 두번을 해야 하며, 하나라도 -1이 나오면 start에서 lever을 거쳐서 exit로 못 가는 것이다

- -1은 길이 없다는 뜻



```java
import java.util.*;

class Solution {
    
    public static int count = 0;
    public static int[][] dr = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
    
    public static int bfs(String[] maps, int[] start, int[] finish) {
        
        Queue<int[]> queue = new LinkedList<>();
        
        queue.add(start);
        
        int[][] visited = new int[maps.length][maps[0].length()];
        
        visited[queue.peek()[0]][queue.peek()[1]] = 1;
        
        while(!queue.isEmpty()) {          
            
            int qSize = queue.size();

            for (int cn = 0; cn < qSize; cn++) {
                int[] cur = queue.remove();
                
                for (int i = 0 ; i < 4; i ++) {
                    int sr = dr[i][0] + cur[0];
                    int sc = dr[i][1] + cur[1];
                    
                    if ((sr >= 0 && sr < maps.length) && (sc >= 0 && sc < maps[0].length())) {

                        if (maps[sr].charAt(sc) != 'X' && visited[sr][sc] == 0) {
                            visited[sr][sc] = 1;
                            queue.add(new int[]{sr, sc});
                            
                            if (sr == finish[0] && sc == finish[1]) return ++ count;
                        }
                    }
                }
            }
            count ++;
        }
        
        return -1;
    }
    
    public int solution(String[] maps) {
        
        Queue<int[]> queue = new LinkedList<>();
        
        int[] start = new int[2];
        int[] lever = new int[2];
        int[] exit = new int[2];
        
        for (int i = 0; i < maps.length; i ++) {
            for (int j = 0; j < maps[i].length(); j ++) {
                if (maps[i].charAt(j) == 'S') {
                    start[0] = i; 
                    start[1] = j;
                } else if (maps[i].charAt(j) == 'L') {
                    lever[0] = i;
                    lever[1] = j;
                } else if (maps[i].charAt(j) == 'E') {
                    exit[0] = i;
                    exit[1] = j;
                }
            }
        }
        
        
        // start -> lever
        int cnt = bfs(maps, start, lever);
        
        // lever -> exit
        int cnt2 = bfs(maps, lever, exit);
        
        if (cnt != -1 && cnt2 != -1) return cnt2;

        return -1;
    }
}
```





