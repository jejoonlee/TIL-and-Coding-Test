# 📋Django 13

#### Category

[사진 업로드](#%EF%B8%8F-사진-업로드)

[imagekit](#%EF%B8%8F-imagekit)



## ✔️ 사진 업로드

#### 1. models.py 에 model을 imagefield로 생성

- DB에 필드 추가

![imageupload1](Django_10.assets/imageupload1.png)

#### 2. HTML의 `<form>` 에 enctype=multipart/form-data 를 추가한다

- Form이 저장되면, 위의 'enctype'을 통해 따로 이미지 파일을 생성한다

![imageupload2](Django_10.assets/imageupload2.png)

#### 3. views.py에 request.POST 와 request.FILES을 설정한다

- 그 전에는 request.POST만 넣었는데, enctype을 통해 파일을 따로 생성했으므로, `request.FILES`도 같이 해준다
- DB에는 파일의 경로만 저장이 되어 있다

![imageupload3](Django_10.assets/imageupload3.png)

> 여기까지는 서버에서만 image가 저장되어 있다

#### 4. settings.py 에 해당 내용을 설정한다

- `MEDIA_ROOT = BASE_DIR / '파일이 저장될 폴더 이름'`
- `MEDIA_URL = '/media/'`

이미지를 (또는 파일을) 서버에서 보여주는 방법이다

![imageupload4](Django_10.assets/imageupload4.png)

#### 5. 파일을 가지고 오는 것

```python
# settings.py가 있는 폴더의 urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  # path 경로들
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```

- static 파일을 settings.py에서 설정한 MEDIA_URL에서 지정한 media 디렉토리에서 가져오겠다는 것

![imageupload5](Django_10.assets/imageupload5.png)





## ✔️ imagekit

>  https://github.com/matthewwithanm/django-imagekit 참고
>
> 이미지 용량을 줄이거나, 적절한 사이즈로 변경하는 등
>
> imagekit 라이브러리를 다운로드 받고 models.py에서 사용한다
>
> - 이미지를 입력 받게 되면, 원하는 용량 또는 사이즈로 imagekit을 통해 변환해준다

1. `pip install django-imagekit`

![imagekit1](Django_10.assets/imagekit1.png)

![imagekit2](Django_10.assets/imagekit2.png)
