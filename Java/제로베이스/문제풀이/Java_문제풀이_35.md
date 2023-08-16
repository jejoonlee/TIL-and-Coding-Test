# 20230815 [Java] 문제풀이 







## [프로그래머스] 택배 배달과 수거하기



#### 기본적으로 뒤에서부터 택배를 수거 또는 배달해야, 최소 이동 거리를 구할 수 있다



#### 뒤에서부터 천천히 수거 또는 배달의 개수를 순회한다



#### deliver 또는 pickup의 개수가 음수일 경우 트럭에 택배를 실을 공간이 있다는 것이다



#### 반대로 양수일 경우에는 해당 지점을 while문을 통해 계속 왕복을 해야 한다 (해당 지점에서 택배를 다 처리할 때까지, 즉 음수가 될 때까지)



```java
class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        
        long deliver = 0;
        long pickup = 0;
        
        // 뒤에서부터 계산을 시작해야지, 최소 이동거리를 구할 수 있다
        // 트럭이 한번 뒤로 갔다가, 앞으로 오기 때문에 갔다 온 거리를 *2 를 해야 한다
        
        for (int i = n - 1; i >= 0; i--) {
            // 물건을 배달하거나 수거한다
            deliver += deliveries[i];
            pickup += pickups[i];
            
            // deliever 또는 pickup이 0 이하일 경우는, 트럭에 빈 공간이 있다는 것이다
            while (deliver > 0 || pickup > 0) {
                deliver -= cap;
                pickup -= cap;
                answer += (i + 1) * 2;
            }    
        }
        
        return answer;
    }
}
```





## 마법의 엘리베이터



#### 1의 자리 수부터 차근차근 보면서 10을 나누면서 0을 도달할 때까지의 값을 구하는 것이다



#### 1의 자리 수가 4 이하일 경후 그냥 그 숫자를 빼주면 된다

- answer += storey % 10;



#### 1의 자리 수가 6 이상일 경우는 그 숫자에 10을 뺀만큼, storey에 더한다

- 즉 6이면 10을 만드는 것이 최소로 돌을 사용할 수 있다



#### 1의 자리 수가 5일 경우, 그리고 그 다음의 10의 자리 숫자가 5 이상일 경우에는 5만큼 빼는 것이 아닌, 5만큼 더해주는 것이 최소로 돌을 사용할 수 있다



```java
class Solution {
    public int solution(int storey) {
        int answer = 0;
        
        while (storey != 0) {
            if (storey % 10 <= 5) {
                if (storey % 10 == 5 && (storey / 10) % 10 >= 5) {
                    answer += 10 - (storey % 10);
                    storey += 10 - (storey % 10);
                }
                answer += storey % 10;
            } else {
                answer += 10 - (storey % 10);
                storey += 10 - (storey % 10);
            }
            
            storey /= 10;
        }
        
        return answer;
    }
}
```





