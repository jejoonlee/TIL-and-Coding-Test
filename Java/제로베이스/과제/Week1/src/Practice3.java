
public class Practice3 {
    public static String solution(char[] str, char[] find, char[] to) {
        String result = "";

        for (int i = 0; i < str.length; i ++) {

            if (str[i] == find[0]) {
                int start = i;
                int end = i;
                for (int j = 1; j < find.length; j ++) {
                    end += 1;
                    if (str[end] != find[j]) {
                        break;
                    }
                }

                if (end - start == find.length - 1) {
                    for (int k = 0; k < to.length; k ++) {
                        result += to[k];
                    }
                }

                i = end;
            } else {
                result += str[i];
            }
        }
        return result;
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
        System.out.println(strExArr);
        System.out.println(findArr);
        System.out.println(toArr);
        System.out.println(solution(strExArr, findArr, toArr));

        strExArr = "POP".toCharArray();
        findArr = "P".toCharArray();
        toArr = "W".toCharArray();
        System.out.println(solution(strExArr, findArr, toArr));
    }
}
