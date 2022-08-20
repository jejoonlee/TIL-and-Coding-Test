# 실습

### 1. 모든 테이블의 이름을 출력하세요.

```sql
.table
```

```sqlite
albums          employees       invoices        playlists
artists         genres          media_types     tracks
customers       invoice_items   playlist_track
```



### 2. 모든 테이블의 데이터를 확인해보세요.

| 공백은 있는지 NULL은 있는지 데이터 타입은 어떤지 등등 데이터를 직접 확인해보세요.

```sqlite
.schema 테이블이름
또는 sqlite 확장프로그램 보기
```




### 3. 앨범(albums) 테이블의 데이터를 출력하세요.
| 단, `Title`을 기준으로 내림차순해서 5개까지 출력하세요.
```sql
SELECT * FROM albums
ORDER BY Title DESC
LIMIT 5;
```

```sqlite
AlbumId  Title                         ArtistId
-------  ----------------------------  --------
208      [1997] Black Light Syndrome   136
240      Zooropa                       150
267      Worlds                        202
334      Weill: The Seven Deadly Sins  264
8        Warner 25 Anos                6
```



### 4. 고객(customers) 테이블의 행 개수를 출력하세요.

| 단, 컬럼명을 `고객 수`로 출력하세요.
```sql
SELECT COUNT(*) '고객 수' FROM customers;
```

```sqlite
고객 수
----
59
```



### 5. 고객(customers) 테이블에서 고객이 사는 나라가 `USA`인 고객의 `FirstName`, `LastName`을 출력하세요.

| 단, 각각의 컬럼명을 `이름`, `성`으로 출력하고, `이름`을 기준으로 내림차순으로 5개까지 출력하세요.
```sql
SELECT FirstName AS '이름', LastName AS '성' FROM customers
WHERE Country = 'USA'
ORDER BY FirstName DESC
LIMIT 5;
```

```sqlite
이름        성
--------  ----------
Victor    Stevens
Tim       Goyer
Richard   Cunningham
Patrick   Gray
Michelle  Brooks
```



### 6. 송장(invoices) 테이블에서 `BillingPostalCode`가 `NULL` 이 아닌 행의 개수를 출력하세요.

| 단, 컬렴명을 `송장수`로 출력하세요.
```sql
SELECT COUNT(BillingPostalCode) AS '송장수' FROM invoices
WHERE BillingPostalCode IS NOT NULL;
```

```sqlite
송장수
---
384
```



### 7. 송장(invoices) 테이블에서 `BillingState`가 `NULL` 인 데이터를 출력하세요.

| 단, `InvoiceDate`를 기준으로 내림차순으로 5개까지 출력하세요.
```sql
SELECT InvoiceId, CustomerId, InvoiceDate FROM invoices
WHERE BillingState IS NULL
ORDER BY InvoiceDate DESC
LIMIT 5;
```

```sqlite
InvoiceId  CustomerId  InvoiceDate
---------  ----------  -------------------
412        58          2013-12-22 00:00:00
411        44          2013-12-14 00:00:00
410        35          2013-12-09 00:00:00
404        6           2013-11-13 00:00:00
403        56          2013-11-08 00:00:00
```



### 8. 송장(invoices) 테이블에서 `InvoiceDate`의 년도가 `2013`인 행의 개수를 출력하세요.

| `strftime`를 검색해서 활용해보세요.
```sql
SELECT COUNT(*) FROM invoices
WHERE strftime('%Y', InvoiceDate) = '2013';
-- strftime: 날짜를 표시하기 위한 함수 중 하나 / 포멧을 지정할 수 있음
-- '%Y'은 년도 / '%m' 월 / '%d' 일
```

```sqlite
COUNT(*)
--------
80
```



### 9. 고객(customers) 테이블에서 `FirstName`이 `L` 로 시작하는 고객의 `CustomerId`, `FirstName`, `LastName`을 출력하세요.

| 단, 각각의 컬럼명을 `고객ID`, `이름`,`성`으로 출력하고, `고객ID`을 기준으로 오름차순으로 출력하세요.

```sql
SELECT CustomerId AS '고객ID', FirstName AS '이름', LastName AS '성' FROM customers
WHERE FirstName LIKE 'L%'
ORDER BY CustomerId ASC;
```

```sqlite
고객ID  이름        성
----  --------  ---------
1     Luis      Goncalves
2     Leonie    Kohler
45    Ladislav  Kovacs
47    Lucas     Mancini
57    Luis      Rojas
```



### 10. 고객(customers) 테이블에서 각 나라의 고객 수와 해당 나라 이름을 출력하세요.

| 단, 각각의 컬렴명을 `고객 수`,`나라`로 출력하고, 고객 수 상위 5개의 나라만 출력하세요.

```sql
SELECT COUNT(*) AS '고객 수', Country AS '나라' FROM customers
GROUP BY Country
ORDER BY COUNT(*) DESC
LIMIT 5;
---------------------------------------
SELECT COUNT(*) AS "고객 수", Country AS "나라" FROM customers
GROUP BY Country
ORDER BY "고객 수" DESC
LIMIT 5;
```

```sqlite
고객 수  나라
----  -------
13    USA
8     Canada
5     France
5     Brazil
4     Germany
```



### 11. 앨범(albums) 테이블에서 가장 많은 앨범이 있는 Artist의 `ArtistId`와 `앨범 수`를 출력하세요.

```sql
SELECT ArtistId, COUNT(ArtistId) AS '앨범 수' FROM albums
GROUP BY ArtistId
ORDER BY COUNT(ArtistId) DESC
LIMIT 1;
```

```sqlite
ArtistId  앨범 수
--------  ----
90        21
```



### 12. 앨범(albums) 테이블에서 보유 앨범 수가 10개 이상인 Artist의 `ArtistId`와 `앨범 수` 출력하세요

| 단, 앨범 수를 기준으로 내림차순으로 출력하세요.

```sql 
SELECT ArtistId, COUNT(ArtistId) AS '앨범 수' FROM albums
GROUP BY ArtistId
HAVING COUNT(ArtistId) >= 10
ORDER BY COUNT(ArtistId) DESC;
```

```sqlite
ArtistId  앨범 수
--------  ----
90        21
22        14
58        11
50        10
150       10
```



### 13. 고객(customers) 테이블에서 `State`가 존재하는 고객들을 `Country` 와 `State`를 기준으로 그룹화해서 각 그룹의 `고객 수`, `Country`, `State` 를 출력하세요.

| 단, `고객 수`, `Country` 순서 기준으로 내림차순으로 5개까지 출력하세요.
```sql 
SELECT COUNT(*) AS "고객 수", Country, State FROM customers
WHERE State IS NOT NULL
GROUP BY Country, State
ORDER BY "고객 수" DESC, Country DESC
LIMIT 5;
```

```sqlite
고객 수  Country  State
----  -------  -----
3     USA      CA
3     Brazil   SP
2     Canada   ON
1     USA      WI
1     USA      WA
```



### 14.  고객(customers) 테이블에서 `Fax` 가 `NULL`인 고객은 'X' NULL이 아닌 고객은 'O'로 `Fax 유/무` 컬럼에 표시하여 출력하세요.

| 단, `CustomerId`와 `Fax 유/무` 컬럼만 출력하고, `CustomerId` 기준으로 오름차순으로 5개까지 출력하세요. 
```sql 
SELECT CustomerId,
    CASE
    WHEN Fax IS NULL THEN 'X'
    ELSE 'O'
    END AS "Fax 유/무"
FROM customers
ORDER BY CustomerId
LIMIT 5;
```

```sqlite
CustomerId  Fax 유/무
----------  -------
1           O
2           X
3           X
4           X
5           O
```