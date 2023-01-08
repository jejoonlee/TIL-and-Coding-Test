# Udemy - Javascript - Sliding Window



## Sliding Window - maxSubarraySum

Given an array of integers and a number, write a function called **maxSubarraySum**, which finds the maximum sum of a subarray with the length of the number passed to the function.

Note that a subarray must consist of *consecutive* elements from the original array. In the first example below, [100, 200, 300] is a subarray of the original array, but [100, 300] is not.

> 숫자로 이루어진 배열과, 그냥 숫자가 주어진다
>
> 배열에 있는 숫자를, 주어진 숫자만큼 연결해서 덧샘을 해야 한다.
>
> 모든 숫자들은 연결을 해서 더해야 하고, 더한 숫자 중 제일 큰 숫자를 구하는 것이다



```javascript
function maxSubarraySum (array, num) {
    if (array.length < num) {
        return null
    }
    
    maxSum = 0

    for (let j = 0 ; j < num ; j ++) {
        maxSum += array[j]
    }

    if (array.length == num) {
        return maxSum
    }

    let tempSum = maxSum

    for (let i = num ; i < array.length ; i++) {

        tempSum = tempSum - array[i - num] + array[i]

        if (tempSum > maxSum) {
            maxSum = tempSum
        }
    }

    return maxSum
}
```

- 먼저 앞에서 연속으로 더해야 할 만큼의 숫자들을 더한다
- 그 이후로부터, 제일 첫 숫자를 앞에 더했던 숫자에 빼고, 새로 순회한 숫자를 더해준다.



<img src="5_Javascript_문제_풀이_3.assets/image-20230107162846254.png" alt="image-20230107162846254" style="zoom:67%;" />



## **Sliding Window - minSubArrayLen**

Write a function called **minSubArrayLen** which accepts two parameters - an array of positive integers and a positive integer.

This function should return the minimal length of a **contiguous** subarray of which the sum is greater than or equal to the integer passed to the function. If there isn't one, return 0 instead.
Examples:

```javascript
minSubArrayLen([2,3,1,2,4,3], 7) // 2 -> because [4,3] is the smallest subarray
minSubArrayLen([2,1,6,5,4], 9) // 2 -> because [5,4] is the smallest subarray
minSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52) // 1 -> because [62] is greater than 52
minSubArrayLen([1,4,16,22,5,7,8,9,10],39) // 3minSubArrayLen([1,4,16,22,5,7,8,9,10],55) // 5
minSubArrayLen([4, 3, 3, 8, 1, 2, 3], 11) // 2minSubArrayLen([1,4,16,22,5,7,8,9,10],95) // 0
```

Time Complexity - O(n)

Space Complexity - O(1)

> 배열 안에 있는 숫자를 연속으로 더한다
>
> 입력된 배열 말고, 입력된 숫자보다 같거나 커야 한다
>
> 즉 입력된 숫자보다, 작으면 배열에 있는 숫자들을 순회하면서 더한다.
>
> 그렇게 더해서 입력된 숫자보다 적은 숫자들의 개수가 제일 적은 개수를 구하는 것이다

위에 예제에서 1번)

[2, 3, 1, 2, 4, 3] 이 주어지고 7이라는 숫자가 주어진다

- 2 + 3 + 1 + 2  까지 해야 7을 넘는다 (여기서 숫자 4개)
- 그 다음 4, 3 이 있다 (2개)
- 즉 정답은 2개다





