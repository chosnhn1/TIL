* Static Files
* Media Files
* Image Upload and Resizing



# Static

//// 정적인 파일들 static files --------------------------------

// static: 개발자, 변경 적음 - media: 사용자, 변경 많음





## Static Files

응답 시 응답 내용에 따른 별도 처리 없이 내용을 그대로 표시하는 파일들

cf. 이미 준비된 HTML, 이미지, JS and CSS, font, ...

v. Dynamic Files 원본 자체가 요청에 따라 변하는 파일들

cf. 동적 디자인된 HTML, ...









### 구성의 단계

1. django.contrib.staticfiles가 INSTALLED_APPS에 포함되었는지 확인

   * 기본 설치됨

2. settings.py 에서 STATIC_URL을 정의

   * 기본: STATIC_URL = '/static/'

3. templates에서 static template tag를 사용하여, 지정된 상대경로에 대한 URL build

   * ```html
     {% load static %}
     <img src="{% static 'my_app/exmaple.jpg' %}" alt="image">
     ```

4. app의 static 폴더에 static file 저장

   * ex. my_app/static**/my_app/example.jpg**



### Django Template Tag

* load
  * 사용자 정의 템플릿 태그 세트 로드
  * 로드하는 라이브러리, 패키지에 등록된 모든
* static
  * STATIC_ROOT에 저장된 정적 파일에 연결

'collectstatic' >> STATIC_ROOT에서 배포를 위해 정적 파일을 수집



STATIC_ROOT: django에서 모든 정적 파일을 한 곳에 모아 넣는 경로

기본적으로 settings.py에 작성되어 있지도 않음

settings.py: DEBUG = True이면 적용되지 않음

실제 서비스 시 django가 여타 웹 서버에서 모든 정적 파일을 제공할 수 있도록....



AWS, Cafe24, ...



#### collectstatic

```
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

```
$ python manage.py collectstatic
```

#### STATIC_URL

STATIC_URL: STATIC_ROOT에 있는 정적 파일을 참조할 때 사용할 URL

개발 단계에서는 실제 정적 파일들이 저장되어 있는 app/static/ 경로와 STATICFILES_DIRS 에 정의된 추가 경로를 탐색

**(빈 값이 아니라면) 반드시 /로 끝낼 것!**



참고: extends 태그는 최상단에



## Uploading Images

### Media File

사용자가 웹에서, 웹에 업로드하는 정적 파일 (User-uploaded)

ImageField를 사용해 이미지 입력 받기!

* ImageField
  * FileField의 서브클래스: FileField의 속성과 메서드 사용 가능
  * 사용자에 의해 업로드된 객체가 유효한지 검사함
  * ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성
  * max_length 인자로 최대 길이 변경 가능
  * ! 사용하려면 반드시 "Pillow" Library 필요

* FileField
  * 파일 업로드에 사용하는 모델 필드
  * 2개의 선택 인자
    * upload_to
    * storage

#### upload_to

업로드 dir 파일 이름 설정 방법 2가지 제공

1. 문자열 경로
2. 함수

```python
class MyModel(models.Model):
    upload = models.FileField(upload_to='uploads/')
    # python strftime()
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
```

```python
# models.py

def articles_image_path(instance, filename):
    #
    return f'user_{instance.user.pk}/{}'
class MyModel():
    upload = models.FileField()
```



### MEDIA_ROOT

사용자가 업로드한 파일들을 보관할 디렉토리의 절대경로

(DB에는 경로를 저장하고 실제 파일은 여기에 저장한다)

settings.py에서 설정

! MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정되어야 한다

```python
MEDIA_ROOT = BASE_DIR / 'media'
```

폴더 직접 만들 필요 없이, 사용자가 업로드하면 폴더 생성

### MEDIA_URL

MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL

업로드된 파일의 URL를 만들어준다

비어있지 않은 값으로 설정한다면 반드시 slash로 끝나야

! MEDIA_URL 역시 STATIC_URL과는 다른 경로로 지정되어야 한다



### Serve User-uploaded Files during dev

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

참고: https://docs.djangoproject.com/en/3.2/howto/static-files/



# Image Upload

```python
class Article(models.Model):
	# ~~~~~
    image = model.ImageField(blank=True, upload_to='images/')
```

* upload_to: 실제 이미지 저장 경로
* blank=True: 빈 값도 받을 수 있도록

참조: blank 인자

기본값: False,

True인 경우 필드를 비워둘 수 있음, 저장될 때는 ''(빈 문자열)로 저장됨

blank=True라면, 유효성 검사 시 빈 값이 입력 가능해짐



참조 2: null 인자

기본값: False

True인 경우 django는 빈 값을 DB에 NULL로 저장

주의!

* 문자열 기반 필드에서는 NULL을 사용하는 것을 피해야
* 만일 문자열 기반 필드에서 NULL을 사용하면,
  * ''과 NULL로 "데이터 없음"을 두 가지 값이 표현하게 됨: 중복!

문자열 기반 필드가 아니라면 둘 다 사용할 수 있음

#### blank와 null의 비교

* blank: validation-related - 유효성 검사에서 확인
* null: database-related - DB에서 확인

null option은 DB에만 영향을 미치므로, form에서 빈값을 허용하려면 blank=True를 설정해야!!!



///

+

게시글 작성 시 form enctype을 설정해줘야....

```
<form enctype="multipart/form-data">
```



1. multipart/form-data
2. application/x-www-form-urlencoded
3. text/plain



+

Views에서 파일을 처리할 수 있도록!

request.FILES에 포함



### input accept="image/"

입력 허용할 파일 형식 필터링 (UX)

유효성 검증까지 하는 것은 아님

```
data=, files=
```



article.image.url **url로 받으세요 제발**

----



# Image Upload: Update

이미지는 Binary data이기 때문에 일부 수정이 불가능, 완전 대체해야



# Image Resizing

실제 원본 이미지를 서버에 그대로 업로드하는 것은 서버의 부담이 크다

그러므로, img으로 resize하는 것도 가능은 하지만 (그래봐야 원본은 그대로...) 아예 직접 올라오는 이미지 사이즈를 resize해보자

django-imagekit 라이브러리 활용!





----

django-cleanup

django.contrib.messages

```python
# pjt/settings.py
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# app/views.py

```

