# Java 문제풀이 (Programmers)





## 분수의 덧셈

- **(numer1 / denom1) + (numer2 / denom2)** 의 값을 구해, 분자는 answer[0]에, 분모는 answer[1]에 저장하는 것이다
- 먼저 answer[0]와 answer[1]에 나누지 않은 채로, 그냥 더해서 저장을 한다
- 그리고 2부터 시작해서 for문을 돌면서 answer[0]과 answer[1]를 나눌 수 있으면, 계속 나눠준다
  - 최대공약수를 나누는 방법과 똑같은 것이다 (대신 최대공약수를 따로 구하는 것이 아니라, 최대공약수를 구하는 식을 for문과 while문을 통해서 구하는 것이다)

```python
class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[] {numer1 * denom2 + numer2 * denom1, denom1 * denom2};
        
        for (int i = 2; i <= answer[1]; i++) {
            while (answer[0] % i == 0 && answer[1] % i == 0) {
                answer[0] /= i;
                answer[1] /= i;
            }
        }
        
        return answer;
    }
}
```



#### 확실히 리스트를 만드는 방법이 파이썬이랑 틀리다 ㅜ.ㅜ

- int[] answer = new int[] {}
  - 리스트 함수에 미리 넣을 값들을 넣는 것 같은 기분이랄까?...
  - new int[] 에 [] 안에 숫자를 넣어, 리스트 안에 몇 개의 숫자가 들어갈지 정할 수 있다
    - 예) new int[2]  : 2개의 원소를 넣을 수 있음





## 배열 두 배 만들기

```java
class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
            
        for (int i = 0; i < numbers.length; i ++) {
            answer[i] = numbers[i] * 2;
        }
        
        return answer;
    }
}
```





## 크기가 작은 부분문자열

- 제일 중요했던 것은 자료형이다
- Integer.parseInt() 를 사용했더니, 런타임 에러가 떴다
- 숫자를 더 크게 사용하는 것을 고려하되 int 보다는 Long.parseLong()을 사용하였다

```java
class Solution {
    public int solution(String t, String p) {
        
        long numP = Long.parseLong(p);
        int answer = 0;
        
        for (int i = 0; i <= t.length() - p.length(); i ++ ){
            long numT = Long.parseLong(t.substring(i, i + p.length()));
            
            if (numT <= numP) {
                answer ++;
            }
        }

        return answer;
    }
}
```







## 가장 가까운 같은 글자

> #### 앞에 글자 중, 제일 가까운 같은 글자랑 얼마나 떨어져 있는지 구하는 것이다
>
> #### 앞에 글자가 없을 경우 -1을 출력한다



- 먼저 answer[0]은 제일 앞에 있는 단어라서, 무조건 -1 이다
- 인덱스 i 는 1부터 시작한다
- 그리고 j 는 i - 1 부터 시작하고, 1씩 내려가면서 i 번째에 있는 알파벳과 제일 가까운, 같은 알파벳을 찾는다

```java
class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        answer[0] = -1;
        
        for (int i = 1; i < s.length(); i++) {
            int count = 0;
            
            for (int j = i - 1 ; j >= 0; j--) {
                if (s.charAt(i) == s.charAt(j)) {
                    count = i - j;
                    break;
                }
            }
            
            if (count == 0) {
                answer[i] = -1;
            } else {
                answer[i] = count;
            }
        }
        
        return answer;
    }
}
```







## 푸드 파이트 대회

> [1, 4, 6, 8, 10] 이 주어지면
>
> "11222333344444044444333322211" 를 출력하는 것
>
> - 숫자는 인덱스를 따라가면 되고, 중간에는 무조건 0이 와야 함
> - 즉 0 앞에 것을, 뒤에는 뒤집으면 됨



```java
class Solution {
    public String solution(int[] food) {
        String answer = "";
        
        for (int i = 1 ; i < food.length ; i++) {
            String s = String.format("%d", i);
            for (int j = 0 ; j < food[i] / 2; j ++) {
                answer += s;   
            }
        }
        
        answer += "0";
        
        for (int i = food.length - 1 ; i >= 1 ; i--) {
            String s = String.format("%d", i);
            for (int j = 0 ; j < food[i] / 2; j ++) {
                answer += s;   
            }
        }
        
        return answer;
    }
}
```

