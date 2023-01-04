# Udemy - Javascript




## Big O Notation

>  #### 다양한 코드가 있으면, 코드의 성능을 보여주는 것
>
> #### 데이터가 더 많아질 수록, 코드의 성능이 매우 중요해진다



## 성능이 좋은 코드?

#### addUpTo 예시)

> n 이 주어지면 1부터 n까지의 합을 구하는 것4



**for문을 사용하기**

```javascript
function addUpTo (n) {
    let total = 0;
    for (let i = 1; i <= n ; i++) {
        total += i;
    }
    return total;
}
```



**수학적으로 해결하기**

```javascript
function addUpTo (n) {
    return n * (n + 1) / 2;
}
```



#### 두가지 코드가 있을 때에 어떤 것이 더 좋은가?

> 더 좋은 코드의 개념은?
>
> **더 빠르고, 메모리 양을 덜 사용하는 코드가 성능이 더 좋은 코드라고 할 수 있다**



#### 시간을 통해 속도 구하는 방법

> 가장 좋은 방법은 아니다...
>
> - 컴퓨터에 따라 속도가 다를 수 있다
> - 너무 빠르게 진행되어서 시간을 제대로 구할 수 없다

```javascript
function addUpTo (n) {
    return n * (n + 1) / 2;
}

var time1 = performance.now();
addUpTo(1000000000);
var time2 = perfomance.now();
console.log(`Time Elapsed: ${ (time2-time1) / 1000} seconds`)
```

- 위에 `function`을 시작하는 시간을 구한다 (`time1`)
- 그리고 `function`이 끝나는 시간을 구한다 (`time2`)
- `(time2 - time1) / 1000` 을 하면 코드의 속도를 구할 수 있다



#### 컴퓨터가 처리해야하는 연산 갯수를 세는 것

**수학적으로 처리하는 addUpTo**

- `n * (n + 1) / 2;`
  - 여기에는 곱하기, 더하기, 나누기, 총 3개의 연산들이 있다
  - 측 n이 숫자가 뭐가 됬든, 연산을 3번만 하면 된다

**for문으로 처리하는 addUpTo**

- `total += i;`
  - 이 연산만 봐도, n이 더 클 수록, 연산은 n만큼 많아진다
  - 이것 말고도 이 function에도 굉장히 많은 연산이 있다



## What is Big O Notation?

#### 빅오는 대략적으로 숫자를 세는 공식적인 표현이다

#### 입력값에 따른 알고리즘의 실행 시간이 어떻게 되는지 설명하는 공식적인 방법이다

![big-o](1_Javascript_Big_O_Notation.assets/big-o.jpeg)

예시)

- **위에서 수학적으로 풀었던 addUpTo**
  - 빅오로 표현하자면 **O(1)** 



- **for문으로 풀었떤 addUpTo**
  - 빅오로 표현하자면 O(n)
    - n의 값에 따라서, n만큼 연산을 한다



- **for문 안에 for문이 있을 때**
  - 빅오로 표현하면 O(n^2)



```javascript
// ----------- 1번 ---------
function logAtLeast10(n) {
    for (var i = 1; i <= Math.max(n, 10); i++) {
        console.log(i);
    }
}

// ----------- 2번 ----------
function logAtLeast10(n) {
    for (var i = 1; i <= Math.min(n, 10); i++) {
        console.log(i);
    }
}
```

1번 : O(n) 이다. n이 10 이전일때까지는, 지속적으로 10만 출력하다가, 이상으로 가게 되면 **n만큼 숫자를 출력**한다

2번 : O(1) 이다. n이 10 이전까지는 10까지만 출력한다. 하지만 n이 10을 넘어갔을 때에도, **지속적으로 10개**까지 출력한다.



## 공간 복잡도

> #### 공간 복잡도도 Big O Notation을 사용할 수 있다



- 불리언, 숫자, undefined, null은 불변 공간이다 O(1)
- 문자열, reference타입, 배열과 객체는 O(n)

```javascript
// 배열에 있는 숫자들을 더하는 것
function sum(arr) {
    let total = 0;
    for (let i = 0 ; i < arr.length; i++) {
        total += arr[i];
    }
    return total
}
```

- 공간 복잡도는 **0(1) 공간** 이다
  - 새로운 배열을 만드는 것이 아닌, **total** 이라는 변수에 숫자들을 더해주는 것이다



```javascript
// 새로운 배열을 만드는 것이다
function double(arr) {
    let newArr = [];
    for (let i = 0; i < arr.length; i++) {
        newArr.push(2 * arr[i]);
    }
    return newArr;
}
```

- 공간 복잡도는 **O(n) 공간**이다
  - 새로운 배열 안에, n개의 숫자만큼 값을 넣는 것이다



## 로그와 섹션

> #### O(1), O(n), O(n^2) 가 가장 많이 나타나긴 하지만 그 외에도 Big O를 표현할 수 있는 것들이 있다



- #### 로그란?

  - 로그함수와 지수함수는 짝이다
  - 예시)  **log2(8) = 3**
    - 2의 몇 제곱이 8인가?
    - 2 ^ 3 = 8
  - **log === log2**
    - 2를 빼고 사용해도 된다
