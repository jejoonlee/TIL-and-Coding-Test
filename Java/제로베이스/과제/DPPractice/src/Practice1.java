// 정수 n이 주어졌을 때 아래의 연산을 통해 1로 만들려고 한다
    // 2로 나누어 떨어지면 2로 나누기
    // 3으로 나누어 떨어지면 3으로 나누기
    // 1 빼기
// 위의 연산ㅇ르 통해 1로 만들 때 필요한 최소한의 연산 횟수를 출력하는 프로그램을 작성

// 입출력 예시
// n : 2
// 출력 : 1

// n : 9
// 출력 : 2

public class Practice1 {
    public static int solution(int num) {
        int[] dp = new int[num + 1];

        for (int i = 2; i <= num; i++) {
            dp[i] = dp[i - 1] + 1;
            if (i % 3 == 0) dp[i] = Math.min(dp[i], 1 + dp[i / 3]);
            if (i % 2 == 0) dp[i] = Math.min(dp[i], 1 + dp[i / 2]);
        }

        return dp[num];
    }
    public static void main(String[] args) {
        System.out.println(solution(2));
        System.out.println(solution(4));
        System.out.println(solution(9));
        System.out.println(solution(10));
    }
}
