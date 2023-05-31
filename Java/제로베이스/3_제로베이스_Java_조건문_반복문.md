# [제로베이스] Java 조건문, 반복

*출처 : 제로베이스 백엔드 스쿨*





## 조건문

> #### 조건에 따라 true or false 일 때에 특정 코드를 실행한다



#### if 문

```java
if (condition1) {
    condition1 이 true일 때 실행한다;
} else if (condition2) {
    condition1 이 false고, condition2가 true일 때에 실행한다;
} else {
    condition2와 condition1 모두 false일 때, 실행한다;
}
```



#### switch

> #### if문 보다는 읽고, 보기가 더 쉽다
>
> #### 특정 타입 (int, char, string)에만 사용이 가능하다
>
> - case 부분에 if문 처럼 조건문을 쓸 수 없고, 입력된 값만 보게 된다
> - 밑에 i 부분을 조건문처럼 사용을 해야 한다



```java
switch (i) {
    case 1 : System.out.println("Number 1"); break;
        // i 가 1 일 때에 Number 1을 출력하고, break
    case 2 : System.out.println("Number 2"); break;
        // i 가 2 일 때에 Number 2를 출력하고, break
    case 3 : System.out.println("Number 3"); break;
        // i 가 3 일 때에 Number 3 를 출력하고, break
    case 4 : System.out.println("Number 4"); break;
        // i 가 4 일 때에 Number 4 를 출력하고, break
    default : System.out.println("Number not included"); break;
        // i 가 1, 2, 3, 4가 아니면 Number not included를 출력하고, break
}
```





