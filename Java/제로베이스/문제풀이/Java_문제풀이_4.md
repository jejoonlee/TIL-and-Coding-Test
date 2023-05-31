# Java 문제풀이 (Programmers)





## 짝수와 홀수

> #### 주어진 숫자가 짝수인지 홀수인지 확인하는 것
>
> - 쉬운 문제지만, 잘 안 쓰는 방법으로 코드를 짰다 (작성하는 줄을 많이 줄였다)

```java
class Solution {
    public String solution(int num) {
        if (num % 2 == 0) return "Even";
        return "Odd";
    }
}
```





## 자연수 뒤집어 배열로 만들기

> #### ArrayList를 이용하여, 10으로 나눈 나머지를 ArrayList에 뒤에 넣어주었다

```java
import java.util.*;

class Solution {
    public ArrayList<Long> solution(long n) {
        ArrayList<Long> tempAnswer = new ArrayList <Long> ();
        
        while (n > 0) {
            tempAnswer.add(n % 10);
            n /= 10;
        }
        return tempAnswer;
    }
}
```





## 문자열 내 p와 y의 개수

> #### " " 와 ' '의 차이점
>
> - " " 는 문자열을 사용할 때 쓰인다
> - ' ' 는 character를 사용할 때 쓰인다!

```java
class Solution {
    boolean solution(String s) {
        s = s.toLowerCase();
        long pCount = 0;
        long yCount = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'p') {
                pCount += 1;
            } else if (s.charAt(i) == 'y') {
                yCount += 1;
            }
        }
        
        if (pCount == yCount) return true;
        return false;
    }
}
```





## 문자열을 정수로 바꾸기

> #### String을 Integer로 바꾸기
>
> - Integer.parseInt() 사용

```java
class Solution {
    public int solution(String s) {
        int answer = Integer.parseInt(s);
        return answer;
    }
}
```



