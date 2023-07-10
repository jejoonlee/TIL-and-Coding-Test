import java.util.*;
public class Main2 {

    static class Edge {
        int from;
        int to;
        int distance;

        Edge(int from, int to, int distance) {
            this.from = from;
            this.to = to;
            this.distance = distance;
        }
    }

    public static void bellmanFord(int vertex, int edge, int[][] data, int start) {
        Edge[] edgeArray = new Edge[edge]; // 모든 간선을 확인해야 한다. 그래서 모든 간선을 하나의 배열 안에 넣는다

        for (int i = 0; i < edge; i++) edgeArray[i] = new Edge(data[i][0], data[i][1], data[i][2]);

        int[] dist = new int[vertex + 1];

        for (int i = 0; i <= vertex; i++) dist[i] = Integer.MAX_VALUE;
        dist[start] = 0;

        boolean isNegCycle = false;

        for (int i = 0; i < vertex + 1; i++) {
            for (int j = 0; j < edge; j++) {
                Edge curEdge = edgeArray[j];

                if (dist[curEdge.from] != Integer.MAX_VALUE && dist[curEdge.to] > dist[curEdge.from] + curEdge.distance) {
                    dist[curEdge.to] = dist[curEdge.from] + curEdge.distance;

                    if (i == vertex) isNegCycle = true;
                }
            }
        }

        if (isNegCycle) {
            System.out.println("음수 사이클");
        } else {
            for(int i = 1; i < dist.length; i ++) System.out.print(dist[i] + " ");
        }
    }
    public static void main(String[] args) {
        int[][] data = {{1, 2, 5}, {1, 3, -4}, {1, 5, 6}, {2, 4, 7}, {3, 4, 3}, {3, 5, 5}, {4, 6, 1}, {5, 6, 9}};
        bellmanFord(6, data.length, data, 1);
    }
}
