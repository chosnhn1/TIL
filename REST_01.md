* HTTP Revisited
* RESTful API
* Response
* Single Model
* 1:N Relation



# HTTP

Hypertext Transfer Protocol

A Protocol for Send/Receive Contents through Web

* Request
* Response



* Stateless
* Connectless

Cookie and Session used for 'pseudo-' state and connect



### HTTP Request Methods

* Define actions towards resources
  * GET
  * POST
  * PUT
  * DELETE



### HTTP Response Status Codes

* Express 
* 5 Groups
  * Informational Responses 1--
  * Successful Responses 2--
  * Redirection Responses 3--
  * Client Error Responses 4--
  * Server Error Responses 5--





### Identifying Resources on Web

* Resource: Objects of HTTP Requests
* Identified by URI (Uniform Resource Identifier)



## Uniform Resource Identifier: URI

URI is URL and URN

### Uniform Resource Locator: URL

* 통합 자원 위치
* Past: Real resource location
* Present: Semantic resource locations
* "link", "web address" 

### Uniform Resource Name: URN

* Unique names
  * i.e. ISBN



### Structure of URI

* Scheme
  * Browser Protocols
    * https
    * data
    * file
    * ftp
    * mailto
    * ...
* Host (Domain name)
  * The name of the web server
  * IP Address
* Port
  * Gate for access resources
  * HTTP Standards (omittable)
    * HTTP 80
    * HTTPS 443
* Path
  * Resource path on web server
* Query 
* Fragment
  * as anchor
  * bookmarks



`https://www.example.com:80/path/to/myfile.html/?key=value#quick-start`



# RESTful API

## Application Programming Interface: API

Communication to applications via programming

* CLI
* GUI
* API

Web API

* R&R to other services
* Open APIs

Data Types

* HTML
* XML
* JSON





## Representational State Transfer: REST

A Methodology of Software Design

cf. Roy Fielding

Set of Network Architecture Principles

"RESTful": System within REST principles



### REST Principles

* Resource and Address
  * Resources: URI
  * Actions: HTTP Method - Get, Post, Put, Delete
  * Expressions: JSON



### JavaScript Object Notation: JSON

Lightweight Data-interchange format

Simple strings in JS notation

* Easy for both human reading and machine parsing
* key-value structure which is easy to convert



Not 'Must' but 'Great'



## RESTful API

API within REST Principles





# Response

예시 코드 1: 직접 만들어 제공

예시 코드 2: 내장 serializers 모듈

예시 코드 3: Django REST Framework (DRF Library)





JsonResponse objects

* HttpResponse subclass making JSON-encoded Response

Safe: True

if Serialization other than dict: False

 



## Serialization: 직렬화

Structure or Object Status >> Restructure Format for other Environment

cf. Reserve-serialization



Serializers in Django

Queryset, Model instance >> Python Datatypes





## Response - Django Serializer





## Django REST Framework



```python
# articles/serializers.py
# use installed rest_framework

from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
```



# Django REST Framework: DRF

Web API를 구축하기 위해 필요한 강력한 기능을 가진 Library



## Single Model

단일 모델의 Data를 serialization, JSON으로 변환하기

CRUD

* DRF Bulit-in Form
* Postman





`many` argument:

단일 인스턴스 대신 QuerySet 등을 직렬화하기 위해서는 many=True 작성



* Build articles as RESTful API 

|             | GET          | POST    | PUT         | DELETE      |
| ----------- | ------------ | ------- | ----------- | ----------- |
| articles/   | 전체 글 조회 | 글 작성 |             |             |
| articles/1/ | 1번 글 조회  |         | 1번 글 수정 | 1번 글 삭제 |



#### `api_view` Decorator

기본적으로 get 메서드 허용, 나머지 405

HTTP 메서드 목록을 인자로 받음

DRF에서는 필수적으로 작성해야 해당 함수 작동