# Java 문제풀이 (Programmers)





## 옷가게 할인 받기

> #### 10만원 이상은 5%, 30만원 이상은 10%, 50만원 이상은 20% 할인

- 소수점과 곱하는 것이라서 double을 사용해야 한다
- 그리고 값은 int 로 반환해서 구해야 한다 (소수점은 버린다고 써져 있)

```java
class Solution {
    public double solution(double price) {
        if (price < 100000) {
            return price;
        } else if(price < 300000) {
            return (int) (price * 0.95);
        } else if (price < 500000) {
            return (int) (price * 0.9);
        } else {
            return (int) (price * 0.8);
        }
    }
}
```





## 점의 위치 구하기

> #### x, y 가 주어진다
>
> - x, y 면 1 / -x, y 면 2 / -x, -y 면 3 / x, -y 면 4를 반환하는 것이다



```java
class Solution {
    public int solution(int[] dot) {
        if (dot[0] > 0 && dot[1] > 0) {
            return 1;
        } else if (dot[0] < 0 && dot[1] > 0) {
            return 2;
        } else if (dot[0] < 0 && dot[1] < 0) {
            return 3;
        } else if (dot[0] > 0 && dot[1] < 0) {
            return 4;
        }
        
        return 0
    }
}
```







## 콜라츠 추측

> #### for문을 통해 500번만 반복할 수 있게 한다
>
> - 500번 안에 1이 만들어 지면 count를 반환한다
> - 500번 이상일 때에는 for문을 빠져나오고, -1을 반환한다



```java
class Solution {
    public int solution(int num) {
        
        for (int count = 0; count < 500; count ++) {
            if (num == 1) {
                return count;
            } else if (num % 2 == 0) {
                num /= 2;
            } else if (num % 2 == 1) {
                num = num * 3 + 1;
            }
        }
        
        return -1;
    }
}
```





## 서울에서 김서방 찾기

> #### String을 찾을 때에는 .equals() 를 사용해야 한다
>
> - python 은 그냥 == 써도 됬는데 ㅜ.ㅜ



```java
class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        
        for (int i = 0; i < seoul.length; i++) {
            if (seoul[i].equals("Kim")) {
                answer = Integer.toString(i);
                break;
            }
        }
        
        return "김서방은 " + answer + "에 있다";
    }
}
```

