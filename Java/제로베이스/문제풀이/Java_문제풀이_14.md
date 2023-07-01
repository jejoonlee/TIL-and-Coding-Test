# 20230629 [Java] 문제풀이 





## 공원 산책



#### 직사각형 모양의 공원 배열과, 로봇 강아지가 수행해야 하는 명령어가 주어진다



#### 직사각형 모양에는 X (장애물), S (시작점), O (강아지가 갈 수 있는 곳)이 있다



#### 명령어는 "방향, 이동하는칸" 이 주어진다

- E 2 : 동쪽으로 2칸
- W 1 : 서쪽으로 1칸
- N 4 : 북쪽으로 4칸
- S 3 : 남쪽으로 3칸



#### 만약 명령어가 주어지는데, 장애물에 부딛히거나, 공원 밖으로 나갈 경우, 명령어를 실행하지 않고, 다음 명령어로 넘어간다



#### 코드는 매우 길지만 간단하다

1. 시작점의 좌표를 찾기
2. 시작점 기준으로 명령어를 하나씩 꺼내보기
3. 만약 현재 좌표에서 명령어를 실행했을 때에 공원 안으로 들어오면, 4번으로 넘어간다
4. for문을 통해, X, 즉 장애물이 있는지 확인을 해본다
5. 만약 공원 안에도 들어오고, 가려고 하는 길 앞에 장애물이 없다면 명령어를 실행하면 된다



#### 이것을 각 동, 서, 남, 북, 4 방향을 각자의 코드로 작성하다 보니, 코드가 길어졌다

- 로직은 똑같지만, 인덱스가 다 달라서, 인덱스에 따라서 방향마다 if문을 넣어주었다

```java
import java.util.*;

class Solution {
    public int[] solution(String[] park, String[] routes) {
        int[] answer = {};
        int[] start = new int[2];
        // 동, 서, 남, 북
        int[][] direction = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        int vertical = park.length;
        int horizontal = park[0].length();
        
        for (int x = 0; x < park.length; x ++) {
            for (int y = 0; y < park[x].length(); y++) {
                if (park[x].charAt(y) == 'S') {
                    start[0] = x;
                    start[1] = y;
                }
            }
        }
        
        for (int i = 0; i < routes.length; i++) {
            String[] command = routes[i].split(" ");
            int steps = Integer.parseInt(command[1]);
            boolean flag = true;
            
            if (command[0].equals("E")) {
                if (start[1] + (direction[0][1] * steps)  < horizontal) {
                    for (int move = 1; move <= steps; move ++) {
                        if (park[start[0]].charAt(start[1] + move) == 'X') {
                            flag = false;
                            break;
                        }
                    }
                    
                    if (flag) {
                        start[1] += direction[0][1] * steps;
                    }
                }
            } else if (command[0].equals("W")) {
                if (start[1] + (direction[1][1] * steps) >= 0) {
                    for (int move = 1; move <= steps; move ++) {
                        if (park[start[0]].charAt(start[1] - move) == 'X') {
                            flag = false;
                            break;
                        }
                    }
                    
                    if (flag) {
                        start[1] += direction[1][1] * steps;
                    }
                }
            } else if (command[0].equals("S")) {
                if (start[0] + (direction[2][0] * steps)  < vertical) {
                    for (int move = 1; move <= steps; move ++) {
                        if (park[start[0] + move].charAt(start[1]) == 'X') {
                            flag = false;
                            break;
                        }
                    }
                    if (flag) {
                        start[0] += direction[2][0] * steps;
                    } 
                }

            } else if (command[0].equals("N")) {
                if (start[0] + (direction[3][0] * steps)  >= 0) {
                    for (int move = 1; move <= steps; move ++) {
                        if (park[start[0] - move].charAt(start[1]) == 'X') {
                            flag = false;
                            break;
                        }
                    }
                    if (flag) {
                        start[0] += direction[3][0] * steps;;
                    } 
                }
            }
            
        }
        
        return start;
    }
}
```



## 바탕화면 정리

#### 파일을 한번의 드래그를 통해 삭제를 하려고 한다



#### #로 파일들이 들어가 있다



#### 파일들의 위치를 먼저 받는다



#### 파일들의 위치를 순회하면서 minRow, maxRow, minColumn, maxColumn을 구한다

- 여기서 중요한 것은 제일 끝자락에 있는 파일은 좌표에 +1을 해야 한다
- 파일이 하나의 정사각형이라고 생각하면, 그 파일을 삭제하기 위해 드래그를 하려면 왼쪽 위부터 오른쪽 아래까지 드래그를 해야 한다



```java
import java.util.*;

class Solution {
    public int[] solution(String[] wallpaper) {
        int minRow = 50;
        int maxRow = 0;
        int minColumn = 50;
        int maxColumn = 0;
        
        ArrayList<ArrayList<Integer>> fileLocation = new ArrayList<ArrayList<Integer>>();
        
        for (int x = 0; x < wallpaper.length; x++) {
            for (int y = 0; y < wallpaper[x].length(); y++) {
                if (wallpaper[x].charAt(y) == '#') {
                    ArrayList<Integer> location = new ArrayList<Integer>();
                    location.add(x);
                    location.add(y);
                    fileLocation.add(location);
                }
            }
        }
        
        for (int i = 0; i < fileLocation.size(); i++) {
            if (fileLocation.get(i).get(0) < minRow) {
                minRow = fileLocation.get(i).get(0);
            }
            
            if (fileLocation.get(i).get(0) + 1 > maxRow) {
                maxRow = fileLocation.get(i).get(0) + 1;
            }
            
            if (fileLocation.get(i).get(1) < minColumn) {
                minColumn = fileLocation.get(i).get(1);
            }
            
            if (fileLocation.get(i).get(1) + 1 > maxColumn) {
                maxColumn = fileLocation.get(i).get(1) + 1;
            }
        }
        
        int[] answer = {minRow, minColumn, maxRow, maxColumn};
        
        return answer;
    }
}
```

