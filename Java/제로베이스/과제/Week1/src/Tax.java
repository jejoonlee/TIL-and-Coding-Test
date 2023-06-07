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

        Double[] taxPercen = {0.06, 0.15, 0.24, 0.35, 0.38, 0.4, 0.42, 0.45};

        System.out.println("[과세금액 계산 프로그램]");
        System.out.print("연소득을 입력해 주세요. : ");
        double income = scanner.nextDouble();
        double cumulDeduc = income;

        // 세금 계산
        double taxCal = 0;

        // 나름, 등급을 나누었음
        int taxLevel = TaxLevel(income);

        // 누진공제 계산
        if (cumulDeduc <= 12000000) {
            cumulDeduc = 0;
        } else {
            cumulDeduc /= taxPercen[taxLevel];
        }

        System.out.println(cumulDeduc);

    }
}
