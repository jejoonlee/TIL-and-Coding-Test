# 📋Web HTML & CSS

#### Category

[Javascript](#%EF%B8%8F-Javascript)

[DOM](#%EF%B8%8F-DOM)

[BOM](#%EF%B8%8F-bom)

[DOM 조작](#%EF%B8%8F-DOM-조작)



## ✔️ Javascript

> Javascript는 현재 브라우저를 조작할 수 있는 유일한 언어이다
>
> 동적으로 콘텐츠를 바꾸고, 멀티미디어를 제어하고, 애니메이션을 추가하는 등 거의 모든 것을 만들 수 있는 스크립팅 언어

- 변수에 값을 저장할 수 있다
- 프로그래밍에서 '문자열(string)'이라고 부르는, 텍스트 조각을 조작한다
- 웹 페이지에서 발생하는 어떤 이벤트에 코드가 응답하도록 한다



#### 브라우저에서 할 수 있는 일

- **DOM (Document Object Model) 조작** [DOM](#%EF%B8%8F-DOM)
  - 문서(HTML) 조작

- **BOM (Browser Object Model) 조작** [BOM](#%EF%B8%8F-bom)
  - navigator, screen, location, frames, history, XHR
- **JavaScript Core (ECMAScript)**
  - Data Structure (Object, Array), Conditional Expression, Iteration
  - 프로그래밍 문법



## ✔️ DOM

> Document Object Model
>
> HTML 콘텐츠 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작할 수 있다 (예. 팝업창)

- HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
- 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
- 문서가 구조화되어 있으며 각 요소는 객체 (object)로 취급
- 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능



#### Parsing

- 구문 분석, 해석
- 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정

![화면 캡처 2022-09-15 140138](Javascript_Basic_DOM.assets/화면 캡처 2022-09-15 140138.png)



## ✔️ BOM

> Browser Object Model

- 자바스크립트가 브라우저와 소통하기 위한 모델
- 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
  - 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능
- window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)를 지칭



## ✔️ DOM 조작

> DOM 조작 순서
>
> 1. 선택 (select)
> 2. 변경 (Manipulate)



### 변수 선언

> Javascript는 변수를 선언할 때 키워드가 필요하다

`var` : 변수를 선언. 추가로 동시에 값을 초기화

`let`  : 변수를 선언. 변수를 변경할 수 있음

`const` :  변수를 선언. 변수를 변경할 수 없음

예시)

`var x = 42`  또는 `const x = 42`



### DOM 선택

`document.querySelector(selector)`

- 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없으면 Null)
- 예) title이라는 `class`가 하나 이상일 때에 위의 선언문을 쓰면, 제일 첫 번째 element 객체를 반환한다

`document.querySelectorAll(selector)`

- 지정된 selector에 일치하는 NodeList를 반환한다
- 즉 title이라는 `class`가 하나 이상일 때에, 위의 선언문을 쓰면, 모든 element 객체를 선택해서 반환한다

`getElementById(id)` /` getElementsByTagName(name)` / `getElementsByClassName(names)`

- 위의 메서드로 id / 태그 이름 / class 이름의 element 객체를 반환할 수 있다

**BUT**

`document.querySelector()` / `document.querySelectorAll()` 을 사용하는 이유는 id, class 그리고 tag 선택자 등을 모두 사용 가능하다



#### DOM 선택 - 선택 메서드별 반환 타입

- 단일 element

  - `getElementById()`
  - `querySelector()`

- HTMLCollection

  > name, id, index 속성으로 각 항목에 접근 가능

  - `getElementsByTagName()`
  - `getElementsByClassName()`

- NodeList

  > index로만 각 항목에 접근 가능
  >
  > 단, HTMLCollection과 달리 배열에서 사용하는 forEach 메서드 및 다양한 메서드 사용 가능

  - `querySelectorAll()`



#### DOM 선택 - Collection

- Live Collection
  - 문서가 바뀔 때 실시간으로 업데이트 됨
  - DOM의 변경사항을 실시간으로 collection에 반영



### DOM 변경

`document.createElement()`

- 작성한 태그 명의 HTML 요소를 생성하여 반환



`Element.append()`

- 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
- 여러 개의 Node 객체, DOMString을 추가할 수 있음
- 반환 값이 없음



`Node.appendChild()`

- 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입 (Node만 추가 가능)
- 한번에 오직 하나의 Node만 추가할 수 있음



`Node.innerText`

- 요소와 그 자손의 텍스트 콘텐츠를 나타낸다



`Element.innerHTML`

- 요소 (element) 내에 포함 된 HTML 또는 XML 마크업을 가져오거나 설정



### DOM 삭제

`ChildNode.remove()`

- Node가 속한 트리에서 해당 Node를 제거

`Node.removeChild()`

- DOM에서 자식 Node를 제거하고 제거된 Node를 반환
- Node는 인자로 들어가는 자식 Node의 부모 Node



### DOM 속성

`Element.setAttribute(name, value)`

- 지정된 요소의 값을 설정
- 예) `anchor` 태그에 `href` 를 주기 위해 `anchor.setAttribute(href, URL)` 을 작성하면 됨

`Element.getAttribute(attributeName)`

- 해당 요소의 지정된 값(문자열)을 반환
- attributeName 의 값을 가지고 온다
