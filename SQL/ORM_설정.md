# ✍️ ORM 시작하기

#### 가상 환경

- **가상 환경 생성**

```python
$ python -m venv venv
```

- **가상 환경 실행**

```python
$ . venv/Scripts/activate
# (venv)
# 이게 확인이 되면 가상 환경 안에 들어온 것

$ deactivate
# 가상 환경 종료
```

- **확인하기**

```python
$ python main.py
```



#### 패키지 설치

- **가상 환경을 실행한 상태로**
- `pip install`

```python
$ pip install -r requirements.txt
# 폴더에 있는 txt 파일 이름을 넣으면 된다
```

- django 패키지 설치 확인

```python
$ python manage.py --version
```



#### Migrations (모델을 migrate하기)

```python
# migrations 폴더 안에, models 파일에 schema를 만든다

python manage.py makemigrations

python manage.py migrate
# schema를 만들고 데이터베이스를 반들기
# 데이터 베이스가 만들어진다
```



#### Schema 예시

```python
from django.db import models

class Director(models.Model):
    name = models.TextField()
    debut = models.DateField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()

class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete = models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    title = models.TextField()
    opening_date = models.DateField()
    running_time = models.IntegerField()
    screening = models.BooleanField()
```



#### Django Shell 진입

```python
$ python manage.py shell_plus
```

