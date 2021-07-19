# Container

여러 개의 값을 저장할 수 있는 객체.

\#Container

* Is it have a order?
  * Sequence Container
    * list
    * tuple
    * range
    * string
    * binary
  * Non-Sequence Container
    * set
    * dictionary

Sequence != Sorted



# Sequence Container

## List

### Create, Access and Mutate

`[1, 2, 3]` `list((1, 2, 3))`

`print(a[0])` `a[0] = '2'`

### 중첩 리스트

```python
a = [[1, 2], [3, 5]]
a[0][1] # 2 from [1, 2]
```



## Tuple

immutable sequence

일반적으로 파이썬 내부에서 활용.

### Create, Access (but not mutable)

`(1, 2, 3, 1)` `tuple((1, 2, 3, 1))`

`print(a[1])` `a[0] = '2' # Error`

`a = (1) # int` `a = (1, ) # tuple`



## Range

for number sequence

`range(n)`: from 0 to n-1 (n numbers)

`range(n, m)`: from n to m-1 (m-n numbers)

`range(n, m, s)`: from n to m-1, s step 

```python
range(4)
list(range(4))
```

굳이 형변환하지 않아도 활용가능

`list(range(6, 1, 1))`같이 도달불가능한 경우 비어있는 결과 출력



## Concatenation

리스트끼리, 튜플끼리, 문자열끼리 가능

(range는 안 됨)

반복도 가능 (by *, 역시 range 안됨)



## Indexing

`[1, 2, 3][1]` 같은 식으로...

(없는 값 참조하면 에러)

## Slicing

[포함:미포함]

(참조) Slicing의 경우 값과 값 사이를 자른다고 생각하기

`[a, b, c, d]`의 경우 [ 0 a 1 b 2 c 3 d 4]

`[a, b, c, d][1:3]`는 [b, c]

[:2] (omit first: 처음부터)

[0:4:2] (step 결정 가능)



## 내장함수 len(), min(), max()

길이, 최솟값, 최댓값

주의: min max에서 문자열은 ASCII 코드를 통해 결정함

(ord()함수 활용하여 확인 가능)



## .count() 메서드

특정 원소 갯수 세기

`[1, 2, 3, 1, 2].count(1) # 2`



# Non-sequence Container

* set
* dictionary

## set

순서가 없는 자료구조

`{}` 혹은 `set()`로 만듦

* 빈 `{}`는 딕셔너리로 만들어지므로 set() 사용해야

순서가 없으므로 별도 값에 접근할 수 없음

수학에서의 집합과 동일한 구조

* 집합 연산 가능
* 중복값이 존재하지 않음: 중복 제거에 쓰이기도 함

#### 집합 연산자

```python
a = {1, 2, 3}
b = {3, 6, 9}
print(a - b) # 차집합 {1, 2}
print(a | b) # 합집합 {1, 2, 3, 6, 9}
print(a & b) # 교집합 {3}
```

#### 활용

1. 중복값 손쉽게 제거
2. 순서가 중요한 경우 사용 불가

```python
samplelist = ["a", "b", "b", "a", "c"]
len(set(samplelist))
```



## Dictionary

Key: Value 쌍으로 이루어진 데이터

`{}`와 `dict()`로 생성

* key는 immutable data만 활용 (ex. key로 list를 쓸 수는 없음)
* value는 모든 값으로 설정 가능



# 컨테이너의 분류

* Immutable
  * literal: number, string, bool
  * range
  * tuple

dictionary의 키로 활용가능

* mutable
  * list
  * set

**immutable과 mutable에서 재할당이 다르게 작동함!**

ct. 원본이 같이 바뀔 수 있음! 참조: copy()







