# 20230803 [Java] 문제풀이 







## [프로그래머스] 호텔 대실



#### 정렬과 우선순위큐를 사용하였다

- 일단 Book이라는 클래스 안에 시작 시간과 끝나는 시간을 넣어 객체를 만들었다
- 여기서 시작 시간과 끝나는 시간은 시를 60을 곱해서 분으로 만들어서, 나머지 분과 더했다
- 끝나는 시간 같은 경우 10분을 더해서 청소 시간까지 더했다



#### 일단 시작 시간을 기준으로 정렬을 했다



#### rooms라는 우선순위큐를 만들었다

- 이 우선순위큐는 객실 중에서, 제일 먼저 사용이 가능한 객실을 제일 앞으로 올 수 있도록 만들었다
  - 그 뜻은 finish 시간이 제일 적은 Book 객체가 제일 앞으로 오는 것이다



#### 만약에 제일 먼저 끝나는 방의 시간보다 다음 예약 시간이 빠를 경우에는, 다음 예약을 rooms에 넣었다

- 다음 예약자는 새로운 방을 사용해야 한다



#### 그것이 아니면, 지금 사용하는 예약시간과 다음 예약시간을 바꾸기만 하면된다



#### 최종 답안은 우선순위큐의 개수를 반환하면 된다



```java
import java.util.*;
class Book{
    int start;
    int finish;
    
    public Book(int start, int finish) {
        this.start = start;
        this.finish = finish;
    }
}

class Solution {
    public int solution(String[][] book_time) {
        ArrayList<Book> array = new ArrayList<>();
        
        for (String[] s : book_time) {
            String[] time1 = s[0].split(":");
            String[] time2 = s[1].split(":");
            
            int t1 = Integer.parseInt(time1[0]) * 60 + Integer.parseInt(time1[1]);
            int t2 = Integer.parseInt(time2[0]) * 60 + Integer.parseInt(time2[1]) + 10;
            
            Book b = new Book(t1, t2);
            
            array.add(b);
        }
        
        Collections.sort(array, (x1, x2) -> x1.start - x2.start);
        
        PriorityQueue<Book> rooms = new PriorityQueue<>((x1, x2) -> x1.finish - x2.finish);
        
        for (Book b : array) {
            if (rooms.isEmpty()) {
                rooms.add(b);
            } else {
                if (rooms.peek().finish <= b.start){
                    Book tempB = rooms.poll();
                }
                rooms.add(b);
            }
        }
        
        return rooms.size();
    }
}
```
