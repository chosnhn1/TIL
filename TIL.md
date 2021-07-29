Today I Learned....

[internal link test][test.md]

# git

~~git gud!!!~~

git is... **분산형 버전 관리 프로그램** 

* 분산형: (cf. 중앙집중형)
  * 모든 작업자가 변동내역을 들고 있게 됨 (분산)
  * 한 쪽에 저장된 git이 소실되어도 복구가능
  * git이 모든 버전을 통째로 들고 있는 것이 아님: 변동내역만 갖고 있음 (~ clothpatch)
* 버전 관리: 파일(코드)의 history를 기록/캡처(commit)하고 업데이트. 비교, 복구할 수 있게 해 줌

git is not...

* github (git에 특화된 저장소 서비스): ~gitlab bitbucket



## Command Line Interface

명령줄(Command Line) 인터페이스 (cf. GUI)

### 주요 개념

* Command: 명령어
* Path 경로

### git bash 명령어

touch

mkdir

rm



pwd

date

clear

* Root Directory: /
* Home Directory: ~ (Tilde)
* 절대 경로: 현재 작업경로와 상관없이 직접적으로 참조할 수 있는 경로
  * /C/Users/ABC/...
* 상대 경로: 

\루트 디렉토리, 홈 디렉토리
절대 경로, 틸드 (~)
상대 경로
cf. . .. 



## git

working directory > staging area > commits || github

add, commit, push/pull

clone pull

branch

git reflog (전체 log)

#### branch

git checkout branch명

git branch 새branch명

git branch

git branch -d 지울branch명

git merge branch명

#### merge

merge는 세가지

1. Fast-forward
2. 겹치지 않는 merge
3. conflict

(참고: branch rebase: 비권장사항)

git merge --no-ff



#### reset

reset은 세가지

1. soft
2. mixed
3. hard

git reset --resetoption commitID

soft: working dir, staging area 는 그대로인 채 repository만 해당 commit으로 돌아감 (HEAD가 해당 commit을 가리킴)

mixed: (기본 옵션) staging area와 repository가 돌아감

잘못된 것이 있을 때 mixed reset을 하고, 수정하고 add commit push하면 됨

hard: wdir까지 전부 다 돌아감 (복구불가능하지 않음)

(특정 시점으로 hard reset 가능)

용어:

* fast-forward
* conflict
* head (in branch)



git revert

(reset으로 돌아갔을 때 push할 수 없을수도 있음: git이 이전 버전을 push 막음)

git push -f (강제 push: 비권장하나 필요할수도)

#### Github Flow Models:

Shared Repository Model: 공동협업모델: 

Fork & Pull Model: 오픈소스모델:

Shared RepositoryModel

​	Repository Owner (관리자) / Collaborator (허가받아 PUSH 권한 생김)



#### git stash

잘못된 branch에서 작업했을 때

git stash로 저장하고

git stash apply로 가져다 붙이기

### .gitignore

git으로 관리될 필요가 없는 (ex. 게시가 불필요한 시스템 파일들, **repository에 절대 올라가면 안 되는 개인정보&토큰 등!** ) 것들 관리

**push를 할 예정이라면 git init 하자마자 만드는 것 권장**

touch .gitignore

git으로 관리되지 않을 blacklist 작성

폴더째로도 가능

https://gitignore.io 참조



# GitHub Pages

GitHub를 통해 배포되는 홈페이지

cv resume 등에 활용

https://pages.github.com/ 참조

https://startbootstrap.com/ 



# Markdown (*.md)

R 공부할 때 rmarkdown도 썼었는데.... 차이점 등에 유의해서 활용하면 좋을 것 같다.





# 웹 크롤링

### 용어

* Crawling
* Parsing

## 예제: 네이버 금융

```python
import requests # library import
from bs4 import BeautifulSoup

url_1 = "https://finance.naver.com/sise/" # 네이버 국내증시
url_2 = "https://finance.naver.com/world/" # 네이버 해외증시
response_1 = requests.get(url_1).text
response_2 = requests.get(url_2).text # 각자 응답받기

data1 = BeautifulSoup(response_1, 'html.parser')
data2 = BeautifulSoup(response_2, 'html.parser') # 각자 parsing

kospi = data1.select_one("#KOSPI_now") # KOSPI는 ID=KOSPI_now 있음
sp500 = data2.select_one("#worldIndexColumn3 > li:nth-child(1) > dl:nth-child(1) > dd:nth-child(2) > strong:nth-child(1)")
result1 = kospi.text 
result2 = sp500.text

print(f'현재 코스피 지수는 {result1}입니다. S&P500 지수는 {result2}입니다.')
```



-----

### 예제: 네이버 쇼핑 검색

```python
import requests

# naver 요청 시 필요 요소
naver_client_id = "~~~~~"
naver_client_secret = "~~~~~"

naver_url = "https://openapi.naver.com/v1/search/shop.json?query="

# 헤더 생성
headers = {
    'X-Naver-Client-Id': naver_client_id,
    'X-Naver-Client-Secret': naver_client_secret
}

# 쿼리 작성
query = "라이젠 노트북"

product = requests.get(naver_url+query, headers = headers).json()['items'][0]
product_name = product['title']
product_price = product['lprice']
product_link = product['link']

# 검색결과 출력
message = f"{product_name}\n{product_price}\n{product_link}"
print(message)

# 텔레그램 챗봇 기본 설정
tele_token = "~~~~~"
tele_url = f"https://api.telegram.org/bot{tele_token}"

# chat_id 가져오기
updates_url = f"{tele_url}/getUpdates"
response = requests.get(updates_url).json()
chat_id = response.get('result')[0].get('message').get('chat').get('id')

######

# 보낼 메시지 작성
text = f"Python으로 보낸 메시지입니다.\n" + message

# 메시지 전달
message_url = f"{tele_url}/sendMessage?chat_id={chat_id}&text={text}"
requests.get(message_url)
```



# Python

## Python 개발 환경

### Python의 특징

* 인터프리터 언어: line-by-line != 컴파일 언어 (ex. C)
* 객체 지향 프로그래밍:  
* 동적 타이핑: 변수에 별도의 타입 지정이 필요하지 않음

### 개발 환경

* Python Interpreter: IDLE
  * 대화형 모드: >>>
  * 기본 제공, but 디버킹, 코드 편집, 반복 실행 어려움
* Python Jupyter Notebook
  * Web Browser 환경에서 사용
  * ~= Google Colab
  * 
* IDEs (PyCharm, VS Code, ...)





## Code Style Guide

[PEP8][https://www.python.org/dev/peps/pep-0008]: Style Guide for Python Code - 손버릇 들이기 :D

[Google Style Guide][https://google.github.io/styleguide/pyguide.html]

##### 왕불편코드 예시

```python
print('hello')
print("world")

a = 'apple'
if True:
		print(True)
else:
			print(False)

b='banana'
```

(코드를 보는것만으로 소화가 안 되기 시작함)

You need to be consistent



## Comment: 주석

`#`으로 표현

multi-line comment: `한 줄씩 #` or `''' '''`(docstring)

VS Code: 블럭 잡아 `Ctrl + /`하면 편하다.

### Doctring: Document String

함수나 클래스의 설명을 작성

```python
def func():
	""" This function is used for ~~~.
	You use docstring"""
```

### Codeline

1 statement for 1 line

If you want multiple statement in a line: `;` (not recommended)



## Variables: 변수 & Identifier: 식별자

`k = 60` assignment operation(할당 연산자)를 퉁해 값을 할당한다.

#### 변수와 대화하기

`type()`: figure out variable's type

`id()`: figure out variable's memory address

#### Assignment Operation

동시 할당 (multiple assignment)

```python
x = y = 1004
```

```python
x, y = 1, 2
```

cf. This is not working

``` python
x, y = 1
x, y = 1, 2, 3
```



#### Value Swap

``` python
x, y = 10, 20
```

##### 1. Temp variable

```python
tmp = x
x = y
y = tmp
print(x, y)
```

##### 2. Pythonic (Simple) Way

```python
y, x = x, y
print(x, y)
```



cf. python(List) == someLanguages(Array)



### Identifiers

The Name of Variables

Rules and Instructions

1. A-Za-z_0-9
2. First char != 0-9
3. no length limt, Case-sensitive
4. reserved word cannot be used
   * False, None, True, ...

```python
import keyword
print(keyword.kwlist)
```

내장 함수, 모듈 등의 이름으로 만들지 않기

cf. the code below is not working properly and not recommended

```python
print(5)
print = hi
print(5)
```



### Datatype

* Number
  * Integer `int`
    * in Python 2 and otherL: `long`
  * Floating Point Number `float`
  * Complex Number `complex`
* String
  * `str`
* Boolean
  * `True` / `False`
* None



#### int

All integer

​	no `long` type in Python 3

No Overflow in Python

​	Arbitrary Precision Arithmetic "임의 정밀도 산출"

Binary 0b00



#### float

all real number but integer

##### floating point rounding error

```python
3.14 - 3.02 == 0.12
```

이진수를 사용해 값을 근사하는 컴퓨터가 십진수 소숫점을 정확히 계산할 수 없음

```python
abs(a - b) <= 1e-10
```

``` python
import sys
print(abs(a - b) <= sys.float_info.epslion)
```

``` python
import math
math.isclose(a, b)
```



#### complex

`a = 3+4j` `a.real` `a.imagine`



### String: 문자열

모든 문자는 str

문자열은 `'` `"`를 활용하여 표기, 동일한 문장부호를 활용

PEP8: Select one and be consistent

##### Escape Sequence

* \n: 줄바꿈
* \t: tab
* \r: 
* \\\: \ 
* \\'
* \\"

#### String Interpolation

Placeholder

* %-formatting
* str.format()
* f-strings (python 3.6+)

```python
print('Hello, %s' % name)
print('Hello, {}'.format(name))
print(f'Hello, {name})
```

```python
import datetime
today = datetime.datetime.now
print(f'{today:%m}월 {today:%d}일')
```



### Boolean

* True / False
* False: 0, 0.0, (), [], {}, '', None

### None

* 값이 없음을 표현



## Type Conversion, Type Casting

* Implicit

  * Python internally, automatically converse type

  * ```python
    True + 3
    3 + 5.0
    3 + 4j + 5
    ```

* Explicit

  * with intention
  * float, some str => int
  * int, some str => float
  * int, float, list, tuple, dict => str

```python
'3' + 4 # Error
int('3') + 4
int('3.5') + 4 # Error

'3.5' + 3.5 # Error
float('3.5') + 3.5
```



## Operator

### Arithmetic Operator

\+ - * / // ** %

(나눗셈은 항상 float로)

* divmod(a, b): (quotient, remainder)

< > <= >= == != is is not

(is와 is not은 객체 확인)

```python
3 > 6
# False
3.0 == 3
# True
'3' != 3
# True
'Hi' == 'hi'
# False

x is None
# False
# (PEP None compare: 'is')
```

A and B

A or B

not A

```python
num = 100
num >= 100 and num % 3 == 1
# True
```

#### 논리 연산자의 단축평가

When the result is clear with first evaluation, Python doesn't evaluate the other one

```
a = 5 and 4
print(a) # 4

b = 5 or 3
print(b) # 5

c = 0 and 5
print(C) # 0

d = 5 or 0
print(D) # 5
```



#### 복합 연산자

`cnt += 1` == `cnt = cnt + 1`



#### Concatenation

`'hello, ' + 'world!'`

#### Containment Test (포함 검사)

```python
'a' in 'apple' # True
```

#### Identity (is, is not)

동일한 객체인지 확인

```python
a = 3
b = 3 # in Python -5~256 has same id
print(a is b) # True
print(id(a), id(b))

c = 257
d = 257 # not same id
print(c is d) # False
print(id(c), id(d))

x = 3
x is None # False
```



### Indexing & Slicing

```python
'hello, world!'[0]
# h
'hello, world!'[1:5]
# ello
```



### 연산자 우선순위

* ()
* Slicing
* Indexing
* **
* 부호(단항 연산자, + -)
* 산술 연산자(*, %, %)
* 산술 연산자(+, -)
* 비교 연산자, in, is,
* not
* and
* or



## Expression (표현식, 식)

Identifier, Value and Operator로 구성됨

평가되고 값으로 변경

하나의 값으로 환원될 수 있는 문장

```python
'hello'
radius = 10
4 +
```

## Statement (문, 문장)

실행가능한 최소한의 코드 단위

Every expression is statement 



#### Python에서의 펠린드롬: [::-1]

list[::-1]

#### 두 리스트 사이에 항목 끼워넣기

print[*a, 'w', *c]





# C++ vs. Java vs. Python

| C++                                       | Java                                      | Python                                                    |
| ----------------------------------------- | ----------------------------------------- | --------------------------------------------------------- |
| 컴파일러                                  | 컴파일러                                  | 인터프리터                                                |
| 연산자 오버로딩 지원                      | 연산자 오버로딩 미지원                    | 연산자 오버로딩 지원                                      |
| 단일/다중 상속 지원                       | 인터페이스를 통해 부분적인 다중 상속 지원 | 단일/다중 상속 지원                                       |
| 플랫폼 의존                               | 플랫폼 독립                               | 플랫폼 독립                                               |
| 스레드 미지원                             | 멀티스레드 빌트인 지원                    | 멀티스레드 지원                                           |
| 라이브러리 지원 제한적                    | UI 등 많은 라이브러리 지원                | 다양한 분야의 광대한 라이브러리 지원                      |
| Java의 절반 정도                          | 제법 긺                                   | Java의 1/4 정도                                           |
| 함수 / 변수들은 클래스 외부에서 사용 가능 | 모든 코드가 클래스 안에 존재              | 함수 / 변수들은 클래스 외부에서도 선언되고 사용될 수 있음 |
| 빠른 컴파일링                             | C++보단 느린 컴파일링                     | 인터프리터라 느림                                         |
| ; {} 등 문법 엄격함                       | . , ; 등 문법 엄격함                      | ; 사용은 선택적                                           |

source: https://www.tutorialspoint.com/cplusplus-vs-java-vs-python



Python

```python
print("Hello, world!")
```

C++

```c++
#include <iostream>
using namespace std;

int main() {
  cout << "Hello, world!";
  return 0;
} 
```

Java

```java
public class Main {
  public static void main(String[] args) {
    System.out.println("Hello World");
  }
}
```



# Modules and Packages

Module: 특정 기능을 파이썬 파일 단위로 작성한 것

Packages: 모듈들의 모음

Library: 모듈과 패키지들의 모음



## Python Standard Library (PSL)

Python에 기본적으로 내장된 라이브러리



**Third-party Library** 외부 라이브러리 (내장되지 않음)

`pip install`

### Python 패키지 관리자 (PIP)

```
pip install PackageName
pip install PackageName==1.0.0
pip install 'PackageName>=1.0.0'

pip uninstall PackageName

pip list

pip freeze
## 현재 패키지들의 버전 정보 출력
pip freeze > requirements.txt
## 파일로 저장
## 파일 이름은 관례적으로 "requirements.txt"를 사용
pip install -r requirements.txt
## 저장된 텍스트로부터 패키지 목록 읽어 설치

pip show PackageName
```



## Using Module

```python
# 모듈 통째로
import moduleName

# 모듈에서 일부만
from moduleName import func1
from moduleName import *
#import *: not recommended

# 패키지에서 모듈을
# 패키지에서 모듈을
from module.abc import name
from module.def import name as def_name
```



## Using Package

package.module

\__init__.py



## Constructing Module

Module.py

* def func1():
* def func2():
* ...



​                                                                                                                                                                                                                         



## Virtual Environment

복수 프로젝트를 진행하는 경우 각 프로젝트마다 독립적으로 패키지를 관리할 수 있음

<> Global Environment: 전역에서 적용되는 환경



### venv

Python 3.5부터 지원되는, 가상 환경을 만들고 관리하는 모듈

* 특정 폴더에 가상 환경이 존재
* 실행 환경에서 가상 환경을 활성화
* 해당 폴더에 존재하는 패키지를 사용/관리



```
python -m venv <folderName>
python -m venv venv
# 관습적으로 가상환경 폴더 이름을 venv로 사용
```

```
# Windows
C:\><venv>\Scripts\activate.bat

source venv\Scripts\activate

deactivate

```



# Object-Oriented Programming (OOP)

## Object

Python world: all things are objects

Class and Instance

~ 대자와 즉자? :D 는 아니겠네





#### example

```python
type('hello')
## <class 'str'>
help(str)
```



### is operator

```python
type(10)

type(10) is int

isinstance(object, classinfo)
```

#### isinstance()

classinfo의 instance이거나 subclass인 경우 True

classinfo가 tuple일 때, 하나라도 일치하면 True

classinfo가 type이 아닌/type로 구성되지 않은 경우 TypeError



### attribute

객체의 속성 (호출되는 것이 아님)

\<object>.\<attribute>

```python
1+3j.real
## 1.0
```



### method

객체에 적용될 수 있는 행위

\<object>.\<method>()

```python
'hello'.capitalize()
## 'Hello'
```



