# 11. Java 조건문





## If Else

```java
if (i == 3) {
    System.out.println("True");
} else {
    System.out.println("i is not 3");
}
```

- i 가 3이면 True를 출력한다
  - if문이 true이기 때문에
- i 가 3이 아니면 'i is not 3' 를 출력
  - else 를 통해 3이 아닌 모든 조건은 'i is not 3'를 출력한다



```java
if (i == 25) {
    System.out.println("i is 25");
} else if (i == 24) {
    System.out.println("i is 24");
} else {
    System.out.println("i is neither 25 or 24");
}
```

- i 가 25 이면 **if (i == 25)** 에서 끝나고 "i is 25"가 출력된다
- i 가 24 이면 **else if (i == 24)** 에서 끝나고 "i is 24"가 출력된다
- i 가 24나 25가 아닐 때에는 else 문으로 넘어가 "i is neither 25 or 24" 가 출력된다





## User Input (입력 방법)

```java
import java.util.Scanner;

Scanner scanner = new Scanner(System.in);

System.out.print("Enter Number1: ");
int number1 = scanner.nextInt();

System.out.println("The number you entered is - " + number1);
```

- Scanner 클래스를 가지고 오고 scanner라는 객체를 만든다
  - scanner.nextInt() : Integer를 입력받을 수 있다







## Swith문

> #### 똑같은 조건문이다
>
> - if문 보다는 읽고, 보기가 더 쉽다
>
> #### 특정 타입에만 사용이 가능하다
>
> - int, char, string 

```java
switch (i) {
    case 1 : System.out.println("Number 1"); break;
    case 2 : System.out.println("Number 2"); break;
    case 3 : System.out.println("Number 3"); break;
    case 4 : System.out.println("Number 4"); break;
    default : System.out.println("Number not included"); break;
}
```



**case 1 : System.out.println("Number 1"); break;**

- **i** 가 **1** 일 때에 **System.out.println("Number 1")**을 실행하고, break를 한다
  - i가 1이 아니면 case 2 로 넘어감 (case 2는 i가 2인지 아닌지 확인하는 것)

**break가 없으면, 모든 case들이 실행이된다**
