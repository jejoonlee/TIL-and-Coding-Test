# Java 문제풀이 (Programmers)





## 나머지가 1이 되는 수 찾기

> #### 가장 작은 수를 찾는 것이니깐, 1부터 시작해서 1씩 더하면서 n 과 나누면 된다
>
> #### 거기서 나머지가 1이 나오는 첫 번째 x 가 답이 되는 것이다

```java
class Solution {
    public int solution(int n) {
        int answer = 0;
        int x = 1;
        
        while (n % x != 1) {
            x += 1;
        }
        
        answer = x;
        
        return answer;
    }
}
```





## 없는 숫자 더하기

> #### check(int value, int[] numbers)
>
> - 0부터 9를 value로 받고, 배열 안에 있는지 확인을 한다
> - 있으면 true를, 없으면 false를 반환한다
>
> #### false이면 answer에 더해주면 된다

```java
class Solution {
    
    public boolean check(int value, int[] numbers) {
        for (int num: numbers) {
            if (num == value) {
                return true;
            }
        }
        return false;
    }
    
    public int solution(int[] numbers) {
        int answer = 0;
        
        for (int i = 0; i <= 9; i ++) {
            if (check(i, numbers) == false) {
                answer += i;
            }
        }
        
        return answer;
    }
}
```

