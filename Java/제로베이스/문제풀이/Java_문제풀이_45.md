# 20230905 [Java] 문제풀이 





## [프로그래머스] 괄호 회전하기



#### .substring 을 이용해서, 문자열을 슬라이싱 하면서 문자열을 한바퀴 돌린다



#### 한바퀴 돌리면서 stack을 사용하여 괄호 문자열이 유효한지 확인해준다



```java
import java.util.*;

class Solution {
    
    public static boolean isCorrect(String str) {
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '(' || str.charAt(i) == '[' || str.charAt(i) == '{') {
                stack.push(str.charAt(i));   
            } else {
                if (stack.isEmpty()) return false;
                
                if ((str.charAt(i) == ')' && stack.peek() != '(') ||
                   (str.charAt(i) == ']' && stack.peek() != '[')  ||
                   (str.charAt(i) == '}' && stack.peek() != '{')) {
                    return false;
                }  else if ((str.charAt(i) == ')' && stack.peek() == '(') ||
                            (str.charAt(i) == ']' && stack.peek() == '[')  ||
                             (str.charAt(i) == '}' && stack.peek() == '{')) {
                    stack.pop();
                }
            }
        }
        
        if (!stack.isEmpty()) return false;
        
        return true;
    }
    
    public int solution(String s) {
        int answer = 0;
        
        for (int i = 0; i < s.length(); i ++) {
            String s1 = s.substring(0, i);
            String s2 = s.substring(i, s.length());
            
            if (isCorrect(s2 + s1)) answer ++;
        }
        
        return answer;
    }
}
```





## [프로그래머스] 순위 검색



#### 새로운 2중 배열로 info와 query를 만든다



#### 그리고 두 배열을 비교하면 되는데, 효율성이 떨어진다...



```java
import java.util.*;
class Solution {
    public int[] solution(String[] info, String[] query) {
        int[] answer = new int[query.length];
        
        ArrayList<String[]> qList = new ArrayList<>();
        ArrayList<String[]> infoList = new ArrayList<>();
        
        // query에 문자열을 배열로 만들어 qList에 넣는다
        for (String str : query) {
            str = str.replace("and ", "");
            String[] queryList = str.split(" ");
            qList.add(queryList);
        }
        
        for (String str : info) {
            String[] iList = str.split(" ");
            infoList.add(iList);
        }
        
        for (int i = 0; i < qList.size(); i++) {
            int count = 0;
            String lang = qList.get(i)[0];
            String devType = qList.get(i)[1];
            String career = qList.get(i)[2];
            String food = qList.get(i)[3];
            int score = Integer.parseInt(qList.get(i)[4]);
            
            for (int j = 0; j < infoList.size(); j++) {
                
                if (!lang.equals("-")) {
                    if (!lang.equals(infoList.get(j)[0])) {
                        continue;
                    }
                }
                
                if (!devType.equals("-")) {
                    if (!devType.equals(infoList.get(j)[1])) {
                        continue;
                    }
                }
                
                if (!career.equals("-")) {
                    if (!career.equals(infoList.get(j)[2])) {
                        continue;
                    }
                }
                
                if (!food.equals("-")) {
                    if (!food.equals(infoList.get(j)[3])) {
                        continue;
                    }
                }
                
                if (score > Integer.parseInt(infoList.get(j)[4])) {
                    continue;
                }
                count ++;
            }
            
            answer[i] = count;
        }
        
        return answer;
    }
}
```





#### 효율성까지 맞추려면, 받은 info에서 모든 경우의 수를 map에다가 넣는다

- key로는 경우의 값, value는 코딩 테스트 점수로 저장을 한다
- 예) java backend junior pizza 150
  - ---- = 150
  - ---pizza = 150
  - --juniorpizza = 150 등등



#### 그리고 더 빠른 검색을 위해 BinarySearch를 사용한다

- BinarySearch를 하기 전에는 모든 value들을 sort 해야 한다
  - value들은 모두 숫자로 된 리스트로 저장되어 있다



```java
import java.util.*;

class Solution {
    
    static HashMap<String, ArrayList<Integer>> map = new HashMap<>();
    
    public void possibleChoice(String[] array, int count, String str) {
        
        if (count == 4) {
            if (!map.containsKey(str)) {
                ArrayList<Integer> numList = new ArrayList<>(); 
                map.put(str, numList);
            }
            map.get(str).add(Integer.parseInt(array[4]));
            return;
        }
        
        possibleChoice(array, count + 1, str + "-");
        possibleChoice(array, count + 1, str + array[count]);
        
    }
    
    public int binarySearch(ArrayList<Integer> list, int score) {
        int left = 0;
        int right = list.size() - 1;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            
            if (list.get(mid) >= score) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        return list.size() - left;
    }
    
    public int[] solution(String[] info, String[] query) {
        int[] answer = new int[query.length];
        
        for (int i = 0; i < info.length; i++) {
            String[] stringArray = info[i].split(" ");
            possibleChoice(stringArray, 0, "");
        }
        
        for (String key : map.keySet()) {
            Collections.sort(map.get(key));
        }
        
        for (int i = 0; i < query.length; i++) {
            String newQuery = query[i].replace("and ", "");
            
            String[] queryArray = newQuery.split(" ");
            
            int score = Integer.parseInt(queryArray[4]);
            
            String compareString = queryArray[0] + queryArray[1] + queryArray[2] + queryArray[3];
            
            if (map.containsKey(compareString)) {
                ArrayList<Integer> scoreList = map.get(compareString);

                answer[i] = binarySearch(scoreList, score);
            }
        }
        
        return answer;
    }
}
```

