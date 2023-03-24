# MySQL



### Select

> 데이터 베이스에서 데이터를 불러올 때 사용 된다

```mysql
SELECT column 1, column 2, .....
FROM table_name

SELECT * FROM table_name

SELECT DISTINCT column 1,
FROM table_name
```

- **SELECT** 를 통해 테이블의 필드를 가지고 온다
- **FROM** 에 테이블의 이름을 넣는다 
- **SELECT ***  은, 테이블에 있는 모든 필드를 가지고 온다
- **SELECT DISTINCT** 는 반복 값을 없앤다
  - 행에 Korea, Korea, USA, Japan을 **SELECT DISTINCT**를 하면, Korea, USA, Japan 만 출력한다
  - 반복되는 Korea를 하나로 묶어서 출력해준다



### WHERE

> 컨디션을 통해, 데이터를 필터링 하는 것이다

```mysql
SELECT * FROM Customers
WHERE Country = 'Mexico';
```

- Customers 테이블에서 Country 행의 값이 "Mexico"인, 모든 행을 출력한다
- 연산자
  - =		>		<		>=		<=		!=
  - BETWEEN (특정 범위)	LIKE (패턴 찾기)	IN





### AND, OR, NOT

```mysql
SELECT * FROM Customers
WHERE Country = 'Germany' AND City = 'Berlin'

SELECT * FROM Customers
WHERE City = 'Berlin' OR City = 'London'

SELECT * FROM Customers
WHERE NOT Country = "Germany"

SELECT * FROM Customers
WHERE Country = "Germany" AND (City = "Berlin" or City = "Stuttgart")
```

1. Country 행에 독일인 값과 City 행에 Berlin인 값을 가진 데이터를 출력
   - Germany와 Berlin이 모두 충족해야 한다
2. City가 Berlin 또는 London 인 모든 값의 데이터를 출력
3. Country가 Germany가 아닌 모든 값의 데이터를 출력
4. Country가 Germany이면서 City가 Berlin 또는 Stuttgart인 모든 데이터를 출력





### ORDER BY

```mysql
SELECT column 1, column 2
FROM table_name
ORDER BY column 1, column 2 ASC
```

- table_name의 column 1과 column 2를 가지고 오고, 두 행 모두 오름차순으로 정렬을 한다
- **ASC 오름차순으로 정렬**
- **DESC 내림차순으로 정렬**













