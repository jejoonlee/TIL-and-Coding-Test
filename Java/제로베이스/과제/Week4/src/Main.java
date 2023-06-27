// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
import java.util.*;
public class Main {
    public static void main(String[] args) {

        String[] string = {"C", "A", "a", "B", "b", "7", "제", "준", "기", "5", "9", "1"};
        Integer[] num = {3, 4, 8, 1, 2, 3};



        ArrayList<String> stringList = new ArrayList<String>();
        ArrayList<Integer> numList = new ArrayList<Integer>();

        for (String s: string) stringList.add(s);
        for (int n: num) numList.add(n);

        Arrays.sort(string);
        Arrays.sort(num);

        Collections.sort(stringList);
        Collections.sort(numList);

        System.out.println("=== 오름차순 정렬 ===");
        System.out.println("배열 (문자열) 정렬 : " + Arrays.toString(string));
        System.out.println("배열 (숫자) 정렬 : " + Arrays.toString(num));
        System.out.println("리스트 (문자열) 정렬 : " + stringList);
        System.out.println("리스트 (숫자) 정렬 : " + numList);

        Arrays.sort(string, Collections.reverseOrder());
        Arrays.sort(num, Collections.reverseOrder());

        Collections.sort(stringList, Collections.reverseOrder());
        Collections.sort(numList, Collections.reverseOrder());

        System.out.println();
        System.out.println("=== 내림차순 정렬 ===");
        System.out.println("배열 (문자열) 정렬 : " + Arrays.toString(string));
        System.out.println("배열 (숫자) 정렬 : " + Arrays.toString(num));
        System.out.println("리스트 (문자열) 정렬 : " + stringList);
        System.out.println("리스트 (숫자) 정렬 : " + numList);
    }
}