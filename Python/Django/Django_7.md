# 📋Django 7

#### Category

[ModelForm](#%EF%B8%8F-ModelForm)



## ✔️ ModelForm

> 이미 models.py 에 저장한 `field`들을 그대로 HTML 문서에 사용하기 위해 이용한다.
>
> - 이렇게 하면, HTML 문서의 `<form>` 태그 사이에 입력값들을 다시 쓸 필요가 없다
>
> models.py 에 정의된 field에 맟춰
>
> - UI를 그려주고 / 유효성을 검사해주고 / DB에 저장시켜준다

------------------------------------------

#### CREATE

> UI 제공 **(GET)**   |   DB 저장 **(POST)**

#### READ

> DB에서 특정 데이터를 가져와서 조회

#### UPDATE

> UI 제공 **(GET)**   |   DB 저장 **(POST)**

#### DELETE

> DB에서 특정 데이터를 가져와서 삭제

------------------------------------------------------------------------------------

#### POST

- 데이터를 저장하거나 기록하는 행위
- 예) 평점 기록

#### GET

- 정보를 조회할 때 사용

### ModelForm 생성하기

> forms.py를 생성하고, 그 안에다 새로운 class를 만든다
>
> class 안에 model (models.py에서 가지고 오는 class 이름)과 해당 모델의 field를 설정한다

![modelform](Django_7.assets/modelform.png)

### Create

> create이라는 함수 안에 입력창과 입력값 저장을 한번에 할 수 있다
>
> 먼저 create/ 이라는 url 에 들어오면 메서드가 `GET`이기 때문에 바로 13번 줄로 가게 된다.
>
> - 13번 줄에서 reviewForm 이라는 ModelForm을 review_form에 저장을 한다
> - 그리고 그 review_form을 HTML 문서에 보낸다
> - HTML 문서에 `{{ review_form.as_p }}` 를 통해 입력창이 보이게 된다
>
> 해당 입력창에 유저가 정보를 입력하면 메서드가 `POST`로 바뀌고 7번줄로 넘어간다
>
> - 7번줄에서 유저가 입력한 데이터를 `request.POST`를 통해 가지고 온다
> - 데이터를 reviewForm에 넣은 후, review_form 변수에 저장을 한다
>
> 해당 변수안에 입력한 데이터가 유효하면 10번 줄로간다
>
> - review_form을 저장하고, index 페이지로 넘어간다
>
> 유효하지 않으면, 다시 18번줄로 가게 되고, 에러 메세지가 나온다

![Modelform2](Django_7.assets/Modelform2.png)

### Update

> create와 똑같다
>
> 다만, Update같은 경우 **특정** 데이터를 수정을 한다
>
> 그래서 `instance=review` 를 통해 수정을 할 특정 데이터를 가지고 올 수 있다
>
> - 여기서 review는 44번 줄에, Review 데이터베이스의 pk값을 일치한 데이터다

![modelform3](Django_7.assets/modelform3.png)
