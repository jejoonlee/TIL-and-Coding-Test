# [제로베이스] Java 자료구조 - 힙





#### 힙은 최소힙이 있고, 최대힙이 있다

- 최소힙은 부모 노드가 항상 자식 노드보다 작은 숫자가 들어간다
  - 즉 최소힙에서는 제일 앞에 있는 숫자, 또는 루트 노드가 제일 작은 숫자로 이루어져 있다
- 최대힙은 부모 노드가 항상 자식 노드보다 크기가 크다
  - 즉 최대힙에서는 제일 앞에 있는 숫자, 또는 루트 노드가 제일 큰 숫자로 이루어져 있다



#### 힙은 이진 트리로 만들어져 있다



#### n의 자식 노드를 구할 때에는 (인덱스가 0으로 시작할 때) / 인덱스가 1로 시작할 때에는

- 왼쪽 노드는 **2n + 1**	|	 **2n**
- 오른쪽 노드는 **2n + 2** 	|     **2n + 1**



#### 부모 노드를 구할 때에는 (인덱스가 0으로 시작할 때) / 인덱스가 1로 시작할 때

- **(n - 1) / 2**    |    **n / 2**

![img](https://blog.kakaocdn.net/dn/cdlhmD/btr0nDxuEWb/6Wp6wMJrZ0kwwCxTA0Mf61/img.png)





#### 값을 추가하기 (MaxHeap)

![img](https://blog.kakaocdn.net/dn/djcGge/btr0gDehDRo/VqeG6zGoOtbulOAlzA9rm0/img.png)







#### 제일 큰 값을 빼기 (MaxHeap)

![img](https://blog.kakaocdn.net/dn/bZogoF/btr0hdUcFl9/gTsbEouusk5ROEGo3laBOK/img.png)





