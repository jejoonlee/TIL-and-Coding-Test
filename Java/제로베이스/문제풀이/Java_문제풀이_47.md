# 20230912 [Java] 문제풀이 





## [프로그래머스] 스킬 트리



#### 기술을 배우기 위해, 앞에 미리 배워야 하는 기술이 있다

- A ->  B -> C  :  C를 배우려면 B를 배워야 하고, B를 배우려면 A를 배워야 한다
  - 즉 A를 배우고 바로 C를 배울 수 없다



#### 그 외에 주어진 것들은 언제든 배울 수 있다



#### Queue에다가 순서대로 배워야 하는 기술들을 넣는다 (skill들)



#### skill_trees를 순회하면서, Queue 대로 즉 선입선출 로직으로 기술들을 배우는지 확인을 한다

- skill = {A, B, C} 		skill_trees = {B, C}
  - B는 skill에 있지만, 먼저 배워야 하는 A가 있기 때문에 기술을 배울 수 없다



```java
import java.util.*;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        
        for (String skills : skill_trees) {
            
            Queue<Character> skillQueue = new LinkedList<>();
            for (int i = 0; i < skill.length(); i++) skillQueue.add(skill.charAt(i));
            boolean isPossible = true;
            
            for (int i = 0; i < skills.length(); i ++) {
                
                if (!skillQueue.isEmpty()) {
                    if (skillQueue.peek() == skills.charAt(i)) {
                        skillQueue.remove();
                    } else if (skillQueue.contains(skills.charAt(i))) {
                        isPossible = false;
                        break;
                    }
                } else break;
            }
            
            if (skillQueue.isEmpty() || isPossible) answer ++;
        }
        
        return answer;
    }
}
```





## [프로그래머스] 타겟 넘버



#### DFS를 하면서, 숫자들을 더하거나 빼면서, target을 만들 수 있는 경우의 수의 개수를 찾는 것이다



#### 여기서 numbers 배열에 있는 숫자들은 움직일 수 없다



```java
class Solution {
    
    static int count;
    
    public void dfs(int[] numbers, int idx, int max, int target, int addNum) {
        
        if (idx == max) {
            if (addNum == target) count ++;
            return;    
        }
        
        dfs(numbers, idx + 1, max, target, addNum + numbers[idx]);
        dfs(numbers, idx + 1, max, target, addNum - numbers[idx]);
    } 
    
    public int solution(int[] numbers, int target) {

        dfs(numbers, 0, numbers.length, target, 0);
        
        return count;
    }
}
```





## [프로그래머스] 구명 보트



#### 한번에 구명 보트는 2명을 태울 수 있다



#### 먼저 오름차순으로 정렬을 하고 deque에 넣어준다



#### 현재 기다리는 사람들 중에서 제일 무거운 사람과 제일 가벼운 사람 기준으로 제한에 걸리는지 확인을 한다

- 제한에 걸리지 않으면 두 사람이 모두 타고 갈 수 있다
- 그리고 제한에 걸리면 제일 무거운 사람만 보트를 타면 된다



```java
import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        Deque<Integer> deque = new LinkedList<>();
        
        Arrays.sort(people);
        
        for (int p : people) deque.add(p);
        
        while (!deque.isEmpty()) {
            if (deque.getLast() + deque.getFirst() <= limit) {
                deque.pollFirst();
            }
            deque.pollLast();
            answer ++;
            
            if (deque.isEmpty()) break;
        }
        
        return answer;
    }
}
```





## [프로그래머스] 큰 수 만들기



#### 스택을 이용하여 풀이를 했다



#### 스택에 숫자들을 넣으면서, 현재 숫자와 스택에 있는 제일 마지막 숫자를 비교

- 마지막 숫자가 현재 숫자보다 작으면, 스택에서 pop
- 여기서 k가 0이 될 때에는 스택에서 pop을 그만한다 (이후 모든 숫자를 스택에 넣으면 된다)
  - k가 0이라는 것은, 이제 더 이상 제거할 숫자가 없다는 것



#### 마지막으로 k가 0이 아닐 경우, 그만큼 스택에서 숫자를 꺼내준다



```java
import java.util.*;

class Solution {
    
    public String solution(String number, int k) {
        
        String[] nums = number.split("");
        
        Stack<Integer> stack = new Stack<>();
        
        for (String num : nums) {
            int n = Integer.parseInt(num);
            
            if (stack.isEmpty()){
                stack.add(n);
            } else {
                if (k != 0 && n > stack.peek()) {
                    while (n > stack.peek()) {
                        stack.pop();
                        k --;
                        if (k == 0 || stack.isEmpty()) {
                            break;
                        }
                    }
                    stack.add(n);
                } else if (k != 0 && n <= stack.peek()) {
                    stack.add(n);
                } else if (k == 0) {
                    stack.add(n);
                }
            }
        }
        
        for (int i = 0; i < k; i ++) stack.pop();
        
        String answer = stack.toString().replace(", ", "");
        
        return answer.substring(1, answer.length() - 1);
    }
}
```



