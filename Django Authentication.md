# Django Authentication System

Django Authentication System will be on `django.contrib.auth`

1. `django.contrib.auth`
   * Authentication Framework
2. `django.contrib.contenttypes`
   * Link Au and Models

cf. OAuth



Django 인증 시스템: Authentication 인증 & Authorization 권한 통합

## Authentication and Authorization

Authentication: Who are you? ~ Identification

Authorization: You can do ~~~: 

*둘 구분하기*





Appname: accounts

django uses 'accounts' as auth name: can be changed, but 



# Cookies and Sessions

HTTP: Hyper Text Transfer Protocol

Client-Server Protocol

* Connectionless
  * After response, connections are closed
* Stateless
  * Lost connection - state not remains
* 즉, 본디 진행형이라는 것이 불가능한 규약
* "But how can it be?: Cookie and Session"

(Cookie and Session: 놀이공원 팔찌와 바코드의 비유)

## Cookie

Server will give little data to browser 

Cookie > [Key-Value] to local > when request, give back cookie



HTTP Cookie will make 'stateful' session

1. rq (i.e login)
2. rs w/ cookie
3. rq another page w/ cookie



1. Session Management

   : 로그인, 자동완성, 팝업 체크, 장바구니 등

2. Personalization

   : Customization, Theme, ...

3. Tracking

   : to analyze user behavior



## Session

Maintain states between the site and browser

rq > rs with cookie containing Session ID



## Cookie Lifetime

1) Session Cookies
   * Current Session
2) Persistent Cookies (Permanent Cookies)
   * Expires, Max-Age



## Session in Django

Django uses database-backed sessions basis

`django_session` table in DB

Middlewares

`SessionMiddleware` and `AuthenticationMiddleware`



# Logins

Login = Session Creating Logic

Django has bulit-in forms for authentication

i.e Login form, ...



### AuthenticationForm

* for user login
* 1st arg: request

https://docs.djangoproject.com/en/3.2/topics/auth/default/#django.contrib.auth.forms.AuthenticationForm



### login() function

`login(request, user, backend=None)`

### get_user() method

return user_cache:

which is...

login user object or None(when not valid)



## Authentication data in templates

context에 담지 않고도? 기본 context값!

`{{ user }}`: 로그인 사용자 auth.User 인스턴스 나타냄, 비로그인시 AnonymousUser 인스턴스



settings.py의 context processors

```python
# settings.py
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth'
            ]
        }
    }
]
```





## Logout

...is session delete logic

### logout(request) function

no return value

session data



## Limiting Access to Logged-in Users

1. raw way: is_authenticated attribute
2. login_required decorator



### is_authenticated

request.user.is_authenticated

권한 미확인, 유효한 세션 등 확인 안 함

오직 User 객체에 대해 True, AnonymousUser 객체에 대해 False를 돌려줄 뿐



```html
{% if request.user.is_authenticated %}
<p>
    Hello, {{ user }}!
</p>
{% else %}

{% endif %}
```



### login_required decorator

사용자가 로그인되어 있지 않으면, settings.LOGIN_URL에 설정된 문자열 기반 절대 경로로 redirect

기본값은 `/accounts/login/`

```python
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    pass
```

?next='redirect'

현재 URL로 요청을 보내기 위해 action값 비우기...!

----



참고: cruD에서 decorator가 오작동하는 이유

login_required가 GET을 들고 delete >> 405 Method Not Allowed 에러

```python
# articles/views.py

@login_required
@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')
```



1. redirect 과정에서 POST 데이터 손실
2. redirect는 GET으로 이루어짐

그렇다면.... @login_required 대신 is_authenticated를 사용하자





# User Creation

UserCreationForm

* username (from the user model)
* password1
* password2
* 권한이 없는 새 user를 생성하는 ModelForm



UserChangeForm

계정 정보 수정



but, admin에서 쓰이는 것과 같은 폼



## get_user_model()

현재 프로젝트에서 활성화된 사용자 유저 모델을 반환

django의 권장사항 ('직접 User 들고 오지 말고')



### What makes User Class?

UserChangeForm

> User
>
> > AbstractUser





password 필드가 계속 출력되는 문제



PasswordChangeForm

SetPasswordForm을 상속받는 서브클래스



암호 변경 시 세션 무효화 방지

update_session_auth_hase(request, user)

암호가 변경되면 인증 정보도 업데이트해주기

