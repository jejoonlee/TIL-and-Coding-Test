
public class nQueen {
    static int n = 4;
    static int[] board = new int[n];
    static int count;

    public static int queen(int row) {

        if (row == n) {
            count ++;

            for (int i = 0; i < n; i++) {
                System.out.print(board[i] + " ");
            }
            System.out.println();
            return count;
        }

        for (int i = 0; i < n; i ++) {
u            board[row] = i;

            if (isPromising(row)) {
                queen(row + 1);
            }
        }

        return count;
    }

    public static boolean isPromising(int row) {
        for (int i = 0; i < row; i++) {
            if (board[row] == board[i] || row - i == Math.abs(board[row] - board[i])) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        System.out.println(queen(0));
    }
}
