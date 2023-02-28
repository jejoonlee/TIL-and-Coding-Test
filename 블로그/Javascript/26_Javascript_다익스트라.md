# Udemy - Javascript - Dijkstra's Algorithm

*Udemy JavaScript*



## 다익스트라 알고리즘

> #### 그래프와 우선순위 큐를 알고 있어야 한다



#### 두 정점 사이에서 제일 짦은 경로를 계산한다



#### 사용성

- GPS - 제일 짧은 거리
- Network Routing - 데이터를 송신할 수 있는 최단 거리
- Biology - 코로나 바이러스 전파
- Airline Tickets - 도착지까지 제일 가격이 저렴한 비행기 티켓을 구할 때 
- 등등



## 가중치 그래프 작성

> #### 그래프를 만들때에 똑같지만, addEdge 쪽에 weight을 추가한다

```javascript
class WeightedGraph {
    constructor(){
        this.adjacencyList = {};
    }
    
    addVertex(vertex){
        if (!this.adjacencyList[vertext]) this.adjacencyList[vertex] = [];
    }
    
    addEdge(vertex1, vertex2, weight) {
        this.adjacencyList[vertex1].push({node: vertex2, weight});
        this.adjacencyList[vertex2].push({node: vertex1, weight});
    }
}
```



