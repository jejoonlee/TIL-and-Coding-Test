
public class Practice3 {
    public static String solution(char[] str, char[] find, char[] to) {

        String newString = "";

        int idx = 0;

        while (idx < str.length) {
            if (idx + find.length <= str.length && str[idx] == find[0]) {
                boolean isSame = true;
                for (int j = 0; j < find.length; j++) {
                    if (idx + j >= str.length || str[idx + j] != find[j]) {
                        isSame = false;
                        break;
                    }
                }
                idx += find.length - 1;

                if (isSame) {
                    for (int i = 0; i < to.length; i++) newString += to[i];
                }

            } else {
                newString += str[idx];
            }
            idx ++;
        }

        return newString;
    }

    public static void main(String[] args) {
        // Test code
        String str = "Hello Java, Nice to meet you! Java is fun!";

        String find = "Java";
        String to = "자바";

        // 기존 String replace
        System.out.println(str.replace(find, to));

        // 자체 구현 replace
        char[] strExArr = str.toCharArray();
        char[] findArr = find.toCharArray();
        char[] toArr = to.toCharArray();
        System.out.println(solution(strExArr, findArr, toArr));

        strExArr = "POP".toCharArray();
        findArr = "P".toCharArray();
        toArr = "W".toCharArray();
        System.out.println(solution(strExArr, findArr, toArr));
    }
}
