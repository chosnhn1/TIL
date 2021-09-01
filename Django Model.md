# Django Model



# Model

단일 데이터에 대한 정보를 가짐

저장된 DB의 구조(Layout)

Django는 Model을 통해 데이터에 접속하고 관리

각각의 Model은 하나의 DB Table에 Mapping됨

*주의: Model != DB*



## Database and Query

Database

체계화된 데이터의 모임

Query

데이터 조회 명령어



### Database

Schema: DB Structure (Layout, Representation, Relation...)

Table: Column(Field) and Row(Record)





Primary Key

각 행의 고유값, 반드시 설정되어야 함

(not null & unique)



Model: 웹 App의 데이터를 구조화하고 조작하기 위한 도구



# Object Relational Mapping: ORM

객체관계매핑

OOP Language를 사용하여, 호환되지 않는 유형의 시스템 간에서 데이터를 변환하는 프로그래밍 기술

OOP 프로그래밍에서 RDBMS를 연동할 때...

Django는 내장 ORM을 사용



ORM Example

Python으로 된 명령: Object >> ORM >> SQL 명령어



Pros and Cons of ORM

* Pros
  * SQL을 몰라도 DB 조작 가능
  * SQL: Procedural vs. OOP: 높은 생산성
* Cons
  * ORM만으로 완전한 서비스를 구현하기 어려운 경우 많음

현대 Web Framework의 요점: Speed(Productivity)

"ORM for Object-Oriented DB Manipulation"





### Example Fields

CharField(max_length=None, **options)

* 길이제한 문자열
* CharField의 max_length: 필수
* 필드의 최대 길이, DB Level과 Django의 유효성 검사에서 활용

TextField(**options)

* 긴 글자열
* max_length 옵션을 작성하면 textarea 위젯에 반영되나 모델과 DB 수준에서 적용되지 않음 (유효성 검사 대상 아님)



# Migrations

django가 model에 생긴 변화를 DB에 반영하는 방법

migrate and schema controlling 명령어들

* makemigrations
* migrate
* sqlmigrate
* showmigrations

```
python manage.py ~~~
```

#### makemigrations

make migration blueprint for applying

appfolder/migrations에 저장됨

pending DB for db.sqlite3



#### migrate

apply migration to actual DB



```
python manage.py makemigrations
python manage.py migrate
python manage.py sqlmigrate Appname 0001
python manage.py showmigrations
```



### 변경하기



DateField

auto_now_add

최초 생성일자, 최초 insert시에만 현재 날짜와 시간으로 갱신

auto_now

최종 수정일

django ORM이 save할 때마다 현재 날짜와 시간으로 갱신



## 정리!

순서:

1. models.py
2. $ python manage.py makemigrations
3. $ python manage.py migrate



# Database API

직접 DB와 communicate하기 위한 도구

model를 만들면 django는 객체를 접근작성할 수 있는 DB-abstract API를 자동으로 만든다

```
Article.objects.all()
# ClassName.Manager.QuerySetAPI
# 예시: 모든 게시글을 조회
```



* Manager (".objects")
  * DB와 소통할 수 있는 method들을 보유
  * DB query 작업이 제공되는 인터페이스
  * 기본적으로 모든 django model 클래스에 objects라는 manager가 추가됨
* Query Set API
  * DB에서 전달받은 객체 목록
  * queryset 내 객체는 없거나 여러개일 수 있음
  * DB로부터 조회, 필터, 정렬을 수행할 수 있음



Django Shell

일반 Python Shell로는 장고 프로젝트 환경에 접근할 수 없음

대신 장고 프로젝트 설정이 load된 python shell을 활용해 DB API 구문 테스트 진행

"Django-extensions" 라이브러리의 shell_plus를 사용해서 진행

```
$ python manage.py shell_plus
```



https://docs.djangoproject.com/en/3.2/ref/models/querysets/

# CRUD

Create, Read, Update, Delete

```
article = Article()
article.title = 'first'
article.content = 'first page.'
article.save()
Article.objects.all()

article.title
article.content
article.id  # pk로 접근할 때, 실제 DB 상에서는 id임을 염두에 둘 것
article.pk  # Django 내부의 숏컷: 이걸로 접근하는 것을 권장
```

```
<Article: Article object (None)>
# id값이 없는 상태
# 저장되지 않은 상태 (save해야)
```

## Create

1. 인스턴스 변수 생성 후 하나하나 넣어주기
2. 초기값과 함께 인스턴스 생성
3. QuerySet API - create() 사용



* save() method:
  * for saving object to DB
  * save()를 호출하기 전에는 객체 id값을 알 수 없음
  * ID값은 django가 아니라 DB에서 계산되기 때문!
* \__str__() method:
  * 모델에 추가하면 개발에 유용하게 표현을 바꿀 수 있음
  * 단, 재작성 후에는 django 재시작해야.
  * 메소드 작성이 blueprint를 바꾸는 행동이 아니므로 makemigrations의 대상이 되지 않음
  * (불확실하면 그냥 makemigrations 할 것)
* 



## Read

QuerySet API method를 사용한 다양한 조회 (필터링!)

두가지 메서드들

* methods return new querysets (cf. all())
* methods do not return querysets (cf. create())



### all()

현재 QuerySet의 copy 반환

### get()

주어진 lookup arguments와 일치하는 객체 반환

단, 그 객체가 단 하나여야

* 없다? DoesNotExist 예외
* 많다? MultipleObjectReturned 예외

그래서 unique 조회에서 사용해야 함 (ex. pk로 접근 등)

### filter()

주어진 lookup arguments와 일치하는 객체를 포함하는 새 QuerySet을 반환



## Update

```
article = Article.objects.get(pk=1)
article.title = 'bye'
article.save()
```



## Delete

```
article = Article.objects.get(pk=1)
article.delete()
```

QuerySet의 모든 행에 대해 SQL 삭제 쿼리를 수행,

삭제된 객체 수와 유형당 삭제 수가 포함된 dict을 반환



삭제하면, 기본적으로 pk를 재사용하지 않음



## CRUD with views

### HTTP method

* GET
  * 특정 리소스를 가져오도록 요청할 때 사용
  * 반드시 데이터를 가져올 때만 사용해야 함!
  * DB에 변화를 주지 않음
  * CRUD에서 R 역할을 담당
* POST
  * 서버로 데이터를 전송할 때 사용
  * 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송
  * 서버에 변경사항을 만듦
  * CRUD에서 C, U, D를 담당

참고: method를 통해 URL 분리: Rest API



### Cross-site Request Forgery: CSRF

Web App 취약점

Against CSRF: django가 스스로 render한 페이지의 hash값을 심어서 확인

Security Token (CSRF Token)

#### Security Token

* 데이터에 임의의 난수값(hash) 제공
* csrf_token







----

Jargon

Primary Key / Foreign Key



cf. Login via Facebook

1. Email 받아오기 (못 쓰는 경우가 생김)
2. 랜덤 ID값 만들어 가상 Email 주소 생성

Frameworks have ORMs



migrations 폴더 내 일부만 삭제 금지금지 (꼬임)

