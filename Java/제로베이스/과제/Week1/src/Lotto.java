import java.util.HashSet;
import java.util.Scanner;
import java.util.*;
import java.util.Random;

public class Lotto {

    // 로또 생성
    public static ArrayList<Integer> LottoGenerator(){
        Random rand = new Random();

        HashSet<Integer> lottoResult = new HashSet<Integer>();

        while (lottoResult.size() != 6) {
            lottoResult.add(rand.nextInt(45) + 1);
        }

        // 출력을 위해 set을 리스트로 변환
        ArrayList<Integer> resultList = new ArrayList<Integer>(lottoResult);

        return resultList;
    }

    // 로또 출력
    public static void PrintLotto(ArrayList<Integer> resultList) {

        for (int i = 0; i < resultList.size(); i++) {
            System.out.printf("%02d", resultList.get(i));
            if (i == 5) {
                break;
            }
            System.out.printf(",");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random rand = new Random();

        System.out.println("[로또 당첨 프로그램]");

        // 로또 개수 입력
        System.out.print("로또 개수를 입력해 주세요. (숫자 1 ~ 10): ");

        int purchase = -1;
        boolean rightAct = true;

        while (true) {
            try {
                purchase = scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("입력 형태는 숫자여야 합니다");
                System.out.println("다시 실행하세요");
                rightAct = false;
                break;
            }

            if (0 < purchase && purchase <= 10) {
                break;
            }
            System.out.println("로또 개수는 1개부터 10개까지 입력이 가능합니다");
        }

        if (rightAct == true) {
            // 나중에 내가 산 로또와, 로또 결과를 바교하기 위해, 로또들을 리스트에 넣는다
            // 2차원 리스트가 만들어짐
            ArrayList myLotto = new ArrayList();

            // 개수 별로 1-45 사이, 6개의 숫자 입력 (중복 숫자 없음)
            for (int i = 0; i < purchase; i++) {
                ArrayList<Integer> lottoNumbers = LottoGenerator();

                myLotto.add(lottoNumbers);

                PrintLotto(lottoNumbers);
                System.out.println();
            }

            System.out.println();

            // 로또 발표 (랜덤 사용해서 1-45 사이, 6개 숫자 발표)
            // 로또 발표는 한번만 (중복되는 숫자가 있으면 안 됨)
            System.out.println("[로또 발표]");
            ArrayList<Integer> lottoResult = LottoGenerator();
            PrintLotto(lottoResult);
            System.out.println();
            System.out.println();

            // 입력한 로또 번호랑, 발표된 로또 비교
            for (int i = 0; i < myLotto.size(); i ++) {
                int count = 0;
                ArrayList<Integer> myCurLotto = (ArrayList<Integer>) myLotto.get(i);

                for (int num : myCurLotto) {
                    if (lottoResult.contains(num)) {
                        count += 1;
                    }
                }

                PrintLotto(myCurLotto);
                System.out.printf(" => %d개 일치", count);
                System.out.println();
            }
        }
    }
}
