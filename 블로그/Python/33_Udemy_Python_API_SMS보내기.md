# Udemy : API, 환경 변수, SMS보내기

https://apilist.fun/



## API Authentication

> #### 인증이 필요한 API 사용하기
>
> - API 중에는, 인증이 필요하지 않은 API가 있지만 인증이 필요한 API도 있다
> - 주로 돈을 내야하는 API가 인증이 필요하다 (데이터를 얻기 위해서는 비용이 필요하다)



#### 인증을 통해, API를 제공하는 사람들이, API를 통해 데이터를 사용하는 사람들을 알 수 있다

- 데이터를 얼마나 사용하는지에 따라, 사람들을 관리할 수 있다
  - 공부를 위해 API를 사용하는지, 상업적 용도로 사용하는지 추적할 수 있다



## env 파일

> environment 파일
>
> 주로 Github에 코드를 올릴때 보안을 위해서 필요하

#### env파일에 미리 변수에 특정 데이터를 저장할 수 있다



#### 보안을 위해 사용이 된다

- API key와 인증이 필요한 것들을 구현한 코드와 나눠서 저장 할 수 있다
- 코드에 API key 또는 보안이 필요한 데이터가 들어가면, 온라인 상 모든 사람들이 볼 수 있다
- 즉, 따로 다른 환경 파일에 보안이 필요한 데이터와 API key를 저장하여 보안을 강화시킬 수 있다



```python
import os
from dotenv import load_dotenv

load_dotenv()

def send_email():
    my_email = os.getenv("my_email")
    receive = "devjoon1996@gmail.com"
    my_password = os.getenv("my_password")

    connection = smtplib.SMTP_SSL(url="smtp.naver.com", port=465)
    connection.login(my_email, my_password)

    msg = MIMEText("12시간 안에 비가 오니 우산 챙겨!")
    msg["From"] = my_email
    msg["Subject"] = "오늘 비가 와요"
    msg["To"] = receive

    connection.sendmail(my_email, receive, msg.as_string())

api_key = os.getenv("api_key")
```

- `.env` 파일에 나의 이메일, 비밀번호, 그리고 API_Key를 저장했다
- `os`와 `load_dotenv`를 import한다
- `load_dotenv`를 통해서 `.env` 파일을 실행 시킨다
- `os.getenv("변수명")`을 넣어서, `env` 파일에 저장한 변수명의 데이터를 가지고 온다







