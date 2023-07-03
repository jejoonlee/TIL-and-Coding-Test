import java.util.*;
public class Baekjoon2167 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.next());
        int m = Integer.parseInt(scanner.next());

        int[][] matrix = new int[n][m];

        for (int x = 0; x < n ; x++) {
            for(int y = 0; y < m; y++) {
                matrix[x][y] = Integer.parseInt(scanner.next());
            }
        }

        int test = scanner.nextInt();

        for (int i = 0; i < test; i ++) {
            int answer = 0;
            int startx = Integer.parseInt(scanner.next()) - 1;
            int starty = Integer.parseInt(scanner.next()) - 1;
            int finishx = Integer.parseInt(scanner.next()) - 1;
            int finishy = Integer.parseInt(scanner.next()) - 1;

            for (int x = startx; x <= finishx; x ++) {
                for (int y = starty; y <= finishy; y++) {
                    answer += matrix[x][y];
                }
            }

            System.out.println(answer);
        }
    }
}
