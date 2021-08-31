# Django

Django, the Web Framework

*!important*

> Django is a high-level Python Web framework, that encorages rapid development and clean, pragmatic design.

> It takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel.

#####

*DRY: Do not repeat yourself*

High-level vs. Low-level

: Human-friendly vs. Device-friendly

#####



API 서버 만들기 등

React, Vue.js // Django, Spring



* Web Framework
* Django Intro
* Request and Response
* Templete
* HTML Form
* URL
* Namespace



# Web Framework

## Framework

*Mealkit? Franchaise?*

* A group of classes and libraries for constructing standard frame dedicated to specified OS
* Reusable codes are integrated into the framework: "Reinventing the wheel" is no longer necessary
* "Application Framework"

What is the difference between Framework and Library?

*the analogy of vehicle and tool*

참고: flask

fast and pragmatic development

## Web Framework



Django Python-grounded Web framework

*Django Using Services*

Spotify Instagram Dropbox





## Framework Architecture

* MVC Design Pattern
  * Model
  * View
  * Controller
* UI로부터 Program Logic을 분리!
* App의 시각적 요소 // 뒷면에서 실행되는 부분을 **서로 영향 없이** 쉽게 고칠 수 있는 애플리케이션을 만들 수 있음
* *MTV Pattern: Template as view, View as controller*

cf. 정보와 계산 (Data and Expression)



Model ~ Data ~ DB

View ~ Representation

Controller - Bridge btw Model and View



### MTV Pattern

* Model
  * Data Structure and DBMS
* Template
  * Definition and Presentation
* View
  * Request and Response



HTTP Request > URLS > View > HTTP Response

View <> Model, Template

URLS as Deliverer



# Starting Django

가상환경 설정, 켜기

```
python -m venv venv
source venv/Scripts/activate
```

참고: 가상환경 끄기

```
deactivate
```

장고 설치와 시작

```
pip install django
django-admin startproject [name] .

python manage.py runserver
>>> Starting development server at ________
```

development server 들어가기

나갈 때는 Ctrl+C (Command + Break)



## 프로젝트 구조

* \__init__.py
  * Python treats it as a library (for compatibility)
* asgi.py
  * Asynchronous Server Gateway Interface
  * Django App이 비동기식 웹 서버와 연결/소통하는 도구
* settings.py
  * All settings of App
* urls.py
  * link url to corresponding views
* wsgi.py
  * Web Server Gateway Interface
  * Django App will communicate w/ Web Server via wsgi.py
* manage.py
  * Command Line Utility



## Application 생성

```
python manage.py startapp AppName
```

*일반적으로 app명은 복수형으로 작명함*

**INSTALLED_APPS에 등록하기!!!!!** (아래 참조)

Django Project=============

​	Config

​	App1

​	App2



* admin.py
  * 관리자용 페이지
* apps.py
  * 앱의 정보가 작성
* models.py
  * 앱에서 사용할 Model을 정의
* tests.py
  * 테스트 코드 작성
  * *참고: Test-driven Development*
* views.py
  * View(Controller) 함수들이 정의되는 곳

*Templates will be constructed manually!*



## Project and Application

* Project
  * collection of apps
* Application



### settings.py

```
Project > settings.py에서
INSTALLED_APPS에 앱 등록
```

**Django에서는 Apps을 사용할 때 위에서부터 아래로 사용한다!**

**매우 중요**



```
LANGUAGE_CODE
TIME_ZONE
USE_I18N
USE_L10N
USE_TZ
```

App 등록할 때는

1. Local Apps
2. Third-Apps
3. Django

순서로 하는 것이 좋다.



# Requests and Responses

​				<<<< Request <<<< (address)

Server											Client   >>>>>> Construct (Browser)

(text, html, ...) >>>> Response >>>>



User > Rq > [Django "URL" > View <> Model and Template]

User < Rs < [Django < View]



## URLS

```python
from articles import views  # add

urlpatterns = [
    path('index/', views.index),  # add
    path('admin/', admin.site.urls),
]
```

= articles / views.py == 

```python
def index(request):							# add
    return render(request, 'index.html')	# add
```





### Static Web Page

서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹페이지

### Dynamic Web Page

방문자와 상호작용하는 웹페이지



# Template

데이터 표현을 제어하는 도구, 표현 관련

Django Template Language: Built-in Template System

## Django Template Language



### DTL Syntax

* Variable
* Filters
* Tags
* Comments



#### Variable

```python
def __():
	return render(request, '.html', {name: ''})
	
def __():
	return render(request, '.html', context)
```

context 변수에 담아 세번째 인자로 넘기는 것이 권장됨

```html
<p>
    {{ foods.0 }}을 제일 좋아합니다.
</p>
```



#### Filter



#### Comments

HTML 주석 `<!-- -->`

DTL 주석 `{%}



### Template Inheritance

템플릿의 공통 부분을 상속받을 수 있도록!





# HTML Form

HTML "form" element

웹에서 사용자 정보를 입력하는 여러 방식을 제공, 서버로 전달

* action: 입력 데이터가 전송될 URL 지정
* method: 입력 데이터 전달 방식 지정



"input" element

데이터 입력받음

* name: 이름에 설정된 값을 넘김
  * GET/POST 방식 key, value



"label"

* UI 항목에 대한 설명
* label과 input 연결하기
  * input에 ID
  * focusing, activating

"for"

* 



# URL

* Django URLs:
  * URL as a dispatcher
  * Web application starts from client requests via URL



**!important**

* Variable Routing
  * URL as a variable
  * view 함수의 인자로 넘길 수 있음
* URL Path Converters
  * str
    * default
  * int
  * slug
  * uuid
  * path
* 



App별 url 분리와 include

```python
urlpatterns = [
    path('articles/', include('articles.urls')),
]
```



참고:

```python
urlpatterns = [
    path('', views.index)
]
# 기본 주소('')로 들어왔을 때의 동작
```



### Name URL Patterns



# Namespace

### Namespace Conflict

주의: settings.py INSTALLED_APPS 앱 순서로 인해

다른 app에서 같은 이름의 함수를 만들어도

먼저번 app의 함수를 가져와 쓰고 끝낸다



해결법:

1. templates / [AppName] / __.html
2. app_name 속성





----



Jargon



Timestamp: date의 표현식 (format)

