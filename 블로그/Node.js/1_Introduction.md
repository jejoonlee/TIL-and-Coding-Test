# Udemy - Node.js [JavaScript Basics]

*Node.js - The Complete Guide (Udemy)*



## Node.js 란?

> #### 자바스크립트의 실행시간이다
>
> - 자바스크트는 브라우저에서 실행되는 언어로, DOM을 조작하거나 브라우저에 로드된 페이지를 조작하는 프로그래밍 언어다
>   - DOM = Document Object Model
>
> #### 자바스크립트를 서버에서 실행할 수 있도록 해준다





## JavaScript on the Server

<img src="1_Introduction.assets/image-20230405172417889.png" alt="image-20230405172417889" style="zoom: 67%;" />

#### 브라우저에 직접적으로 나타나지 않는, 데이터베이스를 연결하거나, 사용자 인증, 입력 유효성 검사까지 서버에서 한다





## JavaScript Basics



#### Boolean, 숫자, 텍스트 같이 데이터를 명확하게 정의하도록 강요하지 않는다

- 숫자를 텍스트로 바꾸는 것과 같이, 데이터 type을 바꿀 수 있다



#### 객체 지향 프로그래밍 언어다

- 데이터가 논리적인 객체로 분류될 수 있다



#### 다양하게 사용할 수 있다

- 다양한 작업을 수행할 수 있다 (파일, 브라우저 내의 이벤트 등)
- 브라우저 / 서버에서 사용될 수 있다



#### 기본 문법

```javascript
var name = 'Alex';
// name은 string (문자열)

var age = 27;
// age는 number (숫자)

var hasHobbies = true;
// hasHobbies는 boolean (true or false)

function summary(userName, userAge, userHasHobbies) {
    return (userName + userAge + userHasHobbies)
}

console.log(summary(name, age, hasHobbies))
// Alex27true 로 출력된다
```

- name, age, hasHobbies 는 **global variable**, 글로벌 변수다
- userName, userAge, userHasHobbies는 function 안에서 사용될 수 있는 로컬 변수다 (**Local Variable**)



#### let vs const

- **let** : 변수의 값을 바꿀 수 있다
- **const** : 변수의 값이 바뀌지 않는다
  - 변수를 const로 지정하면, 변수의 값을 바꾸게 되면, 에러가 뜬다

```javascript
let name = 'Alex';
// name은 string (문자열)

const age = 27;
// age는 number (숫자)

let hasHobbies = true;
// hasHobbies는 boolean (true or false)

name = 'Je Joon'
age = 50

console.log(name)
console.log(age)

// Output : Je Joon
// Output : error
```



#### 화살표

- function을 만들 때에 사용될 수 있다
- function을 만들 때, function이라는 단어를 사용안 한다
- 주로 function의 기능이 변하지 않도록 const를 사용한다

```javascript
let name = 'Alex';
const age = 27;
let hasHobbies = true;

const summary = (userName, userAge, userHasHobbies) => {
    return (userName + userAge + userHasHobbies)
}

const addOne = (a,b) => a + b;

console.log(summary(name, age, hasHobbies))
// Alex27true 로 출력된다
```



#### object and this

- 첫 번째 this는 글로벌을 가리킨다
  - 글로벌에는 name에 대한 데이터가 없어 undefined가 출력된다
  - **greet**라는 function을 만들어야 한다
- 두 번째 this는 **person** 안에 있는 데이터를 가리킨

```javascript
const person = {
    name : 'Alex',
    age : 27,
    greet : () => {
        console.log("greeting " + this.name)
    }
}

person.greet();
// greeting undefined
-----------------------------------------------------------------
    
const person = {
    name : 'Alex',
    age : 27,
    greet() {
        console.log("greeting " + this.name)
    }
}

person.greet();
// greeting Alex
```



#### array

- 문자열, boolean, 숫자 등의 형태의 데이터를 저장할 수 있다

```javascript
const hobbies = ['Alex', 'Lee', 'Joon']

for (let hobby of hobbies) {
    console.log(hobby)
}
// hobbies라는 array를 순회하기 위해 for문을 사용한다
```



#### Spread, Rest Operators

- **...** 을 사용해서 객체를 가지고 오는 것이다
- 똑같은 값을 다른 리스트에 저장하는 것

```javascript
const person = {
    name : 'Alex',
    age : 27,
    greet() {
        console.log("greeting " + this.name)
    }
}

const hobbies = ['Alex', 'Lee', 'Joon']

------------------------------------------
const copiedArray = hobbies.slice();
console.log(copiedArray)
// ['Alex', 'Lee', 'Joon']

------------------------------------------
const copiedArray = [hobbies]
console.log(copiedArray)
// [['Alex', 'Lee', 'Joon']]

------------------------------------------
const copiedArray = [...hobbies]
console.log(copiedArray)
// ['Alex', 'Lee', 'Joon']

------------------------------------------

```

- **const copiedArray = hobbies.slice();**
  - .slice(), 괄호 안에 아무것도 안 넣으면, **hobbies**에 있는 값을 모두 가지고 오는 것
- **const copiedArray = [hobbies]**
  - array 안에 **hobbies**라는 array를 넣는 것과 같다
    - [ ] 안에 [ ] 을 넣는 것
- **const copiedArray = [...hobbies]**



```javascript
const toArray = (arg1, arg2, arg3) => {
    return [arg1, arg2, arg3];
}

console.log(toArray(1, 2, 3))
console.log(toArray(1, 2, 3, 4))

// output : [1, 2, 3]
// output : error

const toArrayTwo = (...args) => {
    return args;
}
console.log(toArrayTwo(1, 2, 3, 4))
console.log(toArrayTwo(1, 2))

// output : [1, 2, 3, 4]
// output : [1, 2]
```

- **toArray(arg1, arg2, arg3)** 
  - 3개의 argument 밖에 못 넣는다
  - 3개 미만 또는 초과하면, 함수는 작동이 안 된다
- **toArrayTwo(...args)** 
  - 제한 없이, argument를 원하는대로 넣을 수 있다
