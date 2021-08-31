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
python manage.py startapp articles
```

*일반적으로 app명은 복수형으로 작명함*

