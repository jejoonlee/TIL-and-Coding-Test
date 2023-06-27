# 20230626 [Java] 문제풀이 



## [프로그래머스] 한 번만 등장한 문자

#### 문자열이 주어진다

#### 문자열 안에, 단어가 한번만 나오는 단어를, 사전 순으로 정렬해서 출력을 한다

- ASCII 코드를 사용하여, 단어들을 숫자로 바꾸고 Collections.sort(); 를 이용해서 정렬을 하고 단어로 바꿔준다



```java
import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        ArrayList<Integer> sortList = new ArrayList<Integer>();
        int tempVal;
        
        HashMap<Character, Integer> hashMap = new HashMap<Character, Integer>();
        
        // 단어의 개수를 해쉬에 넣는다
        for (int i = 0; i < s.length(); i++) {
            if (hashMap.containsKey(s.charAt(i))) {
                tempVal = hashMap.get(s.charAt(i));
                hashMap.put(s.charAt(i), tempVal + 1);
            } else {
                hashMap.put(s.charAt(i), 1);
            }
        }
        
        // 단어의 개수가 하나인 단어를 정렬하기 위해 리스트에 넣는다
        // 이때 숫자로 변환하며 sortList에 넣을 것
        for (Character key : hashMap.keySet()) {
            if (hashMap.get(key) == 1) {
                sortList.add((int)key);
            }
        }
        
        // 정렬하기
        Collections.sort(sortList);
        
        // 정렬된 것을 answer에 단어로 변환하면서 넣는다
        for (int num : sortList) {
            answer += (char) num;
        }
        
        return answer;
    }
}
```





## [프로그래머스] 배열 회전시키기

#### right 또는 left라는 명령어가 주어진다

#### 명령을 따라 배열을 한칸씩 오른쪽 또는 왼쪽으로 옮긴다

#### deque을 사용했다

- 끝 부분에서 값을 뺼 수 있고, 넣을 수 있다
- 그리고 앞 부분에서도 값을 뺼 수 있고, 넣을 수 있다



```java
import java.util.*;

class Solution {
    public Deque<Integer> solution(int[] numbers, String direction) {
        
        Deque<Integer> deque = new LinkedList<Integer>();
        
        for (int i = 0; i < numbers.length; i++) deque.offer(numbers[i]);
        
        if (direction.equals("right")) {
            int lastNum = deque.pollLast();
            deque.offerFirst(lastNum);
        } else {
            int firstNum = deque.pollFirst();
            deque.offer(firstNum);
        }
        
        return deque;
    }
}
```





## [백준] 5613 계산기 프로그램

#### 나와 있는 그래도 구현을 하면 되는 프로그램이다

- +, -, *, / 는 연산이고, = 을 하면 while문을 끝내고, 답을 출력해준다



```java
import java.util.*;

public class Baekjoon5613 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int answer = 0;
        int calculate = 0;

        while (true) {
            String command = scanner.next();

            if (command.equals("=")) {
                break;
            } else if (command.equals("+")) {
                calculate = 0;
            } else if (command.equals("-")) {
                calculate = 1;
            } else if (command.equals("*")) {
                calculate = 2;
            } else if (command.equals("/")) {
                calculate = 3;
            } else {
                if (calculate == 0) {
                    answer += Integer.parseInt(command);
                } else if (calculate == 1) {
                    answer -= Integer.parseInt(command);
                } else if (calculate == 2) {
                    answer *= Integer.parseInt(command);
                } else if (calculate == 3) {
                    answer /= Integer.parseInt(command);
                }
            }
        }

        System.out.println(answer);
    }
}
```





## [백준] 트리의 부모 찾기

#### 트리가 주어지고, 각 2번 노드부터 부모 노드를 찾는 것이다

#### 1번 노드가 루트 노드라고 생각하고 문제를 풀면 된다

#### BFS를 사용하여, 자식 노드들을 탐색할 때에, 부모 노드를 answer에 저장한다

- answer은 노드들의 값이다 
- 즉 자식 노드들을 인덱스로 사용하고, 현재 노드를 인덱스에 저장을 해주면 된다



```java
import java.util.*;
public class Baekjoon11725 {

    public static int[] bfs(int start, ArrayList<ArrayList<Integer>> adjList) {
        Queue<Integer> queue = new LinkedList<Integer>();
        boolean[] visited = new boolean[adjList.size()];
        int[] answer = new int[adjList.size()];

        queue.offer(start);
        visited[start] = true;

        while (queue.size() != 0) {
            int current = queue.poll();

            for (int cur : adjList.get(current)) {
                if (visited[cur] == false) {
                    queue.offer(cur);
                    visited[cur] = true;

                    // 부모 노드 저장
                    answer[cur] = current;
                }
            }

        }
        return answer;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();

        int n = scanner.nextInt();
        for (int i = 0 ; i <= n; i++) adjList.add(new ArrayList<Integer>());

        for (int j = 0; j < n - 1; j++) {
            int nodeA = scanner.nextInt();
            int nodeB = scanner.nextInt();
            adjList.get(nodeA).add(nodeB);
            adjList.get(nodeB).add(nodeA);
        }

        int[] answer = bfs(1, adjList);

        for (int i = 2; i <= n; i++) {
            System.out.println(answer[i]);
        }
    }
}
```

