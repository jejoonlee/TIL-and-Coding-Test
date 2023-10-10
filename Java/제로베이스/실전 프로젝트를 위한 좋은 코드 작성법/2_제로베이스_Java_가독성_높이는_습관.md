# [제로베이스] 가독성 높이는 습관

*출처 : 제로베이스 백엔드 스쿨*





## 이름 짓기



#### 코드의 이름을 통해, 코드가 무엇을 의미, 또는 작동을 하는지 알 수 있다



#### 개발자들끼리 소통을 하기 위해서 발음/ 검색하기 쉬운 이름을 사용하는 것이 좋다



#### 혼자서 일하는 것이 아니기 때문에, 남들이 이해 못 하는 단어를 사용하면 안 된다



#### 이름은 상수 / 변수 / 메서드 / 클래스 / 모듈 / 프로젝트에 지어야 한다

- 신규 프로젝트를 진행하는 것이 아니면 모듈/ 프로젝트 명은 이미 정해져 있다
- 메서드 이름은, 해당 메서드가 어떤 것을 하는지 알 수 있어야 한다



#### 일정한 규칙을 갖고 일관성을 유지해야 한다



#### 축약어보다는 풀어서 필드명을 사용하는 것이 좋다

- 모두 알아볼 수 있다







## 캡슐화



#### 객체의 속성 (data fields)과 행위(메서드, methods)를 하나로 묶고 실제 구현 내용 일부를 외부에 감추어 은닉한다

- 은닉이라는 것이 제일 중요하다



#### 데이터와 그 처리 방법을 숨길 수 있다

- 기능을 명령을 할 수 있지만, 기능이 어떻게 작동하는지 캡슐화를 통해 숨길 수 있다



```java
class User {
    // ======== 속성 ========
    private String name;
    private int age;
    
    // ======== 메서드 =========
    public String getName() {
        return name;
    }
    public int getAge() {
        return age;
    }
}
```

- 위에 private, public 같은 접근지정자가 있다



#### 자바 Bean 규약!

- 기본 생성자를 가지고 있으며, 모든 멤버가 private으로 선언되어 있다
- 멤버를 접근하기 위해서는 getter와 setter가 public으로 선언되어 있다







## Enum



#### 상수 대비 가독성이 뛰어남



#### enum 기본 함수 제공 (name, ordinal, values)



#### 인스턴스 변수 1개가 있음을 보장함



#### 상수 확장성 (필드 및 메서드 등)







## Null



#### 아무런 값도 존재하지 않는 상태



#### NullPointerException을 발생 시킨다



#### 매번 회피 로직을 넣어야 안전하다

- 하지만 의도하지 않는 에러가 생길 수 있다



#### Java에서 null 때문에 발생하는 에러가 많다

```java
boolean hasText(String text) {
    if (text == null)
        return false;
    return text.length() == 0 ? false : true;
}
```

- text를 아예 안 쓰면 null로 들어가게 된다
- 그래서 null에 대한 if문을 만들어 줘야 한다





### null 핸들링

> Assertion 단정문 `assert expression` 이 있는데, 사용을 하지 않는게 좋다
>
> - 레거시 코드에 있을 수 있음



```java
// Null이면 true를 리턴한다
Object.isNull();

// Null이 아니면 true를 리턴한다
Object.nonNull();

Object.requireNonNull(); // NullPointerException 예외를 리턴한다
```

