# 📋Web HTML & CSS

[HTML elements](https://github.com/jejoonlee/TIL/blob/master/Web/HTML_elements.md)

#### Category

[HTML](#%EF%B8%8F-html)

- [HTML 요소 element의 구조](#%EF%B8%8F-HTML-요소-element의-구조)
- [속성 Attribute](#%EF%B8%8F-속성-Attribute)
- [HTML 문서의 구조](#%EF%B8%8F-HTML-문서의-구조)

[CSS](#%EF%B8%8F-CSS)

- [CSS의 Ruleset](#%EF%B8%8F-CSS의-Ruleset)





## ✔️ HTML

> HyperText Markup Language
>
> 웹을 이루는 가장 기초적인 구성 요소
>
> 웹페이지가 어떻게 구조화 되어 있는지 브라우저로 하여금 알 수 있도록 하는 **마크업 언어**
>
> HTML은 요소 (elements)로 구성되어 있으며, (tags)는 웹 상의 다른 페이지로 이동하게 하는 하이퍼 링크 내용들을 생성하거나, 단어를 강조하는 등의 역할을 한다

- **HyperText** : 웹 페이지를 다른 페이지로 연결하는 링크
- `<`태그`>` 로 이루어지고, 태그 안에 요소를 넣으면 된다
- HTML 마크업 : 다양한 '요소'를 사용한다. 에) `<head>`,` <title>`, `<body>` 등



### ✍️ HTML 요소 element의 구조

- **여는 태그와 닫는 태그 (opening tag and closing tag)**

```html
<em>대부분의 tag 들은 opening과 closing tag들이 있다</em>
```

- **내용 (Content)** : 요소의 내용이며, 이 경우 단순한 텍스트이다
- **요소 (Element)** : 여는 태그, 닫는 태그, 내용을 통틀어 요소 (element)라고 한다

```html
<h1>내용</h1>
tag 사이에 들어가는 것이 Content
tag와 내용 전체를 element, 요소라고 한다
```



#### Nesting elements

> 요소 안에 요소가 들어가는 것

```html
<p>My cat is <strong>very</strong> grumpy.</p>
```

- `<p>` 태그 안에 내용이 들어갔다
  - `<p>` 태그 안에 `<strong>` 태그가 들어갔는데, `<p>` 태그 안에 있는 내용 중 강조할 단어를 `<strong>` 태그를 통해 표현
- 요소 안에 요소를 쓰기 위해서는 `<p>`로 요소가 먼저 열리고 `<strong>`요소가 열리면,  `<strong>`으로 먼저 닫히고, `<p>`로 끝나야 한다



#### 블럭 레벨 요소 vs 인라인 요소

- **블록 레벨 요소 (Block-level elements)**
  - 블록 레벨 요소 이전과 이후 요소사이의 줄을 바꾼다
  - 일반적으로 **페이지의 구조적 요소**를 나타낼 때 사용
  - paragraph, lists, navigation bar, footers등을 표현할 수 있다
- **인라인 요소 (Inline element)**
  - 항상 블록 레벨 요소 내에 포함되어 있다
  - 문서의 단락보다 문장, 단어 같은 작은 부분에 대해서만 적용
  - 따로 줄을 만들지 않는다
  - 인라인 요소 태그 예시)  `<a>` (하이퍼링크 정의, anchor) , `<em>`,`<strong>` (text를 강조)



#### 빈요소 (Empty elements)

- 주로 문서에 무언가를 첨부하기 위해 단일 태그(single tag)를 사용하는 요소도 있다
- 예 <img>

```html
<img src="https://raw.githubusercontent.com/mdn/beginner-html-site/gh-pages/images/firefox-icon.png">

파이어 폭스의 로고
```



### ✍️ 속성 Attribute

> 태그의 부가적인 정보를 설정할 수 있다

- **지켜야할 사항**
  - 요소 이름 다음에 바로 오는 속성은 요소 이름과 속성 사이에 공백이 있어야 되고, 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백이 있어야 한다
  - 속성 이름 다음엔 등호(=)가 붙는다
  - 속성 값은 열고 닫는 따옴표로 감싸야 한다

```html
<a href=https://www.mozilla.org/>favorite website</a>
<!--favorite website를 클릭하면 해당 사이트에 들어간다-->

<a href=https://www.mozilla.org/ title='The Mozilla homepage'>favorite website</a>
<!--링크도 생기고, 링크 위에 마우스를 올리면 'The Mozilla homepage'가 표시된다-->
```



### ✍️ HTML 문서의 구조

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <p>This is my page</p>
  </body>
</html>
```

- `<!DOCTYPE html>` : 해당 문서의 형식을 나타내는 것
- `<html>` : 전체 페이지의 콘텐츠를 포함
- `<head>` : 이용자에게 보이지 않지만 검색 결과에 노출 될 키워드, 홈페이지 설명, CSS 스타일 등 HTML 페이지의 모든 내용을 담고 있다
- `<meta charset="utf-8">` : HTML 문서의 문자 인코딩 설정을 UTF-8로 지정하는 것이며 예시에서 지정한 UTF-8에는 전세계에서 사용되는 언어에 대한 대부분의 문자가 포함
- `<title>` : 페이지 제목이 설정되며 브라우저 탭에 표시된다
- `<body>` : 텍스트, 이미지, 비디오, 게임, 재생 가능한 오디오 트랙 등 페이지에 모든 콘텐츠 포함



## ✔️ CSS

> Cascading Style Sheets
>
> HTML이나 XML로 작성된 문서의 표시 방법을 기술하기 위한 **스타일 시트** 언어
>
> HTML 문서에 있는 요소들에 선택적으로 스타일을 적용할 수 있다



### ✍️ CSS의 Ruleset

- **선택자 (selector)**
  - rule set 맨 앞에 있는 HTML 요소 이름. 꾸밀 요소를 선택한다

- **선언**
  - `color: red` 와 같은 단일 규칙. 어떻게 꾸밀지

- **속성 (property)**
  - `color: red` 에서 `color`가 속성이다

- **속성 값**
  - `color: red` 에서 `red`는 속성 값
- 각각의 rule set은 반드시 `{}` 로 감싸져야 한다
- 선언 안에, 각 속성을 해당하는 값과 구분하기 위해 `:` 를 사용한다
- 선언이 끝나면 `;`을 사용해야 한다

```css
p {
  color: red;
  width: 500px;
  border: 1px solid black;
}
```

