// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("[입장권 계산]");
        // 나이 입력
        System.out.print("나이를 입력해 주세요. (숫자):");
        int age = scanner.nextInt();

        // 입장 시간 입력
        System.out.print("입장시간을 입력해 주세요. (숫자입력):");
        int entry = scanner.nextInt();

        // 국가유공자 여부
        System.out.print("국가유공자 여부를 입력해 주세요. (y/n):");
        String nation = scanner.next();


        // 복지카드 여부
        System.out.print("복지카드 여부를 입력해 주세요. (y/n):");
        String welfareCard = scanner.next();

        int cost = 10000;

        if (nation.equals("y") || welfareCard.equals("y")) {
            cost = 8000;
        }

        if (age < 13 || entry >= 17) {
            cost = 4000;
        }

        if (age < 3) {
            cost = 0;
        }

        System.out.println(String.format("입장료: %d", cost));
    }
}