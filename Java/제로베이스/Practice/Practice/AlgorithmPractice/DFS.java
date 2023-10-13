import java.util.*;
public class DFS {

    private static int[] result;
    private static boolean[] visited;

    public static void permutationOne(int[] num, int depth) {

        if (depth == result.length) {
            for (int r : result) System.out.print(r + " ");
            System.out.println();
            return;
        }

        for (int i = 0; i < num.length; i ++) {
            result[depth] = num[i];
            permutationOne(num, depth + 1);
        }
    }

    public static void permutationTwo(int[] num, int depth) {
        if(depth == result.length) {
            for (int r : result) System.out.print(r + " ");
            System.out.println();
            return;
        }

        for (int i = 0; i < num.length; i ++) {

            if (!visited[i]) {
                visited[i] = true;
                result[depth] = num[i];
                permutationTwo(num, depth + 1);
                visited[i] = false;
            }
        }
    }

    public static void combinationOne(int[] num, int start, int depth) {
        if (depth == result.length) {
            for (int i = 0; i < num.length; i++) {
                if (visited[i]) System.out.println(num[i]);
            }
            return;
        }

        for (int i = 0; i < num.length; i ++) {

            if (!visited[i]) {
                visited[i] = true;
                result[depth] = num[i];
                combinationOne(num, i + 1, depth + 1);
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) {

        int[] numbers = new int[]{3, 6, 9};
        int limit = 2;
        result = new int[limit];
        visited = new boolean[numbers.length];

        permutationOne(numbers, 0);
        System.out.println("======================");
        permutationTwo(numbers, 0);
        System.out.println("======================");
        combinationOne(numbers, 0, 0);
    }
}
