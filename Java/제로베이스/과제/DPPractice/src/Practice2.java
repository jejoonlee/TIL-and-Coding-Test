// 수열 arr 이 주어졌을 때,
// 부분 수열 중 증가하는 부분이 가장 긴 길이를 출력하는 프로그램을 작성

// 입출력 예시
// arr : {10, 20, 30, 10, 50, 10}
// 출력 : 4

public class Practice2 {
    public static int solution(int[]array) {
        int n = array.length;
        int[] dp = new int[n];
        dp[0] = 1;
        int maxVal = 1;

        for (int i = 1; i < n; i++) {
            for(int j = i - 1; j >= 0; j--) {
                if (array[j] < array[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }

            if (dp[i] > maxVal) maxVal = dp[i];
        }

        return maxVal;
    }
    public static void main(String[] args) {
        int[] array = new int[] {70, 60, 50};
        System.out.println(solution(array));
    }
}
