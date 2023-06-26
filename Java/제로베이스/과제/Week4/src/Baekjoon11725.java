import java.util.*;
public class Baekjoon11725 {

    public static int[] bfs(int start, ArrayList<ArrayList<Integer>> adjList) {
        Queue<Integer> queue = new LinkedList<Integer>();
        boolean[] visited = new boolean[adjList.size()];
        int[] answer = new int[adjList.size()];

        queue.offer(start);
        visited[start] = true;

        while (queue.size() != 0) {
            int current = queue.poll();

            for (int cur : adjList.get(current)) {
                if (visited[cur] == false) {
                    queue.offer(cur);
                    visited[cur] = true;

                    // 부모 노드 저장
                    answer[cur] = current;
                }
            }

        }
        return answer;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();

        int n = scanner.nextInt();
        for (int i = 0 ; i <= n; i++) adjList.add(new ArrayList<Integer>());

        for (int j = 0; j < n - 1; j++) {
            int nodeA = scanner.nextInt();
            int nodeB = scanner.nextInt();
            adjList.get(nodeA).add(nodeB);
            adjList.get(nodeB).add(nodeA);
        }

        int[] answer = bfs(1, adjList);

        for (int i = 2; i <= n; i++) {
            System.out.println(answer[i]);
        }
    }
}
