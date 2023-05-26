public class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        answer[0] = -1;

        for (int i = 1; i < s.length(); i++) {
            int count = 0;

            for (int j = i - 1 ; i >= 0; i--) {
                if (s.charAt(i) == s.charAt(j)) {
                    count = i - j;
                    break;
                }
            }

            if (count == 0) {
                answer[i] = -1;
            } else {
                answer[i] = count;
            }
        }

        return answer;
    }
}
