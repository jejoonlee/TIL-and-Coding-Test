# Udemy - Node.js [JavaScript Basics]

*Node.js - The Complete Guide (Udemy)*



## Async Code (비동기식 코드)

> #### 비동기식 코드란?
>
> - 코드를 바로 실행하지 않고, 어느 정도 시간을 주고 코드를 실행하는 것을 비동기식 코드라고 한다

```javascript
setTimeout(() => {
  console.log("안녕")
}, 2000);

console.log('Hello from Node.js');

// Hello from Node.js
// 안녕
```



- **console.log('Hello from Node.js');**
  - 해당 코드는 비동기식 코드가 아니다
  - 해당 코드는, 바로 실행이 된다
- **setTimeout**
  - 비동기식 코드다
  - callback 함수로 인식을 한다
    - 앞에 비동기가 아닌 코드를 실행하고, 2초 뒤에 해당 코드를 callback하는 것
  - 2000milisecond, 즉 2초 기다리고 **console.log("안녕")**를 실행한다



- 즉 원래 코드를 볼 때에는, **'안녕'**이 먼저 실행되고, **'Hello from Node.js'**가 실행되어야 한다 (X 비동기)
  - 코드가 적혀있는대로 실행되는 것
- 비동기는, **'안녕'**은 2초 동안 기다리니깐, 2초 안에 다른 코드를 실행한다
  - 그래서 **Hello from Node.js**, 다음으로 **'안녕'**이 출력된다



