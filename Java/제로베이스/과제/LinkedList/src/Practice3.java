import java.util.Arrays;
import java.util.LinkedList;
public class Practice3 {
    public static void main(String[] args) {

        // 연결 리스트 객체 만들기
        LinkedList <Integer> linkedList = new LinkedList<Integer>();

        //======= 값 추가하기 =======
        linkedList.addFirst(1); // 리스트 제일 앞에 값을 추가
        linkedList.addLast(5); // 리스트 제일 뒤에 값을 추가
        linkedList.add(3); // 리스트 제일 앞에 데이터 추가
        linkedList.add(2,7); // 2번째 인덱스에 데이터 추가

        //======= 삭제하기 =======
        linkedList.removeFirst(); // 리스트 제일 앞의 데이터 삭제
        linkedList.removeLast(); // 리스트 제일 뒤의 데이터 삭제
        linkedList.remove(1); // 리스트의 인데스 1번째 데이터 삭제
        linkedList.remove(); // 리스트의 인덱스 0번째 데이터 삭제
        linkedList.clear(); // 리스트에 들어 있는 모든 값을 삭제

        //======= 리스트 크기 구하고, 값 출력 =======
        LinkedList<Integer> list = new LinkedList<Integer>(Arrays.asList(1, 2, 3, 4));

        list.size(); // 리스트 크기 구하기
        list.get(3); // 리스트의 인덱스 3번째 값 반환하기

        for (Integer num : list) {
            System.out.print(num + " ");
        }                               // 리스트에 있는 모든 데이터 출력하기
        System.out.println();

        //======= 리스트 값 검색 =======
        list.contains(1); // 리스트 안에 1이라는 값이 있는지 확인 (true or false 반환)
        list.indexOf(4); // 4가 있는 인덱스를 반환 (데이터가 없으면 -1을 반환)
    }
}
