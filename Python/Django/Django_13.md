# 📋Django 17

#### Category

[views.py](#%EF%B8%8F-views.py)



## ✔️ views.py

> view.py에서 클라이언트에 응답 (response)를 해주는 것은 HTML이 아닌 HTTP다
>
> `render`를 통해 HTML 템플릿을 응답하는 것
>
> - render: 2xx + HTML
>
> - redirect: 3xx 
>
> - @login-required

#### HTTPS

- 400번대 에러
  - URL를 잘 못 입력 했을 때 / URL을 못 찾을 때
- 500번대 에러
  - URL 외에, 모든 에러가 발생했을 때9
