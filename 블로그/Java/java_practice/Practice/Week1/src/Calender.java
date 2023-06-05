import java.util.Scanner;
import java.time.*;

public class Calender {

    public static void printDate(String[] week, int startDay, int lastDate) {
        for (int date = 1 ; date <= lastDate ; date ++) {
            week[startDay % 7] = String.format("%02d", date);

            if (startDay % 7 == 6) {
                for (String d: week) {
                    System.out.print(d + "\t");
                }
                System.out.println();
            }
            startDay += 1;
        }

        // 마지막 주 출력하기
        for (String d: week) {
            if (d.equals(String.format("%d", lastDate))) {
                System.out.print(d + "\t");
                break;
            }
            System.out.print(d + "\t");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("[달력 출력 프로그램]");

        // 년도 입력
        System.out.print("달력의 년도를 입력해 주세요. (yyyy):");
        int year = scanner.nextInt();

        // 월 입력
        System.out.print("달력의 월을 입력해 주세요. (mm):");
        int month = scanner.nextInt();


        if (0 < month && month <= 12) {
            LocalDate inputDate = LocalDate.of(year, month, 1);
            DayOfWeek dayOfWeek = inputDate.getDayOfWeek();

            int startDay = dayOfWeek.getValue();
            int lastDate = inputDate.lengthOfMonth();

            // 달력
            String calenderTitle = String.format("%d년 %d월", year, month);

            System.out.println(String.format("[%s]", calenderTitle));
            System.out.println("일\t월\t화\t수\t목\t금\t토");

            String[] week = {"", "", "",  "",  "", "",  ""};

            printDate(week, startDay, lastDate);


        } else {
            System.out.println("입력을 제대로 해주세요");
        }

    }
}
