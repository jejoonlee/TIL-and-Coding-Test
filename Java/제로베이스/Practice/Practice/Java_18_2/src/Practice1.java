import java.util.HashMap;

public class Practice1 {
    public static void solution(String s) {
        char[] rome =  {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
        int[] num = {1, 5, 10, 50, 100, 500, 1000};

        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < rome.length; i++) map.put(rome[i], num[i]);

        int i = 0;
        int result = 0;

        while (i < s.length()) {

            boolean combined = false;

            if (i + 1 < s.length() && s.charAt(i) == 'I') {
                if (s.charAt(i + 1) == 'V') {
                    result += 4;
                    i ++;
                    combined = true;
                } else if (s.charAt(i + 1) == 'X') {
                    result += 9;
                    i ++;
                    combined = true;
                }
            } else if (i + 1 < s.length() && s.charAt(i) == 'X') {
                if (s.charAt(i + 1) == 'L') {
                    result += 40;
                    i ++;
                    combined = true;
                } else if (s.charAt(i + 1) == 'C') {
                    result += 90;
                    i ++;
                    combined = true;
                }
            } else if (i + 1 < s.length() && s.charAt(i) == 'C') {
                if (s.charAt(i + 1) == 'D') {
                    result += 400;
                    i ++;
                    combined = true;
                } else if (s.charAt(i + 1) == 'M') {
                    result += 900;
                    i ++;
                    combined = true;
                }
            }

            if (!combined) {
                result += map.get(s.charAt(i));
            }

            i++;
        }

        System.out.println(result);
    }

    public static void main(String[] args) {
        // Test code
        solution("III");
        solution("IV");
        solution("VI");
        solution("XIII");
        solution("XXVI");
        solution("MCMXCIV");
    }
}
