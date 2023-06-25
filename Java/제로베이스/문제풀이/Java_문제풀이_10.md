# 20230625 Java 문제풀이 





## 전국 대회 선발 고사

#### 학생 3명을 선발하는 문제이다

#### 문제에서는 학생들의 등수가 담긴 배열과, 학생들의 참여 여부가 담긴 배열이 주어진다

#### 두 개의 배열을 탐색하며, 선발 고사를 참여하는 학생들 중, 높은 등수를 가진 학생들을 고른다

#### 높은 등수부터 10000 * (제일 높은 등수) + 100 * (2번째 높은 등수) + (3번째 높은 등수) 의 식을 구하는 것이다



```java
import java.util.*;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        ArrayList<Integer> list = new ArrayList<Integer> ();
        
        // number는 등수를 말하는 것
        // 즉 등수는 1씩 증가할 것이고, 참가하는 학생이면 list에 제일 먼저 들어올 것
        int number = 1;
        while(list.size() < 3) {
            
            for (int i = 0; i < rank.length; i++) {
                if (rank[i] == number && attendance[i] == true) {
                    list.add(i);
                }
            }
            number++;
        }
        
        int answer = 10000 * list.get(0) + 100 * list.get(1) + list.get(2);
        
        return answer;
    }
}
```





## 배열의 원소 삭제하기

#### 배열 2개가 주어진다

- 정수가 담긴 배열1
- 배열1에서 빼내야 할 정수들이 담긴 배열2가 주어진다



#### 차집합을 통해서 배열1 중에, 배열2와 겹치는 숫자들을 없앤다

- **차집합** : setOne.removeAll(setTwo);
- **교집합** : setOne.allAll(setTwo);
- **합집합** : setOne.retainAll(setTwo);



#### 배열1과 같은 순서로 출력을 해야 해서, 배열1을 순회하며, 차집합으로 만들어진 set 안에 들어가 있는지 확인하면서 정답에 넣는다

- **.contains()** 를 사용하면 된다



```java
import java.util.*;

class Solution {
    
    public HashSet<Integer> toSet(int[] array) {
         HashSet<Integer> set = new HashSet<Integer> ();
        
        for (int i = 0; i < array.length; i++) {
            set.add(array[i]);
        }
        
        return set;
    }
    
    public ArrayList<Integer> solution(int[] arr, int[] delete_list) {
        ArrayList<Integer> answer = new ArrayList<Integer> ();
        
        HashSet<Integer> setOne = toSet(arr);
        HashSet<Integer> setTwo = toSet(delete_list);
        
        setOne.removeAll(setTwo);
        
        for (int i = 0; i < arr.length; i++) {
            if (setOne.contains(arr[i])){
                answer.add(arr[i]);
            }
        }
        
        return answer;
    }
}
```





## 정수를 나선형으로 배치하기

#### 말 그대로 n이라는 정수가 주어지고 1부터 n * n의 정수를 그래프에 다가 배치를 하는 것읻

예)

n = 4

1		2		3	4

12	13	14	  5

11	16	15	  6

10	  9	  8	  7



#### 처음에는 테스트 케이스 하나가 시간 초과 에러가 났다

- 반례 n = 1 을 한번 해보았고, 역시 에러가 났다
- 그래서 while문을 들어가기 전에 **if (n == 1)** 을 통해, 먼저 1에 대한 그래프를 반환했다



#### 그 외에는 모두 while문을 사용하여, 그래프 밖으로 나가거나 해당 좌표가 0일 때까지 한 방향으로 숫자를 넣을 수 있도록 했다



```java
import java.util.*;

class Solution {
    public int[][] solution(int n) {
        
        int[][] answer = new int[n][n];

        int x = 0;
        int y = 0;
        int number = 1;
        
        if (n == 1) {
            answer[x][y] = 1;
        } else {
            while (number <= n * n) {
            
                while (y < n && answer[x][y] == 0) {
                    answer[x][y] = number;
                    y ++;
                    number ++;
                }
                y -= 1;
                x += 1;

                while (x < n && answer[x][y] == 0) {
                    answer[x][y] = number;
                    x ++;
                    number ++;
                }
                x -= 1;
                y -= 1;

                while (0 <= y && answer[x][y] == 0) {
                    answer[x][y] = number;
                    y --;
                    number ++;
                }
                x -= 1;
                y += 1;

                while (y < n && answer[x][y] == 0) {
                    answer[x][y] = number;
                    x --;
                    number ++;
                }
                x += 1;
                y += 1;
            }
        }
        
        return answer;
    }
}
```





## OX퀴즈

#### 기본적으로 모든 식은 X [연산자] Y = Z 이다

#### 즉 문자열을 배열로 만들면, 배열의 길이는 무조건 5이다

#### 이런 점을 사용하여, 연산자가 뭔지 알아낼 수 있고, X와 Y를 연산한 후 Z와 같은지 비교할 수 있다



```java
class Solution {
    public ArrayList<String> solution(String[] quiz) {
        ArrayList<String> answer = new ArrayList<String>();
        int tempNum = 0;
        
        for (int i = 0; i < quiz.length; i++) {
            
            String[] calculate = quiz[i].split(" ");
            
            if (calculate[1].equals("-")) {
                tempNum = Integer.parseInt(calculate[0]) - Integer.parseInt(calculate[2]);
            } else if (calculate[1].equals("+")) {
                tempNum = Integer.parseInt(calculate[0]) + Integer.parseInt(calculate[2]);
            }
            
            if (tempNum == Integer.parseInt(calculate[4])) {
                answer.add("O");
            } else {
                answer.add("X");
            }
            
        }
        
        return answer;
    }
}
```

