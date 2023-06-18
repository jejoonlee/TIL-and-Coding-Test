# [제로베이스] Java 자료구조 - 연결리스트

*출처 : 제로베이스 백엔드 스쿨*





## 연결리스트 (Linked List)

#### 각 노드에 데이터와, 포인터가 있고, 노드끼리 연결되어 있는 것을 연결리스트라고 한다

- 여기서 포인터는, 이전 노드 또는 다음 노드와의 연결을 담당한다



![image-20230615072145420](16_제로베이스_Java_자료구조_연결리스트.assets/image-20230615072145420.png)

#### 제일 처음에 있는 노드를 Head라고 한다

- 제일 마지막 노드의 포인터는 NULL과 연결이 되어 있다



#### 데이터 추가/삭제는 비교적 쉽게 실행되지만, 인덱스가 없다는 점에서, 데이터를 찾으려면 Head부분부터 순회를 해야 한다 (탐색 속도 저하)





### 연결 리스트 종류

<img src="16_제로베이스_Java_자료구조_연결리스트.assets/Singly-Linked-List1.png" alt="Singly-Linked-List1" style="zoom:50%;" />

- **단일 연결 리스트 (Single Linked List)**
  - 노드에 다음 노드가 참조된 제일 간단한 형태의 연결 리스트다
  - 일반적으로 큐를 구현할 때에 사용이 된다
  - Head가 제일 중요하여, Head를 잃어버린다면, 데이터 전체를 사용을 못 한다



<img src="16_제로베이스_Java_자료구조_연결리스트.assets/Doubly-Linked-List.png" alt="Doubly-Linked-List" style="zoom:50%;" />

- **이중 연결 리스트 (Double Linked List)**
  - 노드끼리 양방향으로 연결이 되어 있다
  - 특히 이전 노드와 다음 노드를 참조 하고 있는 것이 이중 연결 리스트의 특징이다
  - 이중으로 연결되어 있어, 삭제할 때에는 데이터 손상이 덜 하지만, 추가 또는 정렬을 할 때에는 더 많은 작업량이 소모된다





<img src="16_제로베이스_Java_자료구조_연결리스트.assets/Circular-Linked-List.png" alt="Circular-Linked-List" style="zoom:50%;" />

- **원형 연결 리스트 (Circular Linked List)**
  - 제일 끝의 노드와 제일 앞의 노드가 연결되어 있다는 것이 특징이다





## 연결 리스트 기본 연산



#### 제일 앞에 데이터 추가

<img src="16_제로베이스_Java_자료구조_연결리스트.assets/image-20230615080755786.png" alt="image-20230615080755786" style="zoom:50%;" />





#### 제일 뒤에 데이터 추가

<img src="16_제로베이스_Java_자료구조_연결리스트.assets/image-20230615081148993.png" alt="image-20230615081148993" style="zoom:50%;" />





#### 노드와 노드 사이에 데이터를 추가하기

<img src="16_제로베이스_Java_자료구조_연결리스트.assets/image-20230615090011115.png" alt="image-20230615090011115" style="zoom:50%;" />





#### 첫 노드 삭제하기

<img src="16_제로베이스_Java_자료구조_연결리스트.assets/image-20230615091240851.png" alt="image-20230615091240851" style="zoom:50%;" />





#### 마지막 노드 삭제하기

<img src="16_제로베이스_Java_자료구조_연결리스트.assets/image-20230615091222727.png" alt="image-20230615091222727" style="zoom:50%;" />





#### 노드 사이에 있는 노드 삭제하기

<img src="16_제로베이스_Java_자료구조_연결리스트.assets/image-20230615092156050.png" alt="image-20230615092156050" style="zoom:50%;" />







#### 이중 연결 리스트는, 현재 데이터 앞에 연결되어 있는 데이터 정보와, 뒤에 연결되어 있는 데이터 정보가 노드에 들어가 있다

- 그런 이유로, 데이터를 추가, 삭제를 하기 위해서는 이전 데이터 정보에 대해서 추가적으로 코드를 짜야 한다





## 연결리스트 사용하기

#### java.util 에 LinkedList 클래스를 사용하여 연결리스트를 사용한다



#### LinkedList를 선언할 때에, 타입도 선언할 수 있다

- <> 를 활용하여 Class, Integer, String , Character 등, 선언이 가능하다 



```java
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
```



