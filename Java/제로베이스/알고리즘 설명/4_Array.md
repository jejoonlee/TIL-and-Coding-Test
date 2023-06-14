# [Java] Array





## 배열 (Array)

![objects-tenElementArray](4_Array.assets/objects-tenElementArray.gif)



#### 여러 개의 동일한 자료형의 데이터를 연속된 공간에 저장하는 자료구조다

#### 각 데이터는 인덱스 번호와 매핑이 되어 있다

- 인덱스는 0부터 시작하여, 1씩 증가한다
- 인덱스로 통해 데이터에 접근이 빠르게 가능하다

#### 배열은 데이터를 추가/ 삭제가 어렵고, 애초에 처음 만들 때에 최대 크기를 고정으로 만든다

- 추가/ 삭제 하기 위해서는, 새로운 배열을 만들어야 한다



#### 배열 길이 : 5

|  인덱스   |  0   |  1   |  2   |  3   |  4   |
| :-------: | :--: | :--: | :--: | :--: | :--: |
| 데이터 값 |  7   |  8   |  9   |  10  |  11  |



#### 배열 길이를 설정하고, 안에 있는 값들을 0에서, 원하는 값으로 바꾼다

- [0, 0, 0, 0, 0] => [7, 8, 9, 10, 11]

```java
import java.util.Arrays;

public class MakeArray {
	public static void main(String[] args) {
        int[] numbers = new int[5];
        numbers[0] = 7;
        numbers[1] = 8;
        numbers[2] = 9;
        numbers[3] = 10;
        numbers[4] = 11;
        
        System.out.println(Arrays.toString(numbers));
        // output : [7, 8, 9, 10, 11]
	}
}
```



#### 처음부터 객체를 만들 때에, 배열 안에 값을 넣는다

```java
import java.util.Arrays;

public class MakeArray {
	public static void main(String[] args) {
        int[] numbers = {7, 8, 9, 10, 11};
        
        System.out.println(Arrays.toString(numbers));
        // output : [7, 8, 9, 10, 11]
	}
}
```

