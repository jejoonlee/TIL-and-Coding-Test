import java.util.*;
public class baekjoon1260 {

    public static void dfs(int[] visited, ArrayList<ArrayList<Integer>> matrix, int start) {

        System.out.print(start + " ");
        visited[start] = 1;

        for (int i = 0; i < matrix.get(start).size(); i++) {
            if (visited[matrix.get(start).get(i)] != 1) {
                dfs(visited, matrix, matrix.get(start).get(i));
            }
        }
    }

    public static void bfs(ArrayList<ArrayList<Integer>> matrix, int start) {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(start);
        int[] visited = new int[matrix.size()];
        visited[start] = 1;

        while (!queue.isEmpty()) {
            int current = queue.poll();
            System.out.printf(current + " ");

            for (int i = 0; i < matrix.get(current).size(); i++) {
                if (visited[matrix.get(current).get(i)] == 0) {
                    visited[matrix.get(current).get(i)] = 1;
                    queue.add(matrix.get(current).get(i));
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = Integer.parseInt(scanner.next());
        int M = Integer.parseInt(scanner.next());
        int V = Integer.parseInt(scanner.next());

        ArrayList<ArrayList<Integer>> matrix = new ArrayList<>();

        for (int i = 0; i < N + 1; i ++) matrix.add(new ArrayList<Integer>());

        for (int i = 0; i < M; i ++) {
            int s = Integer.parseInt(scanner.next());
            int e = Integer.parseInt(scanner.next());

            matrix.get(s).add(e);
            matrix.get(e).add(s);
        }

        for (ArrayList<Integer> arrayList : matrix) Collections.sort(arrayList);


        int[] visited = new int[N + 1];

        dfs(visited, matrix, V);
        System.out.println();
        bfs(matrix, V);

    }
}
