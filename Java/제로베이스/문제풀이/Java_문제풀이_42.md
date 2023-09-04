# 20230828 [Java] 문제풀이 





## [프로그래머스] 전력망을 둘로 나누기



#### 1부터 n까지의 전력망이 있고, 모두 연결이 되어 있다



#### 하나의 연결 선을 끊고 둘로 나누면서, 두 개의 연결되어 있는 노드 그룹의 차이 중, 제일 적은 차이를 출력한다



#### DFS를 통해서, Union Find를 사용했고, 하나의 그룹에 몇 개의 노드가 있는지 찾았다

- 연결선 하나만 자르게 되면, 어차피 2개의 그룹으로 나뉜다



#### (n - nodeCount) - nodeCount 를 통해 두 그룹의 노두 개수의 차이를 구했다



```java
import java.util.*;

class Solution {
    
    public int dfs(ArrayList<ArrayList<Integer>> wr, int[] visited) {
        Stack<Integer> stack = new Stack<>();
        int count = 1;
        
        stack.push(1);
        visited[1] = 1;
        
        while (!stack.isEmpty()) {
            int current = stack.pop();
            
            for (int i = 0; i < wr.get(current).size(); i++) {
                int nextNode = wr.get(current).get(i);
                
                if (visited[nextNode] == 0) {
                    stack.push(nextNode);
                    visited[nextNode] = 1;
                    count ++;
                }
            }
        }
        return count;
    }
    
    
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        
        ArrayList<ArrayList<Integer>> wireRoute = new ArrayList<>();
            
        for (int i = 0; i <= n; i++) wireRoute.add(new ArrayList<>());
            
        for (int i = 0; i < wires.length; i++) {
            wireRoute.get(wires[i][0]).add(wires[i][1]);
            wireRoute.get(wires[i][1]).add(wires[i][0]);
        }
        
        for (int i = 0; i < wires.length; i ++) {
            int w1 = wires[i][0];
            int w2 = wires[i][1];
            
            wireRoute.get(w1).remove(Integer.valueOf(w2));
            wireRoute.get(w2).remove(Integer.valueOf(w1));
            
            
            int nodeCount = dfs(wireRoute, new int[n + 1]);
            int difference = Math.abs((n - nodeCount) - nodeCount);
            answer = Math.min(answer, difference);
            
            wireRoute.get(w1).add(Integer.valueOf(w2));
            wireRoute.get(w2).add(Integer.valueOf(w1));
        }
    
        return answer;
    }
}
```





## [프로그래머스] 피로도



#### 순열을 사용했다

- depth는 순열의 길이를 나타낸다 (m개의 숫자 중 n개의 숫자로 순열을 만들 때, n이 depth가 되는 것)
- 이 문제는 m과 n이 똑같지만, m이 n보다 클 때에, for문에 m이 들어가면 된



```java
public static int[] visited;
public static int[] array;

public void permutations(int cnt, int depth) {

    if (cnt == depth) {
        System.out.println(Arrays.toString(array));
        return;
    }

    for (int i = 0; i < depth; i ++) {
        if (visited[i] == 0) {
            visited[i] = 1;
            array[cnt] = i;
            permutations(cnt + 1, depth);
            visited[i] = 0;
        }
    }
}
```





### 최종 코드

- permutations를 통해서 인덱스 위주로 순열을 구한다
- 그렇게 구한 인덱스를 통해서,  dungeonTravel 메서드를 만들어서, 몇 개의 던전을 탐험할 수 있는지 확인한다

```java
import java.util.*;
class Solution {
    public static int[][] dg;
    public static int[] visited;
    public static int[] array;
    public static int answer;
    
    public void permutations(int cnt, int depth, int k) {

        if (cnt == depth) {
            int life = k;
            int travels = dungeonTravel(array, life);
    
            answer = Math.max(travels, answer);
            
            return;
        }

        for (int i = 0; i < depth; i ++) {
            if (visited[i] == 0) {
                visited[i] = 1;
                array[cnt] = i;
                permutations(cnt + 1, depth, k);
                visited[i] = 0;
            }
        }
    }
    
    public int dungeonTravel(int[] array, int life) {
        
        int count = 0;
        
        for (int i = 0; i < array.length; i++) {
            int[] currentDungeon = dg[array[i]];
            
            if (currentDungeon[0] > life) {
                return count;
            } else {
                life -= currentDungeon[1];
                count += 1;
            }
        }
        
        return count;
    }
    
    public int solution(int k, int[][] dungeons) {
        answer = 0;
        int dLen = dungeons.length;
        dg = dungeons;
        
        visited = new int[dLen];
        array = new int[dLen];
        
        permutations(0, dLen, k);
        
        return answer;
    }
}
```





## [프로그래머스] 주차 요금 계산



#### in과 주차장에 있었던 시간을 저장하는 map을 두 개 만든다



#### 입차를 하면 in에 차량 번호와 시간을 분으로 바꿔서 넣는다



#### 출차를 할 때에는 입차 정보를 가지고 와서 주차를 한 시간을 time 맵에다가 넣는다



#### 이미 차량 번호가 time에 있을 경우는, 기존 주차 시간 정보에, 시간을 더해주면 된다



#### 그런 후 fees, 즉 요금 관련된 배열을 참고하여 차량 주차 요금을 계산하면 된다 



```java
import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[] fees, String[] records) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        HashMap<String, Integer> in = new HashMap<>();
        HashMap<String, Integer> time = new HashMap<>();
        
        for (int i = 0; i < records.length; i++) {
            
            String[] record = records[i].split(" ");
            String[] timeString = record[0].split(":");
            int minTime = Integer.parseInt(timeString[0]) * 60 + Integer.parseInt(timeString[1]);
            String carNumber = record[1];
            
            if (record[2].equals("IN")) {
                in.put(carNumber, minTime);
                
            } else if (record[2].equals("OUT")) {
                
                if (in.containsKey(carNumber)) {
                    if (!time.containsKey(carNumber)) {
                        time.put(carNumber, minTime - in.get(carNumber));
                    } else {
                        int addTime = time.get(carNumber) + (minTime - in.get(carNumber));
                        time.put(carNumber, addTime);
                    }
                    
                    in.remove(carNumber);
                }
            }
        }
        
        int day = 23 * 60 + 59;
        
        for (String carNum : in.keySet()) {
            if (!time.containsKey(carNum)) {
                time.put(carNum, day - in.get(carNum));
            } else {
                time.put(carNum, time.get(carNum) + (day - in.get(carNum)));
            }    
        }
        
        ArrayList<String> list = new ArrayList<>(time.keySet());
        
        Collections.sort(list);
        
        for (String num : list) {
            int parkTime = time.get(num);
            int parkCost = 0;
            
            if (parkTime <= fees[0]) {
                parkCost = fees[1];
                
            } else {
                int partCost;

                if ((parkTime - fees[0]) % fees[2] != 0) {
                    partCost = ((parkTime - fees[0]) / fees[2] + 1) * fees[3];
                } else {
                    partCost = ((parkTime - fees[0]) / fees[2]) * fees[3];
                }
                parkCost = fees[1] + partCost;
            }
            
            answer.add(parkCost);
        }
       
        return answer;
    }
}
```

