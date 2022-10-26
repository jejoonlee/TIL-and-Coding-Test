# 📋Django 16

#### Category

[M:N관계](#%EF%B8%8F-M:N관계)

- [Follow 기능](#follow-기능)





## ✔️ M:N관계

> 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
>
> `ManyToManyField`를 사용하게 되면, 중개 모델을 자동으로 만들어 준다
>
> `ManyToManyField`는 M:N 관계를 가진 모델 어디에 위치해도 상관이 없다

중계 모델을 따로 하나를 만들거나, `ManyToManyField`를 사용할 수 있다.

- `ManyToManyField`를 사용하게 되면, 중개 모델을 자동으로 만들어 준다
- `ManyToManyField`는 이어줄 모델들의 `ID` 값만 필드로 사용한다
  - `ID`값 외에도, 추가로 필드를 만들고 싶다면 중개 모델을 따로 만들어 주는 것이 좋다



```python
class Patient(models.Model):
    # ManyToManyField 작성
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()
```

`ManyToManyField(Doctor)` 를 통해 중개 모델이 따로 만들어졌다.

- 여기같은 겨우 `doctors` 필드는 `Patients` 모델 안에 있어, 의사 정보를 통해 환자의 정보를 받아오려면 역참조를 이용해야한다
  - `doctor1.patient_set.all()` : 의사 1의 환자 목록
- 뒤에 `related_name`을 통해 `patient_set` 말고 `patients`를 사용할 수 있다
  - `related_name`을 설정하면 기존 `_set manager`는 사용할 수 없다

```python
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
```

- 직접 중개 모델을 작성하고, `through`옵션을 사용하여, 중개 테이블을 나타내는 모델을 지정할 수 있다



#### Methods

| 메서드     | 기능                                       |
| ---------- | ------------------------------------------ |
| `add()`    | 지정된 객체를 관련 객체 집합에 추가        |
| `remove()` | 관련 객체 집합에서 지정된 모델 객체를 제거 |



### Follow 기능

> 유저와 유저와의 관계

```python
class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # symmetrical이 False라서 팔로우를 하면 서로 친구가 안 된다
```

- 'self' 를 넣어줘서, 그 자체 관계를 표현해준다 (1:N 기능에서도 가능하다)
- symmetrical = True (팔로우를 하면, 자동으로 맞팔을 한다)
- symmetrical = False (팔로우를 하면, 상대방도 맞팔을 해야, 맞팔이 형성된다)
  - 테이블에 `from_user_id` 와 `to_user_id`가 형성이 된다
