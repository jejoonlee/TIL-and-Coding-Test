import java.math.BigDecimal;
import java.util.HashSet;
import java.util.Scanner;

import java.util.ArrayList;

public class Practice {

    public ArrayList<Integer> getDivisor(int num) {
        ArrayList<Integer> result = new ArrayList<Integer>();

        for (int i = 1; i <= num; i ++) {
            if (num % i == 0) {
                result.add(i);
            }
        }
        return result;
    }

    public int getGCD(int numA, int numB) {
        ArrayList<Integer> list1 = getDivisor(numA);
        ArrayList<Integer> list2 = getDivisor(numB);

        int gcd = -1;

        for (int num1 : list1) {
            for (int num2 : list2) {
                if (num1 == num2 && num1 > gcd) {
                    gcd = num1;
                    break;
                }
            }
        }
        return gcd;
    }

    public int getLCM(int numA, int numB) {
        int lcm = -1;

        int gcd = this.getGCD(numA, numB);

        if (gcd != -1) {
            lcm = numA * numB / gcd;
        }

        return lcm;
    }
}
