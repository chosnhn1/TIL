## OOP

#### Procedural Programming: 절차 지향 프로그래밍

data > proc 1 > proc 2 > ... > proceedings



#### in OOP...

Object [data <> method ]



#### Square Example

Procedural

```python
a = 10
b = 30
square1_area = a * b
square2_circumference = 2 * (x + y)


a = 10
b = 30
def area(x, y):
    return x * y
def circumference(x, y):
    return 2 * (x + y)

area(10, 30)
circumference(10, 30)
```

Object-oriented

```python
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def area(self):
        return self.x * self.y
    
    def circumference(self):
        return 2 * (self.x + self.y)
    
r1 = Rectangle(10, 20)
r1.area()
r1.circumference()
```



## Class and Instance

`a = 10`일 때, "a는 int class의 instance다"

### Class

Class has

* attribute: 객체가 가질 정보
* method: 객체가 취할 행동

Name Convention on Class: Pascal Case (`UseThisNameConvention`)

*Camel Case*: (`thisIsCamelCase`)

```python
class MyClass:
    pass
```



#### attribute

특정 class의 obj들이 가지게 될 상태

#### method

특정 class의 obj에 공통적으로 적용가능한 행위(function)

#### self

인스턴스 자기 자신

```python
'apple'.capitalize()
# and...
str.capitalize('apple')
```

Python에서 instance method는 호출 시 **반드시 첫번째로** self를 첫번째 인자로 정의됨

'self' 이외의 이름을 쓸 수도 있음 (not recommended)



#### constructor: 생성자

```python
class Person:
    def __init__(self, name):
        print(f'Hello, I\'m {name}')
```

#### destructor: 소멸자

```python
class Person:    def __del__(self):        print('byebye')
```



#### Magic Methods

double underscore(__)로 묶인, 특수한 동작을 위해 만들어진 메서드들



### instance variable

인스턴스의 속성, 각 인스턴스들의 고유한 변수

* self.name으로 정의
* 생성 이후 instance.name으로 접근, 할당

```python
class Person:
    
    def __init__(self, name):
        self.name = name
```



```python
john = Person(name)
print(john.name)
john.name = 'John'
print(john.name)
```



#### class variable

= class attribute

* 모든 인스턴스가 공유, 클래스 선언 내부에서 정의
* classname.name으로 접근 및 할당
* (단, instance에서 접근할 수 있음)



#### Namespaces in Class

* def Class >> Class Namespace 생성
* Class()로 instance 생성 >> instance Namespace 생성
* instance에서 attribute 접근 시 instance -> Class 순서로 접근



### Methods

* instance method
* class method
* static method

#### instance method

인스턴스가 사용할 메서드

클래스 내부에 정의되는 메서드의 기본

호출 시 첫째 인자로 반드시 자기 자신이 전달됨

(없으면 인스턴스가 호출 불가)

*'인수로 self가 있으면 instance method겠네~'*



#### class method

클래스가 사용할 메서드

`@classmethod` 데코레이터를 사용하여 정의

호출 시 첫번째 인자로 클래스(`cls`)가 전달됨

```python
class MyClass:        @classmethod    def class_method(cls, arg, ...):		pass    MyClass.class_method()
```



#### static method

클래스가 사용할 메서드

`@staticmethod` 데코레이터를 사용하여 정의

호출 시 어떠한 인자도 전달되지 않음 (클래스 정보에 접근/수정 불가)

```python
class MyClass:        @staticmethod    def class_method(arg1, ...):        pass    MyClass.static_method(...)
```



#### 세 메서드 비교

인스턴스 메서드

- self 매개변수로 동일객체 속성, 다른 메서드에 자유롭게 접근
- 클래스 자체에 접근 가능 (not recommended)

클래스 메서드

* 클래스를 가리키는 cls 매개변수를 받음
* cls 인자에만 접근 가능, 인스턴스 상태 수정은 불가

스태틱 메서드

* 임의 개수의 매개변수 받을 수 있음
* self, cls 매개 변수는 사용않음
* 독자 함수처럼 쓰이나 클래스 이름공간에 귀속됨



##### cf. Static method 언제 써요?

* 제약이 많아보이지만...
* '독립적'인 메서드를 만들 수 있음
* self, cls 인자가 전달되지 않는다는 것을 보장할 수 있음 (dev intention)
* 일반함수처럼 쓰이기 때문에 OOP-Procedural을 잇는 역할을 하기도 함



#### 클래스 변수와 인스턴스 변수

**클래스 변수는 동일한 이름의 인스턴스 변수에 의해 가려질 수 있기 때문에 주의해야 한다**



### 객체 비교

== & is

* ==: equal: 내용이 같다면 True
* is: identical: 동일한 객체를 가리킨다면 True





## Inheritance: 상속

클래스를 생성할 때 다른 클래스의 속성, 메소드를 참조

Parent Class / Child Class

Base Class / Derived Class

Super Class / Sub Class

부모 클래스의 속성, 메서드가 자식 클래스에 상속됨:

코드 재사용성 +++

```python
Class Person:
    def __init__(self, ...)
    
Class Professor(Person):
    def __init__(self, ...)
    
```

#### issubclass(class, classinfo)

```python
issubclass(bool, int)
issubclass(Professor, (Person, Cat))
# classinfo에 tuple: or 검사
```



#### super()

sub에서 super를 쓰고 싶을 때

```python
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # Person에서 갖고오기     
        super().__init__(name, age, number, email)
        self.student_id = student_id
```



#### Method Overriding

상속받은 메서드를 재정의하기

상속받은 클래스에서 같은 이름의 메서드로 덮어씀



#### Namespace in Inheritance

instance > subclass > superclass 순



#### 다중 상속

두 개 이상의 클래스를 상속받는 경우 다중 상속이 됨

: 두 superclass의 요소를 활용가능

중복된 속성/메서드가 있는 경우 **앞에 상속받은 걸 쓴다**

```python
class C(A, B):
    pass
## 중복된 속성/메서드는 A로부터 먼저 가져다 쓴다
```





TBC in OOP:

캡슐화, 다형성, Solid





##### 참조

method overloading: 같은 이름의 메서드를 다르게 동작하게 디자인

<> method overriding: 같은 이름의 메서드를 덮어쓰기

method resolution order (MRO): 메서드 찾기 순서: instance >> subclass >> superclass

다이아몬드 상속



## SOLID

* Single Responsibility Principle
  * 단일 객체 단일 책임
  * every class should have only one responsibility
* Open-Closed Principle
  * Open for extension but Closed for modification
* Liskov Substitution Principle
  * super에서 되는거 sub에서도 돼야 한다
  * overriding 할 때 주의해야
* Interface Segregation Principle
  * 자기가 사용할 인터페이스만 구현해라
  * many client-specific interfaces are better than one general-purpose interface
* Dependency Inversion Principle
  * depend on solid not liquid(fluctuating)
  * depend upon abstractions not concretions







##### External Links

https://blog.bitsrc.io/solid-principles-every-developer-should-know-b3bfa96bb688

