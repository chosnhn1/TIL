# Django Form

데이터 유효성 검증 등 편리하게: Django Form

일반 HTML form, input을 이용하면 유효성 검증 수행 등이 굉장히 time-consuming한 작업.... (중요하지만 작업량이 너무 과중해짐)

Django에서의 process flowchart

참고 이미지: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms/form_handling_-_standard.png

Django Form을 사용하면?

* 주요 유효성 검사 도구
* 공격, 우연한 데이터 손상에 대응하는 수단
* Form 기능의 방대한 부분을 단순, 자동화

Django가 처리하는 세 부분

* 렌더링 위한 데이터 준비와 재구성
* HTML Forms 생성
* 데이터 수신 및 처리

Django Form Class

* Form 관리 시스템의 핵심
* Form 내 Field, 배치, Widget, Label, 초기값, 유효하지 않은 값에 대한 Error Msg 등 결정
* 과중한 작업과 코드 반복을 줄여줌



Form 선언하기

```python
# articles/forms.py ## 작성하기

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField() # Model과 다름: TextField 없음
```

Form 클래스의 인스턴스를 사용

```
{{ form.as_p }}
```

각각을 p 태그로 묶어 표시

Form Rendering Options

* as_p()
* as_ul(): li 태그로 감싸기 *
* as_table(): tr 태그로 감싸기 *

ul 태그와 table 태그는 직접 작성해야



참고: cleaned_data





## Django의 HTML input 요소 표현 방법 두 가지

1. Form inputs
   * input에 대한 유효성 검사 로직을 처리
   * 템플릿에서 직접 사용됨
2. Widgets
   * 웹 페이지의 HTML input 요소 렌더링
   * GET/POST dict에서 데이터 추출
   * widget은 반드시 form fields에 할당됨



## Widgets





주의:

Form Fields는 유효성 처리

Widget은 원초적인 rendering만 (Form Fields 이하에서 쓰여야)



```python
class ArticleForm(forms.Form):
    
```

```python
class ArticleForm(forms.Form):
    REGION_A = 'sl'
    REGION_B = 'dj'
    REGION_C = 'dg'
    REGION_D = 'bs'
    REGION_CHOICES = [
        (REGION_A, '서울'),
        (REGION_B, '대전'),
        (REGION_C, '대구'),
        (REGION_D, '부산'),
    ]
    region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select())
    
```



# ModelForm

Model에서 정의한 것을 Form에서 재정의

Django는 그 대신 Model을 통해 Form Class를 만들 수 있는 Helper를 제공 ("ModelForm")

## ModelForm Class

Model을 통해 Form Class를 만들 수 있음

일반 Form Class와 완전히 같은 방식으로 view에서 사용 가능

```python
# articles/form.py

class ArticleForm(forms.ModelForm):
    # 굳이 재정의하지 않음
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)
```

클래스 안에 Meta 클래스를 선언하고, 어떤 모델을 기반으로 form을 작성할지 서술

## Meta Class

참고: Inner class, Metadata



## 유효성 검사

```python
form = ArticleForm(request.POST)

new_article = f.save()

# update

article = Article.objects.get(pk=pk)
form = ArticleForm(request.POST, instance=article)
form.save()
```

### `is_vaild()` method

* 유효성 검사를 실행하고 데이터 유효 여부를 boolean으로 반환



### `save()` method

* form에 bind된 데이터에서 DB 객체를 만들고, 저장
  * DB에 한 줄을 저장, 객체를 반환
* Model 
* instance 인자!

참고: https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/



## Widget 적용하기: Customization

첫번째 방식: Meta 클래스에 widget 직접 작성하기

```python
class Meta:
    widgets = {
        'title': forms.TextInput(attrs={
            'class': 'title',
            'placeholder': ...,
        })
    }
```

두번째 방식: 권장

```python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
    label='제목',
    widget=forms.TextInput(
    	attrs={
            'class': 'title',
            'placeholder': 'Enter the title:',       
        }
    )
    )
```







## Form vs. ModelForm

* Form
  * 어떤 Model에 저장해야 하는지 알 수 없음
  * 그러므로 유효성 검사 이후 cleaned_data dict을 생성
  * cleaned_data dict에서 데이터를 가져온 후 .save() 호출해야
  * model에 연관되지 않은 데이터를 받을 때 사용
* ModelForm
  * Django가 해당 model에서 양식에 필요한 대부분의 정보를 이미 정의
  * 어떤 레코드를 만들어야 할지 알고 있으므로, 바로 .save() 호출 가능

"Is ModelForm upgraded Form?" (Nope!)





# Handling HTTP Requests

Django에서 HTTP Request를 처리하는 방법

1. Django shortcut functions
   * cf. render(), redirect()
2. View decorators



## Django Shortcuts Functions

django.shortcuts

* render()
* redirect()
* get_object_or_404()
* get_list_or_404()



### `get_object_or_404()`

* 모델 manager objects에서 get()을 호출하나,
  해당 객체가 없을 경우 DoesNotExist 예외 대신 HTTP 404를 Raise
* get() 메서드의 경우, 조건에 맞는



### Django View Decorators

(Decorator: 원본 함수를 수정하지 않고 기능을 연장해주는 함수)

요청 메서드에 따라 view 함수에 대한 액세스를 제한

조건 미충족시 405 에러 반환

* Allowed HTTP Methods
  * require_http_methods()
  * require_POST()
  * require_safe()
  * require_GET() # 사용 권장않음





# Manual Field Rendering

form을 쪼개서 위치 변경, 스타일 적용 등을 할 수 있다

```html
<form>
    <div>
        {{ form.title.errors }}   
        {{ form.title.label_tag }}
        {{ form.title }}
	</div>
</form>

```







# 