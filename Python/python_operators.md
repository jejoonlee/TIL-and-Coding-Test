# 📋Python Operators

[논리 연산자 (Logical Operator)](#-논리-연산자-logical-operator)

[산술 연산자 (Arithmetic Operator)](#-산술-연산자-arithmetic-operator)

[복합 연산자 (In-place Operator)](#-복합-연산자-in-place operator)

[비교 연산자 (Comparison Operator)](#-비교-연산자-comparison-operator)

[Escape Sequence](#-escape-sequence)

[Sequence-Operator](#-sequence-operator)



### ✔️ 논리 연산자 (Logical Operator)

| 연산자  |                             내용                             |
| :-----: | :----------------------------------------------------------: |
| A and B |      A와 B 모두 True시, `True` / 그렇지 않으면 `False`       |
| A or B  | A와 B 중 하나만이라도 True면, `True` / A와 B 모두 False시, `False` |
|   Not   |                True를 False로, False를 True로                |





### ✔️ 산술 연산자 (Arithmetic Operator)

| 연산자 |   내용   |
| :----: | :------: |
|  `+`   |   덧셈   |
|  `-`   |   뺄셈   |
|  `*`   |   곱셈   |
|  `%`   |  나머지  |
|  `/`   |  나눗셈  |
|  `//`  |    몫    |
|  `**`  | 거듭제곱 |





### ✔️ 복합 연산자 (In-place Operator)

| 연산자  |    내용    |
| :-----: | :--------: |
| a += b  | a = a + b  |
| a -= b  | a = a - b  |
| a *= b  | a = a * b  |
| a /= b  | a = a / b  |
| a //= b | a = a// b  |
|  a%=b   | a = a % b  |
| a **=b  | a = a ** b |



### ✔️ 비교 연산자 (Comparison Operator)

| 연산자 |   내용    |
| :----: | :-------: |
|   <    |   미만    |
|   <=   |   이하    |
|   >    |   초과    |
|   >=   |   이상    |
|   ==   |   같음    |
|   !=   | 같지 않음 |





### ✔️ Escape Sequence

| 예약문자 |   내용(의미)    |
| :------: | :-------------: |
|   `\n`   |     줄 바꿈     |
|   `\t`   |       탭        |
|   `\r`   |   캐리지리턴    |
|   `\0`   | 널 (null, none) |
|   `\\`   |       `\`       |
|   `\'`   | 단일인용부호(') |
|   `\"`   | 이중인용부호(") |





### ✔️ Sequence Operator

| 연산             | 결과                                                     |
| ---------------- | -------------------------------------------------------- |
| s[i]             | s의 i 번째 항목, 0에서 시작                              |
| s[i:j]           | s의 i 에서 j까지의 슬라이스                              |
| s[i:j:k]         | s 의 i 에서 j까지 스탭 k의 슬라이스                      |
| s + t            | s와 t의 이어 붙이기                                      |
| s * n 또는 n * s | s 를 그 자신에 n 번 더하는 것                            |
| x in s           | s 의 항목 중 하나가 x와 같으면 True, 그렇지 않으면 False |
| x not in s       | s 의 항목 중 하나가 x와 같으면 False, 그렇지 않으면 True |
| len(s)           | s 의 길이                                                |
| min(s)           | s 의 가장 작은 항목                                      |
| max(s)           | s 의 가장 큰 항목                                        |