# 20230718 [Java] 문제풀이 



## [백준] 1260 DFS와 BFS



#### 예전에 파이썬으로 풀었던 문제를 자바로 풀어보았다



#### DFS와 BFS를 구현하는 것이다



#### 여기서 만약에 자식 노드, 즉 다음 정점의 개수가 1개 이상일 경우, 제일 작은 것부터 탐색을 한다

- 즉 모든 자식 노드들을 오름차순으로 정렬을 해주면 된다



```java
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
```





## [백준] 2606 바이러스

#### 1번의 컴퓨터를 통해서 감염된 컴퓨터의 갯수를 출력하는 것이다



#### DFS로 문제를 풀었고, 1번 제외, 다른 노드들을 순회할 때마다 1을 더해주면 된다



```java
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
```

