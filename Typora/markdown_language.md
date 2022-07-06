# ✔️ 마크다운 문법 정리



## 📝Heading

> `#`의 개수에 따라 대응되는 수준 (Heading Level)이 있으며, h1~h6까지 표현 가능

***📌뛰어쓰기 필수***



예시)

### h3 (`#` 3개)

#### h4 (`#` 4개)





## 📝List

> 리스트는 순서가 있는 리스트와 순서가 없는 리스트로 구성한다

- 순서가 없는 리스트는 `-` 또는 `*` 를 이용한다

- 순서가 있는 리스트는 `1.`를 이용하면 된다

📌***리스트도 뛰어쓰기가 필수***



예시)

- ul
  - ul + tab

1. ol
   1. ol + tab





## 📝Fenced Code Block

> 코드 블록은 backtick 기호 3개를 활용하여 작성 ```
>
>  backtick 사이에 특정 언어를 명시하면 Syntax Highlighting 적용 가능

예시)

```python
# simple.py
languages = ['python', 'perl', 'c', 'java']

for lang in languages:
	if lang in ['python', 'perl']:
		print("%6s need interpreter" % lang)
	elif lang in ['c', 'java']:
		print("%6s need compiler" % lang)
	else:
		print("should not reach here")
```





## 📝Inline Code Block

> 인라인 코드 블록은 backtick 1개를 인라인에 활용하여 작성

함수, elements 등을 글로 설명할 때 사용할 수 있음

하이라이트 기능으로도 사용?



예시)

`h1` , `p` , `안녕하세요` 





## 📝Link

> `[문자열](url)` 를 통해 링크를 만들 수 있다



예시)

[내 깃허브 ctrl+클릭](https://github.com/JeJoonLee) 





## 📝Image

> `![문자열](url)` 를 통해 이미지를 사용할 수 있음 

***Typora 이미지 설정을 '상대 경로'로 설정을 해놔야, 다른 컴퓨터에서도 보인다***



예시)

![상대 결로가 설정되어 있음](markdown_language.assets/20220521_100736.jpg)





## 📝Blockquotes

> `>` 를 통해 인용문을 작성





## 📝Table

> 본문 > 표 > 표 삽입 (ctrl + t) 를 이용해서 표를 만들 수 있음

예시)

| 스포츠 | 공모양 |
| ------ | ------ |
| 축구   | ⚽      |
| 농구   | 🏀      |





## 📝Text 

> 굵게 (bold) 와 기울임 (italic)을 통해 특정 글자들을 강조
>
> `**bold**` : ctrl + b
>
> `*italic*` : ctrl + i

예시)

- `**bold**` : **Bold**

- `*italic*` : *italic*





## Horizontal Line

> `***` `---` `___` 를 사용하면 수평선을 만들 수 있다

예시)

***

---

___













