# [TIL] Java (Split, Join)





#### split 은 문자열을 배열로 바꿔준다

- **.split(String regex)**
  - 해당 문자열 (regex) 을 바탕으로 문자열을 잘라서 배열에 넣어준다
- **.split(String regex, int limit)**
  - 해당 문자열 (regex) 을 바탕으로 문자열을 잘라서 배열에 넣어주지만, limit만큼 잘라준다
- **"|" 을 사용하여, 여러 구분자를 사용할 수 있다**
- 이미 `^`, `*` 같은 연산자를 구분자로 사용하고 싶을 때에는 `\\^` 또는 `\\*` 처럼 앞에 `\\`을 추가해주면 된다



```java
import java.util.*;
public class Main {
    public static void main(String[] args) {
        String string = "JeJoon,Alex,Messi";
        String string1 = "JeJoon^Alex^Messi";
        String string2 = "JeJoon Jayjay,Alex^Messi@Google*Samsung|Hello";

        String[] newArray = string.split(",");
        String[] newArray1 = string1.split("\\^");
        String[] newArray2 = string2.split(" |,|\\^|@|\\*|\\|");

        System.out.println(Arrays.toString(newArray));
        // output : [JeJoon, Alex, Messi]
        System.out.println(Arrays.toString(newArray1));
        // output : [JeJoon, Alex, Messi]
        System.out.println(Arrays.toString(newArray2));
        // output : [JeJoon, Jayjay, Alex, Messi, Google, Samsung, Hello]
        
    }
}
```







#### join 은 배열을 문자열로 바꿔준다

- **String.join(String delimiter, Array)**
  - **delimiter** 로 구분자로 배열을 문자열로 바꿔준다

```java
import java.util.*;
public class Main {
    public static void main(String[] args) {
        String[] array = {"JeJoon", "Jayjay", "Alex", "Messi", "Google", "Samsung"};

        System.out.println(String.join("|||", array));
        // output : JeJoon|||Jayjay|||Alex|||Messi|||Google|||Samsung
    }
}
```





#### 이름 사이에 * 과 , 을 대신 공백을 넣어서 출력하기

- 문자열을 **.split();** 을 통해서 이름들을 배열에 넣는다
- **String.join();**을 통해, 원하는 구분자를 넣어서 새로운 문자열을 만든다 

```java
import java.util.*;
public class Main {
    public static void main(String[] args) {
        String string = "JeJoon,Alex,Messi*Samsung";

        String newString = String.join(" ", string.split(",|\\*"));

        System.out.println(newString);
        // output : JeJoon Alex Messi Samsung
    }
}
```

