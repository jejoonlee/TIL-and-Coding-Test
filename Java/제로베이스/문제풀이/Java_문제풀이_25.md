# 20230719 [Java] 문제풀이 



## [백준] 2667 단지번호붙이기



#### 1과 0으로 된 정사각형의 행렬이 주어진다

- 1은 아파트, 0은 빈공간



#### 아파트는 동서남북으로 연결이 되어 있다



#### 아파트의 수와, 각 아파트의 크기를 구하면 된다

- apartNum 에 아파트의 수를 저장했다
- 그리고 apartments에는 아파트의 크기들을 넣었다 (나중에 sort으로 정렬을 한 후 오름차순으로 출력을 했다)
  - 물론 0은 출력하면 안 됨



```java
import java.util.*;

public class baekjoon2667 {

    static int[][] map;
    static int[] dr = {-1, 0, 0, 1};
    static int[] dc = {0, -1, 1, 0};
    static int[] apartments = new int[25*25];
    static int apartNum = 0;
    static int[][] visited;
    static int N;

    public static void dfs(int x,int y) {

        visited[x][y] = 1;
        apartments[apartNum] ++;

        for (int i = 0; i < 4; i++) {
            int sr = dr[i] + x;
            int sc = dc[i] + y;

            if ((0 <= sr && sr < N) && (0 <= sc && sc < N)) {
                if (map[sr][sc] == 1 && visited[sr][sc] == 0) {
                    dfs(sr, sc);
                }
            }
        }
    }


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        N = Integer.parseInt(scanner.next());

        map = new int[N][N];

        visited = new int[N][N];

        for (int i = 0; i < N; i ++) {
            String[] input = scanner.next().split("");

            for (int j = 0; j < N; j ++) {
                map[i][j] = Integer.parseInt(input[j]);
            }
        }

        for (int i = 0; i < N; i ++) {
            for (int j = 0; j < N; j ++) {
                if (map[i][j] == 1 && visited[i][j] == 0) {
                    apartNum ++;
                    dfs(i, j);
                }
            }
        }

        System.out.println(apartNum);
        Arrays.sort(apartments);
        for (int i = 1; i < apartments.length; i++) {
            if (apartments[i] == 0) continue;
            System.out.println(apartments[i]);
        }

    }
}
```



