import java.util.ArrayList;
import java.util.*;

public class graphMatrix {

    public static void dfs(int start, int[][] matrix){

        Stack<Integer> stack = new Stack<>();

        int[] visited = new int[matrix.length + 1];
        int current;
        visited[start] = 1;

        stack.add(start);

        while (stack.size() != 0) {
            current = stack.pop();
            System.out.print(current + " ");

            for (int cur = 0; cur < matrix[current].length ; cur++) {
                if (matrix[current][cur] == 1 && visited[cur] == 0) {
                    stack.push(cur);
                    visited[cur] = 1;
                }
            }
        }
    }

    public static void bfs(int start, int[][] matrix){
        Queue<Integer> queue = new LinkedList<>();

        int[] visited = new int[matrix.length + 1];
        int current;
        visited[start] = 1;

        queue.offer(start);

        while (queue.size() != 0) {
            current = queue.remove();
            System.out.print(current + " ");

            for (int cur = 0; cur < matrix[current].length; cur++) {
                if (matrix[current][cur] == 1 && visited[cur] == 0) {
                    queue.offer(cur);
                    visited[cur] = 1;
                }
            }
        }

    }

    public static void main(String[] args) {

        int[][] edge = {{1, 2}, {1, 3}, {2, 4}, {3, 4}, {3, 5}, {4, 5}};

        int nodeNum = 5;

        int[][] matrix = new int[nodeNum + 1][nodeNum + 1];

        for (int i = 0; i < edge.length; i ++) {
            int[] link = edge[i];

            matrix[link[0]][link[1]] = 1;
            matrix[link[1]][link[0]] = 1;
        }

        for (int i = 1; i <= nodeNum; i++) {
            for (int j = 1; j <= nodeNum; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }

        dfs(1, matrix);
        bfs(1, matrix);

    }
}
