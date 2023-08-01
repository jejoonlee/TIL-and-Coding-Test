# 20230801 [Java] 문제풀이 







## [프로그래머스] 리코쳇 로봇



#### 동, 서, 남, 북 으로만 움직일 수 있고, 한 방향으로 움직이기 시작하면 게임판 내 또는 "D"를 마주할때까지 앞으로 움직인다



#### 그렇게 움직임을 세면서 제일 적은 횟수로 "G"까지 도달할 수 있도록 구현을 하는 문제이다



#### BFS로 구현을 했다



```java
import java.util.*;

class Solution {
    public int solution(String[] board) {
        
        String[][] newBoard = new String[board.length][board[0].length()];
        int[][] visited = new int[board.length][board[0].length()];
        
        int[] dr = {-1, 0, 0, 1};
        int[] dc = {0, -1, 1, 0};
        
        Queue<int[]> queue = new LinkedList<>();
        
        for(int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length(); j++) {
                newBoard[i][j] = Character.toString(board[i].charAt(j));
                
                if (board[i].charAt(j) == 'R') queue.add(new int[] {i, j});
            }
        }
        
        boolean goal = false;
        int count = 0;
        
        while (!queue.isEmpty()) {
            
            int sizeQ = queue.size();
            
            count ++;
            for (int sizeCount = 0; sizeCount < sizeQ; sizeCount ++) {
                int[] current = queue.remove();
                visited[current[0]][current[1]] = 1;

                for (int i = 0; i < 4; i++) {
                    int sr = dr[i] + current[0];
                    int sc = dc[i] + current[1];

                    while ((0 <= sr && sr < newBoard.length) && (0 <= sc && sc < newBoard[0].length)) {
                        if (newBoard[sr][sc].equals("D")) {
                            if (visited[sr - dr[i]][sc - dc[i]] != 1) {
                                if (newBoard[sr - dr[i]][sc - dc[i]].equals("G")) return count;
                                visited[sr - dr[i]][sc - dc[i]] = 1;
                                queue.add(new int[]{sr - dr[i], sc - dc[i]});
                            }
                            break;
                        }
                        sr += dr[i];
                        sc += dc[i];
                    }

                    if (sr == -1 || sr == newBoard.length || sc == -1 || sc == newBoard[0].length) {
                        sr -= dr[i];
                        sc -= dc[i];

                        if (newBoard[sr][sc].equals("G")) return count;

                        if (visited[sr][sc] == 0) {
                            visited[sr][sc] = 1;
                            queue.add(new int[]{sr, sc});
                        }
                    }
                }
            }
        }
        
        return -1;
    }
}
```
