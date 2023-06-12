# [TIL] Java (Scanner)

*출처 : 제로베이스 백엔드 스쿨*





## Scanner란?

> #### 파이썬을 공부하면서, 코드를 짤 때, 또는 문제를 풀 때에, 유저들이 값을 입력했다
>
> #### 파이썬에서는 간단하게 input() 메서드를 사용하면, 값을 입력 받을 수 있었다



#### java는 Scanner라는 클래스가 있다 (java.util 패키지 안에 있다)

- 파이썬과 달리, 자바에서는 입력값을 받을 때에, 무슨 자료형을 입력 받을지 코드에 명시를 해야 한다
- 즉 다른 입력값을 받게 된다면, 바로 에러가 뜨게 된다



```java
import java.util.Scanner;

public class Practice {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
    }
}
```

- import을 통해서 Scanner을 가져온다
- **Scanner scanner = new Scanner(System.in);**
  - Scanner 객체를 만들어 준다
  - 여기서 **System.in** 은 콘솔에서 유저들로부터 입력을 받기 위한 스트림이다



```java
import java.math.BigDecimal;
import java.util.Scanner;

public class Practice {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        byte b = scanner.nextByte();
        short sh = scanner.nextShort();
        int number = scanner.nextInt();
        long largeNumber = scanner.nextLong();

        float floatNum = scanner.nextFloat();
        double doubleNum = scanner.nextDouble();
        BigDecimal bigDecimal = scanner.nextBigDecimal();

        boolean isTrue = scanner.nextBoolean();

        String word = scanner.next(); // 공백 기준 한 단어만 입력 받는다
        String sentence = scanner.nextLine(); // 한 줄을 읽는다
        
    }
}
```

- 위와 같이, 자료형에 따라 입력값을 받을 수 있다
