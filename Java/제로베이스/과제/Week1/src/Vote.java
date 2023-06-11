import java.util.ArrayList;
import java.util.Scanner;
import java.util.regex.*;
import java.util.Random;

public class Vote {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random rand = new Random();

        System.out.print("총 진행할 투표수를 입력해 주세요. ");
        double numVote = scanner.nextInt();

        System.out.print("가상 선거를 진행할 후보자 인원을 입력해 주세요. ");
        int candidateNum = scanner.nextInt();

        ArrayList<String> candidateInfo = new ArrayList<String>();
        ArrayList<Double> candidateVote = new ArrayList<Double>();

        int num = 1;
        while (num <= candidateNum) {
            System.out.print(num + "번째 후보자 이름을 입력해 주세요. ");
            String candidateName = scanner.next();

            // 이름 관련해서, 한글이고, 10자 미만만 입력이 가능
            // if문이 true일 경우 후보 이름을 candidateInfo에, 후보가 받을 투표 수를 candidateVote에 넣는다
            // 즉 투표 수는, 처음이니깐 0을 넣으면 된다
            if (Pattern.matches("^[ㄱ-ㅎ가-힣]*$", candidateName) == true) {
                if ( 0 < candidateName.length()  && candidateName.length() < 10) {
                    candidateInfo.add(candidateName);
                    candidateVote.add(0.0);
                    num ++;
                }
            } else {
                System.out.println("후보자 이름은 한글이어야 하고, 8자 미만이어야 합니다.\n다시 입력해주세요.");
            }
        }

        System.out.println();

        int count = 0;

        do {
            for (double i = 1; i <= numVote; i++) {
                double voterPercen = (i / numVote) * 100;

                int randomVote = rand.nextInt(candidateInfo.size());

                String vote = candidateInfo.get(randomVote);

                System.out.println(String.format("[투표진행률]: %.2f%%, %.0f명 투표 => %s", voterPercen, i, vote));

                // 후보자의 이름이 있으면, 투표를 하고, 없으면, 다시 이름을 쓰도록 한다
                while (true) {
                    if (candidateInfo.contains(vote)) {
                        // 인덱스를 활용해서, 특정 후보자를 투표했을 때에 1을 더해준다 (.set()을 활용)
                        candidateVote.set(candidateInfo.indexOf(vote), candidateVote.get(candidateInfo.indexOf(vote)) + 1);
                        break;
                    } else {
                        String candidateList = "";

                        for (String name : candidateInfo) {
                            candidateList = candidateList + String.format("%s   ", name);
                        }

                        // 유저가 보기 좋도록, 후보 리스트를 출력
                        System.out.println("해당 후보는 없습니다. 다시 입력해주세요");
                        System.out.println("후보 리스트 : " + candidateList);
                        vote = scanner.next();
                    }
                }

                for (int j = 0; j < candidateInfo.size(); j++) {
                    String name = String.format("%s:", candidateInfo.get(j));
                    String canPercen = String.format("%.2f%%", candidateVote.get(j) / numVote * 100);
                    String voteNum = String.format("(투표수: %.0f)", candidateVote.get(j));

                    System.out.printf("[기호:%d] %-8s\t%-5s\t%10s", j + 1, name, canPercen, voteNum);
                    System.out.println();
                }

                System.out.println();
            }

            // 당선인 고르기
            double max_vote = 0.0;
            for (int i = 0; i < candidateVote.size(); i++) {
                if (candidateVote.get(i) > max_vote) {
                    max_vote = candidateVote.get(i);
                }
            }

            // 중복이 있는지 확인
            for (int i = 0; i < candidateVote.size(); i++) {
                if (max_vote == candidateVote.get(i)) {
                    count += 1;
                }
            }

            if (count != 1) {
                System.out.println("당선인이 2명 이상 뽑혀, 다시 투표를 진행합니다\n");
                count = 0;
                for (int k = 0 ; k < candidateVote.size(); k ++) {
                    candidateVote.set(k, 0.0);
                }
            } else {
                System.out.printf("[투표결과] 당선인 : %s", candidateInfo.get(candidateVote.indexOf(max_vote))).println();
            }

        } while (count != 1);
    }
}
