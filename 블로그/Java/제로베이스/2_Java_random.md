# [TIL] Java (random number)

*출처 : 제로베이스 백엔드 스쿨*



## Math.random()

```java
double num = Math.random();

System.out.println(num);
// output : 0.2868302445390779

System.out.println(String.format("%6.0f", num * 1000000));
// output : 286830
```

- 무작위 숫자를 출력해준다
- 여기서 Math.random() 은 double 형태의 자료형 밖에 안 된다
  - 즉 int 를 자료형으로 선택했을 때는 에러가 발생한다
  - 0.0 이상, 1.0 미만의 double 숫자를 가지고 와준다
- String.format() 을 통해서, 어느 정도 정수의 값을 가지고 올 수 있다





## Random

```java
import java.util.Random;

Random rand = new Random();

System.out.println(rand.nextInt(100000));
```

- **.nextInt(100)** : 0 이상, 100 미만의 숫자를 랜덤으로 출력해준다

- **nextBoolean()** : Boolean 형 난수를 반환해준다

- **nextLong()** : long 형 난수를 반환해준다

- **nextFloat()** : 0.0 이상 0.1 미만의 float형 난수를 반환해준다

- **nextDouble()** : 0.0 이상 0.1 미만의 double형 난수를 반환해준다

  

