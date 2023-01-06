# Udemy - Javascript



## 일반적인 문제풀이 패턴

#### 빈도수 세기 패턴

- 다중의 입력값들을 비교할 때 유용
- 배열을 이용하는 것이 아닌 / 주어진 입력값을 객체 (`{}`) 에 넣고, 문제를 해결하는 것이다



```javascript
function anagram(word1, word2) {
    
    if (word1.length !== word2.length) {
        return false
    } else if (word1.length === 0 & word2.length === 0) {
        return true
    }

    let anagramObject1 = {}
    let anagramObject2 = {}
    
    for (let word = 0;  word < word1.length ; word++) {
        if (word1[word] in anagramObject1) {
            anagramObject1[word1[word]] += 1
        } else {
        anagramObject1[word1[word]] = 1
        }
    }

    for (let word = 0;  word < word2.length ; word++) {
        if (word2[word] in anagramObject2) {
            anagramObject2[word2[word]] += 1
        } else {
        anagramObject2[word2[word]] = 1
        }
    }

    for (let word in anagramObject1) {
        if (! (word in anagramObject2)) {
            return false
        }
        if (anagramObject2[word] !== anagramObject1[word]) {
            return false
        }
        return true
    }
}


anagram('', '')
```

- 첫 두개의 for문은 **객체** 안에 각 단어의 알파벳과, 그 알파벳의 갯수를 넣는 것이다
- 그리고 마지막 for문은 두 개의 **객체**들을 비교하는 것이다
  - 만약 첫 번째 객체의 단어들을 순회하며, 그 단어가 두 번째 객체에 었으면 `false`를 출력한다
  - 같은 단어가 있지만, 단어의 갯수가 다르면 `false`를 출력한다



## 다중 포인터 패턴

> 포인트를 리스트 안에 넣고, 만약에 그 두 포인트에 대한 값이 원하는 값이 아니면, 포인트 들을 바꾼다

리스트 안에 숫자들이 있다. 그 안에 중복되지 않은 숫자의 개수를 구하는 것.

예시) [1, 1,  2, 2, 2] 의 답은 2 다 (1과 2 밖에 없음)

```python
function countUniqueValues(array) {
    let i = 0
    let j = i + 1
    let result = 1

    if (array.length !== 0) {

    while (j < array.length) {
        if (array[i] === array[j]) {
            j += 1 ;
        } else {
            i = j ;
            j = i + 1 ;
            result += 1 ;
        }
    }
    return result
    } else {
        result = 0
        return result
    }
}
```

- `i` 와 `j` 는 두 개의 포인터다
- `i`의 값과 `j`의 값이 같으면 `j`를 한 단계 뒤로 옮긴다
- `i`와 `j`의 값이 다르면, `result`에 1을 더해주고, `i`를 `j` 위치로 옮기는 동시, `j`를 `i` 뒤에 옮겨 놓는다



## 슬라이딩 윈도우

> 문자열이나 배열의 문제를 해결할때 도움이 된다
>
> 해당 데이터의 하위 집합을 찾는데 유용한다

예시) 문자열이 주어지면, 문자열 안에 알파벳이 중복되지 않고 쓰여지나?

- "hellothere"
  - hel 까지 앞에는 3개 (l 뒤에 또 l 이 있어 멈춘다)
  - 그 뒤에 lother 5개 (다른 겹치는 알파벳이 없다)

```javascript
function maxSubArraySum(array, num) {
    let maxSum = 0
    let tempSum = 0
    
    for (let n = 0 ; n < num ; n ++) {
        tempSum += array[n]
    }

    for (let i = num ; i < array.length ; i ++) {
        tempSum = tempSum - array[i - num] + array[i] ;

        if (tempSum > maxSum) {
            maxSum = tempSum
        }
    }

    return maxSum;
}

maxSubArraySum([2,6,9,2,1,8,5,6,3], 3)
```

- 처음 for문에서는 배열 제일 앞부터, 더해야 하는 숫자들의 값만 먼저 구해서 tempSum에 저장을 한다
- 그 이후, for문을 배열 끝가지 돈다.
  - 여기서 `i`, 인덱스는 배열 끝까지 하나씩 증가를 한다
  - 증가할때마다, `i` 번째의 숫자를 tempSum에 더해주고, 반대로 `i - num` 번째는 빼준다
- 거기서 구한 tempSum 이 maxSum보다 크면, maxSum을 바꿔준다



## 분할과 정복 패턴

> 데이터를 더 적은 덩어리로 줄이는 것이다
>
> 줄이면서 시간 복잡도를 줄이는 것

예시) binary search / binary tree
