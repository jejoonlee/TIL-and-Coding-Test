# 12. Java 반복문



## For 반복문

> #### javascript for문의 구조와 같다

```java
for (int i = 0; i <= 10 ; i++) {
    System.out.print(i + " ");
}

// output : 0 1 2 3 4 5 6 7 8 9 10
```

**(int i = 0; i <= 10 ; i++)**

- **int i = 0** : 시작 점
- **i <= 10** : i가 10과 같거나 이하일때까지 반복을 하는 것
- **i++** : i를 1씩 더해주면서 반복한다



#### 즉 i 는 0부터 시작해서, 1씩 더해주면서 10이 될때까지 반복한다



### 연습

- 숫자가 소수인지 아닌지 = isPrime()
- 입력된 숫자까지의 덧샘 = sumUpTo()
- 1과 자기 자신 빼고, 나눠 떨어지는 숫자들의 덧샘 구하기 = sumOfDivisors()
- 세모를 만들기, 2중 for문 사용하기 = printANumberTriangle()

```java
public class MyNumber {
	private int number;
	
	MyNumber (int num) {
		this.number = num;
	}
	
	public boolean isPrime() {
		for (int i = 2; i <= (this.number + 1) / 2; i++) {
			if (this.number % i == 0) {
				return false;
			}
		}
		return true;
	}
	
	public int sumUptoN() {
		int ans = 0;
		
		for (int i = 1; i <= this.number; i ++) {
			ans += i;
		}
		
		return ans;
	}
	
	public int sumOfDivisors() {
		int answer = 0;
		for (int i = 2; i <= (this.number + 1) / 2; i ++) {
			if (this.number % i == 0) {
				
				if (i == this.number/i) {
					answer += i;
				} else {
					answer += (i + (this.number / i));
				}
			}
		}
		return answer;
	}
	
	public void printANumberTriangle() {
		for (int i = 1; i <= this.number; i ++) {
			for (int j = 1 ; j <= i ; j ++) {
				System.out.print(j + " ");
			}
			System.out.println();
		}
	}
	
}
```









## While 반복문

#### while 반복문의 구조

- while문은 while문이 끝나는 조건을 넣어야 한다 (**밑에는 i가 i 미만일때만 반복하는 것이다**)
  - if문과 같은데, while문은 조건이 맞으면 계속 진행이 된다
  - 즉, 조건이 계속 맞으면 무한 루프에 빠지게 된다
    - **i ++** 가 없다면, i는 2보다 계속 작기 때문에, 무한 루프에 빠진다

```java
int i = 0;
while (i < 2) {
    i ++;
}
```





### 연습

```java
public class WhileNumberPlayer {

	private int number;
	
	WhileNumberPlayer (int num) {
		this.number = num;
	}
	
	public void printANumberTriangle() {
		int i = 1;
		
		while (i * i <= this.number) {
			System.out.print((i * i) + " ");
			i ++;
		}
		System.out.println();
	}
	
	public void printCubesUptoLimit() {
		int i = 1;
		
		while (i * i * i <= this.number) {
			System.out.print((i * i * i) + " ");
			i ++;
		}
		System.out.println();
	}
}
```









## Do While 반복문

> #### 구조는 while과 매우 비슷하다



#### Do While

- while문이 끝나는 조건이 아래에 가 있다
- 먼저 **System.out.print(i + " ");**와 **i ++;** 를 진행하고, **i 가 5보다 작은지** 확인해라
- 즉 **do while**은 while의 끝나는 조건이 만족이 되더라도, 한번은 실행하고 멈춘다

```java
int i = 1
do {
    System.out.print(i + " ");
    i ++;
} while (i < 5);


i = 10;

while (i < 5) {
    System.out.print(i + " ");
    i ++;
}

// output : 없음

do {
    System.out.print(i + " ");
    i ++;
} while (i < 5);

// output : 10
```





### 연습

- -1 을 입력할 때까지 입력한 값을 세제곱해서 출력해주는 것이다

```java
public class DoWhileExercise {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int inputValue;
		
		do {
			System.out.print("Enter a number: ");
			inputValue = scanner.nextInt();
			if (inputValue != -1) {
				System.out.println("Cube is " + (inputValue * inputValue * inputValue));
			} else {
				System.out.println("Thank You! Have Fun!");
			}
		} while (inputValue != -1);

	}

}
```







## Break & Continue

### Break

- 중간에 특정 조건을 만족하면 강제로 반복문을 빠져 나가는 것이다

```java
for (int i = 1; i <= 10; i++) {
    if (i == 5)
        break;
    System.out.print(i + " ")
}
// output : 1 2 3 4

// i 가 5가 되면 for문을 빠져 나온다
```



### Continue

- 해당 조건에 대해는 무시한다

```java
for (int i = 1; i <= 10; i++) {
    if (i % 2 == 0)
        continue;
    System.out.print(i + " ")
}

// output : 1 3 5 7 9

// i 가 짝수일 때는 무시하고 다음 차례로 간다
```

