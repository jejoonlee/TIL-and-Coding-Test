import java.util.Scanner;
import java.util.Random;
public class RegistrationNumber {

    public static int genderNumber(String gender, int year) {
        if (gender.equals("m") || gender.equals("M")) {
            if (year <= 1899) {
                return 9;
            } else if (year <= 1999) {
                return 1;
            } else {
                return 3;
            }
        } else if (gender.equals("f") || gender.equals("F")) {
            if (year <= 1899) {
                return 0;
            } else if (year <= 1999) {
                return 2;
            } else {
                return 4;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random rand = new Random();

        // 제목
        System.out.println("[주민등록번호 계산]");

        // 출생년도
        System.out.print("출생년도를 입력해 주세요. (yyyy):");
        int year = scanner.nextInt();

        // 출생월
        System.out.print("출생월을 입력해 주세요. (mm):");
        int month = scanner.nextInt();

        // 출생일
        System.out.print("출생일을 입력해 주세요. (dd):");
        int day = scanner.nextInt();

        // 성별
        System.out.print("성별을 입력해 주세요. (m/f):");
        String gender = scanner.next();

        int genderNum = genderNumber(gender, year);

        if (genderNum == -1) {
            System.out.println("정보를 제대로 입력을 안 했습니다");
        } else {
            // 주민등록번호 앞자리 6부분
            String firstPart = String.format("%02d%02d%02d", year % 100, month, day);

            // nextInt(999999) 의 범위는 0이상 999999 미만
            // 1이상 1000000 미만을 하려면 1을 더해주면 된다
            int randomNumber = rand.nextInt(999999) + 1;
            String secondPart = String.format("%d%06d", genderNum, randomNumber);

            System.out.println(firstPart + "-" +secondPart);
        }
    }
}
