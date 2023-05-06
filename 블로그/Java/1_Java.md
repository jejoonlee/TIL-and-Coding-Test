# 1. Java 기초



## 데이터 출력하기

```java
System.out.println(출력할 데이터)
    
System.out.println(3 * 4)
// output : 12
// 숫자 출력
    
System.out.println(3.0 / 2)    
// output : 1.5
// float 출력
    
System.out.println("5 * 10 = 50")
// output : 5 * 10 = 50
// 문자열 출력
    
System.out.println("Hello \nWorld")
// output
// Hello
// World

System.out.println("Hello \tWorld")
// output : Hello	World
```

- **System.out.println()** 은, '출력할 데이터' 즉 expression 을 출력해주는 메서드다
- **System** : 자바의 클래스 중 하나다
- **out** : **System** 안에 속하는 변수 
- **println** : **out** 의 메서드
- 출력할 데이터 = parameter



#### System.out.printf().println()

> 포멧을 한 데이터를 출력한다

```java
// --------- 1 --------
System.out.printf("5 * 2 = 10").println()
// output : 5 * 2 = 10
    
// --------- 2 --------
System.out.printf("5 * 2 = 10 %d", 5 * 2).println()
// output : 5 * 2 = 10 10

// --------- 3 --------
System.out.printf("5 * 2 = %d", 5 * 2).println()
// output : 5 * 2 = 10

// --------- 4 --------
System.out.printf("%d %d %d", 5, 7, 3 * 5).println()
// output : 5 7 15

// --------- 5 --------
System.out.printf("%d * %d = %d", 5, 7, 3 * 5).println()
// output : 5 * 7 = 15

// --------- 6 --------
System.out.printf("%d + %d + %d = %d", 5, 6, 7, 5 + 6 + 7).println()
// output : 5 + 6 + 7 = 18
```



1. **System.out.printf("5 * 2 = 10").println()**
   - 기본적인 문자열을 출력하는 것이라서, 그대로 **5 * 2 = 10**을 출력한다

2. **System.out.printf("5 * 2 = 10 %d", 5 * 2).println()**

   - **%d**가 문자열 안에 있다

   - **%d** 가 들어오면, 뒤에 parameter를 가지고 와야 된다

   - 즉 출력을 할 때에는 **%d** 자리에 **5 * 2** 의 값이 들어간다

> 3번부터 6번까지도 모두 2번과 동일하게 **%d** 자리에는 뒤에 **parameter**에 넣은 값들이 출력이 된다



#### %d 는 숫자, int를 넣을 때 사용된다

#### %s 는 문자열, string을 parameter로 넣을 수 있다

#### %f 는 float를 parameter로 넣을 수 있다
























