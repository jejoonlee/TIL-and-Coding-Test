
import java.util.*;
public class Main {
    public static void main(String[] args) {
        String bin1 = "1011010";
        String bin2 = "1101001";

        // 연산자를 사용하기 위해서 이진수를 십진수로 바꿔야 한다
        int num1 = Integer.parseInt(bin1, 2);
        int num2 = Integer.parseInt(bin2, 2);

        int num1AndNum2 = Integer.parseInt(String.valueOf(num1 & num2));
        int num1OrNum2 = Integer.parseInt(String.valueOf(num1 | num2));
        int num1XorNum2 = Integer.parseInt(String.valueOf(num1 ^ num2));


        // AND, OR, XOR 연산자를 활용해서 2진수 연산을 하며 십진수를 출력한다
        System.out.println(Integer.toBinaryString(num1AndNum2));
        System.out.println(Integer.toBinaryString(num1OrNum2));
        System.out.println(Integer.toBinaryString(num1XorNum2));


    }
}