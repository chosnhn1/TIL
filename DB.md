# Database & SQL



# Database

Structured & Integrated Set of Data

Table, Dictionary, ...

cf. RDBMS, NOSQL

중복회피, 구조화된 자료 집합



## Pros on Database

*!Important*

* Minimize Duplication 중복 최소화
* Data Integrity 데이터 무결성
* Data Consistency 데이터 일관성
* Data Independence 데이터 독립성
* Data Standardization 데이터 표준화
* Data Security 데이터 보안유지

**SQLD**

DBMS (Database Management System)

* <> DB Language
  * <> DB Manager
  * <> User & Applications
* <> Storage Manager
  * <> DB
  * <> Data Dictionary



## Relational Database: RDB

Relations of keys and values are represented by table

### Words

* Schema
* Table
* Column
* Row
* Primary Key

#### Schema

Description of data structure, representation and relations

ex)

| column | datatype |
| ------ | -------- |
| id     | INT      |
| name   | TEXT     |
| age    | INT      |

#### Table



#### Column



#### Row

~ Record

Data 

#### Primary Key

Unique, Not Null-key that used as 



## Relational Database Management System: RDBMS

cf.

* MySQL
* SQLite



# SQLite

Lite, file-form rather than server-form

Easy on Local, Opensource, often used in Android & Embedded system



## SQL: Structured Query Language

RDBMS의 데이터 관리를 위해 설계된 *특수 목적 프로그래밍 언어*

What can SQL do?

* make and modify schema
* manage and search data
* access DB objects

### 

!important

* DDL
  * CREATE, DROP, ALTER, ...
* DML
  * INSERT, SELECT, UPDATE, DELETE, ...
* DCL



### Make DB in SQLite3

```sqlite
$ splite3 tutorial.sqlite3
sqlite> .database
```





```sql
SELECT * FROM examples;
```



```sql
CREATE TABLE tablename (
field1 INTEGER PRIMARY KEY,
field2 TEXT
);
```

```sqlite
sqlite> .schema classmates
```

```sql
DROP TABLE tablename;
```



SQLite Datatype

* NULL: null값
* INTEGER: 정수
* REAL: 실수
* TEXT: 텍스트
* BLOB: (통으로)



## DML: Data Manipulation Language

### Create: INSERT

```sql
INSERT INTO classmates (name, age) VALUES ('김철수', 21);
```



### Read: SELECT

테이블에서 데이터 조회

다양한 절(clause)과 함께 쓰이며 SQL에서 가장 복잡한 형태가 되기도 함

WHERE, ORDER BY, DISTINCT, LIMIT, ...

```sql
```

```sql
SELECT rowid, name FROM classmates
SELECT rowid, name FROM classmates LIMIT 3;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
```



## SQLite Functions

"window function"

* COUNT
* AVG
* MAX
* MIN
* SUM



!important

LIKE Operator



%: 0개 이상의 문자

_: 임의의 단일 문자

cf. 김, 김이, 김이박

김%: 셋 다 나옴

김_: '김이'만 나옴



2%_%



----



### SELECT: ORDER BY

조회 결과 집합을 정렬

ASC (기본값)

DESC



```sql
SELECT * FROM classmates ORDER BY age ASC;
-- 표기하지 않으면 기본값은 ASC

SELECT * FROM table ORDER BY col1, col2 DESC; 
-- 1. col1을 ASC하고,
-- 2. 같은 col1에서 col2을 DESC한다
```



### SELECT: GROUP BY

"to make a set of summary rows, from a set of rows": 행 집합에서 요약 행 집합을 만들기

sentence에 WHERE 절이 있다면 WHERE 절 뒤로 가야

```sql
SELECT col1, aggregate_function(col2) FROM table GROUP BY col1, col2;
```



```sql
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;

SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
```

AS (Aliasing): 들고 오는 column명을 바꿀 수 있음



### ALTER TABLE

자주 쓰이지는 않는 기능

```sql
ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;
```

```sql
CREATE TABLE articles (
title TEXT NOT NULL,
content TEXT NOT NULL
);

INSERT INTO articles VALUES ('1번 제목', '1번 내용');


```

!important 아래 코드는 왜 에러가 날까요? 어떻게 해결할 수 있을까요?

```sql
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL; 
```

기존 레코드들에는 새로 추가할 필드에 대한 정보가 부재

1) NOT NULL 없이 추가하기
2) DEFAULT 설정하기



# SQL with ORM



----

in SQLite

.shell clear

.exit

in django_shell_plus

clear

exit

$ python manage.py shell_plus --print-sql

```python
User.objects.all()

```

```sql
SELECT "users_user"."id", ... FROM "users_user"
```



!important ORM/SQL 구문에서 뭘 잘못 작성하면 INSERT가 되지 않는지 확인하자

(pk not unique, value not null, ...)







```python

User.objects.filter(age=30).values('first_name')
```



__gte: >

__get: >=

__lte: <= 

__lt: <

```python
Entry.objects.filter(id__gt=4)
```

```sql
SELECT ... WHERE id > 4;
```

```python
User.objects.filter(age__gte=30).count()
User.objects.filter(age=30, last_name='김').count()
# filter는 기본적으로 AND 연산
# 그럼 OR은 어떻게?

from django.db.models import Q
User.objects.filter(Q(age=30) | Q(last_name='김'))
```

```sql
SELECT * FROM users_user WHERE age=30 OR last_name='김';
```

```python
User.objects.filter(phone__startswith='02-').count()
```



```python
## 검색
User.objects.filter(first_name__contains='명')
```

```python
User.objects.filter(country='강원도', last_name='황').values('first_name')
```

!important

```python
User.objects.order_by('-age')[:10]
User.objects.order_by('balance')[:10]

# 주의: ORM -- 5번째는 4로 접근
User.objects.order_by('-last_name', '-first_name')[4]
```



```sql
SELECT * FROM users_user ORDER BY age DESC LIMIT 10;
SELECT * FROM users_user ORDER BY balance LIMIT 10;

SELECT * FROM users_user ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSET 4;
```



----

# Django Aggregation

Aggregate calculates values for the entire queryset.

cf. SQLite Window Functions

```python
from django.db.models import Avg
User.objects.aggregate(Avg('age'))
```

```sql
SELECT AVG(age) FROM users_user;
-- SELECT AVG(age) AS age_AVG FROM users_user;
```



```python
User.objects.filter(last_name='김').aggregate(Avg('age'))
```

```sql
SELECT AVG(age) FROM users_user WHERE last_name='김';
```

```python
User.objects.filter(country='강원도').aggregate(Avg('balance'))
```

```sql
SELECT AVG(balance) FROM users_user WHERE country='강원도';
```

```python
from django.db.models import Max, Min
User.objects.aggregate(Max('balance'))
User.objects.aggregate(Min('age'))
```

```sql
SELECT MAX(balance) FROM users_user;
SELECT MIN(age) FROM users_user;
```



## Annotate

Annotate calculates summary values for each item in the queryset.

*원본 테이블을 변형시키지 않은 채* 주석 column

```python
from django.db.models import Count

User.objects.values('country').annotate(Count('country'))
User.objects.values('country').annotate(num_countries=Count('country')) # Aliasing
```



```sql
SELECT country, COUNT
```



```python
User.objects.values('country').annotate(Count('country'), avg_balance=Avg('balance'))
```



----

!important

.tables: 

Primary Key (vs. 'id': django )