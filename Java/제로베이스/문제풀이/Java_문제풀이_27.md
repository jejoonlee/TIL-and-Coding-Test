# 20230725 [Java] 문제풀이 

#### 기초 다지기!!!!!



## [프로그래머스] 문자열 겹쳐쓰기

#### StringBuilder 또는 StringBuffer를 더 많이 사용해봐야겠다!

```java
class Solution {
    public StringBuilder solution(String my_string, String overwrite_string, int s) {
        StringBuilder answer = new StringBuilder();
        
        answer.append(my_string.substring(0, s));
        answer.append(overwrite_string);
        answer.append(my_string.substring(overwrite_string.length() + s, my_string.length()));
        
        return answer;
    }
}
```





## [프로그래머스] 두 수의 연산값 비교하기

```java
class Solution {
    public int solution(int a, int b) {
        int num1 = a * b * 2;
        
        int num2 = Integer.parseInt(String.format("%d%d", a, b));
        
        return Math.max(num1, num2);
    }
}
```



## [프로그래머스] 공배수

```java
class Solution {
    public int solution(int number, int n, int m) {
        if (number % n == 0 && number % m == 0) return 1;
        if (number % n != 0 || number % m != 0) return 0;
        
        return 0;
    }
}
```





## [프로그래머스] 홀짝에 따라 다른 값 반환하기

```java
class Solution {
    public int solution(int n) {
        int answer = 0;
        
        if (n % 2 == 1) {
            for (int i = 1; i <= n; i += 2) answer += i;
        } else {
            for (int i = 2; i <= n; i += 2) answer += Math.pow(i, 2);
        }
        
        return answer;
    }
}
```





## [프로그래머스] flag에 따라 다른 값 반환하기

```java
class Solution {
    public int solution(int a, int b, boolean flag) {
        if (flag == true) return a + b;
        if (flag == false) return a - b;
        return 0;
    }
}
```





## [프로그래머스] 이어 붙인 수

```java
class Solution {
    public int solution(int[] num_list) {
        String s1 = "", s2 = "";
        
        for (int num : num_list) {
            if (num % 2 == 1) s1 += num;
            else s2 += num;
        }
        
        return Integer.parseInt(s1) + Integer.parseInt(s2);
    }
}
```





## [프로그래머스] 수열과 구간 쿼리 3

```java
class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        
        for (int i = 0; i < queries.length; i++) {
            int tempNum = arr[queries[i][0]];
            arr[queries[i][0]] = arr[queries[i][1]];
            arr[queries[i][1]] = tempNum;
        }
        
        return arr;
    }
}
```





## [프로그래머스] 수열과 구간 쿼리 

```java
import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int[] arr, int[][] queries) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        
        for (int i = 0; i < queries.length; i++) {
            int tempNum = Integer.MAX_VALUE;
            
            for (int j = queries[i][0]; j <= queries[i][1]; j ++) {
                if (arr[j] > queries[i][2])  {
                    tempNum = Math.min(tempNum, arr[j]);
                }
            }
            
            if (tempNum == Integer.MAX_VALUE) {
                answer.add(-1);
            } else {
                answer.add(tempNum);
            }
        }
        
        return answer;
    }
}
```

