# 14. Java String 대체 클래스



#### string 같은 경우, 변수가 만들어지면, 변수의 값은 바뀔 수가 없다



## StringBuffer

> #### 멀티스레딩이 가능한 클래스다
>
> - 하지만 싱글스레딩을 할 때에는 느릴 수 있다

```java
jshell> StringBuffer sb = new StringBuffer("Test");
sb ==> Test

jshell> sb.append("Test");
$27 ==> TestTest

jshell> sb
sb ==> TestTest

jshell> sb.setCharAt(3, 's');

jshell> sb
sb ==> TessTest
```

- **StringBuffer** 클래스를 사용하면, 문자열의 값을 바꿀 수 있다
  - **.setCharAt(index, string);**
    - index에 있는 알파벳을, string으로 바꿀 수 있다





## StringBuilder

> #### 싱글스레딩을 위한 클래스고, 최근에 만들어졌다

```java
jshell> StringBuilder StringB = new StringBuilder("test");
StringB ==> test

jshell> StringB.setCharAt(0, 'T');

jshell> StringB
StringB ==> Test

jshell> StringB.append(" Test");
$34 ==> Test Test
```

