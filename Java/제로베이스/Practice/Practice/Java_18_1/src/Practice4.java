import java.util.Arrays;

public class Practice4 {
    public static void solution(int n, int type) {
        if (type == 1) {
            System.out.println("== Type1 ==");
            type1(n);
        } else if (type == 2) {
            System.out.println("== Type2 ==");
            type2(n);
        } else if (type == 3) {
            System.out.println("== Type3 ==");
            type3(n);
        } else if (type == 4) {
            System.out.println("== Type4 ==");
            type4(n);
        } else if (type == 5) {
            System.out.println("== Type5 ==");
            type5(n);
        } else {
            System.out.println("해당 타입은 없습니다");
        }
    }

    public static void type1(int n) {
        String star = "";
        for (int i = 0 ; i < n ; i ++) star += "*";
        for (int i = 0 ; i < n ; i ++) {
            System.out.println(star);
        }

        System.out.println();
    }

    public static void type2(int n) {

        for (int i = 1 ; i <= n ; i ++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        System.out.println();
    }

    public static void type3(int n) {

        for (int i = 0; i < n ; i ++) {
            for (int j = 0; j < n ; j ++) {
                if (j < n - i - 1) {
                    System.out.print(" ");
                }else {
                    System.out.print("*");
                }
            }
            System.out.println();
        }

        System.out.println();
    }

    public static void type4(int n) {

        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < n - i - 1 ; j ++) {
                System.out.print(" ");
            }

            for (int j = 0; j < i * 2 + 1; j++) {
                System.out.print("*");
            }

            System.out.println();
        }

        System.out.println();
    }

    public static void type5(int n) {

        int firstHalf = n / 2 + 1;
        for (int i = 0; i < firstHalf; i ++) {
            for (int j = 0; j < firstHalf - i - 1 ; j ++) {
                System.out.print(" ");
            }

            for (int j = 0; j < i * 2 + 1; j++) {
                System.out.print("*");
            }

            System.out.println();
        }

        int tempN = n;
        int count = 1;
        for (int i = firstHalf; i < n; i++) {
            tempN -= 2;

            for (int j = 0; j < count; j ++) {
                System.out.print(" ");
            }
            count += 1;

            for (int j = 0; j < tempN; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        System.out.println();
    }

    public static void main(String[] args) {
        // Test code
        solution(3, 1);
        solution(3, 2);
        solution(3, 3);
        solution(3, 4);
        solution(7, 5);
    }
}
