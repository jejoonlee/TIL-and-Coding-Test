# 20230706 [Java] 문제풀이 



## [프로그래머스] 신규 아이디 추천

#### 그냥 1단계부터 7단계까지, 구현을 하라고 문제에서 나온 대로, 코드를 작성했다



#### 특히 아스키 코드를 많이 썼고, 그리고 문자열 슬라이싱을 많이 사용했던 것이 특이점이다



#### 다른 분의 코드 (정규 표현식 사용하기)

- **.toLowerCase()** : 이것을 사용해서 대문자를 소문자로 바꾸기
- **replaceAll()** : 문자열에서 변경할 점들을 바꾸기
  - **.replaceAll("[.]{2,}", ".");**  =>  '.' 이 2개 이상이면 '.' 하나로 바꾸기
  - `.replaceAll("^[.][.]$", "");`  =>   앞뒤에 '.'이 있으면, 없애기



```java
import java.util.*;
class Solution {
    public String solution(String new_id) {
        String answer = "";
        
        // 1번과 2번을 한꺼번에
        String tempId = "";
        
        for (int i = 0; i < new_id.length(); i++) {
            if ((int) new_id.charAt(i) > 64 && (int) new_id.charAt(i) < 91 ) {
                tempId += (char) (new_id.charAt(i) + 32);
            } else if ((int) new_id.charAt(i) > 96 && (int) new_id.charAt(i) < 123) {
                tempId += (char) new_id.charAt(i);
            } else if ((int) new_id.charAt(i) == 45 || (int) new_id.charAt(i) == 46 || (int) new_id.charAt(i) == 95) {
                tempId += (char) new_id.charAt(i);
            } else if ((int) new_id.charAt(i) > 47 && (int) new_id.charAt(i) < 58) {
                tempId += (char) new_id.charAt(i);
            }
        } 
        
        // 연속된 마침표를 하나로
        new_id = tempId;
        tempId = "";
        
        if (new_id.length() > 1) {
            int count = 0;
            
            for (int i = 0; i < new_id.length(); i ++) {
                if (new_id.charAt(i) == '.') {
                    count += 1;
                } else {
                    if (i - 1 >= 0 && new_id.charAt(i - 1) == '.' && count > 0) {
                        tempId += '.';
                        count = 0;
                    }
                    tempId += new_id.charAt(i);
                }
            }
            if (count > 0) tempId += '.';
            new_id = tempId;
        }
        
        // 처음과 끝에 있는 마침표 제거
        if (new_id.charAt(0) == '.') new_id = new_id.substring(1, new_id.length());
        if (new_id.length() > 0 && new_id.charAt(new_id.length() - 1) == '.') {
            new_id = new_id.substring(0, new_id.length() - 1);
        }
        
        // 빈 문자열이면 "a"를 대입
        if (new_id.length() == 0) {
            new_id += "a";
        } else if (new_id.length() > 15) {
            new_id = new_id.substring(0, 15);
            
            if (new_id.charAt(14) == '.') new_id = new_id.substring(0, 14);
        }
        
        while (new_id.length() < 3) {
            new_id += new_id.charAt(new_id.length() - 1);
        }
        
        return new_id;
    }
}
```





## [프로그래머스] 키패드 누르기

#### 1, 4, 7 는 왼쪽 손가락으로, 3, 6, 9는 오른쪽 손가락으로 누르면 된다

- 이건 어렵지 않다



#### 단 2, 5, 8을 눌렀을 때에, 제일 가까운 손가락으로 누르거나, 거리가 같다면, 자주 사용하는 손으로 그 번호를 누른다



#### 일단 key에는 0부터 9까지 키패드의 좌표를 넣었다

- `#` 과 `*` 은 인덱스 10과 11에 넣었다 (시작할 때 2, 5, 8을 누를 수도 있으니깐)



#### HashMap 에는 right와 left를 key로 넣고, value에는 전에 각 두 손가락으로 어떤 번호를 눌렀는지 저장을 해 놓는다



#### 그렇게 2, 5, 8을 눌렀을 때에 맨해튼 거리 구하기 공식을 사용해서, 두 손가락 중 가까운 손가락으로, 해당 키패드를 누르게 한다

- **|x1 - x2| + |y1 - y2|** 가 맨해튼 거리 구하기 공식이다
- 왼쪽 손에서의 거리 : `Math.abs(key[map.get("left")][0] - key[num][0]) + Math.abs(key[map.get("left")][1] - key[num][1]);`
- 오른쪽 손에서의 거리 : `Math.abs(key[map.get("right")][0] - key[num][0]) + Math.abs(key[map.get("right")][1] - key[num][1]);`



```java
import java.util.*;
class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int[][] key = {{3, 1}, {0, 0}, {0, 1}, {0, 2}, {1, 0}, {1, 1}, {1, 2}, {2, 0}, {2, 1}, {2, 2}, {3, 0}, {3, 2}};
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        
        map.put("right", 10);
        map.put("left", 11);
        int count = 0;
        
        for (int num : numbers) {
            count += 1;
            if (num == 1 || num == 4 || num == 7) {
                answer += "L";
                map.put("left", num);
            } else if (num == 3 || num == 6 || num == 9) {
                answer += "R";
                map.put("right", num);
            } else {
                int leftDist = Math.abs(key[map.get("left")][0] - key[num][0]) + Math.abs(key[map.get("left")][1] - key[num][1]);
                int rightDist = Math.abs(key[map.get("right")][0] - key[num][0]) + Math.abs(key[map.get("right")][1] - key[num][1]);
                
                if (leftDist > rightDist) {
                    answer += "R";
                    map.put("right", num);
                } else if (rightDist > leftDist) {
                    answer += "L";
                    map.put("left", num);
                } else {
                    if (hand.equals("right")) answer += "R";
                    else if (hand.equals("left")) answer += "L";
                    map.put(hand, num);
                }
            }
        }
        
        return answer;
    }
}
```

