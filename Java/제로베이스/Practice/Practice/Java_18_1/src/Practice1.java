
public class Practice1 {
    public static void solution(int num) {
        boolean isMinus = false;
        int tempNum = 0;

        if (num < 0) {
            isMinus = true;
            num *= -1;
        }

        while (num > 0) {
            int reverse = num % 10;
            tempNum = tempNum * 10 + reverse;
            num /= 10;
        }

        if (isMinus) {
            System.out.println(tempNum * -1);
        } else {
            System.out.println(tempNum);
        }

    }

    public static void main(String[] args) {
        // Test code
        solution(12345);
        solution(-12345);
        solution(100);
        solution(0);
    }
}
