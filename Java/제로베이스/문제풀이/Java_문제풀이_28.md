# 20230726 [Java] 문제풀이 

#### 기초 다지기!!!!!



## [프로그래머스] 수열과 구간 쿼리 4

```java
import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        
        int[] answer = new int[arr.length];
        for(int num = 0; num < arr.length; num++) answer[num] = arr[num];
        
        for (int[] q : queries) {
            for (int i = q[0]; i <= q[1]; i++){
                if (i % q[2] == 0) answer[i] += 1;;
            }
        }
        
        return answer;
    }
}
```





## [프로그래머스] 카운트 

```java
class Solution {
    public int[] solution(int start, int end) {
        int[] answer = new int[end - start + 1];
        
        for (int i = 0; i <= end - start; i ++) answer[i] = i + start;
        
        return answer;
    }
}
```





## [프로그래머스] 배열 만들기

```java
import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int l, int r) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        
        if (l % 5 != 0) {
            int tempL = l / 5;
            l = (5 * (tempL + 1));
        }
        
        for (int i = l ; i <= r; i += 5) {
            
            int num = i;
            boolean isTrue = true;
            
            while (num > 0) {
                int tempI = num % 10;
                
                if (tempI != 5 && tempI != 0) {
                    isTrue = false;
                    break;
                }
                
                num = num / 10;
            }
            
            if (isTrue) answer.add(i);
        }
        
        if (answer.size() == 0) answer.add(-1);
        return answer;
    }
}
```





## [프로그래머스] 문자열 여러 번 뒤집기

```java
class Solution {
    public StringBuffer solution(String my_string, int[][] queries) {
        StringBuffer answer = new StringBuffer();
        answer.append(my_string);
        
        for (int[] q : queries) {
            StringBuffer tempString = new StringBuffer(answer.substring(q[0], q[1] + 1));
            answer.delete(q[0], q[1] + 1);
            answer.insert(q[0], tempString.reverse());
        }
        
        return answer;
    }
}
```





## [프로그래머스] 부분 문자열 이어 붙여 문자열 만들기

```java
class Solution {
    public StringBuffer solution(String[] my_strings, int[][] parts) {
        StringBuffer answer = new StringBuffer();
        
        for (int i = 0; i < my_strings.length; i ++) {
            answer.append(my_strings[i].substring(parts[i][0], parts[i][1] + 1));
        }
        
        return answer;
    }
}
```





## [프로그래머스] 접미사 배열

```java
import java.util.*;
class Solution {
    public String[] solution(String my_string) {
        String[] answer = new String[my_string.length()];
        
        int lastIdx = my_string.length();
        
        for (int i = 0; i < my_string.length(); i ++) {
            answer[i] = my_string.substring(i, lastIdx);
        }
        
        Arrays.sort(answer);
        return answer;
    }
}
```





## [프로그래머스] 배열 만들기 1

```java
import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int n, int k) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        
        for (int i = k; i <= n; i += k) answer.add(i);
        
        return answer;
    }
}
```





## [프로그래머스] 카운트 다운

```java
import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int start, int end) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        
        for (int i = start; i >= end; i --) answer.add(i);
        
        return answer;
    }
}
```



## [프로그래머스] 가까운 1 찾기

```java
class Solution {
    public int solution(int[] arr, int idx) {

        for (int i = idx; i < arr.length; i ++) {
            if (arr[i] == 1)
                return i;
        }
        
        return -1;
    }
}
```





## [프로그래머스] 배열 만들기 3

```java
import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[] arr, int[][] intervals) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        
        for (int[] i : intervals) {
            for (int j = i[0]; j <= i[1]; j ++) answer.add(arr[j]);
        }
        
        return answer;
    }
}
```





## [프로그래머스] 2의 영역

```java
import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int[] arr) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        
        int i = 0;
        int j = arr.length - 1;
        
        while (i < j) {
            if (arr[i] != 2) i++;
            if (arr[j] != 2) j--;
            
            if (arr[i] == 2 && arr[j] == 2) break;
        }
        
        if (i == j && arr[i] == 2) {
            answer.add(2);
        } else if (i < j) {
            for (int idx = i; idx <= j; idx++) {
                answer.add(arr[idx]);
            }
        } else {
            answer.add(-1);
        }
        
        return answer;
    }
}
```





## [프로그래머스] 순서 바꾸기

```java
class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] answer = new int[num_list.length];
        
        int idxCount = 0;
        
        for(int i = n; i < num_list.length; i++) answer[idxCount ++] = num_list[i];
        
        for (int i = 0; i < n; i ++) answer[idxCount++] = num_list[i];
        
        return answer;
    }
}
```





## [프로그래머스] 5명씩

```java
import java.util.*;
class Solution {
    public ArrayList<String> solution(String[] names) {
        ArrayList<String> answer = new ArrayList<String>();
        
        for (int i = 0; i < names.length; i += 5) answer.add(names[i]);
        
        return answer;
    }
}
```





## [프로그래머스] 할 일 목록

```java
import java.util.*;
class Solution {
    public ArrayList<String> solution(String[] todo_list, boolean[] finished) {
        ArrayList<String> answer = new ArrayList<String>();
        
        for (int i = 0; i < todo_list.length; i++) if (!finished[i]) answer.add(todo_list[i]);
        
        return answer;
    }
}
```





## [프로그래머스] 원하는 문자열 찾기

```java
class Solution {
    public int solution(String myString, String pat) {
        myString = myString.toLowerCase();
        pat = pat.toLowerCase();
        
        if (myString.contains(pat)) return 1;
        
        return 0;
    }
}
```





## [프로그래머스] 특정한 문자를 대문자로 바꾸기

```java
class Solution {
    public StringBuffer solution(String my_string, String alp) {
        StringBuffer answer = new StringBuffer();
        
        for (int i = 0; i < my_string.length(); i++) {
            String tempString = String.valueOf(my_string.charAt(i));
            
            if (tempString.equals(alp)) {
                answer.append(tempString.toUpperCase());
            } else {
                answer.append(tempString);
            }
        }
        
        return answer;
    }
}
```



## [프로그래머스] 문자열이 몇 번 등장하는지 세기

```java
class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        
        for (int i = 0; i <= myString.length() - pat.length(); i++) {
            if (myString.substring(i, i+pat.length()).equals(pat)) answer += 1;
        }
        
        return answer;
    }
}
```



## [프로그래머스] 공백으로 구분하기 2

```java
import java.util.*;
class Solution {
    public ArrayList<String> solution(String myString) {
        ArrayList<String> answer = new ArrayList<String>();
        String[] stringA = myString.split("x");
        Arrays.sort(stringA);
        
        for (String s : stringA) {
            if (!s.equals("")) answer.add(s);
        }
        return answer;
    }
}
```

