
import java.util.Scanner;
public class Practice2 {
    public static void solution() {
        Scanner scanner = new Scanner(System.in);
        char input = scanner.nextLine().charAt(0);

        if ((int) input >= 97 && (int) input <= 122) {
            int alp = (int) input - 32;
            System.out.println((char) alp);
        } else if ((int) input >= 65 && (int) input <= 90) {
            int alp = (int) input + 32;
            System.out.println((char) alp);
        } else {
            System.out.println("Not alphabet");
        }
    }

    public static void reference() {
        int a = (int)'a';
        System.out.println("a = " + a);
        int z = (int)'z';
        System.out.println("z = " + z);
        int A = (int)'A';
        System.out.println("A = " + A);
        int Z = (int)'Z';
        System.out.println("Z = " + Z);
        int etc = (int)'%';
        System.out.println("etc = " + etc);
    }

    public static void main(String[] args) {
        reference();    // 아스키 코드 참고
        solution();
    }
}
