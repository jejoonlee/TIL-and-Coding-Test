# Udemy - Javascript



## 객체의 빅오

```java
let instructor = {
    firstName : "Kelly",
    isInstructor: true,
    favoriteNumbers: [1,2,3,4],
}
```

- Key와 Value가 있다
- 객체를 사용할 때
  - 정렬이 필요하지 않을 때
  - 데이터를 빠르게 접근을 하거나, 추가를 하거나, 삭제를 할 때
-  **객체의 빅오**
  - 추가하기 (Insertion) : O(1)
  - 삭제하기 (Removal) : O(1)
  - 찾기 (Searching) : O(N)
    - Value를 찾는 것
  - 데이터에 접근하기 (Access) : O(1)



#### 객체의 메서드 (Object Methods)

- object.keys : O(N)
- object.values : O(N)
- object.entries : O(N)
- hasOwnProperty : O(1)

keys 또는 values 또는 entries를 메서드를 통해 찾을 때에, 배열에 넣어서 찾기 때문에 O(N)이 된다



## 배열의 빅오

```javascript
let names = ["Michael", "Melissa", "Andrea"];

let values = [true, {}, [], 2, "awesome"];
```

- 배열은 정렬이 되어 있다 / 하지만 시간이 걸릴 수 있다

- **배열의 빅오**
  - 추가하기 (Insertion) : 상황에 따라 다르다
  - 삭제하기 (Removal) : 상황에 따라 다르다
  - 찾기 (Searching) : O(N)
  - 데이터에 접근하기 (Access) : O(1)
    - 몇 번째 원소가 필요한지 찾는 것
- insertion / removal 은 제일 뒤에 넣거나 뺄때는 O(1)이다 (넣거나 빼고, 인덱스 숫자를 넣거나 빼기만 하면 된다)
- insertion/ removal 은 제일 앞에 넣으면 O(N)이다 (뒤에 있는 원소들의 인덱스 숫자를 바꿔야 한다)



#### 배열 메서드 빅오

- push : O(1)
- pop : O(1)
  - push 와 pop은 배열의 맨 마지막에 넣는 것이다
- shift : O(N)
- unshift : O(N)
  - shift와 unshift 배열 앞에 넣거나 빼는 것이다
- concat : O(N)
  - 2개 이상의 배열을 연결하는 것 (새로운 인덱스를 만들어야 한다)
- slice : O(N)
  - 배열의 일부분을 자르는 것 (새로운 인덱스를 만들어야 한다)
- splice : O(N)
  - 원소를 없애고, 새로운 원소를 넣는다
- sort : O(N * log N)
  - 
- forEach/map/filter/reduce/etc  : O(N)
