# 6. Java Eclipse





## Eclipse

> #### 자바의 IDE이다



#### 구구단 클래스 만들기

```java
package com.in28minutes.firstjavaproject;

public class MultiplicationTable {
	
	void printMultiply(int number) {
		for (int i = 1; i < 10 ; i ++) {
			System.out.printf("%d * %d = %d", number, i, number * i).println();
		}
	}
}
```

- 먼저 **MultiplicationTable** 이라는 구구단 클래스를 만든다
  - 클래스 안에 **printMultiply(int number)** 라는 메서드를 넣어준다





#### 새로운 파일 만들어서 구구단 실행하기

```java
package com.in28minutes.firstjavaproject;

public class MultiplicationTableRunner {

	public static void main(String[] args) {
		MultiplicationTable table = new MultiplicationTable();
		table.printMultiply(5);

	}
```

- **MultiplicationTable** 클래스를 가지고 와서, **MultiplicationTableRunner** 클래스를 통해 실행을 시켜준다



