# SQLite



#### SQLite는 MySQL과 PostgreSQL과 같은 데이터 베이스 관리 시스템이다



#### 하지만 다른 점이 있다면, 서버리스다

- MySQL과 PostgreSQL는 데이터 베이스를 관리할 때에 서버를 통해 관리를 한다
- 하지만 SQLite는 응용프로그램에 넣어서 데이터를 사용하는 비교적 가벼운 데이터 베이스다
- 그래서, 대규모의 데이터가 아니라면 괜찮게 사용이 가능하다





#### 실행하기

```sqlite
MissionOneProject> sqlite3

만약에 sqlite3가 설치가 안 되어 있으면

MissionOneProject> sudo apt install sqlite3
```



#### 데이터 베이스 생성

```sqlite
sqlite> .open 데이터베이스이름.db
```



#### 데이터 베이스 열기

```sqlite
MissionOneProject> sqlite3 데이터베이스이름.db
```





#### 테이블 만들

- PK 는, 원하는 column에 Primary Key 를 지정해주면 된다
  - AUTOINCREMENT는 알아서 PK를 지정해주되, 번호를 1씩 더해서 데이터를 저장한다
- FK는 Foreign Key 와 References를 사용하여 만들어주면 된다

```sqlite
CREATE TABLE Table1 (
	parent_id     INTEGER  Primary Key AUTOINCREMENT  NOT NULL , -- 북마크 ID
	register_time DATETIME NULL     , -- 등록 시간
	update_time   DATETIME NULL      -- 수정시간
)

CREATE TABLE Table2 (
	manage_num       VARCHAR(50)  Primary Key  NOT NULL, -- 관리번호
	parent_id        INTEGER      NULL, -- 북마크 ID
	distance         INTEGER      NULL, -- 거리
	Gu               VARCHAR(50)  NULL, -- 자치구
	
	FOREIGN KEY(parent_id) REFERENCES Table1(parent_id)
)
```

