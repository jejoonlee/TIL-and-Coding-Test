# 4. Java Method





## 메서드

> #### 메서드를 따로 만들어서 사용하기



#### 메서드 Syntax

```java
ReturnType nameOfTheMethod() {
    // Body of the method;
}
```



#### Hello World 두 번 출력하기

> **void**는 return 되는 타입이 없는 것이다

```java
void twoHelloWorld() {
    System.out.println("Hello World");
    System.out.println("hello World");
}

twoHelloWorld();
// Hello World
// hello World

// jshell에서 메서드를 확인하는 방법
/methods

/save backup.txt
// 메서드를 backup.txt에 저장하는 것
    
/edit twoHelloWorld
// 메서드를 수정하는 방법
```





## 인자와 매개변수



> #### 메서드를 실행할 때에 값을 같이 넣고 싶을 때 (argument를 넣고 싶을 때)
>
> - 즉 메서드를 만들 때에 parameter를 만들어야 한다
>
> - sayHelloWorld(4)
>   - "Hello World"를 4번 출력하는 것

```java
ReturnType nameOfTheMethod(Type argumentName) {
    // Body of the method;
}
```





```java
void sayHelloWorld(int num) {
    for (int i = 1; i < num ; i ++) {
        System.out.println("Hello World");
       }
}

sayHelloWorld(4)
// output
// Hello World
// Hello World
// Hello World
// Hello World
```





```java
void multiplicationTable(int number) {
    for (int i = 1 ; i <= 10 ; i ++) {
        System.out.printf("%d * %d = %d", number, i, number * i).println();
    }
}

multiplicationTable(7)
```

- 7의 구구단 테이블 (1~10) 을 출력해주는 메서드를 만들었다



### 메서드 오버로딩

> 같은 메서드 이름을 사용하되, 다른 파라미터를 가진 메서드다
>
> - 파라미터가 없는 메서드
> - 파라미터가 들어간 메서드

```java
void multiplicationTable(int number) {
    for (int i = 1 ; i <= 10 ; i ++) {
        System.out.printf("%d * %d = %d", number, i, number * i).println();
    }
}

void multiplicationTable() {
    for (int i = 1 ; i <= 10 ; i ++) {
        System.out.printf("%d * %d = %d", 5, i, 5 * i).println();
    }
}

multiplicationTable(7);
multiplicationTable();
```

- 첫번째 메서드는 7의 구구단 표를 출력할 것이다 
  - 여기서는 7 대신, 다른 숫자를 넣으면, 그 숫자의 구구단 표를 출력한다
- 두번째 메서드는 5의 구구단 표만 출력할 것이다



 ```java
 Math.max(1, 2);
 // 2개의 숫자를 argument로 보내면, 둘 중에 큰 숫자를 출력;
 ```







## Return value of Method

> #### 위와 같은 메서드들은 값을 출력하는 것이지, 반환하는 것이 아니다
>
> - 즉 메서드에서 나오는 값들을 변수에 저장할 수 없다
> - 변수에 메서드 값을 저장하려면, 에러가 뜬다
>
> #### 값을 return 하게 되면, 변수를 반환하며 메서드에서 나온 값을 변수에 저장하는 것이다



```java
int sumOfTwoNumbers(int firstNumber, int secondNumber) {
   int sum = firstNumber + secondNumber;
   return sum;
}

int plus = sumOfTwoNumbers(2, 4);
// plus == 6

int findAngle(int firstAngle, int secondAngle) {
   int angle = 180 - (firstAngle + secondAngle);
   return angle;
}

angle = findAngle(90, 60);
// angle ==> 30
```

