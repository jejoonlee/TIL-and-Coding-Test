# Udemy - Javascript - Frequency Counter



## Frequency Counter

Write a function called **sameFrequency.** Given two positive integers, find out if the two numbers have the same frequency of digits.

Your solution MUST have the following complexities:

Time: O(N)

Sample Input:

```javascript
sameFrequency(182,281) // true
sameFrequency(34,14) // false
sameFrequency(3589578, 5879385) // true
sameFrequency(22,222) // false
```

> sameFrequency라는 function 코드를 짜는 것이다. 두 개의 양수의 정수가 주어진다. 주어진 두 숫자를 비교하여, 같은 숫자들이 같은 개수만큼 있는지 구하여라.
>
> 시간 복잡도는 O(N)이어야 한다



#### 풀이 설명

- 일단 시간 복잡도가 O(N)이어야 하는 것이 제일 중요하다
- 배열을 사용하면 쉽고 더 짧게 코드를 짤 수 있을테지만, 이중 for문을 사용해야 해서 O(N)을 만들 수가 없다
  - 그래서 객체를 이용해서 문제를 풀었다
- 일단 주어진 숫자들을 문자열로 바꾼다
  - 문자열로 바꿔야지, 숫자 하나하나를 순회할 수 있다
- 먼저 두 문자열 중 하나를 객체 안에다 넣는다
  - 여기서, 객체 안에 없는 숫자면 `숫자를 key`로 그리고 `1 (숫자의 갯수)를 value`로 넣는다
  - 그리고 객체 안에 있는 숫자면, 그 숫자의 value에 1을 누적시킨다
- 두번째 for문에서는 다른 하나의 문자열을 비교하는 것이다
  - 두번째 문자열을 순회를 한다
  - 순회하면서, 해당 숫자가 객체 존재해야 하고, 값이 0이면 안된다
    - 순회하는 숫자가 객체 안에는 존재하지만, 값이 0이면, 두번째 문자열에서 그 숫자를 하나 더 가지고 있다는 뜻이다



#### 풀이 코드

```javascript
function sameFrequency(num1, num2) {
    num1 = String(num1) ;
    num2 = String(num2) ;

    if (num1.length !== num2.length) {
        return false
    }

    numObject = {} ;
    
    for (let number = 0 ; number < num1.length ; number ++) {
        if (!(num1[number] in numObject )) {
            numObject[num1[number]] = 1 ;
        } else {
            numObject[num1[number]] += 1 ;
        }
    }

    // num2의 숫자가 numObject에 없는 경우
    // num2의 숫자가 numOject에 있는 수보다 많을 경우
    
    for (let num = 0 ; num < num2.length ; num ++) {
        if (!(numObject[num2[num]])) {
                return false               
            }
        if (num2[num] in numObject) {
            numObject[num2[num]] -= 1
            if (numObject[num2[num]] == -1) {
                return false
            }
        }
    }

    return true
}
```





## Frequency Counter / Multiple Pointers

Implement a function called, **areThereDuplicates** which accepts a **variable number of arguments,** and checks whether there are any duplicates among the arguments passed in. You can solve this using the frequency counter pattern OR the multiple pointers pattern.

Examples:

```javascript
areThereDuplicates(1, 2, 3) // false
areThereDuplicates(1, 2, 2) // true 
areThereDuplicates('a', 'b', 'c', 'a') // true 
```

**Restrictions:**

Time - O(n)

Space - O(n)

**Bonus:**

Time - O(n log n)

Space - O(1)

> `areThereDuplicates` 라는 function은 여러 개수의 arguments를 받는 function이다 (고정된 숫자가 아니다). arguments를 받을 때에, 중복되는 숫자 또는 문자가 있는지 확인을 하는 function이다. 빈도수 세기 패턴 또는 투 포인터를 사용해서 풀면 된다.



#### Frequency Counter

> 여러개의 arguments를 입력 받을 때에는, `arguments` 라는 배열 같은 객체를 쓰면 된다

```javascript
function areThereDuplicates() {
    
    argumentObject = {}
    
    for (let i in arguments) {
        if (arguments[i] in argumentObject) {
            return true
        } else {
            argumentObject[arguments[i]] = 1
        }
    }

    return false
}
```

- 위에 했던 `sameFrequency`보다 쉬웠다.
- 똑같이 객체에, 입력 받은 입력값들을 넣는다
  - 여기서 다른 것은, 만약 입력값이 객체에 존재하면, 바로 `true`를 출력한다
    - 입력값이 객체에 존재한다는 것은, 같은 값이 2번 나온다는 것이다
  - 반대로, 지속적으로 다른 입력값만 객체에 넣게 되면, 마지막에 `false`를 출력하면 된다



#### Multi pointers

> function에 arguments에 `(...args)` 를 하면 arguments 숫자는 곶

```javascript
function areThereDuplicates(...args) {
    let array = args ;
    array.sort() ;

    console.log(array)

    for (let i = 0 ; i <= array.length - 1 ; i ++) {
        if (array[i] === array[i + 1]) {
            console.log(array[i], array[i+1])
            return true
        }
    }

    return false
}
```

- 투 포인터를 이용한 것
- 오름차순으로 정렬을 한다.
- 배열을 순회하는데, 해당 인덱스랑, 인덱스 앞에 있는 숫자가 같으면 `true`를 출력
- 그게 끝까지 아니면 `false`를 출력한다
