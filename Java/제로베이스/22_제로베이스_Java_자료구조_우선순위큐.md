# [Java] 자료구조 - 우선순위 큐



 

## 우선순위 큐

#### Queue라고 할 수 있지만, 큐는 먼저 들어온 값이 먼저 나가는 것라고 하면, 우선순위 큐는, 우선순위가 높은 값부터 먼저 나가는 것이다

- 만약 우선순위가 동일하다면, 먼저 들어온 값이 먼저 나가는 FIFO (First In First Out)이 적용이 된다



#### 우선순위의 Enqueue와 Dequeue는 최소 힙 또는 최대 힙과  같다



#### 자바에서는 PriorityQueue 클래스를 사용하면 된다

- Heap으로 작동하는 클래스다





## 오름차순

#### PriorityQueue 클래스를 만들고, 만들어진 객체에, 값들을 넣으면 된다

- 숫자는 기본적으로 오름차순으로 바로 정렬이 된다
- 문자열이면 **숫자 => 소문자 => 대문자 => 한글** 순으로 정렬이 된다

```java
import java.util.*;

public class PQ {
    public static void main(String[] args) {
        int[] numArray = {3, 4, 7, 2, 1};
        String[] stringArray = {"J", "A", "C", "D", "c", "1", "7", "4", "안녕", "우선"};

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        PriorityQueue<String> spq = new PriorityQueue<>();

        for (int num:numArray) pq.add(num);
        for (String s:stringArray) spq.add(s);

        System.out.println("== 오름차순 ==");
        System.out.println(pq);
        System.out.println(spq);
    }

}

/*
== 오름차순 ==
[1, 2, 7, 4, 3]
[1, 4, 7, D, c, C, A, J, 안녕, 우선]
*/
```





## 내림차순

#### PriorityQueue 클라스를 사용하되 Collections.reverseOrder() 통해 내림차순으로 바꾼다

- 문자열을 내림차순으로 정렬을 하면 **한글 => 대문자 => 소문자 => 숫자** 순으로 정렬이 된다



```java
import java.util.*;

public class PQ {
    public static void main(String[] args) {
        int[] numArray = {3, 4, 7, 2, 1};
        String[] stringArray = {"J", "A", "C", "D", "c", "1", "7", "4", "안녕", "우선"};

        PriorityQueue<Integer> pq2 = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<String> spq2 = new PriorityQueue<>(Collections.reverseOrder());

        for (int num:numArray) pq2.add(num);
        for (String s:stringArray) spq2.add(s);

        System.out.println("== 내림차순 ==");
        System.out.println(pq2);
        System.out.println(spq2);
    }

}

/*
== 내림차순 ==
[7, 3, 4, 2, 1]
[우선, 안녕, C, J, c, 1, 7, 4, A, D]
*/
```





## compareTo를 사용하기

#### 우선순위에 따라 특정 값을 반환하고 싶을 때에 사용이 된다

- 예) 등수가 높은 학생의 이름을 출력하기 | 학생의 이름 순으로 등수를 출력하기



#### 비교하고 싶은 값과, 반환하고 싶은 값이 들어간 클래스를 만든다 (파이썬 같은 경우 주로 튜플에다가 넣었다)

- PriorityQueue는 객체를 비교할 수 없다
- 그래서 Comparable 또는 새로운 비교 메서드를 만들어서 객체 안에 들어가 있는 속성들을 비교한다





#### 에러 코드

- 아래 에러를 보게 되면, Person 이라는 클래스는 java.lang.Comparable에 적용이 안 된다
- Person에는 2가지 요소가 들어가 있는 객체가 만들어진다

```java
import java.util.*;

class Person {
    String name;
    int grade;

    Person(String name, int grade) {
        this.name = name;
        this.grade = grade;
    }
}

public class PQ {
    public static void main(String[] args) {
        String[] name = {"Alex", "Joon", "JayJay", "Green", "Houston", "Cesinha"};
        int[] grade = {3, 1, 5, 7, 2, 6};

        PriorityQueue<Person> pq = new PriorityQueue<Person>();

        for (int i = 0; i < grade.length; i++) {
            pq.add(new Person(name[i], grade[i]));
        }

        System.out.println(pq);
    }
}

// output : Person cannot be cast to java.lang.Comparable
```





#### 방법 1 - 1 (숫자)

- Comparable 인터페이스를 가지고 와서 compareTo 메서드를 오버라이드를 한다 (Person 클래스에)
- **오름차순**
  - **return this.grade >= add.grade ? 1 : -1**
    - **this.grade** (새로 추가하는 값) 이 더 적어야, 변경을 하는 것이다
    - **1** 은 그냥 놔두는 것이고, **-1**은 변경
    - 즉  **this.grade >= add.grade** 가 참일 경우에는 그냥 놔두고, 아닐 경우 변경을 하는 것 (1 : -1)
- **내림차순**
  - **return this.grade >= add.grade ? -1 : 1;**
    - **this.grade** (새로 추가하는 값) 이 더 크거나 같을 때에 변경을 한다
    - 즉  **this.grade >= add.grade** 가 참일 경우에는 변경을 하고, 아닐 경우 그냥 놔둔다 (-1 : 1)

```java
import java.util.*;

class Person implements Comparable<Person>{
    String name;
    int grade;

    Person(String name, int grade) {
        this.name = name;
        this.grade = grade;
    }

    @Override
    public int compareTo(Person add) {
        // 오름차순
        return this.grade >= add.grade ? 1 : -1;

        // 내림차순
		// return this.grade >= add.grade ? -1 : 1;
    }
}
public class PQ {
    public static void main(String[] args) {
        String[] name = {"Alex", "Joon", "JayJay", "Green", "Houston", "Cesinha"};
        int[] grade = {3, 1, 5, 7, 2, 6};

        PriorityQueue<Person> pq = new PriorityQueue<Person>();

        for (int i = 0; i < grade.length; i++) {
            pq.add(new Person(name[i], grade[i]));
        }

        for (Person person : pq) {
            System.out.println(person.grade + " " + person.name);
        }
    }
}

/*
1 Joon
2 Houston
5 JayJay
7 Green
3 Alex
6 Cesinha

하나씩 꺼낼 때에는 순서대로 꺼내진다
*/
```





#### 방법 2 - 1 (숫자)

- 따로 오버라이드 하는 것이 아니라, 람다 함수를 사용하는 것이다

- PriorityQueue 클래스를 불러와 객체를 만들 때에, **(Person p1, Person p2) -> p1.grade >= p2.grade ? 1 : -1** 을 넣었다

  - **(Person p1, Person p2) -> p1.grade >= p2.grade ? 1 : -1**
    - **오름차순으로 정렬**
    - p1 은 새로 추가하는 값
    - p1이 작으면 비교한 값(p2) 와 변경하는 것이다
  - **(Person p1, Person p2) -> p1.grade >= p2.grade ? -1 : 1**
    - 내림차순으로 정렬

  

```java
import java.util.*;

class Person {
    String name;
    int grade;

    Person(String name, int grade) {
        this.name = name;
        this.grade = grade;
    }
}

public class PQ {
    public static void main(String[] args) {
        String[] name = {"Alex", "Joon", "JayJay", "Green", "Houston", "Cesinha"};
        int[] grade = {3, 1, 5, 7, 2, 6};

        PriorityQueue<Person> pq = new PriorityQueue<Person>(
            (Person p1, Person p2) -> p1.grade >= p2.grade ? 1 : -1);

        for (int i = 0; i < grade.length; i++) {
            pq.add(new Person(name[i], grade[i]));
        }

        for (Person person : pq) {
            System.out.println(person.grade + " " + person.name);
        }
    }
}

/*
1 Joon
2 Houston
5 JayJay
7 Green
3 Alex
6 Cesinha
*/
```





#### 방법 2 - 1 (문자열)

- 람다 함수를 사용했다
- **(Person p1, Person p2) -> p1.name.compareTo(p2.name)**
  - .compareTo 를 문자열을 비교해준다 (오름차순으로 정렬)
- **(Person p1, Person p2) -> p2.name.compareTo(p1.name)**
  - 내림차순으로 정렬을 한 것

```java
import java.util.*;

class Person {
    String name;
    int grade;

    Person(String name, int grade) {
        this.name = name;
        this.grade = grade;
    }
}

public class PQ {
    public static void main(String[] args) {
        String[] name = {"Alex", "Joon", "JayJay", "Green", "Houston", "Cesinha"};
        int[] grade = {3, 1, 5, 7, 2, 6};

        PriorityQueue<Person> pq = new PriorityQueue<Person>(
            (Person p1, Person p2) -> p1.name.compareTo(p2.name));

        for (int i = 0; i < grade.length; i++) {
            pq.add(new Person(name[i], grade[i]));
        }

        for (Person person : pq) {
            System.out.println(person.grade + " " + person.name);
        }
    }
}

/*
Alex 3
Green 7
Cesinha 6
Joon 1
Houston 2
JayJay 5
*/
```

