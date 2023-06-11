import java.util.ArrayList;
import java.util.Scanner;

public class Tax {
    public static int TaxLevel(double income) {
        int taxCount = 0;

        if (income <= 12000000) {
            taxCount = 0;
        } else if (income <= 46000000) {
            taxCount = 1;
        } else if (income <= 88000000) {
            taxCount = 2;
        } else if (income <= 150000000) {
            taxCount = 3;
        } else if (income <= 300000000) {
            taxCount = 4;
        } else if (income <= 500000000) {
            taxCount = 5;
        } else if (income <= 1000000000) {
            taxCount = 6;
        } else {
            taxCount = 7;
        }
        return taxCount;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] taxStandard = {12000000, 34000000, 42000000, 62000000, 150000000, 200000000, 500000000, 1000000000};
        Double[] taxPercen = {0.06, 0.15, 0.24, 0.35, 0.38, 0.4, 0.42, 0.45};
        int[] cumul = {0, 1080000, 5220000, 14900000, 19400000, 25400000, 35400000, 65400000};

        System.out.println("[과세금액 계산 프로그램]");
        System.out.print("연소득을 입력해 주세요. : ");
        int income = scanner.nextInt();
        int cumulDeduc = income;

        // 세금 계산
        int taxCal = 0;

        // 나름, 등급을 나누었음
        int taxLevel = TaxLevel(income);

        // 세율에 의한 세금
        if (income <= 12000000) {
            taxCal += income * taxPercen[0];
            System.out.printf("%12d * %4.0f%% = %15.0f", taxStandard[0], taxPercen[0] * 100, taxStandard[0] * taxPercen[0]).println();
        } else {
            for (int i = 0; i <= taxLevel; i ++) {
                if (income <= taxStandard[i]) {
                    taxCal += income * taxPercen[i];
                    System.out.printf("%12d * %4.0f%% = %15.0f", income, taxPercen[i] * 100, income * taxPercen[i]).println();
                    break;
                }
                System.out.printf("%12d * %4.0f%% = %15.0f", taxStandard[i], taxPercen[i] * 100, taxStandard[i] * taxPercen[i]).println();
                taxCal += taxStandard[i] * taxPercen[i];
                income -= taxStandard[i];
            }
        }

        // 누진공제 계산
        cumulDeduc *= taxPercen[taxLevel];
        cumulDeduc -= cumul[taxLevel];

        System.out.println();
        String taxTitle = "[세율에 의한 세금]:";
        String deducTitle = "[누진공제 계산에 의한 세금]:";
        System.out.printf("%-25s\t%d", taxTitle, taxCal).println();
        System.out.printf("%-23s\t%d", deducTitle, Math.round(cumulDeduc));

    }
}
