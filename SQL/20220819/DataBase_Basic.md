# 📋DataBase 기본 함수와 연산

### Practice

[CASE](https://github.com/jejoonlee/sql_practice/blob/master/20220819/Practice/CASE.sql)

[Sub Query](https://github.com/jejoonlee/sql_practice/blob/master/20220819/Practice/subquery.sql)

[실습](https://github.com/jejoonlee/TIL/blob/master/SQL/20220819/Practice.md)



### Category

[CASE](#%EF%B8%8F-case)

[서브 쿼리](#%EF%B8%8F-서브-쿼리)



## ✔️ CASE

> CASE문은 특정 상황에서 데이터를 변화하여 활용할 수 있음
>
> ELSE를 생략하는 경우 NULL 값이 지정된

```sqlite
CASE
	WHEN 조건식 THEN 식
	WHEN 조건식 THEN 식
	ELSE 식
END
```

**예시) gender가 1인 경우는 남자를 gender 2인 경우에는 여자를 출력**

```sqlite
SELECT
	id,
	CASE
		WHEN gender = 1 THEN '남자'
		WHEN gender = 2 THEN '여자'
	END Gender AS "성"
FROM healthcare
LIMIT 3;
```

- END 뒤에 `AS "성"` 을 넣으면, `gender` 행의 이름을 바꿀 수 있다

예시2) 나이에 따라 청소년 (~18), 청년(~30), 중장년(~64), 노년 을 출력

```sqlite
SELECT first_name,age,
    CASE
    	WHEN age <= 18 THEN '청소년'
    	WHEN age <= 30 THEN '청년'
    	WHEN age <= 64 THEN '중장년'
    	ELSE '노년'
    END
FROM users
LIMIT 100;
```





## ✔️ 서브 쿼리

> 특정한 값을 메인 쿼리에 반환하여 활용하는 것
>
> 실제 테이블에 없는 기준을 이용한 검색이 가능함
>
> 서브 쿼리는 소괄호로 감싸서 사용하며, 메인 쿼리의 칼럼을 모두 사용할 수 있음

예시1) **단일행 서브 쿼리**

```sqlite
-- users에서 가장 나이가 작은 사람의 수
SELECT COUNT(*) FROM users
WHERE age = (SELECT MIN(age) FROM users);
-- 먼저 나이 중 제일 어린 나이를 구한다 (15살)
-- 그리고 모든 사람들 수 중에, 
-- 서브 쿼리를 통해 제일 나이가 어린 사람들의 수를 가져온다
```

- **단일행 서브 쿼리**
  - 서브쿼리의 결과가 0 또는 1개인 경우
  - 단일행 비교 연산자와 함께 사용 (`=`, `<` , `<=`, `>=`, `>`, `<>`)
- **다중행 서브쿼리**
  - 서브쿼리 결과가 2개 이상인 경우
  - 다중행 비교 연산자와 함께 사용 (IN, EXISTS 등)
- **다중컬럼 서브 쿼리**



예시2) **다중행 서브 쿼리**

```sqlite
-- users에서 이은정과 같은 지역에 사는 사람의 수
SELECT COUNT(*) FROM users
WHERE address IN (SELECT address FROM users
WHERE last_name || first_name = '이은정');
-- IN 을 사용해서 이은정과 같은 지역에 사는 모든 사람의 수를 구한다
-- 이은정이라는 사람은 2명이고, 둘 다 다른 지역에서 산다
```



예시3) **다중칼럼 서브쿼리**

```sqlite
-- 특정 성씨에서 가장 어린 사람들의 이름과 나이
SELECT last_name, first_name, age FROM users
WHERE (last_name, age) IN
(SELECT last_name, MIN(age) FROM users
GROUP BY last_name)
ORDER BY last_name;

SELECT last_name, MIN(age) FROM users
GROUP BY last_name;
-- 성씨를 기준으로 가장 어린 사람들을 구한다
```



**다른 테이블이랑 이동하면서 사용**

```sqlite
-- 가수(artists) 테이블에서 앨범(albums)의 개수가 가장 많은 가수의 Name을 출력

SELECT Name FROM artists
WHERE ArtistId = 
    (SELECT ArtistId FROM albums
    GROUP BY ArtistId
    ORDER BY COUNT(*) DESC
    LIMIT 1);
    
-- ArtistId 는 90 이고
-- 21개의 앨범이 있다
```

- 서브쿼리를 통해 앨범의 개수가 많은 가수의 ID를 찾고
- 그 가수의 ID를 통해서 artist 테이블에서, 가수의 이름을 가져온다
