# Java 문제풀이 (Programmers)





## 삼총사

#### 수열을 잘 만들면 된다

- 삼총사를 구하면 되기 때문에, 3중 for문을 이용하면 된다



```java
class Solution {
    public int solution(int[] number) {
        int answer = 0;
       
        for (int i = 0; i < number.length - 2; i ++) {
            for (int j = i + 1; j < number.length - 1; j ++) {
                for(int k = j + 1; k < number.length; k ++) {
                    if (number[i] + number[j] + number[k] == 0) {
                        answer += 1;
                    }
                }
            }
        }
        
        return answer;
    }
}
```





## 나머지 구하기

> #### 연산자 % 를 사용하여, 나머지를 구하는 것이다

```java
class Solution {
    public int solution(int num1, int num2) {
        int answer = num1 % num2;
        return answer;
    }
}
```





## 나이 출력

> #### 그냥 연도에 나이를 빼는 방법도 있지만 localDate을 사용하는 방법도 있다



#### 그냥 빼버리기

```java
class Solution {
    public int solution(int age) {
        int answer = 2022 - (age - 1);
        return answer;
    }
}
```



#### locatDate 사용하기

- 현재 시간을 출력하는 것이다
- 즉 년도가 바뀌면, 바뀌는 만큼 또 계산을 해야 한다는 것 (문제의 기준은 2022년이다)

```java
import java.time.*;

class Solution {
    public int solution(int age) {
        
        
        LocalDate DateNow = LocalDate.now();
        
        int answer = DateNow.getYear() - age;
        
        return answer;
    }
}
```





## 각도기

> #### 조건문을 사용하는 것
>
> - 즉 if문과 else if 문을 사용하면 된다



```java
class Solution {
    public int solution(int angle) {
        int answer = 0;
        
        if (angle < 90) {
            answer = 1;
        } else if (angle == 90) {
            answer = 2;
        } else if (angle < 180) {
            answer = 3;
        } else if (angle == 180) {
            answer = 4;
        }
        
        return answer;
    }
}
```





## 짝수의 합

> #### for문을 돌면서 n 이하의 수들을 순회한다
>
> #### if문을 통해 짝수를 구해주면서, 짝수인 수들을 더하면 된다

```java
class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i = 1; i <= n ; i ++) {
            if (i % 2 == 0) {
                answer += i;
            }
        }
        
        return answer;
    }
}
```





## 배열의 평균값

> #### for문을 통해 배열에 있는 원소들의 값을 모두 더해준다
>
> #### 원소의 수만큼 나눠주면 평균값이 나온다

```java
class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        
        for (int i = 0; i < numbers.length; i ++) {
            answer += numbers[i];
        }
        
        return answer / numbers.length;
    }
}
```



