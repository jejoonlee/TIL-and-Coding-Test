// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        System.out.println("------ Integer --------------");
        System.out.println(Integer.MAX_VALUE);
        System.out.println(Integer.MIN_VALUE);

        int num1 = Integer.MAX_VALUE;
        System.out.printf("Integer.MAX_VALUE + 2 = %d", num1 + 2).println();

        System.out.println("------ Long --------------");
        long longNum = (long) Integer.MAX_VALUE + 10;
        System.out.println("long으로 변환하기");

        // 2, 8, 16 진수
        int numBase2 = 0b1100;
        int numBase8 = 014;
        int numBase16 = 0xC;
        // 모두 12를 반환한다

        // 2, 8, 16 진수로 반환하기
        System.out.println("0b" + Integer.toBinaryString(numBase2));
        System.out.println("0" + Integer.toOctalString(numBase8));
        System.out.println("0x" + Integer.toHexString(numBase16));
    }
}