
public class Fibo {
    public static int FiboRecur(int num) {
        if (num == 0) return 0;
        if (num < 2) return 1;
        return FiboRecur(num - 1) + FiboRecur(num -2);
    }

    public static int FiboOne(int num) {
        int[] fiboArray = new int[num + 1]; // dp 테이블
        if (fiboArray.length > 1) fiboArray[1] = 1;

        for(int i = 2; i <= num; i++) fiboArray[i] = fiboArray[i - 1] + fiboArray[i - 2];

        return fiboArray[num];
    }

    static int[] fiboDP= new int[1000];
    public static int FiboTwo(int num) {
        if (num == 0) return 0;
        if (num <= 2) return 1;

        if (fiboDP[num] != 0) {
            return fiboDP[num];
        }

        fiboDP[num] = FiboTwo(num - 1) + FiboTwo(num - 2);
        return fiboDP[num];
    }

    public static void main(String[] args) {
        System.out.println(FiboRecur(10));
        System.out.println(FiboOne(10));
        System.out.println(FiboTwo(10));
    }
}
