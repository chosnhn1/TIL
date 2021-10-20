# Model Relationship

* Case Study: Hospital Records
* `ManyToManyField`
  * Apply #1: Like
  * Apply #2: Profile Page
  * Apply #3: Follow





# Case Study: Hospital Records

병원 진료 기록 시스템에서 필요로 하는 DB

Relationship Expression & Modeling



상호참조 대신 중개 모델을 이용한 참조



Doctor / Reservation 중개 모델 / Patient

1 : N : 1

```python
doctor1.reservation_set.all()
patient1.reservation_set.all()


```



## ManyToManyField

M:N 관계 설정 시 사용하는 모델 필드

하나의 필수 위치인지가 필요

```python
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()

# 

# ManyToManyField를 사용한 Reservation
patient1.doctors.add(doctor1)

# 참조
patient1.doctors.all()

# 역참조
doctor1.patient_set.all()

# doctor에서 reservation 생성
doctor1.patient_set.add(patient2)

# reservation 삭제
doctor1.patient_set.remove(patient1)

```

`related_name`

* target model이 source model을 참조할 때 사용할 manager 이름을 설정
  * 이 경우 target model: Doctor (MtoMField가 없는 쪽)
  * source model: Patient (MtoMField가 있는 쪽)



## 중개 모델(테이블)의 직접 작성 v. 자동 생성

중개 테이블은 Django의 ManyToManyField를 통해 자동 작성 가능

중개 테이블 수동 지정 가능 (`through` 옵션)

M:M 중개 테이블에 추가 데이터가 사용되는 경우에 주로 사용





# ManyToManyField

* M:N 관계 설정 시 사용하는 모델 필드
* 하나의 필수 위치인자 필요
* RelatedManager를 사용하여 관련 개체 추가, 제거 가능
  * add()
  * remove()
  * create()
  * clear()
  * ...
* arg 1: related_name
  * 역참조 시 사용할 이름 설정
* arg 2: through
  * 중개 테이블 직접 작성 시 모델을 지정
  * extra data with a many-to-many relationship
* arg 3: symmetrical



## Related Manager

* add()
  * 지정된 객체를 관련 객체 집합에 추가
  * 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
  * 모델 인스턴스, 필드 값(pk)을 인자로 허용
* remove()
  * 관련 객체 집합에서 지정된 모델 객체를 제거
  * 내부적으로 QuerySet.delete()를 사용
  * 모델 인스턴스, 필드 값(pk)을 인자로 허용
  * 



## 중개 테이블의 필드 생성 규칙

* Source Model != Target Model
  * id
  * <containing_model>_id
  * <other_model>_id
* ManyToMnayField가 동일한 모델을 가리키는 경우
  * id
  * from\_\<model>_id
  * to\_\<model>_id





# Case Study II: Like

"좋아요" 기능은 어떻게 저장될까?

User <> Like <> Article

User:Article M:N 관계의 중개 테이블

```
User 1:N Article

User M:N Article



User < like_users(필드명) < Article
User > User.article_set(X 중복) > Article
User > User.liked_articles(related_name) > Article

```



-----

학생 : 강의 = M : N

* 1학생: 여러 강의
* 1강의: 여러 학생



장바구니 예시

Atomic characteristic of DB

10가지의 상품을 구매한 1회의 결제를 처리하기 위해

Transaction: 10개의 자료 처리(atomic) = 1개의 commit



비효율적 자료 구조 해결: 중개 테이블



1. ForeignKey 두 개 들고 직접 중개 테이블 작성
2. ManytoManyField로 자동 중개 테이블 작성
   * 사용 용이
   * (기본적으로) 커스텀 불가



related_name: (역참조 manager명이 겹칠 때) 이름을 바꿀 수 있음



ManytoManyField로 생성되는 중개 테이블을 커스텀하는 법: through

symmetrical: 동일 테이블이 MtoM 관계가 될 때 설정 (i.e. 이웃, 팔로우 기능)

True: 기본값, 대칭

False: 비대칭





```
article.user
	1:N 참조
article.like_users
	M:N 참조
user.article_set
	1:N 역참조
user.like_articles
	M:N 역참조
```



----



```python
@require_POST
def likes(request, article_pk):
    # 로그인 여부
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        # 좋아요
        # "현재 좋아요 요청 사용자가(request.user) 해당 게시글에 좋아요를 누른 회원 목록에 있다면-"

        # 1. DB API의 exists()
        # 2. in all()
        # 대개 1이 2보다 효율적으로 찾음 (큰 QuerySet에서 존재 여부만 판단하는 경우)
        if article.liked_users.filter(pk=request.user.pk).exists():
        # if request.user in article.liked_users.all():
            # 좋아요 취소
            article.liked_users.remove(request.user)
        else:
            # 좋아요 등록
            article.liked_users.add(request.user)
        return redirect('articles:index')
    else:
        return redirect('accounts:login')
```

