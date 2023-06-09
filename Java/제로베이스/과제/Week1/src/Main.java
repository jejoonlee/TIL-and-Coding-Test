// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.

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