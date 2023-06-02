# [제로베이스] Java 추상 클래스, 인터페이스

*출처 : 제로베이스 백엔드 스쿨*





## 추상 클래스



### 추상 메서드

- 선언만 하고, 내용은 없다

```java
abstract void 추상메서드명();
```



### 추상 클래스

- 추상 메서드를 하나 이상 포함된 클래스
- 객체를 생성 못 한다

```java
abstract class 추상클래스명 {
    
    abstract void 추상메서드명();
}
```







## 인터페이스

#### 다중 상속처럼 사용할 수 있다

#### 상수와 추상 메서드로 이루어져 있다

```java
접근제어자 interface 인터페이스명 {
    public static final 타입 상수이름 = 값;
    public abstract 반환타입 메서드이름(매개변수);
}

class 클래스명 implements 인터페이스명 {
    
}

// 다중

class 클래스명 extends 추상클래스명 implements 인터페이스명 {
    
}
```



