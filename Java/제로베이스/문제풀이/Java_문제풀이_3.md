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





## 배열 원소의 길이

> #### 배열을 순회하면서, 원소 (문자열)의 길이를 구해서, 새로운 배열에 넣어서 출력하는 것이다

```java
class Solution {
    public int[] solution(String[] strlist) {
        int[] answer = new int[strlist.length];
        for (int i = 0; i < strlist.length; i++) {
            answer[i] = strlist[i].length();
        }
        
        return answer;
    }
}
```





## 문자열 뒤집기

> #### 문자열의 인덱스를 뒤에서부터 읽으면서 answer에 넣으면 된다

```java
class Solution {
    public String solution(String my_string) {
        String answer = "";
        for (int i = my_string.length() - 1; i >= 0; i--) {
            answer += my_string.charAt(i);
        }
        
        return answer;
    }
}
```





## 핸드폰 번호 가리기

> #### 마지막 4자리를 slicing을 통해 가지고 온다
>
> - .substring()을 사용할 것
>
> #### 앞에 숫자들을 for문으로 돌면서 * 로 넣어준다

```java
class Solution {
    public String solution(String phone_number) {
        String answer = "";
        String lastFourDigit = phone_number.substring(phone_number.length() - 4, phone_number.length());
        for (int i = 0; i < phone_number.length() - 4; i++) {
            answer += "*";
        }
        
        return answer + lastFourDigit;
    }
}
```





## 하샤드 수

> #### x의 자릿수들을 더하고, 더한 값을 x와 나누어 떨어지면 true를 출력한다

```java
class Solution {
    public boolean solution(int x) {
        int temp_x = x;
        int sum = 0;
        
        while (temp_x > 0) {
            sum += temp_x % 10;
            temp_x /= 10;
        }
        
        if (x % sum != 0) {
            return false;
        }
        return true;
    }
}
```

