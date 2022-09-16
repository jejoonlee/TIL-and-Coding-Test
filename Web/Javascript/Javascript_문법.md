# 📋Web JavaScript

#### Category

[ECMA Script](#%EF%B8%8F-ECMA-Script)

[변수와 식별자](#%EF%B8%8F-변수와-식별자)

[연산자](#%EF%B8%8F-연산자)

[조건문](#%EF%B8%8F-조건문)

[반복문](#%EF%B8%8F-반복문)

[함수](#%EF%B8%8F-함수)

[Arrow Function](#%EF%B8%8F-Arrow-Function)

[문자열](#%EF%B8%8F-문자열)

[배열](#%EF%B8%8F-배열)

[객체](#%EF%B8%8F-객체)





## ✔️ ECMA Script

> 코딩 스타일의 핵심은 합의된 원칙과 일관성
>
> - 절대적인 하나의 정답은 없으며, 상황에 맞게 원칙을 정하고 일관성 있게 사용하는 것이 중요
>
> 코딩 스타일은 코드의 품질에 직결되는 중요한 요소
>
> - 코드의 가독성, 유지보수 또는 팀원과의 커뮤니케이션 등 개발 과정 전체에 영향을 끼침

[참고](https://github.com/airbnb/javascript#variables--unary-increment-decrement)



## ✔️ 변수와 식별자

> 식별자 (identifier)는 변수를 구분할 수 있는 변수명을 말함
>
> 식별자는 반드시 문자, 달러 ($), 또는 밑줄 (_)로 시작
>
> 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
>
> 예약어* 사용 불가능

- (참고) 선언, 할당, 초기화
- **선언 (Declaration)**
  - 변수를 생성하는 행위 또는 시점

```javascript
let foo				// 선언
console.log(foo)	// undefined
```

- **할당 (Assignment)**
  - 선언된 변수에 값을 저장하는 행위 또는 시점

```javascript
foo = 11			// 할당
console.log(foo)	// 11
```

- **초기화 (Initialization)**
  - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

```javascript
let bar = 0			// 선언 + 할당
console.log(bar)	// 0
```



### let, const

**`let` 은 변수의 값에 재할당이 가능**

```javascript
let number = 10		// 1. 선언 및 초기값 할당
number = 10			// 2. 재할당

console.log(number)	// 10
```

**`const` 는 변수의 값에 재할당이 불가능하다**

```javascript
const number = 10 	// 1. 선언 및 초기값 할당
number = 10 		// 2. 재할당 불가능
```



**`let`과 `const`는 재선언이 불가능 하다**

```javascript
let number = 10
let number = 50

const number = 10
const number = 50

// 위 둘은 불가능 하다
```



**`let`과 `const`는 블록 스코프 (block scope)를 가지고 있다**

```javascript
let x = 1

if (x === 1) {
    let x = 2
    console.log(x)	// 2
}

console.log(x)		// 1
```

Block Scope는 `if`, `for`, `함수` 등의 중괄호 내부를 가리킨다

블록 스코프를 가지는 변수는 블록 바깥에서 접근이 불가능 하다



### VAR

- var로 선언하는 변수는 재선언 및 재할당 모두 가능하다
- 하지만 호이스팅 되는 특성으로 인해 예기치 못한 문제 발생이 가능하다
  - 호이스팅 (hoisting) : 끌어 올리는 것
  - `var`을 선언한 변수의 경우 호이스팅 시 undefined로 변수를 초기화한다
  - 반대로 `let` 와 `const`로 선언한 변수의 경우 호이스팅 시 변수를 초기화하지 않는다

```javascript
console.log(username)		// undefined
var username = '홍길동'

console.log(email)			// Uncaught ReferenceError
let email = 'gildong@gmail.com'	// 초기화

console.log(age)			// Uncaught ReferenceError
const age = 50					// 초기화
```



### let, const, var 비교

| 키워드  | 재선언 | 재할당 |   스코프    |     비교     |
| :-----: | :----: | :----: | :---------: | :----------: |
|  `let`  |   X    |   O    | 블록 스코프 | ES6부터 도입 |
| `const` |   X    |   X    | 블록 스코프 | ES6부터 도입 |
|  `var`  |   O    |   O    | 함수 스코프 |    사용 X    |

[⬆️ back to top](#category)



## ✔️ 데이터 타입

> JavaScript의 모든 값은 특정한 데이터 타입을 가진다
>
> 크게 **원시 타입 (Primitive Type)**과 **참조 타입 (Reference Type)**으로 분류된다

#### 원시 타입 (Primitive Type)

- **Number / String /Boolean**
- **Undefined / null / Symbol**

#### 참조 타입 (Reference Type)

- **Objects**
  - **Array / Function / etc**

[⬆️ back to top](#category)





### 원시 타입

> Primitive Type

객체 (Object)가 아닌 기본 타입

- 변수에 해당 타입의 값이 담긴다
- 다른 변수에 복사할 때 실제 값이 복사됨

```javascript
let message = '안녕하세요!'		// 1. message 선언 및 할당

let greeting = message		   // 2. greeting에 message 복사
console.log(greeting)		   // 3. '안녕하세요!' 출력

message = 'Hello, world!'	   // 4. message 재할당
console.log(greeting)		   // 5. 'Hello, world!' 출력
```

- #### 숫자 (Number) 타입

  - 정수, 실수 구분 없는 하나의 숫자 타입

```javascript
const a = 13			// 양의 정수
const b = -5			// 음의 정수
const c = 3.14			// 실수
const d = 2.99e8		// 거듭제곱
const e = Infinity		// 양의 무한대
const f = - Infinity	// 음의 무한대
const g = NaN			// Not a Number
```

- #### 문자열 (string) 타입

  - 텍스트 데이터를 나타내는 타입
  - 작은 따옴표 또는 큰 따옴표 모두 가능

```javascript
const firstName = 'Alex'
const lastName = 'Lee'
const fullName = `${firstName} ${lastName}`

console.log(fullName) // Alex Lee

/* `${}` 는 파이선에서 f-string과 같은 역할을 한다
대신 따옴표 대신 backtick(``)을 사용한다 */
```



- #### Undefined

  - 변수의 값이 없음을 나타내는 데이터 타입

```javascript
let firstName
console.log(firstName) // undefined
```



- #### null

  - 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입

```javascript
let firstName = null
console.log(firstName) // null

typeof null // object, typeof는 자료형 평가를 위한 연산자
```



- #### Boolean 타입

  - 논리적 참 또는 거짓을 나타내는 타입
  - true 또는 false로 표현

```javascript
let isAdmin = true
console.log(isAdmin) // true

idAdmin = false
console.log(isAdmin) // false
```

|  데이터 타입  |    거짓    |        참        |
| :-----------: | :--------: | :--------------: |
| **Undefined** | 항상 거짓  |        X         |
|   **Null**    | 항상 거짓  |        X         |
|  **Number**   | 0, -0, NaN | 나머지 모든 경우 |
|  **String**   | 빈 문자열  |  나머지 모든 경  |
|  **Object**   |     X      |     항상 참      |

[⬆️ back to top](#category)



### 참조 타입

> Reference type

객체 (object) 타입의 자료형

- 변수에 해당 객체의 참조 값이 담김
- 다른 변수에 복사할 때 참조 값이 복사됨

```javascript
const message = ['안녕하세요']	// 1. message 선언 및 할당

const greeting = message	   // 2. greeting에서 message 복사
console.log(greeting)		   // 3. ['안녕하세요'] 출력

message[0] = ['Hello, world!'] // 4. message에 재할당
console.log(greeting)		   // 5. ['Hello, world!'] 출력
```

[⬆️ back to top](#category)



## ✔️ 연산자

### 할당 연산자

```javascript
let x = 0			// 0

x += 10
console.log(x)		// 10

x -= 3
console.log(x)		// 7

x *= 10
console.log(x)		// 70

x /= 10
console.log(x)		// 7

x++					// += 1 와 동일
console.log(x)		// 8

x--					// -= 1 와 동일
console.log(x)		// 7
```



### 비교 연산자

```javascript
const numOne = 1
const numTwo = 100
console.log(numOne < numTwo) // true

const charOne = 'a'
const charTwo = 'z'
console.log(charOne > charTwo) // false
/* 알파벳끼리 비교할 경우
		알파벳 순서상 후 순위가 더 크다
		소문자가 대문자보다 더 크다 */
```



### 일치 비교 연산자

> ===

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환

```javascript
const a = 1004
const b = '1004'
console.log(a === b) // false

const c = 1
const d = true
console.log(c === d) // false
```

'==' 도 동등 비교 연샂나로 있지만 특별한 경우를 제외하고 사용하지 않는다

- 압묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교

```javascript
const a = 1004
const b = '1004'
console.log(a === b) // true

const c = 1
const d = true
console.log(c === d) // true

// 자동 타입 변환 예시 //
console.log(a + b) // 10041004
console.log(c + d) // 2
```



### 논리 연산자

`&&`  : and 연산

`||` : or 연산

`!` : not 연산

```javascript
// and 연산
console.log(true && false)	// false
console.log(true && true)	// true
console.log(1 && 0)			// 0
console.log(4 && 7)			// 7
console.log('' && 5)		// ''

// or 연산
console.log(true || false)	// true
console.log(false || false)	// false
console.log(1 || 0)			// 0
console.log(4 || 7)			// 4
console.log('' || 5)		// 5

// not 연산
console.log(!true)			// false
console.log(!'bonjour!')	// false
```



### 삼항 연산자 (Ternary Operator)

- 세 개의 피연산자를 사용하여 조건에 따라 값을 변환하는 연산자
- 가장 왼쪽의 조건식이 참이면 콜론(:) 앞의 값을 사용하고 그렇지 않으면 콜론(:) 뒤의 값을 사용

```javascript
console.log(true ? 1 : 2)		// 1
console.log(false ? 1 : 2)		// 2

/* Math.PI가 4보다 큰가? 사실이면 : 기준 왼쪽의 값을
거짓이면 : 기준 오른쪽의 값을 출력해라 */ 
const result = Math.PI > 4 ? 'Yes' : 'No'
console.log(result)				// No
```

[⬆️ back to top](#category)



## ✔️ 조건문

> `if` statement
>
> - 조건 표현식의 결과값을 Boolean 타입으로 변환 후 참/거짓을 판단
>
> `switch` statement
>
> - 조건 표현식의 결과값이 어느 값(case)에 해당하는지 판별
> - 조건이 많아질 경우 if문보다 가독성이 나을 수 있다
> - break가 필요함



#### if 문

> if , else if , else
>
> - 조건은 소괄호 (condition) 안에 작성
> - 실행할 코드는 중괄호{} 안에 작성

```javascript
const nation = 'Korea'

if (nation === 'Korea') {
    console.log('안녕하세요!')
} else if (nation === 'France') {
    console.log('Bonjour!')
} else {
    console.log('Hello')
}
```



#### switch statement

> 표현식 (expression)의 결과값을 이용한 조건문
>
> 표현식의 결과값과 case 문의 오른쪽 값을 비교
>
> break 및 default문은 [선택적]으로 사용 가능
>
> break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행

```javascript
switch(expreesion) {
    case 'first value': {
        // do something
        [break]
    }
    case 'second value': {
        // do something
        [break]
    }
    [default: {
     // do something
     }]
}
```

예시)

```javascript
const nation = 'Korea'

switch(nation) {
    case 'Korea': {
        console.log('안녕하세요!')
        break
    }
    case 'France': {
        console.log('Bonjour!')
        break
    }
    default: {
        console.log('Hello!')
    }
}
```

- 만약 두 case 들에 `break`가 없으면 '안녕하세요!', 'Bonjour!', 'Hello!' 가 다 출력이 된다

[⬆️ back to top](#category)



## ✔️ 반복문

> `while` / `for` / `for... in` / `for...of`

### while

> 조건문이 참(true)인 동안 반복 시행
>
> 조건은 소괄호 안에 작성
>
> 실행할 코드는 중괄호 안에 작성

```javascript
while(condition) {
    // do something
}

// 예시

let i = 0

while (i < 6) {
    console.log(i)	// 0, 1, 2, 3, 4, 5
    i += 1
}
```



### for

> 세미콜론 (;) 으로 구분되는 세 부분으로 구성
>
> initialization
>
> - 최초 반복문 진입 시 1회만 실행되는 부분
>
> condition
>
> - 매 반복 시행 전 평가되는 부분
>
> expression
>
> - 매 반복 시행 이후 평가되는 부분

```javascript
for (initialization; condition; expression) {
    // do something
}

// i는 0으로 초기화 initialization (let i = 0)
// i는 6 미만일 때까지 condition (i < 6)
// i를 1씩 증가시킨다 (i++)
for (let i = 0; i < 6; i++) {
    console.log(i)	// 0, 1, 2, 3, 4, 5
}
```



### for...in

> **객체(object)의 속성(key)들을 순회할 때 사용**
>
> 배열도 순회 가능하지만 권장하지 않음
>
> 실행할 코드는 중괄호 안에 작성

```javascript
for (variable in object) {
    // do something
}

// 예시
const capitals = {
    Korea: 'Seoul',
    France: 'Paris',
    USA: 'Washinton D.C.'
}

for (let capital in capitals) {
    console.log(capital) // Korea, France, USA
}
```



### for...of

> 반복 가능한 (iterable) 객체를 순회하며 값을 꺼낼 때 사용
>
> 실행할 코드는 중괄호 안에 작성

```javascript
for (varibale of iterables) {
    // do something
}

// 예시
const fruits = ['딸기', '바나나', '멜론']

for (let fruit of fruits) {
    fruit = fruit + '!'
    console.log(fruit)
}
// 딸기!, 바나나!, 멜론!
```



#### for...in VS for...of

**array를 사용했을 경우**

- `for...in` : 각 요소의 인덱스를 출력한다
- `for...of` : object에 있는 key를 출력한다

**Object를 사용했을 경우**

- `for...in` : 각 요소들을 출력한다
- `for...of` : 에러 메세지가 뜬다

[⬆️ back to top](#category)



## ✔️ 함수

> 참조 타입 (Reference Type) 중 하나로써 function 타입에 속한다
>
> 주로 함수 선언식 / 함수 표현식으로 2가지로 구분한다
>
> 함수 선언식 - 익명 함수 불가능 / 호이스팅 가능
>
> 함수 표현식 - 익명 함수 가능 / 호이스팅 불가능

#### 함수 정의

- 함수의 이름과 함께 정의하는 방식
- 3가지 부분으로 구성
  - 함수의 이름 (Name) / 매개변수 (args) / 함수 body (중괄호 내부)

```javascript
function name(args) {
    // do something
}
----------------------------------------
function add(num1, num2) {
    return num1 + num2
}

add(1, 2)
```



#### 함수 표현식

- 함수를 표현식 내에서 정의하는 방식
  - 표현식이란 어떤 하나의 값으로 결정되는 코드의 단위
- 함수의 이름을 생략하고 익명 함수로 정의 가능
- 3가지 부분으로 구성
  - 함수의 이름 (생략 가능) / 매개변수 (args) / 함수 body (중괄호 내부)

```javascript
const name = function (args) {
    // do something
}
-----------------------------------------
const add = function (num1, num2) {
    return num1 + num2
}
add(1, 2)
```



#### 기본 인자

- 인자 작성시 '=' 문자 뒤 기본 인자 선언 가능

```javascript
const greeting = function (name = 'Anonymous') {
    return 'Hi ${name}'
}
greeting() // Hi Anonymous
```



#### 매개변수와 인자의 개수 불일치 허용

- 매개변수보다 인자의 개수가 많을 경우

```javascript
const noArgs = function () {
    return 0
}
noArgs(1, 2, 3) // 0

const twoArgs = function (arg1, arg2) {
    return [arg1, arg2]
}
twoArgs(1, 2, 3) // [1, 2]

/* 파이선 같은 경우, 함수에 넣어야 할 요소가 더 많거나 적을 때에,
에러 메세지를 뜨게 한다 */
```

- 매개변수보다 인자의 개수가 적을 경우

```javascript
const threeArgs = function (arg1, arg2, arg3){
    return [arg1, arg2, arg3]
}
threeArgs()		// [undefined, undefined, undefined]
threeArgs(1)	// [1, undefined, undefined]
threeArgs(1, 2)	// [1, 2, undefined]

/* 인자의 개수가 적을 경우 undefined로 채워 넣는다 */
```



#### Rest Parameter

- rest parameter (...)를 사용하면 함수가 정해지지 않은 수의 매개변수를 배열로 받는다
  - 만약 rest parameter로 처리한 매개변수에 인자가 넘어오지 않을 경우에는, 빈 배열로 처리

```javascript
const restOpr = function (arg1, arg2, ...restArgs){
    return [arg1, arg2, restArgs]
}

restOpr(1, 2, 3, 4, 5)	// [1, 2, [3, 4, 5]]
restOpr(1, 2)			// [1, 2, []]
```



#### Spread Operator

- spread operator (...)를 사용하면 배열 인자를 전개하여 전달 가능

```javascript
const spreadOpr = function (arg1, arg2, arg3) {
    return arg1 + arg2 + arg3
}

const numbers = [1, 2, 3]
spreadOpr(...numbers) // 6
```



#### 함수 타입

```javascript
// 함수 표현식
const add = function (args) {}
// 함수 선언식
function sub(args) {}

console.log(typeof add)		// function
console.log(typeof args)	// function
```



#### 호이스팅

```javascript
// 함수 선언식을 사용하면 함수 호출 이후에 선언해도 동작한다

add(2, 7) // 9

function add (num1, num2) {
    return num1 + num2
}

// 함수 표현식을 사용했을 때, 선언한 함수는 함수 정의 전에 호출 시 에러 발생
// var를 키워드로 작성을 해도 변수가 선언 전 undefined로 초기화 되어 다른 에러가 발생

add(2, 7) // Uncaught ReferenceError: Cannot access 'sub' before initialization

const sub = function (num1, num2) {
    return num1 + num2
}
```



[⬆️ back to top](#category)



## ✔️ Arrow Function

> 함수를 비교적 간결하게 정의 할 수 있는 문법

```javascript
const arrow1 = function (name) {
    return 'Hello, ${name}'
}

// 1. function 키워드 삭제
const arrow2 = (name) => { return 'Hello, ${name}' }

// 2. 매개변수가 1개일 경우에만 () 생략 가능
const arrow3 = name => { return 'Hello, ${name}' }

// 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 {} 과 return 삭제 가능
const arrow4 = name => return 'Hello, ${name}'
```



[⬆️ back to top](#category)

## ✔️ 문자열

|   메서드   |                   설명                    |                     비고                     |
| :--------: | :---------------------------------------: | :------------------------------------------: |
| `includes` | 특정 문자열의 존재여부를 참/거짓으로 반환 |                                              |
|  `split`   |   문자열을 토큰 기준으로 나눈 배열 반환   | 인자가 없으면 기존 문자열을 배열에 담아 반환 |
| `replace`  | 해당 문자열을 대상 문자열로 교체하여 반환 |                  replaceAll                  |
|   `trim`   |     문자열의 좌우 공백 제거하여 반환      |              trimStart, trimEnd              |

```javascript
// include
const str = 'a santa at nasa'

// str에 해당 문자를 포함하는가?
str.includes('santa')	// true
str.includes('asan') 	// false

// split
const str = 'a cup'
str.split()		// ['a cup']
str.split('')	// ['a', '', 'c', 'u', 'p']
str.split(' ')	// ['a','cup']

// replace
const str = 'a b c d'
str.replace('', '-')	// 'a-b c d'
str.replaceAll('', '-')	// 'a-b-c-d'

// trim
const str = '   hello    '
str.trim()		// 'hello'
str.trimStart()	// 'hello    '
```

[⬆️ back to top](#category)



## ✔️ 배열

> 키와 속성들을 담고 있는 참조 타입의 객체 (Object)
>
> 순서를 보장하는 특징이 있음
>
> 주로 대괄호를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
>
> 배열의 길이는 array.length 형태로 접근 가능

```javascript
const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0])		// 1
console.log(numbers[-1])	// undefined
console.log(numbers.length)	// 5
console.log(numbers[numbers.length - 1]) // 5
```

|      메서드       |                       설명                        |           비고           |
| :---------------: | :-----------------------------------------------: | :----------------------: |
|     `reverse`     |      원본 배열의 요소들의 순서를 반대로 정렬      |                          |
|   `push & pop`    |      배열의 가장 뒤에 요소를 추가 또는 제거       |                          |
| `unshift & shift` |      배열의 가장 앞에 요소를 추가 또는 제거       |                          |
|    `includes`     | 배열에 특정 값이 존재하는지 판별 후 참/ 거짓 반환 |                          |
|     `indexOf`     |  배열에 특정 값이 존재하는지 판별 후 인덱스 반환  | 요소가 없을 경우 -1 반환 |
|      `join`       |     배열의 모든 요소를 구분자를 이용하여 연결     | 구분자 생략 시 쉼표 기준 |

```javascript
// reverse
const numbers = [1, 2, 3, 4, 5]

numbers.reverse()
console.log(numbers) // [5, 4, 3, 2, 1]

// push & pop
const numbers = [1, 2, 3, 4, 5]

numbers.push(100)
console.log(numbers) // [1, 2, 3, 4, 5, 100]

numbers.pop()
console.log(numbers) // [1, 2, 3, 4, 5]

// shift & unshift
const numbers = [1, 2, 3, 4, 5]

numbers.shift(100)
console.log(numbers) // [100, 1, 2, 3, 4, 5]

numbers.unshift()
console.log(numbers) // [1, 2, 3, 4, 5]

//includes
const numbers = [1, 2, 3, 4, 5]

console.log(numbers.includes(100))	// false
console.log(numbers.includes(4))	// true

// indexOf
const numbers = [1, 2, 3, 4, 5]
let result

result = numbers.indexOf(3)
console.log(result)				// 2

result = numbers.indexOf(100)
console.log(result)				// -1

// join
const numbers = [1, 2, 3, 4, 5]
let result

result = numbers.join()
console.log(result)			// 1,2,3,4,5

result = numbers.join('')
console.log(result)			// 12345

result = numbers.join(' ')
console.log(result)			// 1 2 3 4 5

result = numbers.join('-')
console.log(result)			// 1-2-3-4-5
```

[⬆️ back to top](#category)



### Spread Operator

> spread operator (...)를 사용하면 배열 내부에서 배열 전개 가능

```javascript
const array = [1, 2, 3]
const newArray = [0, ...array, 4]

console.log(newArray) // [0, 1, 2, 3, 4]
```



### 배열 관련 주요 메서드 목록 심화

> 메서드 호출 시 인자로 callback 함수를 받는 것이 특징

|  메서드   |                             설명                             |     비고     |
| :-------: | :----------------------------------------------------------: | :----------: |
| `forEach` |        배열의 각 요소에 대해 콜백 함수를 한 번씩 실행        | 반환 값 없음 |
|   `map`   |      콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환      |              |
| `filter`  | 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환 |              |
| `reduce`  |    콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환     |              |
|  `find`   |        콜백 함수의 반환 값이 참이면 해당 요소를 반환         |              |
|  `some`   |    배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환    |              |
|  `every`  |      배열의 모든 요소가 판별 함수를 통과하면 참을 반환       |              |

```javascript
/* 콜백 함수는 3가지 매개변수로 구성
	element: 배열의 요소
	index: 배열 요소의 인덱스
	array: 배열 자체 */
--------------------------------------------------

// forEach
array.forEach((element, index, array) => {
    // do something
})

const fruits = ['딸기', '수박', '사과', '체리']

fruits.forEach((fruit, index) => {
    console.log(fruit, index)
    // 딸기 0
    // 수박 1
    // 사과 2
    // 체리 3
})
--------------------------------------------------

// map
array.map((element, index, array) => {
    // do something
})

const numbers = [1, 2, 3, 4, 5]

const doubleNums = numbers.map((num) => {
    return num * 2
})

console.log(doubleNums) // [2, 4, 6, 8, 10]
--------------------------------------------------

// filter
array.filter((element, index, array) => {
    // do something
})

const numbers = [1, 2, 3, 4, 5]

const oddNums = numbers.filter((num, index) => {
    return num % 2
})

console.log(oddNums) // 1, 3, 5
--------------------------------------------------

// reduce
array.reduce((acc, element, index, array) => {
    // do something
}, initialValue)

const numbers = [1, 2, 3]

const result = numbers.reduce((acc, num) => {
    return acc + num
}, 0)

console.log(result) // 6

acc |  num (number의 요소들)
0	+	1	= 1 (acc로 저장)
1	+	2	= 3 (acc로 저장)
3	+	3	= 6
--------------------------------------------------

// find
array.fine((element, index, array) => {
    // do something
})

const avengers = [
    {name = 'Tony Stark', age: 45},
    {name = 'Steve Rogers', age: 32},
    {name = 'Thor', age: 40},
]

const result = avengers.find((avenger) =>{
    return avenger.name === 'Tony Stark'
})

console.log(result) // {name = 'Tony Stark', age: 45}
--------------------------------------------------

// some
array.some((element, index, array) => {
    // do something
})

const numbers = [1, 3, 5, 7, 9]

const hasEvenNumber = numbers.some((num) => {
    return num % 2 === 0
})
console.log(hasEvenNumber) // false

const hasOddNumber = numbers.some((num) => {
    return num % 2
})
console.log(hasOddNumber) // true
--------------------------------------------------

// every
array.every((element, index, array) => {
    // do something
})

const numbers = [2, 4, 6, 8, 10]

const isEveryNumberEven = numbers.every((num) => {
    return num % 2 === 0
})
console.log(isEveryNumberEven) // true

const isEveryNumberOdd = numbers.every((num) => {
    return num % 2
})
console.log(isEveryNumberOdd) // false
```

[⬆️ back to top](#category)



## ✔️ 객체

> 객체는 속성 (property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현
>
> key는 문자열 타입만 가능 : 따옴표가 있어야 함
>
> value는 모든 타입(함수포함) 가능
>
> 객체 요소 접근은 점 또는 대괄호로 가능

```javascript
const me = {
    name: 'jack',
    phoneNumber: '01012345678',
    'samsung products': {
        buds: 'Galaxy Buds pro'
        galaxy: 'Galaxy s20',
    },
}

console.log(me.name)						// 'jack'
console.log(me.phoneNumber)					// '01012345678'
console.log(me['samsung products'])			// {buds: 'Galaxy Buds pro', galaxy: 'Galaxy s20'}
console.log(me['samsung products'].buds)	// 'Galaxy Buds pro'
```



- 메서드는 객체의 속성이 참조하는 함수
- 객체.메서드명()으로 호출 가능
- 메서드 내부에서는 this 키워드가 객체를 의미함

```javascript
const me = {
	firstName: 'John',
	lastName: 'Doe',
	getFullName: function () {
		return this.firstName + this.lastName
	}
}
```

[⬆️ back to top](#category)
