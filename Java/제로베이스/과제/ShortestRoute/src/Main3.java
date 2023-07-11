import java.util.*;
public class Main3 {

    static int[][] dist;
    static int INF = 1000000000;

    public static void floydWarshall(int nodes, int edge, int[][] data, int start){
        dist = new int[nodes + 1][nodes + 1];
        for (int i = 1; i <= nodes; i++) {
            for (int j = 1; j <= nodes; j++) {
                if (i != j) dist[i][j] = INF;
            }
        }

        for (int i = 0; i < edge; i++) {
            // data[i][0] 는 시작점
            // data[i][1] 는 바로 옆에 연결되어 있는 점
            // data[i][2] 가중치
            dist[data[i][0]][data[i][1]] = data[i][2];
        }

        for (int cross = 1; cross <= nodes; cross ++) {
            for (int i = 1; i <= nodes; i ++) {
                for (int j = 1; j <= nodes; j ++) {
                    if (dist[i][cross] != INF && dist[cross][j] != INF) {
                        dist[i][j] = Math.min(dist[i][j], dist[i][cross] + dist[cross][j]);
                    }
                }
            }
        }

        for (int i = 1; i <= nodes; i++) {
            for (int j = 1; j <= nodes; j ++) {
                if (dist[i][j] == INF) {
                    System.out.print("INF" + " ");
                }   else {
                    System.out.print(dist[i][j] + " ");
                }
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        int[][] data = {{1, 2, 5}, {1, 3, -4}, {1, 5, 6}, {2, 4, 7}, {3, 4, 3}, {3, 5, 5}, {4, 6, 1}, {5, 6, 9}};
        floydWarshall(6, data.length,data, 1);
    }
}
