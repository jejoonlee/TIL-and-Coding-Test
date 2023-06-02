# [제로베이스] Java 상속, 다향성

*출처 : 제로베이스 백엔드 스쿨*





![img](https://blog.kakaocdn.net/dn/on9oW/btsibc3XF9u/lNxBNKMm4EXY117gBunUt0/img.png)



## 상속

#### 기존 클래스를, 새로운 클래스 안에 속성과 메서드를 넣는 것

#### 다중 상속은 불가능하다



```java
class 자식클래스 extends 부모클래스 {
    새로운 속성;
    새로운 메서드;
}
```

- **super, super()**
  - 부모 클래스의 변수 또는 생성자를 호출할 때에 사용한다





## Overriding (오버라이딩)

#### 부모 클래스에 존재하는 메서드를 자식 클래스가 동일한 메서드 이름을 가지고, 안에 코드를 재정의 하는 것이다



```java
class Parent{
    void eat() {
        System.out.println("Eat breakfast");
        System.out.println("Eat lunch");
    }
}
/*
output
Eat breakfast
Eat lunch
*/

class Children extends Parent {
    void eat() {
        super.eat();
        System.out.println("Eat dinner");
    }
}

/*
output
Eat breakfast
Eat lunch
Eat dinner
*/
```

- 같은 **eat()** 이지만, 다른 기능을 반환한다





## 다향성

#### 부모-자식 상속 관계에 있는 클래스에서 상위 클래스가 동일한 메세지로 하위 클래스들을 서로 다르게 동작시키는 원리

- 부모가 자식을 참조할 수 있다 (반대로는 불가능하다)



### instanceof

- 참조하고 있는 객체의 타입을 확인시켜준다



```java
class Website {
    public void print() {
        System.out.println("This is Website")
    }
}
class Google extends Website {
    public void print() {
        System.out.println("This is Google")
    }
    
    public void print2() {
        System.out.println("Please Search")
    }
}

Website website = new Google();
// Google google = new Website(); 는 불가능 하다

System.out.println(website instanceof Website);
// output : true
    
System.out.println(website instanceof Google);
// output : true

website.print();
// output : This is Google

website.print2();
// output : Error
```

- website는 Google() 클래스를 참조 하지만, Google() 클래스에 있는 속성이나 메서드는 사용할 수 없다
  - 단, Google 클래스에 Website 클래스에서 오버라이딩한 메서드가 있다면, Google 클래스 기준에서 실행이 된다
