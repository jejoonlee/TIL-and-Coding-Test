// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {

        int [][] testArray1 = new int[3][3];

        for (int i = 0; i < 3; i ++) {
            for (int j = 0; j < 3; j ++) {
                testArray1[i][j] = 1;
                if (i == j) {
                    testArray1[i][j] = 10;
                }
            }
        }

        for (int[] itemRow: testArray1) {
            for (int item: itemRow) {
                System.out.print(item + " ");
            }
            System.out.println();
        }
    }
}