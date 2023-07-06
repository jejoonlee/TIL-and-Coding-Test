// 배낭에 물플을 담으려고 한다
// 배낭에는 k 무게 만큼의 물품을 담을 수 있다
// n 개의 물품이 주어지고 이 물품의 무게와 가치 정보가 items 2차원 배열에 주어졌을 때,
// 최대 가치가 되도록 물품을 담았을 때의 가치를 출력하는 프로그램을 작성해라

// 입출력 예시
// items : {{6, 13}, {4, 8}, {3, 6}, {5, 12}}
// n : 4
// k : 7
// 출력 14

import java.util.*;
public class Practice3 {
    public static int solution(int[][] items, int n, int k) {
        int[][] dp = new int[n + 1][k + 1];

        for (int i = 0; i < n; i ++) {
            for (int j = 1; j <= k; j ++) {
                if (items[i][0] > j) {
                    dp[i + 1][j] = dp[i][j];
                } else {
                    dp[i + 1][j] = Math.max(dp[i][j], items[i][1] + dp[i][j - items[i][0]]);
                }
            }
        }

        for (int i = 0; i < dp.length; i++) {
            System.out.println(Arrays.toString(dp[i]));
        }

        return dp[n][k];
    }
    public static void main(String[] args) {
        int[][] items = {{6, 13}, {4, 8}, {3, 6}, {5, 12}};
        System.out.println(solution(items, 4, 7)); // 14
    }
}
