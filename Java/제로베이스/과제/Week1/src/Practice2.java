
public class Practice2 {
    public static void solution(char alphabet) {
        int alphaNum = (int) alphabet;

        if (alphaNum >= 97 && alphaNum <= 122) {
            alphaNum -= 32;
        } else if (alphaNum >= 65 && alphaNum <= 90) {
            alphaNum += 32;
        } else {
            alphaNum = -1;
        }

        char answer = (char) alphaNum;

        if (alphaNum == -1) {
            System.out.println("알파벳이 아닙니다");
        } else {
            System.out.println(answer);
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
        solution('a');
        solution('b');
        solution('C');
        solution('D');
    }
}
