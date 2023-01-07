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
