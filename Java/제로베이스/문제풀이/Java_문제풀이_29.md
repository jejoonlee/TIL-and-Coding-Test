# 20230731 [Java] 문제풀이 







## [프로그래머스] 과제 진행하기



#### 하면서 혼자서 디버깅을 계속 하다가, 왜 에러가 뜨는지 찾을 수 있었다

- 값을 출력하면서 디버깅 계속하는 습관 들이기!!!



#### 일단 시작 시간을 시:분 에서 분으로 만들어 놓는다



#### 그리고 다음 과제를 시작할 때에, 현재 과제를 못 끝내면, 현재 과제를 스택에 넣는다



#### 그리고 만약 다음 과제를 끝내기 전에 현재 과제를 끝냈으면 스택에 넣지 않는다

- 대신 다음 과제를 시작하기 전에 시간이 남고, 스택에 과제가 있으면, 그 과제를 진행한다



#### 계속 틀렸던 부분은 while문에서 스택에서 과제를 꺼냈는, 다음 과제를 시작하기 전에 못 끝냈을 때 (else부분)에 break를 넣지 않아서 계속 틀렸다



```java
import java.util.*;

class Homework{
    public String subject;
    public int start;
    public int time;
    
    public Homework(String s, int sT, int time) {
        this.subject = s;
        this.start = sT;
        this.time = time;
    }
    
}

class Solution {
 
    public ArrayList<String> solution(String[][] plans) {
        
        ArrayList<String> answer = new ArrayList<String>();
        
        ArrayList<Homework> array = new ArrayList<>();
        Stack<Homework> stack = new Stack<Homework>();
        
        // homework 객체를 만들어서 array에 넣기
        // 시간 같은 경우 분으로 맞춰서 homework.start에 저장하기
        for (String[] plan : plans) {
            String[] sT = plan[1].split(":");
            int startTime = Integer.parseInt(sT[0]) * 60 + Integer.parseInt(sT[1]);
            Homework homework = new Homework(plan[0], startTime, Integer.parseInt(plan[2]));
            array.add(homework);
        }
        
        // 과제 시작 시간 기준으로 정렬하기
        Collections.sort(array, (x1, x2) -> x1.start - x2.start);
        
        Homework beforeTime = array.get(0);
        
        for (int i = 1; i < array.size(); i++) {
            
            Homework currentTime = array.get(i);
            
            // 다음 과제가 시작하기 전에, 현재 과제를 끝낼 수 있는 경우
            if (beforeTime.time + beforeTime.start <= currentTime.start) {
                answer.add(beforeTime.subject);
                
                // 다음 과제를 시작하기 전에, 현재 과제를 끝내고 시간이 남는 경우
                int posWorkTime = currentTime.start - (beforeTime.time + beforeTime.start);
                
                // 스택에서 과제가 있으면 하나씩 빼서, 다음 과제를 시작하기 전에, 최대한 많은 과제를 끝내려고 해야 한다
                while (posWorkTime > 0) {
                    if (stack.isEmpty()) break;
                    
                    Homework tempH = stack.pop();
                    
                    if (tempH.time <= posWorkTime) {
                        answer.add(tempH.subject);
                        posWorkTime -= tempH.time;
                    } else {
                        tempH.time -= posWorkTime;
                        stack.add(tempH);
                        break;
                    }
                }
            } else {
                // 다음 과제를 시작하기 전에, 현재 과제를 못 끝낼 경우
                beforeTime.time -= (currentTime.start - beforeTime.start);
                stack.add(beforeTime);
            }
            beforeTime = currentTime;
            
        }
        
        stack.add(array.get(array.size() - 1));
        while (!stack.isEmpty()) answer.add(stack.pop().subject);
        
        return answer;
    }
}
```





## [프로그래머스] 광물 캐기

#### 곡갱이는 5개를 캔 후에는 더 이상 사용할 수 없다

- 사용할 수 있는 곡괭이를 아무거나 하나를 선택한다
- 한 번 사용하기 시작한 곡괭이를 사용할 수 없을 때까지 사용한다
- 광물은 주어진 순서대로만 캘 수 있다
- 광산에 있는 모든 광물을 캐거나, 더 사용할 곡괭이가 없을 때까지 광물을 캔다



#### 하나의 곡괭이가 사용할 때에, 5개의 광물을 연속으로 캐는 것이 제일 중요한 포인트다

- 그래서 광물들을 5개씩 묶고, 5개 씩 더해서 우선 순위를 만들었다
  - 광물들의 피로도는 일단 곡괭이가 돌인 기준으로 세웠다
  - 그래야 피로도가 최대인 구간들을 구할 수 있고, 피로도가 제일 심한 구간을 기준으로 내림차순으로 정한다
  - 여기서 중요한 것은 사용할 수 있는 곡괭이가 광물의 구간보다 적을 때에 에러가 뜰 수 있다
    - 곡괭이가 2개 뿐인데, 3개의 구간이 있고, 만약 우선순위 중 3번째 구간이 1등일 때는 성립할 수가 없다
    - 광물은 연속으로 캐야한다



```java
import java.util.*;

class Solution {
    public int solution(int[] picks, String[] minerals) {
        int answer = 0;
        
        int sumPicks = 0;
        for(int num : picks) sumPicks += num;
        
        ArrayList<ArrayList<Integer>> newM = new ArrayList<>();
        
        for (int i = 0; i < Math.ceil((double) minerals.length / 5); i ++) newM.add(new ArrayList<Integer>());
        
        int idx = -1;
        for (int i = 0; i < minerals.length; i ++) {
            if (i % 5 == 0) idx++;
            
            if (minerals[i].equals("diamond")) {
                newM.get(idx).add(25);
            } else if (minerals[i].equals("iron")) {
                newM.get(idx).add(5);
            } else {
                newM.get(idx).add(1);
            }
        }
        
        if (sumPicks < newM.size()) {
            int newArraySize = newM.size() - sumPicks;
            
            for (int i = 0; i < newArraySize; i++) newM.remove(newM.size() - 1);
        }
        
        
        int[][] maxWork = new int[newM.size()][2];
        
        idx = -1;
        for (int i = 0; i < newM.size(); i ++) {
            maxWork[i][0] = i;
            
            for (int num : newM.get(i)) {
                maxWork[i][1] += num;
            }
        }
        
        Arrays.sort(maxWork, (x1, x2) -> x2[1] - x1[1]);
        
        int maxWorkIdx = 0;
        for (int i = 0; i < 3; i ++) {
            if (maxWorkIdx >= maxWork.length) break;
            
            for (int j = 0; j < picks[i]; j++) {
                if (maxWorkIdx >= maxWork.length) break;
                
                for (int k = 0; k < newM.get(maxWork[maxWorkIdx][0]).size(); k++) {
                    if (i == 0) {
                        answer += 1;
                    } else if (i == 1) {
                        if (newM.get(maxWork[maxWorkIdx][0]).get(k) == 25) {
                            answer += 5;
                        } else {
                            answer += 1;
                        }
                    } else { 
                        answer += newM.get(maxWork[maxWorkIdx][0]).get(k);
                    }
                }

                if (picks[i] != 0) {
                    maxWorkIdx ++;
                    if (maxWorkIdx > maxWork.length) break;
                }
            }
        }
        
        return answer;
    }
}
```

