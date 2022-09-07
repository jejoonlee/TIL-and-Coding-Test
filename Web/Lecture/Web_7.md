# 📋Web HTML & CSS

[실습](https://github.com/jejoonlee/TIL/blob/master/Web/%EC%8B%A4%EC%8A%B5/20220906/README.md)

#### Category

[Bootstrap Grid System](#%EF%B8%8F-Bootstrap-grid-system)



## ✔️ Bootstrap Grid System

#### Grid system (web design)

> 요소들의 디자인과 배치에 도움을 주는 시스템
>
> 주로 동일하게 요소들을 보이고 싶을 때 사용한다

**기본요소**

- column : 실제 컨텐츠를 포함하는 부분
- Gutter : 칼럼과 칼럼 사이의 공간 (사이 간격)
- Container : Column들을 담고 있는 공간

✍️ **Bootstrap Grid system은 Flexbox로 제작됨**

✍️ **Container, rows, column으로 컨텐츠를 배치하고 정렬**

✍️ **반드시 기억해야 할 2가지**

1. 12개의 column
2. 6개의 grid breakpoints (화면 너비에 따라 비율이 보이는 것)



#### Grid system breakpoint

| class | size (px) | Container Max-width | Class prefix |
| ----- | --------- | ------------------- | ------------ |
| `xs`  | < 576px   | None (auto)         | `col-`       |
| `sm`  | >= 576px  | 540px               | `col-sm-`    |
| `md`  | >= 768px  | 720px               | `col-md-`    |
| `lg`  | >= 992px  | 960px               | `col-lg-`    |
| `xl`  | >= 1200px | 1140px              | `col-xl-`    |
| `xxl` | >= 1400px | 1320px              | `col-xxl-`   |



#### Offset

> offset을 사용하면 빈 column을 준다



#### Flex

> grid system은 기본적으로 flex를 써서, justify나 align을 사용할 수 있다
