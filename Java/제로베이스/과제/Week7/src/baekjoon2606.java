import java.util.*;

public class baekjoon2606 {

    static int[] visited;
    static ArrayList<ArrayList<Integer>> matrix;
    static int count = 0;

    public static void dfs(int start) {

        visited[start] = 1;

        for (int i = 0; i < matrix.get(start).size(); i++) {
            if (visited[matrix.get(start).get(i)] == 0) {
                visited[matrix.get(start).get(i)] = 1;
                count += 1;
                dfs(matrix.get(start).get(i));
            }
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int nodes = Integer.parseInt(scanner.next());
        int lines = Integer.parseInt(scanner.next());

        visited = new int[nodes + 1];

        matrix = new ArrayList<>();

        for (int i = 0; i < nodes + 1; i ++) matrix.add(new ArrayList<>());

        for (int i = 0; i < lines; i ++) {
            int s = Integer.parseInt(scanner.next());
            int e = Integer.parseInt(scanner.next());

            matrix.get(s).add(e);
            matrix.get(e).add(s);
        }

        dfs(1);
        System.out.println(count);
    }
}
