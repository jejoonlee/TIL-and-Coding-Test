public class PracticeMath {

    private int[] num = {};
    public PracticeMath(int... value) {
        this.num = value;
    }

    public int sum() {
        int answer = 0;
        for (int value : this.num) {
            answer += value;
        }
        return answer;
    }
}
