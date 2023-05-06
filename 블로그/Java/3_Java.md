# 3. Java 기초





## JShell 단축키

> #### JShell을 사용할 때에는 ';'를 사용하지 않아도 된다

- **ctrl + a** : 코드 제일 앞 부분으로 커서를 옮겨준다
- **ctrl + e** : 코드 제일 뒷 부분으로 커서를 옮겨준다
- **ctrl + r** : 코드 검색 기능





## if 문

> #### if문은 조건문 (condition)이다
>
> **=** : 값들을 계산해준다
>
> **==** :  비교해주는 operator이다
>
> - 즉 if문은 true or false를 출력해주는 것이다
> - 즉 = 이 아니라 ==을 사용하는게 맞다

```java
int i = 10;

if (i = 10)
    System.out.println("i is 10");
// Output : i is 10

int a = 10 ; int b = 7 ; int c = 8 ; int d = 17

if (a + b  > c + d)
	System.out.println("'a + b' is larger than 'c + d'");
// c+d가 더 크기 때문에 아무것도 출력이 안 된다


int number = 7
 if (number % 2 == 0) {
       System.out.println("The number is even number");
   } else {
       System.out.println("The number is odd number");
   }
// output : The number is odd number
```

- {} 를 사용하여, 추가적인 조건문을 넣을 수 있다
  - 자바는 **if문**, **else if문**, **else문**이 있다



```java
if (조건식1) {
    실행문 1;
} else if (조건식 2) {
    실행문 2; 
} else {
    실행문 3; 
}
```

- **실행문 1** : **조건식1**이 true일 때에 실행된다
- **실행문 2** : **조건식1**이 false, **조건식2**가 true일 때, 실행된다
- **실행문 3** : **조건식1**과 **조건식2**, 모두 false 일 때 실행된다





## 반복문

> #### 반복문을 만들 때에는 initialization, condition, update가 필요하다
>
> - initialization : 초기화식 (반복의 시작점)
> - condition : 조건식 (언제까지 반복하는지?)
>   - 조건식은 true or false이다
>   - 조건식이 true일 때에 반복문은 진행되고, false일 때에는 반복문이 끝난다
> - update : 증감식 (얼마만큼 증가하는가)

```java
for(initialization; condition; update)
    statement;
```



```java
int i;
for (i = 1 ; i <= 10 ; i ++) {
    System.out.printf("%d * %d = %d", 5, i, 5 * i).println();
}
// output
// 5 * 1 = 5
// 5 * 2 = 10
// 5 * 3 = 15
// 5 * 4 = 20
// 5 * 5 = 25
// 5 * 6 = 30
// 5 * 7 = 35
// 5 * 8 = 40
// 5 * 9 = 45
// 5 * 10 = 50
```

- **JavaScript 반복문이랑 똑같은 것 같다!**



```java
int i;
for (i = 1 ; i <= 10 ; i ++){
   if (i % 2 == 0) {                                                                                     			System.out.println(i * i);
   }
}

// 또는

for (i = 2; i <= 10 ; i = i + 2){
    System.out.printf("%d", i * i).println();
}
```

- 1번부터 10까지, 짝수 중에서, 제곱으로 곱하여 출력하기





