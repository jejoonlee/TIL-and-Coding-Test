# 📋DataBase 기본 함수와 연산

### Practice

[ALTER TABLE](https://github.com/jejoonlee/sql_practice/blob/master/20220818/practice.sql)

[Healthcare](https://github.com/jejoonlee/TIL/blob/master/SQL/20220818/Practice.md)



### Category

[기본 함수와 연산](#%EF%B8%8F-기본-함수와-연산)

​		[문자열 함수](#문자열-함수)

​		[숫자 함수](#숫자-함수)

​		[산술 연산자](#산술-연산자)

[GROUP BY](#%EF%B8%8F-group-by)

​		🚨🚨[SELECT 문장 실행 순서](#SELECT-문장-실행-순서)🚨🚨

[ALTER TABLE](#%EF%B8%8F-alter-table)





## ✔️ 기본 함수와 연산

### 문자열 함수

| 함수                                               | 기능                          |
| -------------------------------------------------- | ----------------------------- |
| `SUBSTR(문자열, start, length)`                    | 문자열 자르기                 |
| `TRIM(문자열)` /` LTRIM(문자열)` / `RTRIM(문자열)` | 무자열 공백 제거              |
| `LENGTH(문자열)`                                   | 문자열 길이                   |
| `REPLACE(문자열, 패턴, 변경값)`                    | 패턴에 일치하는 부분을 변경   |
| `UPPER(문자열)`, `LOWER(문자열)`                   | 대소문자 변경                 |
| `(문자열) || (문자열)`                             | 문자열 합치기 (concatenation) |

```sqlite
-- 주어진 정보 (users)

-- 이름   age  country  phone          balance
-- ---  ---  -------  -------------  -------
-- 유정호  40   전라북도     016-7280-2855  370
-- 이경희  36   경상남도     011-9854-5133  5900
-- 구정자  37   전라남도     011-4177-8170  3100
-- 장미경  40   충청남도     011-9079-4419  250000
-- 차영환  30   충청북도     011-2921-4284  220
```

```sqlite
-- 이름과 age를 합치는 것
SELECT 이름 || age FROM users;

-- phone에 '-'을 없애는 것. 번호만 출력된다
SELECT REPLACE(phone, '-', '') FROM users;
```



### 숫자 함수

| 함수                                               | 기능                          |
| -------------------------------------------------- | ----------------------------- |
| `ABS(숫자)`                                        | 절대 값                       |
| `SIGN(숫자)`                                       | 부호 (양수 1, 음수 -1, 0 0)   |
| `MOD(숫자1, 숫자2)`                                | 숫자 1을 숫자 2로 나눈 나머지 |
| `CEIL(숫자)` / `FLOOR(숫자)` / `ROUND(숫자, 자리)` | 올림, 내림, 반올림            |
| `POWER(숫자1, 숫자2)`                              | 숫자1의 숫자2 제곱            |
| `SQRT(숫자)`                                       | 제곱근                        |



### 산술 연산자

- `+`, `-`, `*`, `/`  와 같은 산술 연산자와 우선 순위를 지정하는 () 기호를 연산에 활용할 수 있다

```sqlite
SELECT age + 1 FROM users;
```





## ✔️ GROUP BY

> MAKE A SET OF SUMMARY ROWS FROM A SET OF ROWS
>
> Aggregate Function (집계 함수)가 있어야 한다
>
> GROUP BY는 SELECT DISTINCT와 다르다

**Aggregate Function**

- 값 집합에 대한 계산을 수행하고 단일 값을 반환
  - 여러 행으로부터 하나의 결과값을 반환하는 함수
- 예) `COUNT(*)` / `AVG(age)`



**ALIAS**

- 칼럼이나 테이블명이 너무 길거나 다른 명칭으로 확인하고 싶을 때는 ALIAS를 활용
- AS를 생략하여 공백으로 표현할 수 있음
- 별칭에 공백, 특수문자 등이 있는 경우 따옴표로 묶어서 표기

```sqlite
SELECT last_name 성 FROM users;
SELECT last_name AS 성 FROM users;
SELECT last_name AS 성 FROM users WHERE 성='김';
```



### GROUP BY

- SELECT문의 optional 절
- 행 집합에서 요약 행 집합을 만듦
- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦
- **문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성해야 함**

```sqlite
SELECT * FROM 테이블이름 GROUP BY 컬럼1, 컬럼2;
```



`is_drinking` 을 지정하고, `is_drinking` 기준으로 출력을 한다

- 즉 is_drinking 기준으로 사람 수를 센다
- 그 중 혈압이 200이상인 사람들의 수만 센다

```sqlite
SELECT is_drinking, COUNT(is_drinking) FROM healthcare
WHERE blood_pressure >= 200
GROUP BY is_drinking;
```

```sqlite
-- users에서 각 성(last_name)씨가 몇 명씩 있는지 조회
SELECT last_name, COUNT(*) FROM users
GROUP BY last_name;
```



#### HAVING

- 집계함수는 WHERE 절의 조건식에서 사용할 수 없다
- 집계 결과에서 조건에 맞는 값을 따로 활용하기 위해서 `HAVING`을 활용

```sqlite
-- 시도(sido)에 사는 사람의 수가 50000명 이산인 시도의 코드와 그 시도에 사는 사람의 수를 출력하기
SELECT sido, COUNT(sido) FROM healthcare
GROUP BY sido
HAVING COUNT(sido) >= 50000;

--------------------------
sido  COUNT(sido)
----  -----------
11    166231
26    69025
28    58345
41    247369
47    54438
48    68530
```



### SELECT 문장 실행 순서

- FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
  - FROM : 테이블 대상으로
  - WHERE : 제약조건에 맟춰서 뽑아서
  - GROUP BY : 그룹화 한다
  - HAVING : 그룹 중에 조건과 맞는 것 만을
  - SELECT : 조회하여
  - ORDER BY : 정렬하고
  - LIMIT/OFFSET : 특정 위치의 값을 가져온다

```sqlite
SELECT 칼럼명
FROM 테이블명
WHERE 조건식
GROUP BY 칼럼 혹은 표현식
HAVING 그룹조건식
ORDER BY 칼럼 혹은 표현식
LIMIT 숫자 OFFSET 숫자;
```





## ✔️ ALTER TABLE

```sqlite
-- 1. 테이블 이름 변경
ALTER TABLE table_name
RENAME TO new_name;

-- 2. 새로운 칼럼 추가
ALTER TABLE table_name
ADD COLUMN column_definition

-- 3. 칼럼 이름 수정
ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;

-- 4. 칼럼 삭제
ALTER TABLE table_name
DROP COLUMN column_name;
```

`RENAME TO new_name` 

- 테이블 이름 변경

`ADD COLUMN column_definition`

- 테이블 칼럼 추가

`RENAME COLUMN __ TO __`

- 칼럼 이름 수정

`DROP COLUMN column_name`

- 칼럼 삭제
