# Udemy - Javascript - Multiple Pointers



## Multiple Pointers - averagePair

Multiple Pointers - averagePair

Write a function called **averagePair.** Given a sorted array of integers and a target average, determine if there is a pair of values in the array where the average of the pair equals the target average. There may be more than one pair that matches the average target.

**Bonus Constraints:**

Time: O(N)

Space: O(1)

> 정렬된 배열이 주어진다. 어떤 두 숫자의 평균이, 배열의 평균과 같아지는지 찾는 것이다.

```javascript
function averagePair(array, num){
    let i = 0
    let j = array.length - 1

    while (i < j) {
        if ((array[i] + array[j])/2 === num) {
            return true
        } else if ((array[i] + array[j])/2 < num) {
            i ++
        } else if ((array[i] + array[j])/2 > num) {
            j --
        }
    }

    return false
}
```

- `i` 와 `j` 는 두 개의 투 포인터이다
  - `i`는 맨 앞에서 시작하고
  - `j`는 맨 뒤에서 시작한다
- 기본적으로 배열에 있는 두 숫자들을 더한 후, 2로 나누어서 두 숫자의 평균을 구한다
  - 두 숫자의 평균이 `num`보다 작으면 `i` 포이터를 1을 누적시켜서, 오른쪽으로 한칸 올라간다
  - 두 숫자의 평균이 `num`보다 크면 `j` 포인터에서 1을 뺀다
  - 그리고 `num`와 두 숫자의 평균이 같으면, `true`를 출력한다
- 만약 `true`를 출력하지 못 하고, while문을 끝까지 실행했다면 `false`를 출력해야 한다



## Multiple Pointers - isSubsequence

Write a function called **isSubsequence** which takes in two strings and checks whether the characters in the first string form a subsequence of the characters in the second string. In other words, the function should check whether the characters in the first string appear somewhere in the second string, **without their order changing.**

Your solution MUST have AT LEAST the following complexities:

Time Complexity - O(N + M)

Space Complexity - O(1)

> 두 개의 문자열을 받는다.  두 문자열 중, 첫번째 문자열의 알파벳들이 순서대로 두번째 문자열에 있는지 확인하는 것이다. 모든 문자열 바꿀 수 없다
>
> 예시)
>
> `isSubsequence('abc', 'acb'); // false (order matters)`
>
> - 같은 알파벳이 있지만, `true`가 되기 위해서는 두번째 문자열도 'abc'이어야 한다
>
> `isSubsequence('sing', 'sting'); // true`
>
> - 두번째 문자열에, 중간에 `t`가 있지만, 그 이후로 순서대로 첫번째 문자열과 알파벳들이 나열되어 있어, `true`다



```javascript
function isSubsequence(string1, string2) {
    let i = 0
    let j = 0

    while (j < string2.length) {
        if (string1[i] === string2[j]) {
            i ++
            j ++
        } else if (string1[i] !== string2[j]) {
            j ++
        }

        if (i === string1.length) {
            return true
        }
    }

    return false
}
```

- 투 포인터를 사용하는 것인데, `string1` 에 포인터 한개, `string2`에 포인터 한개를 사용한다
- 처음 시작은 제일 앞에 있는 알파벳부터 시작을 한다
- while문은 `string2`를 다 돌았을 때 끝난다.
  - 만약 `string1`에서 `i`번째 인덱스의 값이, `string2`의 `j`번째 인덱스의 값과 같으면, `i`와 `j`에 모두 1씩 더한다
  - 값이 다르면 `j`를 한칸 움직인다
  - 그리고 `string1`을 while문이 끝나기 전에, 다 돌았으면, `true`를 출력한다
- while문을 그대로 끝냈으면 `false`로 출력한다
