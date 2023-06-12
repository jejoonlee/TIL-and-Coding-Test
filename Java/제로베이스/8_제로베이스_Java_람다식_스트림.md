# [제로베이스] Java 람다식, 스트림

*출처 : 제로베이스 백엔드 스쿨*





## 람다식

#### 메서드를 만드는 것보단, 식으로 표현을 한다

- 단 익명 함수라서, 일회성이다



```java
(매개변수, ...) -> {실행문 ...}

(int i, int j) -> {return i * j}
// i와 j를 곱한 값을 반환한다

// 예시
interface Calculate {
    public abstract int number(int i, int j);
}

public class Main {
    public static void main(String[] args) {
        
        Calculate cal = (i, y) -> {i * j};
        
       	System.out.println(cal.number(5 * 7));
    }
}

// output : 35
```





## 스트림

#### 배열, 컬렉션 등 자료형을 순회하는 것이다 (for문을 간결하게 만들 수 있다)

#### Stream 생성 / 중개 연산 / 최종 연산



```java
// ====== 배열 스트림 =======
int[] arr = new int[]{1, 2, 3};
Stream stream = Arrays.stream(arr);

// ====== 컬렉션 스트림 =====
ArrayList list = new ArrayList(Arrays.asList(1, 2, 3));
Stream stream = list.stream();
```



### Filtering

- 참, 거짓에 따라 결과 값을 추출

```java
IntStream intStream = IntStream.range(1, 10).filter(n -> n % 2 == 0);
// 1이상 10미만인 숫자들 중 짝수 값을 추출하는 것
```



### Mapping

- 특정 숫자들, 값들을 순회하면서, 결과 값을 추출하는 것

```java
IntStream intStream = IntStream.range(1, 10).map(n -> n * 2);
// 1이상 10미만의 숫자들에 2를 곱해서 값을 추출하는 것
```



### Min, Max, Average

- 최소, 최대, 평균도 구할 수 있다



### 그 외

```java
import java.util.Arrays;
import java.util.stream.*;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        ArrayList arrayList = new ArrayList(Arrays.asList(1, 2, 3, 4, 5));

        Stream stream = arrayList.stream();

        // forEach를 사용하여, 리스트 안에 있는 원소 출력
        // stream.forEach(System.out::println); -> 사용 가능
        stream.forEach(num -> System.out.println(num));

        // builder 사용하기 - stream을 만든다
        Stream streamBuilder = Stream.builder().add(1).add(2).add(3).build();
        streamBuilder.forEach(num1 -> System.out.println(num1));

        // generate 사용하기
        // abc가 3번 반복해서 출력이 된다
        Stream streamg = Stream.generate(() -> "abc").limit(3);
        streamg.forEach(System.out::println);

        // iterate
        // 1번 parameter : 초기값
        // 2번 paramater : 초기값에 대해 어떤 기능을 수행하고 싶은지 (연산자)
        // 즉 10으로 시작해서 곱하기 2를 누적시켜주는 것이다
        // 10 -> 20 -> 40 -> 80 -> 160
        Stream streamIterate = Stream.iterate(10, n -> n * 2).limit(5);
        streamIterate.forEach(System.out::println);

        // Sorting (오름차순으로 정렬을 해준다)
        IntStream intStream = IntStream.builder().add(4).add(3).add(7).add(5).build();
        IntStream sortedStream = intStream.sorted();
        sortedStream.forEach(System.out::println);
    }
}
```
