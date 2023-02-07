# Udemy - Javascript - Data Structure



## 자료구조

> #### 자료 구조는 데이터에 적용될 수 있는 값들 및 기능 혹은 작업들 사이의 관계를 포함한다

예를 들어 배열을 생각한다

- 배열 안에는 값들 사이에 관계가 있다 (정렬을 하거나, 값을 추가할 수 있거나 없앨 수 있다)



자료 구조에는 많은 종류가 있고, 각자 쓰임세가 다르다



## ES2015

> 자료 구조를 클래스로 만들 예정

### What is Class?

- 클래스는 객체를 생성하기 위해 미리 속성 및 메소드를 정의한 **블루프린트**이다



```javascript
class Student {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
}

let firstStudent = new Student("Joon", "Lee")
let secondStudent = new Student("Alex", "Lee")
```

- `constructor()` : 새로운 `Student`의 인스턴스를 인스턴스화 시킬 때 사용한다
  - 즉 새로운 학생이 있으면, 학생의 `firstName`과 `lastName`을 받게 된다
- 클래스를 이용하여 새로운 인스턴스를 만드려면 `new`가 앞에 붙어야 한다
  - `new Student()` : `Student`의 인스턴스를 생성



#### 인스턴스에 메소드 추가하기

```javascript
class Student {
    constructor(firstName, lastName, year) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.grade = year;
        this.tardies = 0;
        this.scores = [];
    }
    fullName() {
        return `Your full name is ${this.firstName} ${this.lastName}`
    }
    markLate() {
        this.tardies += 1;
        return `${this.firstName} ${this.lastName} has been late ${this.tardies}`
    }
    addScore(score) {
        this.scores.push(score)
    }
}

let firstStudent = new Student("Joon", "Lee", 1)

firstStudent.fullName()
// "Your full name is Joon Lee"

firstStudent.markLate()
// "Joon Lee has been late 1"
firstStudent.tardies
// 1
```

- `fullName()` 클래스에 속한 인스턴스 메소드
- `markLate()`  : 메서드가 호출되면 클래스 속성에 있는 `this.tardies` 값에 1을 더하는 것
  - `학생.tardies` : 몇 번 지각했는지 속성을 통해 볼 수 있다
- `addScore(score)` : score을 입력하면, 그 score을 `this.scores` 배열에, 점수를 넣어준



#### Class Method

> 많이 사용하지는 않는다
>
> 특정 인스턴스에 제한되지 않는 메서드다
>
> 앞에 `static`을 붙이고 메서드를 만든다

```javascript
class Student {
    constructor(firstName, lastName, year) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.grade = year;
        this.tardies = 0;
        this.scores = [];
    }
    fullName() {
        return `Your full name is ${this.firstName} ${this.lastName}`
    }
	
    static enrollStudents(...students) {
        return "ENROLLING STUDENTS"
    }
}

let firstStudent = new Student("Joon", "Lee", 1)
let secondStudent = new Student("Alex", "Lee")

Student.enrollStudents([firstStudent, SecondStudent])
```

- `firstStudent.enrollStudents()`를 하면 안 된다.
  - `firstStudent`는 인스턴스다
  - 클래스, `Student`를 넣어야 한다

