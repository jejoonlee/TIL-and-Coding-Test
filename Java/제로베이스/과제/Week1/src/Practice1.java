

public class Practice1 {
    public static void solution(int num) {
        int answer = 1;
        String stringNum = String.format("%d", num);
        String reverseNum = "";

        for (int i = stringNum.length() - 1; 0 <= i ; i--) {
            char tempNum = stringNum.charAt(i);
            if (tempNum == '-') {
                answer *= -1;
                break;
            }

            reverseNum += stringNum.charAt(i);
        }

        answer *= Integer.parseInt(reverseNum);

        System.out.println(answer);
    }

    public static void main(String[] args) {
        // Test code
        solution(12345);
        solution(-12345);
        solution(100);
        solution(0);
    }
}
