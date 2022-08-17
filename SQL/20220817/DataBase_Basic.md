# 📋DataBase Basic

### Practice

[수업 복습](https://github.com/jejoonlee/sql_practice/blob/master/20220817/Practice_1/1_user.sql)

[Healthcare](https://github.com/jejoonlee/sql_practice/tree/master/20220817/Practice_2)



### Category

[CRUD](#%EF%B8%8F-CRUD)

[WHERE절에서 사용할 수 있는 연산자](#%EF%B8%8F-where절에서-사용할-수-있는-연산자)

[SQL 사용할 수 있는 연산자](#%EF%B8%8F-sql-사용할-수-있는-연산자)

[연산자 우선순위](#%EF%B8%8F-연산자-우선순위)

[SQLite Aggregate Function](#%EF%B8%8F-sqlite-aggregate-function)

[LIKE](#%EF%B8%8F-like)

[ORDER BY](#%EF%B8%8F-order-by)



## ✔️ CRUD

|         | 구문       | 예시                                                         |
| ------- | ---------- | ------------------------------------------------------------ |
| C reate | **INSERT** | `INSERT INTO 테이블 이름 (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ...);` |
| R ead   | **SELECT** | `SELECT * FROM 테이블이름 WHERE 조건;`                       |
| U pdate | **UPDATE** | `UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2=값2 WHERE 조건;`     |
| D elete | **DELETE** | `DELETE FROM 테이블이름 WHERE 조건;`                         |



## ✔️ WHERE절에서 사용할 수 있는 연산자

- **비교 연산자**
  - `=` ,` >` , `>=` , `<`, `<=`  는 숫자 혹은 문자 값의 대/소, 동일 여부를 확인하는 연산자
- **논리 연산자**
  - `AND` : 앞에 있는 조건과 뒤에 오는 조건이 모두 참인 경우
  - `OR` : 앞의 조건이나 뒤의 조건이 참인 경우
  - `NOT` : 뒤에 오는 조건의 결과를 반대로

```sqlite
-- 1. 키가 175인 사람과 키가 183이면서 몸무개가 80인 사람
~~~ WHERE height = 175 or height = 183 AND weight = 80

-- 2. 키가 175 또는 183이면서 몸무개가 80인 사람
~~~ WHERE (height = 175 or height = 183) AND weight = 80
```

1. 키가 175인 모든 사람과 키가 183이면서 몸무개가 80인 사람을 출력함
2. 키가 175 또는 183이면서 몸무개가 80인 사람을 출력함



## ✔️ SQL 사용할 수 있는 연산자

- **BETWEEN 값1 AND 값2**
  - 값1과 값2 사이의 비교 (값1 <= 비교값 <= 값2)
- **IN (값1, 값2, ---)**
  - 목록 중에 값이 하나라도 일치하면 성공
- **LIKE**
  - 비교 문자열과 형태 일치
  - 와일드카드 (%: 0개 이상 문자, _ : 1개 단일 문자)
- **IS NULL / IS NOT NULL**
  - NULL 여부를 확인할 때는 항상 `=` 대신 `IS`를 활용
- **부정 연산자**
  - 같지 않다 (`!=`, `^=`, `<>`)
  - ~와 같지 않다 (NOT 칼럼명 =)
  - ~보다 크지 않다 (NOT 칼럼명 >)

```sqlite
~~ WHERE 칼럼명1 != 비교값1
	AND 칼럼명2 ^= 비교값2
	AND 칼럼명3 <> 비교값3
	AND NOT 칼럼명4 = 비교값4
	AND NOT 칼럼명5 > 비교값5; 
```



## ✔️ 연산자 우선순위

1순위 : 괄호 ()

2순위 : NOT

3순위 : 비교 연산자, SQL

4순위 : AND

5순위 : OR



## ✔️SQLite Aggregate Function

> 각 집합에 대한 계산을 수행하고 단일 값을 반환
>
> 여러 행으로부터 하나의 결괏값을 반환하는 함수

**SELECT 구문에서만 사용됨**

- **COUNT**
  - 그룹의 항목 수를 가져옴
- **AVG**
  - 모든 값의 평균을 계산
- **MAX**
  - 그룹에 있는 모든 값의 최대값을 가져옴
- **MIN**
  - 그룹에 있는 모든 값의 최소값을 가져옴
- **SUM**
  - 모든 값의 합을 계산

```sqlite
SELECT COUNT(칼럼) FROM 테이블이름;
SELECT AVG(칼럼) FROM 테이블이름;
SELECT MAX(칼럼) FROM 테이블이름;
SELECT MIN(칼럼) FROM 테이블이름;
SELECT SUM(칼럼) FROM 테이블이름;
```



## ✔️ LIKE

> query data based on pattern matching
>
> 패턴 일치를 기반으로 데이터를 조회하는 방법
>
> SQLite는 패턴 구성을 위한 2개의 wildcards를 제공

#### %	 (percent sign)

- 이 자리에 문자열이 있을 수도, 없을 수도 있다

#### _	   (underscore)

- 반드시 이 자리에 한 개의 문자가 존재해야 한다



```sqlite
-- LIKE statement : 패턴을 확인하여 해당하는 값을 조회
SELECT * FROM 테이블이름 WHERE 컬럼 LIKE '패턴';
```

| 와일드카드 패턴  | 의미                                          |
| ---------------- | --------------------------------------------- |
| `2%`             | 2로 시작하는 값                               |
| `%2`             | 2로 끝나는 값                                 |
| `%2%`            | 2가 들어가는 값                               |
| `_2%`            | 아무 값이 하나 있고 두 번째가 2로 시작하는 값 |
| `1_ _ _`         | 1로 시작하고 총 4자리인 값                    |
| `2_%_% / 2_ _ %` | 2로 시작하고 적어도 3자리인 값                |





## ✔️ ORDER BY

> sort a result set of a query
>
> 조회 결과 집합을 정렬
>
> SELECT 문에 추가하여 사용

#### ASC - 오름차순 (default)

#### DESC - 내림차순

```sqlite
SELECT * FROM 테이블이름 ORDER BY 컬럼 ASC;
SELECT * FROM 테이블이름 ORDER BY 컬럼 DESC;
```

