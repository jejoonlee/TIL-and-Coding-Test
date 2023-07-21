import java.util.*;

public class test {
    static int[] arrA;
    static int[] arrB;
    static List<Integer> list = new ArrayList<>();
    public static void main(String[] args) {
        int[] a = {1};
        int[] b = {9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9};
        arrA = a.clone();
        arrB = b.clone();

        soltuion(a.length - 1, b.length - 1);

        int[] answer = new int[list.size()];
        int index = list.size() - 1;
        for (int i = 0 ; i < answer.length; i++) {
            answer[i] = list.get(index--);
        }
        System.out.println(answer);
    }

    private static void soltuion(int aIdx ,int bIdx) {
        // 한쪽만 종료된 경우 1
        if (aIdx < 0 && bIdx >= 0) {
            // 한쪽이 10이 넘는 경우가 있음 그러면 자릿 수 올리기 또는 그냥 나눈 값 넣기
            if (arrB[bIdx] >= 10) {
                list.add(arrB[bIdx] % 10);
                if (bIdx - 1 >= 0) {
                    arrB[bIdx - 1] +=1;
                }else {
                    list.add(arrB[bIdx] / 10);
                }
            } else {
                list.add(arrB[bIdx]);
            }
            soltuion(aIdx,--bIdx);
            return;
        }
        // 한쪽만 종료된 경우 2
        else if (aIdx >= 0 && bIdx < 0) {
            if (arrA[aIdx] >= 10) {
                list.add(arrA[aIdx] % 10);
                if (aIdx - 1 >= 0) {
                    arrA[aIdx - 1] += 1;
                } else {
                    list.add(arrA[aIdx] / 10);
                }
            } else {
                list.add(arrA[aIdx]);
            }
            soltuion(--aIdx,bIdx);
            return;
        } else if (aIdx < 0 && bIdx < 0) { // 둘다 0 이하인 경우
            return;
        }

        // 두 개의 index가 0이상인 경우 아래의 재귀를 수행
        if (arrA[aIdx] + arrB[bIdx] >= 10) {
            list.add((arrA[aIdx] + arrB[bIdx]) % 10);

            if (aIdx - 1 >= 0) {
                arrA[aIdx - 1] += 1;
            } else if (bIdx - 1 >= 0) {
                arrB[bIdx - 1] += 1;
            }else if (aIdx == 0 || bIdx == 0) list.add(1);
        } else {
            list.add(arrA[aIdx] + arrB[bIdx]);
        }

        soltuion(--aIdx, --bIdx);
    }
}