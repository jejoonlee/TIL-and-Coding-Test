# [제로베이스] Java

*출처 : 제로베이스 백엔드 스쿨*





## Java란?

#### 자바는 선호도가 높은 프로그래밍 언어 중, 하나다

#### 객체 지향 프로그래밍 언어다

#### 다른 운영체제라도, 같은 코드를 사용해도 된다



<img src="https://blog.kakaocdn.net/dn/ATMXA/btsey6E8SZw/V8rukGM67PvIRSf5k4kI1k/img.webp" alt="img" style="zoom:67%;" />

- Java Compiler 는 Java 코드를 바이트 코드로 컴파일, 즉 반환해 준다
- 바이트 코드 (ByteCode) 는, 기계가 알아들을 수 있는 언어다
- JVM 은 Java Virtual Machine으로, 각 운영체제에 맞게, 바이트 코드를 반환해 주는 소프트웨어다





## 변수와 자료형

> #### 변수는 영어로 Variable

```java
int number = 77;
String name = "Alex";
```

#### **(자료형)  (변수 이름) = (값);**

- 변수 이름은 숫자로 시작하거나, 공백이 있을 수 없다
- 대소문자 모두 구분을 한다
- 주로 카멜 표기법을 사용한다 (예. firstNumber, secondNumber)
- 클래스를 표기할 때에는 파스칼 표기법을 사용한다 (예. AddNum, DivideNum)





### 자료형

- **숫자 (Number)** 

  - **정수** : int / long (int 와 long의 최댓값과 최솟값)
    - Integer 보다, 더 큰 값이 나오면, Long으로 자료형을 바꿔줘야 한다

  ![image-20230526142948428](1_제로베이스_Java.assets/image-20230526142948428.png)

  

  - **실수** : float / double (float 와 double의 최댓값과 최솟값)

  ![image-20230526143126528](1_제로베이스_Java.assets/image-20230526143126528.png)

  

  - **2, 8, 16 진수**
    - 0b 로 시작 / 0 으로 시작 / 0x 로 시작

  

- **부울 (Boolean)**

  - **boolean** : true 또는 false

- **문자 (Character)**

  - **char** : 한 개의 문자만 저장할 수 있음



