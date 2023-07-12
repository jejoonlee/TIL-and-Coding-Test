import java.util.*;

public class Practice2 {

    public static int[][] getPositions() {
        Scanner scanner = new Scanner(System.in);
        int[][] positions = new int[10][2];

        for (int i = 0; i < 10; i ++) {
            System.out.printf("%d/10 번째 입력", i + 1).println();

            System.out.println("임의의 좌표 x값을 입력해 주세요");
            int x = scanner.nextInt();
            System.out.println("임의의 좌표 y값을 입력해 주세요");
            int y = scanner.nextInt();

            positions[i][0] = x;
            positions[i][1] = y;
        }

        return positions;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("내 좌표 x값을 입력해 주세요.");
        int myX = scanner.nextInt();
        System.out.println("내 좌표 y값을 입력해 주세요.");
        int myY = scanner.nextInt();

        int[][] positions = getPositions();


    }
}
