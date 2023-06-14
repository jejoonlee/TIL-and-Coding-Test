import java.util.ArrayList;

public class Recurrence {
    static int threeMultiply(int num) {
        if (num == 1) {
            return 1;
        }

        return threeMultiply(num - 1) * 3;
    }

    static int nSum(int num){
        if (num == 1) {
            return 1;
        }
        return num + nSum(num - 1);
    }

    static int fibo(int num) {
        if (num <= 2) {
            return 1;
        }

        return fibo(num - 1) + fibo(num - 2);
    }

    static int factorial(int num) {
        if (num == 1) {
            return 1;
        }
        return num * factorial(num - 1);
    }

    static int gcd(int num1, int num2) {
        if (num1 % num2 == 0) {
            return num2;
        }
        return gcd(num2, num1 % num2);
    }

    static ArrayList<ArrayList<Integer>> pascal(int num) {
        ArrayList<ArrayList<Integer>> pascalTriangle = new ArrayList<>();

        for (int i = 0; i < num; i ++) {
            ArrayList<Integer> newList = new ArrayList<Integer> ();

            for (int j = 0; j < i + 1 ; j ++) {
                if (j == 0 || j == i) {
                    newList.add(1);
                } else {
                    ArrayList<Integer> tempList = pascalTriangle.get(i - 1);

                    newList.add(tempList.get(j - 1) + tempList.get(j));
                }

            }
            pascalTriangle.add(newList);
        }

        return pascalTriangle;
    }
    public static void main(String[] args) {
        System.out.println(pascal(4));
        System.out.println(pascal(5));
        System.out.println(pascal(6));
        System.out.println(pascal(7));

    }
}