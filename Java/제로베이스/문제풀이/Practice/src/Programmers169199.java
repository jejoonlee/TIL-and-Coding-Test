import java.util.*;
public class Programmers169199 {
    static class Solution {
        public int solution(String[] board) {
            int answer = 0;

            String[][] newBoard = new String[board.length][board[0].length()];

            int[] dr = {-1, 0, 0, 1};
            int[] dc = {0, -1, 1, 0};

            Queue<int[]> queue = new LinkedList<>();

            for(int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[i].length(); j++) {
                    newBoard[i][j] = Character.toString(board[i].charAt(j));
                    if (board[i].charAt(j) == 'R') queue.add(new int[] {i, j});
                }
            }

            boolean goal = false;
            int count = 0;

            while (!queue.isEmpty()) {
                if (goal == true) break;

                int[] current = queue.remove();
                newBoard[current[0]][current[1]] = "V";

                count ++;
                for (int i = 0; i < 4; i++) {
                    int sr = dr[i] + current[0];
                    int sc = dc[i] + current[1];

                    while (true) {
                        if ((0 <= sr && sr < newBoard[0].length) && (0 <= sc && sc < newBoard.length)) {
                            if (sr == 0 || sr == newBoard[0].length - 1 || sc == 0 || sc == newBoard.length - 1) {
                                if (newBoard[sr][sc] != "D") {
                                    if (newBoard[sr - dr[i]][sc - dc[i]] == "G") {
                                        goal = true;
                                    }
                                    newBoard[sr][sc] = "V";
                                    break;
                                }
                            }

                            if (newBoard[sr][sc] == "V") {
                                break;
                            } else if (newBoard[sr][sc] == "D") {
                                if (newBoard[sr - dr[i]][sc - dc[i]] == "G") {
                                    goal = true;
                                }
                                newBoard[sr - dr[i]][sc - dc[i]] = "V";
                                queue.add(new int[]{sr - dr[i], sc - dc[i]});
                                break;
                            }
                        }
                        sr = dr[i] + current[0];
                        sc = dc[i] + current[1];

                    }
                    if (goal) break;
                }

            }

            for (String[] s : newBoard) System.out.println(Arrays.toString(s));

            return answer;
        }
    }

    public static void main(String[] args) {
        String[] string = {"...D..R", ".D.G...", "....D.D", "D....D.", "..D...."};

        Solution sol = new Solution();

        sol.solution(string);
    }
}
