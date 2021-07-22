# Function

* 이름
* 매개변수
* 함수 바디
* 반환값

```python
def pstdev(data, mu=None): #def 옆에 parameter
    """Return the square root of the population variance.
    """
    var = pvariance(data, mu)
    try:
        return var.sqrt()
    except AttributeError:
        return math.sqrt(var)
```

```python
def foo():
    """this func is...
    """
foo.__doc__
```

def로 선언(등록)하고 나중에 실행될 때 호출됨

return은 항상 한 개의 객체를 뱉는다

여러개? tuple

없다? None

return은 print와 다르다

return 밑에 적은 건 실행 X (결과물 나오면 멈춘다)

cf. yield



*REPL 환경에서는 return과 print를 착각할 수 있으니 주의*



### 함수의 input

#### 위치 인자

위치가 정해짐

#### 기본 인자값

기본값 지정, 입력하지 않아도 되게

#### 키워드 인자

강조 등



#### 가변 인자 리스트

함수가 임의의 개수 인자로 호출될 수 있도록 지정

튜플로 묶여 처리, 앞에 *를 붙여 표현

"패킹"

```python
def add(*args):
    for arg in args:
        print(arg)
```

#### 가변 키워드 인자

딕셔너리로 묶여 처리, **를 붙여 표현



### 함수 정의 시의 주의사항

인자 순서!



#### 함수 스코프

Python은 함수 안에만 스코프가 있다

global scope

local scope

built-in scope









### 이름 검색 규칙

LEGB Rule:

Local: 함수

Enclosed: 특정 함수의 상위 함수

Global: 함수 밖 변수, Import 모듈

Bulit-in: Python 내장 함수 및 속성

안에서는 밖의 변수에 접근 가능, 하지만 수정은 불가

밖에서는 안에 접근 불가

`del`: 변수를 삭제하는 연산자 `del abcd`



```python
a = 0
b = 1
def enclosed():
    a = 10
    c = 3
    def local(c):
        print(a, b, c)
    local(300) # 10 1 300
    print(a, b, c)
enclosed() # 10 1 3
print(a, b) # 0 1
```

### global

```python
a = 10
def func1():
    global a
    a = 3
print(a)
func1() # global a 선언
print(a)
```

제한 1: global 나열된 이름은 global 앞에 등장 X

제한 2: 매개변수, for 루프 대상, 클래스, 함수 정의 등으로 정의되지 않아야

not recommended

#### nonlocal



# 재귀함수

자기 자신을 호출하는 함수

알고리즘 설계 구현에서 유용하게 활용

1개 이상의 base case가 발생할 수 있도록

높은 가독성, 재귀로 직관적인 표현이 가능할 수 있음

ex)

factorial(4) < return 4 * factorial(3)

```python
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
    
factorial(4)
```

maximum recursion depth: 1000(default)

recursion error, stack overflow

base case에 도달할 때까지....



# Error & Exception Handling

