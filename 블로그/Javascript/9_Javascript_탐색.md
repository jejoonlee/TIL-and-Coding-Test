# Udemy - Javascript - 탐색



## 선형 탐색 (Linear Search)

> 배열이 있으면, 원소 하나하나를 비교해서 탐색하는것

#### 자바스크립트에서 선형 탐색을 하는 메서드들

- `indexOf`
- `includes`
- `find`
- `findIndex`



### indexOf 를 코드로 표현

```javascript
function linearSearch(array, number){

    for (let i = 0; i < array.length ; i ++) {
        if (array[i] === number) return i;
    }

    return -1
}
```



### Big O

- Best case : O(1)
  - 나오기 굉장히 어렵다
- Worst case : O(n)
- Average : O(n)





## 이진 탐색 (Binary Search)

> 선형 탐색보다 탐색이 훨씬 빠르다
>
> **하지만 이진 탐색은 데이터가 정렬이 되어 있을 때에만 가능하다**

1. 중간 지점을 찾는다
2. 탐색하는 원소가, 중간 지점보다 작거나 큰지 비교를 한다 (데이터 반이 없어지는 것)
3. 그리고 또 중간 지점을 찾는다 (이것을 숫자를 찾을 때까지 반복을 한다)

**즉, 중간 지점을 찾으면, 데이터 절반을 무시할 수 있다**

![image-20230118170630258](9_Javascript_탐색.assets/image-20230118170630258.png)

> 10개를 다 탐색하는 것이 아니라, 4번만 탐색을 하면, 찾고 싶은 값을 찾을 수 있다



