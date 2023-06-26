import java.util.*;
public class graphPractice {

    public static void dfs(int start, ArrayList<ArrayList<Integer>> adjList){
        System.out.println(adjList);
        Stack<Integer> stack = new Stack<Integer>();

        int[] visited = new int[adjList.size() + 1];
        int current;
        visited[start] = 1;

        stack.push(start);

        while (stack.size() != 0) {
            current = stack.pop();
            System.out.print(current + " ");

            for (int cur : adjList.get(current)) {
                if (visited[cur] == 0) {
                    stack.push(cur);
                    visited[cur] = 1;
                }
            }
        }

    }

    public static void bfs(int start, ArrayList<ArrayList<Integer>> adjList){
        System.out.println(adjList);
        Queue<Integer> queue = new LinkedList<>();

        int[] visited = new int[adjList.size() + 1];
        int current;
        visited[start] = 1;

        queue.offer(start);

        while (queue.size() != 0) {
            current = queue.remove();
            System.out.print(current + " ");

            for (int cur : adjList.get(current)) {
                if (visited[cur] == 0) {
                    queue.offer(cur);
                    visited[cur] = 1;
                }
            }
        }

    }
    public static void main(String[] args) {
        int[][] edge = {{1, 2}, {1, 3}, {2, 4}, {3, 4}, {3, 5}, {4, 5}};

        int nodeNum = 5;

        ArrayList<ArrayList<Integer>> adjList = new ArrayList<ArrayList<Integer>>();

        for (int i = 0; i <= 5; i++) adjList.add(new ArrayList<>());

        for (int i = 0; i < edge.length; i++) {
            adjList.get(edge[i][0]).add(edge[i][1]);
            adjList.get(edge[i][1]).add(edge[i][0]);
        }

        for (int i = 1; i < adjList.size(); i++) {
            System.out.print(i + "의 인접 정점 :  ");
            for (int j = 0; j < adjList.get(i).size(); j++) {
                System.out.print(adjList.get(i).get(j) + " ");
            }
            System.out.println();
        }

        dfs(1, adjList);
        bfs(1, adjList);
    }
}
