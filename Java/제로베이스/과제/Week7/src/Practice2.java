import java.util.*;

public class Practice2 {

    public static int[][] getPositions() {
        Scanner scanner = new Scanner(System.in);
        HashSet<String> checkPositions = new HashSet<String>();
        int[][] positions = new int[10][2];

        for (int i = 0; i < 10; i ++) {
            System.out.printf("%d/10 번째 입력", i + 1).println();

            System.out.println("임의의 좌표 x값을 입력해 주세요");
            int x = scanner.nextInt();
            System.out.println("임의의 좌표 y값을 입력해 주세요");
            int y = scanner.nextInt();

            String checkLocate = String.format("%d, %d", x, y);

            if (checkPositions.isEmpty() || !checkPositions.contains(checkLocate)) {
                checkPositions.add(checkLocate);
                positions[i][0] = x;
                positions[i][1] = y;
            } else {
                while (checkPositions.contains(checkLocate)) {
                    System.out.println("동일한 좌표값이 이미 존재합니다. 다시 입력해주세요");
                    System.out.printf("%d/10 번째 입력", i + 1).println();

                    System.out.println("임의의 좌표 x값을 입력해 주세요");
                    x = scanner.nextInt();

                    System.out.println("임의의 좌표 y값을 입력해 주세요");
                    y = scanner.nextInt();

                    checkLocate = String.format("%d, %d", x, y);
                }
                checkPositions.add(checkLocate);
                positions[i][0] = x;
                positions[i][1] = y;
            }
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

        double minDist = Double.MAX_VALUE;
        int[] finalResult = new int[2];

        for (int i = 0; i < positions.length; i++) {
            int xLocate = positions[i][0];
            int yLocate = positions[i][1];

            int xDif = Math.abs(xLocate - myX);
            int yDif = Math.abs(yLocate - myY);

            double dist = Math.sqrt(Math.pow(xDif, 2) + Math.pow(yDif, 2));

            if (dist < minDist) {
                minDist = dist;
                finalResult[0] = xLocate;
                finalResult[1] = yLocate;
            }

            System.out.printf("(%d, %d) => %.06f", xLocate, yLocate, dist).println();
        }

        System.out.println("제일 가까운 좌표:");
        System.out.printf("(%d, %d) => %.06f", finalResult[0], finalResult[1], minDist);
    }
}
