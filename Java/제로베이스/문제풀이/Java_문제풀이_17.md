# 20230704 [Java] 문제풀이 





## [프로그래머스] 숫자 짝꿍

#### 두 개의 숫자가 문자열로 주어진다



#### 두 숫자가 공통으로 가진 숫자들을 모아서 제일 큰 수를 만드는 것읻

- 110, 11110 이면 110이 있어 110이 가장 큰 숫자다
- 1234, 123456 에서는 1234가 있고 4321이 가장 큰 숫자다





#### 0~9까지, 각각 숫자들의 개수를 넣으려는 배열을 2개 만들었다

- 하나는 X 수에 대한 배열
- 하나는 Y 수에 대한 배열



#### 두 배열을 제일 뒷부분에서 순회하면서, 0이 아닐 경우 겹치니깐 두 배열 중 작은 숫자만큼 문자열에 넣어주면 된다



#### StringBuffer를 사용할 때에는 .toString() 을 이용하면 문자열로 바꿔준다

```java
import java.util.*;

class Solution {
    
    public String solution(String X, String Y) {
        StringBuffer answer = new StringBuffer();
        
        int[] numX = new int[10];
        int[] numY = new int[10];
        
        for (int i = 0; i < X.length(); i++) {
            numX[(int) X.charAt(i) - 48] ++;
        }
        
        for (int i = 0; i < Y.length(); i++) {
            numY[(int) Y.charAt(i) - 48] ++;
        }
        
        for (int i = 9; i >= 0; i--) {
            if (numX[i] != 0 && numY[i] != 0) {
                int minNum = Math.min(numX[i], numY[i]);
                
                for (int j = 0; j < minNum; j++) {
                    answer.append(i); 
                }
            }
        }
        
        if (answer.length() == 0) return "-1";
        if (answer.charAt(0) == '0') return "0";
        return answer.toString();
        
    }
}
```







## 성격 유형 검사하기

#### 유형 별로 점수를 맥여서, MBTI 처럼 결과를 나타내는 것이다



#### HashMap을 사용하고, key에는 각 나눠지는 유형과, value에는 2개의 길이의 배열을 넣었다

- "RT" 를 key로 넣고 배열 첫번째 인덱스는 R에 대한 점수, 두 번째는 T에 대한 점수를 넣었다



#### type과 typeString 배열을 만들어서, 나중에 총 계산을 할 때에, 그리고 성격 유형을 제대로 만들 때에, 활용을 했다

- type을 통해서 RT 중에 R인지 T인지, RT의 인덱스를 저장했다 (R의 점수가 크거나 두 점수가 같을 경우 0을, T 점수가 크면 1을 넣었다)
  - 이렇게 해서, 나중에 최종 결과를 낼 때에, typeString을 순회하면서, 각 두 개의 유형 중 인덱스를 type에서 꺼내면 된다



```java
import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        
        HashMap<String, int[]> result = new HashMap<String, int[]>();
        
        result.put("RT", new int[2]);
        result.put("CF", new int[2]);
        result.put("JM", new int[2]);
        result.put("AN", new int[2]);
        
        int[] type = new int[4]; 
        String[] typeString = {"RT", "CF", "JM", "AN"};
            
        int[] score = {3, 2, 1, 0, 1, 2, 3};
        Character upLetter;
        
        for (int i = 0; i < survey.length; i++) {
            if (choices[i] != 4) {
                if (choices[i] > 4) {
                    upLetter = survey[i].charAt(1);
                    
                    if (survey[i].equals("RT") || survey[i].equals("TR")) {
                        if (upLetter == 'R') {
                            result.get("RT")[0] += score[choices[i] - 1];
                        } else {
                            result.get("RT")[1] += score[choices[i] - 1];
                        }
                    } else if (survey[i].equals("CF") || survey[i].equals("FC")) {
                        if (upLetter == 'C') {
                            result.get("CF")[0] += score[choices[i] - 1];
                        } else {
                            result.get("CF")[1] += score[choices[i] - 1];
                        }
                    } else if (survey[i].equals("JM") || survey[i].equals("MJ")) {
                        if (upLetter == 'J') {
                            result.get("JM")[0] += score[choices[i] - 1];
                        } else {
                            result.get("JM")[1] += score[choices[i] - 1];
                        }
                    } else if (survey[i].equals("AN") || survey[i].equals("NA")) {
                        if (upLetter == 'A') {
                            result.get("AN")[0] += score[choices[i] - 1];
                        } else {
                            result.get("AN")[1] += score[choices[i] - 1];
                        }
                    }
                    
                } else {
                    upLetter = survey[i].charAt(0);
                    
                    if (survey[i].equals("RT") || survey[i].equals("TR")) {
                        if (upLetter == 'R') {
                            result.get("RT")[0] += score[choices[i] - 1];
                        } else {
                            result.get("RT")[1] += score[choices[i] - 1];
                        }
                    } else if (survey[i].equals("CF") || survey[i].equals("FC")) {
                        if (upLetter == 'C') {
                            result.get("CF")[0] += score[choices[i] - 1];
                        } else {
                            result.get("CF")[1] += score[choices[i] - 1];
                        }
                    } else if (survey[i].equals("JM") || survey[i].equals("MJ")) {
                        if (upLetter == 'J') {
                            result.get("JM")[0] += score[choices[i] - 1];
                        } else {
                            result.get("JM")[1] += score[choices[i] - 1];
                        }
                    } else if (survey[i].equals("AN") || survey[i].equals("NA")) {
                        if (upLetter == 'A') {
                            result.get("AN")[0] += score[choices[i] - 1];
                        } else {
                            result.get("AN")[1] += score[choices[i] - 1];
                        }
                    }
                    
                }
            }
        }
        
        
        int i = 0;
        for (String string : result.keySet()) {
            System.out.println(Arrays.toString(result.get(string)));
            if (result.get(string)[0] < result.get(string)[1]) {
                type[i] = 1;
            }
            i ++;
        }
        
        for (int idx = 0; idx < 4; idx++) {
            answer += typeString[idx].charAt(type[idx]);
        }
        
        return answer;
    }
}
```
