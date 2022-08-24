# 데이터베이스 07 - ORM

<aside>
💡 코드를 작성한 실습 파일을 압축해서 실라버스에 제출해주세요.

</aside>

### 1. `db/models.py` 파일에 아래의 모델 2개 `Director` `Genre` 를 작성하세요.

> 기본 코드
> 

```python
class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()
```



### 2. 모델을 마이그레이트(migrate) 하세요.

```bash
# 가상환경 실행 확인 후 아래 명령어를 터미널에 입력합니다.
python manage.py makemigrations

python manage.py migrate
```



### 3. Queryset 메소드 `create` 를 활용해서  `Director` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| name | debut | country |
| --- | --- | --- |
| 봉준호 | 1993-01-01 | KOR |
| 김한민 | 1999-01-01 | KOR |
| 최동훈 | 2004-01-01 | KOR |
| 이정재 | 2022-01-01 | KOR |
| 이경규 | 1992-01-01 | KOR |
| 한재림 | 2005-01-01 | KOR |
| Joseph Kosinski | 1999-01-01 | KOR |
| 김철수 | 2022-01-01 | KOR |

> 코드 작성
> 

```python
Director.objects.create(name = '봉준호', debut = '1993-01-01', country = 'KOR')
Director.objects.create(name = '김한민', debut = '1999-01-01', country = 'KOR')
Director.objects.create(name = '최동훈', debut = '2004-01-01', country = 'KOR')
Director.objects.create(name = '이정재', debut = '2022-01-01', country = 'KOR')
Director.objects.create(name = '이경규', debut = '1992-01-01', country = 'KOR')
Director.objects.create(name = '한재림', debut = '2005-01-01', country = 'KOR')
Director.objects.create(name = 'Joseph Kosinski', debut = '1999-01-01', country = 'KOR')
Director.objects.create(name = '김철수', debut = '2022-01-01', country = 'KOR')
```



### 4. `인스턴스 조작` 을 활용하여`Genre` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| title |
| --- |
| 액션 |
| 드라마 |
| 사극 |
| 범죄 |
| 스릴러 |
| SF |
| 무협 |
| 첩보 |
| 재난 |

> 코드 작성
> 

```python
genre = Genre(title = '액션')
genre.save()
genre = Genre(title = '드라마')
genre.save()
genre = Genre(title = '사극')
genre.save()
genre = Genre(title = '범죄')
genre.save()
genre = Genre(title = '스릴러')
genre.save()
genre = Genre(title = 'SF')
genre.save()
genre = Genre(title = '무협')
genre.save()
genre = Genre(title = '첩보')
genre.save()
genre = Genre(title = '재난')
genre.save()
---------------------------------------------------------------
gen = ['액션', '드라마', '사극', '범죄', '스릴러', 'SF', '무협', '첩보', '재난']
for i in gen:
    genre = Genre()
    genre.title = i
    genre.save
```



### 5. Queryset 메소드 `all` 을 활용해서 `Director` 테이블의 모든 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
Joseph Kosinski 1999-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
director = Director.objects.all()
for i in director:
    print(i.name, i.debut, i.country)
```



### 6. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `id` 가 1인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
director = Director.objects.get(id = 1)
print(director.name, director.debut, director.country)
```



### 7. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 USA인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
> 

```python
Director.objects.get(country = 'USA')
```

```python
DoesNotExist: Director matching query does not exist
```



### 8. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
> 

```bash
DoesNotExist: Director matching query does not exist
```

> 이유 작성
> 

```
.get은 하나의 데이터만 출력한다. 하지만 country에 USA는 존재하지 않아, 값이 존재를 안 한다고 애러가 떴다.
만약 KOR를 찾게 되면, `MultipleObjectsReturned`라고 오류 메세지가 뜬다
```



### 9. Queryset 메소드 `get` 과 `save` 를 활용해서 `Director` 테이블에서  `name` 이 Joseph Kosinski인 데이터를 조회해서 `country` 를 USA 로 수정하고, 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
Joseph Kosinski 1999-01-01 00:00:00 USA
```

> 코드 작성
> 

```python
director = Director.objects.get(country = 'USA')
print(director.name, director.debut, director.country)
```

### 10. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
> 

```python
Director.objects.get(country = 'KOR')
```

### 11. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
> 

```bash
MultipleObjectsReturned
```

> 이유 작성
> 

```
KOR 라는 값이 많아서, 애러가 뜬다
.get은 입력한 값이 하나만 존재 할 때 출력이 된다
```

### 12. Queryset 메소드 `filter` 를 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
director = Director.objects.filter(country = 'KOR')
for i in director:
    print(i.name, i.debut, i.country)
```



### 13. 본인이 생각하는 혹은 찾은 `get` 과 `filter` 의 차이를 작성하세요.

```
.get 은 찾는 행의 값들 중에, 값이 하나만 있을 경우 데이터를 출력한다. 아예 없거나, 2개 이상 데이터가 존재할 경우, 애러가 뜬다. 그래서 주로 ID처럼 값이 하나 밖에 없는 데이터를 검색할 때에 .get을 쓰는게 좋은 것 같다. 
.filter는 SQL에서 WHERE 같이, 데이터를 조회하고 싶을 때 사용한다. 일종의 리스트이다.
```



### 14. Queryset 메소드 `get` 과 `delete`를 활용해서  `Director` 테이블에서 `name` 이 김철수인 데이터를 삭제하는 코드를 작성하세요.

> 코드 작성
> 

```python
director = Director.objects.get(name = '김철수')
director.delete()

director = Director.objects.all()
for i in director:
    print(i.name, i.debut, i.country)
```

```python
(1, {'db.Director': 1})

봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
Joseph Kosinski 1999-01-01 00:00:00 USA
```

