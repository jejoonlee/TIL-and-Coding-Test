# Udemy : 파이썬 API



## HTML unescape

> #### 데이터 안에 기호들을, 읽지 못 할 때에, 특정 코드로 기호들을 표시한다
>
> #### 그 특정 코드를 기호로 다시 바꾸고 싶을 때에 HTML의 unescape 메서드를 사용한다



#### `&amp;`를 `&`로 바꾸기

```python
import html

html.unescape("Kim &amp; Lee")
```

