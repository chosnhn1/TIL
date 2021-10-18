DB

# Model Relationship I



Recap: CRUD and Auth





# Foreign Key

* 외래키 (외부키)
* 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
* 참조하는 테이블에서 1개의 키에 대항하고,
  참조되는 측 테이블의 기본 키를 가리킴
* 참조하는 테이블의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응
* 참조하는 테이블의 행 여러 개가 참조되는 테이블의 동일한 행을 참조할 수 있음

i. e. 게시글 TABLE << 댓글 TABLE [게시글 FIELD에서 게시글 TABLE의 게시글번호(기본 키) 참조]



## Foreign Key의 특징

* 키를 사용하여 부모 테이블의 유일한 값을 참조
* 외래키의 값이 반드시 부모 테이블의 기본키일 필요는 없으나, 유일한 값이어야 함
* (참조 무결성) >> 기본키 값



## ForeignKey field: Foreign Key in Django Model

[참고]:https://docs.djangoproject.com/en/3.2/ref/models/fields/#foreignkey

* M:1 Relationship
* 2개의 위치 관계 필요
  * 참조하는 model class
  * on_delete 옵션
* migrate 작업 시 필드 이름에 _id를 추가하여 데이터베이스 열 이름을 만듦



참고: 재귀 관계 (자신과 1:M)



i. e. comment 모델 정의하기

```python
# articles/models.py
class Comment(models.Model):
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

articles_comment

| id   | content | created_at | updated_at | article_id |
| ---- | ------- | ---------- | ---------- | ---------- |
|      |         |            |            |            |

* on_delete 인자
  * 외래 키가 참조하는 객체가 사라졌을 때 외래 키를 가진 객체를 어떻게 처리할 것인지 정의
  * 데이터 무결성을 위해 매우 중요한 설정
  * 가능한 값들: CASCADE, PROTECT, SET_NULL, SET_DEFAULT, SET(), DO_NOTHING, RESTRICT
    * CASCADE: 부모 객체가 삭제되었을 때 이를 참조하는 객체들도 삭제
    * PROTECT: 참조 객체가 있는 한 부모 객체를 삭제할 수 없음 (에러)
    * SET_NULL: NULL값으로 채움
    * SET_DEFAULT: 기본값으로 채움
    * SET(): parameter 내의 값으로 바꿈
    * DO_NOTHING: 그대로 유지
    * RESTRICT: 특정 객체는 유지



cf. 데이터 무결성

* Entity Integrity: 개체 무결성
  * pk NOT NULL UNIQUE
* Referential Integrity: 참조 무결성
  * FK 참조
* Domain Integrity: 범위 무결성
  * 정의된 형식 내에서 모든 컬럼이 선언



참조: 복합 키 - 여러 개의 데이터를 조합하여 PK처럼 쓰이는 키



ForeignKey 인스턴스를 생성할 때에는 명시적 모델 관계를 파악하기 위해 참조하는 클래스 이름의 소문자(단수형)으로 작성하는 것이 바람직함



## 1:N Related Manager

* 역참조 comment_set
  * Article(1) -> Comment(N)
  * `article.comment_set` manager가 생성됨
    * 참조관계를 생성할 때 역참조 manage도 생성됨
  * 게시글에 몇 개의 댓글이 작성되었는지 Django ORM이 보장할 수 없기 때문
    * article에는 comment가 있을 수도, 없을 수도
    * Article 클래스에는 Comment와의 어떤 관계도 작성되어 있지 않음
      * 역참조 != 상호참조
* 참조 article
  * Comment(N) -> Article(1)
  * comment는 반드시 자신이 참조하고 있는 article이 있으므로
    comment.article 과 같이 접근할 수 있음
  * 실제 ForeignKeyField 또한 Comment 클래스에서 작성됨

```python
article = Article.objects.get(pk=1)
article.comment_set.all()


```



### related_name: ForeignKey argument

역참조 시 사용할 이름('model_set' manager)을 변경할 수 있는 옵션

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
```

article.comment_set을 사용할 수 없게 되고, 대신 article.comments로 대체됨

migration 필요



# Comment Create





# Comment 추가사항

## 댓글 개수 출력

```
{{ comments|length }}
{{ article.comment_set.all|length }}
{{ comments.count }}
```





# Customizing Auth in Django

## Substituting a Custom User Model

* 일부 프로젝트에서는 Django의 내장 User 모델이 제공하는 요구사항이 적절하지 않을 수 있음
  * username 대신 email로 식별토큰을 사용하고 싶다면?
* Django는 User를 참조하는 데 사용하는 AUTH_USER_MODEL 값을 제공,
  default user model을 override(재정의)할 수 있음 (settings.py)
* Django는 새 프로젝트를 시작하는 경우, 기본 사용자 모델이 충분하더라도
  커스텀 유저 모델을 설정하는 것 highly recommended
* 단, 프로젝트의 모든 migrations, 첫 migrate를 실행하기 전에 이 작업을 마쳐야



### AUTH_USER_MODEL

* User를 나타내는 데 사용하는 모델
* 프로젝트 진행되는 동안은 변경 불가
* 프로젝트 시작 시 설정하기 위함, 첫번째 migration에서 사용할 수 있어야 함
* 기본값: `auth.User`



cf. 프로젝트 중간에 AUTH_USER_MODEL 변경

* 모델 관계 전체에 영향을 주기 때문에 지난한 작업이 필요
* 즉 중간 변경은 비권장사항, 초기 설정을 권장



### Define Custom User Model

```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):		# 이름이 같아도 상관없음
    pass		# AbstractUser를 받아서 쓰되, custom은 자유
```

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```



하지만 이대로는 UserCreationForm, UserChangeForm이 작동하지 않음

(이들 기본 제공 Form들은 auth.User를 사용하고 있는 중임)

그렇다면... 이들을 상속받아 custom form들을 만들자



cf. User 직접 참조 대신 get_user_model을 했었던 이유



### get_user_model()

현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환

즉, User 모델을 커스터마이징했다면 Custom User model을 반환

Django는 기본 모델이든, 커스텀 모델이즌 User 모델 직접 참조를 권장하지 않음



# User와 Article, Comment 관계 설정하기



User 모델 참조하기

1. settings.AUTH_USER_MODEL
   * models.py에서 User 모델을 참조할 때
2. get_user_model()
   * 나머지 경우



