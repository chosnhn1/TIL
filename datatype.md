



# String: 문자열





### Slicing

s[start:stop:step]

```python
'exercise'[3:6]
### rci

'exercise'[2:]
### ercise

'exercise'[:6]
### exerci

'exercise'[0:6:2]
### eec

'exercise'[-6:-2]
### erci

'exercise'[-2:]
### se

'exercise'[2:5:-1]
### (cannot reach end value by step)

'exercise'[::]
'exercise'[:]
### exercise

'exercise'[::-1]
### esicrexe
```



```python
'02-123-4567'[:3]
'로꾸거 로꾸거 로꾸거 말해말'[::-1]
```



```python

```



### str: method

##### .find(x)

첫번째 x의 위치를 반환 (없을 시 -1)

```python
'banana'.find('a')
### 1

'apple'.find('s')
### -1
```

##### .index(x)

첫번째 x의 위치를 반환 (없을 시 `ValueError`)

```python
'banana'.index('a')
###
'apple'.index('s')
###
```



##### .replace(old, new[,count])

바꿀 대상 글자를 새로운 글자로 바꾼 복사본을 반환

count가 지정될 시 해당 갯수만큼 시행

```python
'cuhn'.replace('c', 'k')
### 'kuhn'

'banabana apple'.replace('a', 'o', 4)
### bonobono apple
```



##### .strip([chars])

char를 미지정할 시 공백이 기본

```python
'  Today: Clear    '.strip()
### 'Today: Clear'
'____the world is yours____'.strip('_')
### 'the world is yours'
```



##### .split(sep=None)

여러개의 리스트로 문자열 쪼개기	

sep이 없다면 whitespace로 나눔

```python
''.
```



##### 'separator'.join(iterable)

```python
' '.join(['1', '2', '3'])
### '1 2 3'
```



##### .capitalize()

```python
'a quick brown fox'.capitalize()
### A quick browm fox 
```



##### .title(), .upper(), lower()

```python
'lady vengeance'.title()
### 'Lady Vengeance'

'christian dior'.upper()
### CHRISTIAN DIOR
```



##### .isalpha(), .isupper(), .islower(), .istitle()

```python
'유니코드'.isalpha()
### True

'ABC'.isupper()
### True


```



##### .isdecimal() .isdigit() .isnumeric()





##### jargon

method

[Backus-Naur form][https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form], Backus normal form (BNF)



# List

##### .append(x)

리스트 끝에 값을 추가

```python
cafe = ['starbucks', 'tom n toms']
cafe.append('angel-in-us')
print(cafe)
### ['starbucks', 'tom n toms', 'angel-in-us']
```

##### .extend(iterable)

리스트에 iterable의 항목을 추가

(+=와 같은 동작)

```python

```

##### .insert(i, x)

insert x at i

cf. i가 len(list)보다 길다면? error 없이 가능한 끝에 넣어버림

*x에 len(i) 대신 -1을 넣는다면? 마지막이 아니라 막전*임에 주의

##### .remove(x)

값이 x인 첫번째 항목 삭제

cf. x가 없다면? `ValueError`



##### .pop(i)

remove i from list and **return i**

cf. i가 없다면? 마지막 항목



##### .clear()

remove all in list

```python
a = ['1', 'a', 'c']
a.clear()
print(a)
### []
```



#### 탐색과 정렬

##### .index(x)

첫번째 x값의 index값을 반환

cf. x가 없다면 `ValueError`

```python
num = ['1', '2', '3', '4']
num.index('3')
### 2
```

##### .count(x)

x값의 갯수를 반환

cf. 없다면? 0을 반환

```
```

**리스트에서 모든 해당 값을 삭제하기**

```python
l = [1, 2, 1, 2, 4, 5]
tgt = 1
for i in range(l.count(tgt)):
    l.remove(tgt)
print(l)
```





##### .sort()

**원본 리스트를 정렬하고** None을 반환

cf. sorted(): 정렬된 복사본을 반환



##### .reverse()

순서를 반대로 뒤집음 (mutate)



#### 리스트의 복사

같은 위치 참조 **(주의!)**

```python
original_list = [1, 2, 3]
copied_list = original_list
# 이 때 같은 주소의 리스트를 참조

copy_list[0] = 'hello'
print(original_list)
### ['hello', 2, 3]
```

##### Slice 연산자를 통한 shallow copy

```python
original_list = [1, 2, 3]
s_copied_list = original_list[:]
# 이 때 연산된 리스트가 다른 주소로 저장됨

s_copied_list[0] = 'hello'
print(original_list)
### [1, 2, 3]
```

##### list() 함수를 활용한 shallow copy

```python
original_list = [1, 2, 3]
s_copied_list = list(original_list)
# 이 때 연산된 리스트가 다른 주소로 저장됨

s_copied_list[0] = 'hello'
print(original_list)
### [1, 2, 3]
```

##### Shallow copy의 주의사항

복사한 리스트의 원소가 주소를 참조하는 경우

(특히 리스트 안에 리스트가 있는 경우):

안에 들어간 리스트가 여전히 같은 주소를 참조

```python
a = [1, 2, ['a', 'b']]
b = a[:]

b[2][0] = 0
print(a)
### [1, 2, [0, 'b']]
```



#### Deep copy: 내부의 모든 항목들이 다 온전히 복사되길 원할 때

```python
import copy
a = [1, 2, ['a', 'b']]
b = copy.deepcopy(a)
print(a, b)
b[2][0] = 0
print(a, b)
```



### List comprehension

일명 "파이썬의 꽃": 가독성이 확보된 상황에서 쓰기

indented 반복문 vs. comprehension: 개취?



```python
even_list = []
for i in range(1, 4):
    if i % 2 == 0:
        even_list.append[i]

print(even_list)
```

```python
[x for x in range(1, 4) if x % 2 == 0]

print(even_list)
```

값이 앞으로, for 문이 다음에, 조건이 그 다음으로



```python
girls = ['jane', 'ashley']
boys = ['justin', 'eric']

pair = []
for boy in boys:
    for girl in girls:
        pair.append((boy, girl))
```

```python
[(boy, girl) for boy in boys for girl in girls]
```



### map(function, iterable)

iterable의 모든 요소에 function을 적용하고, 결과를 map으로 반환

```python
nums = [1, 2, 3]
result = map(str, nums)
print(result, type(result))

list(result)
### ['1', '2', '3']
```



### filter(function, iterable)

iterable의 모든 요소에 function을 적용하되, 그 결과가 true인 결과만 filter로 반환

```python
def odd(n):
    return n % 2

numbers = [1, 2, 3]
result = filter(odd, numbers)
print(result, type(result))
```



### zip(*iterables)

iterable들을 모아 튜플을 원소로 하는 zip을 반환

*zipper를 연상하면 좋을듯*

```python
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']

pair = list(zip(girls, boys))
print(pair)
# [('jane', 'justin'), ('ashley', 'eric'), ('mary', 'david')]
```



# set



##### .add(elem)

set에 값 추가

```python
a = {'apple', 'banana', 'watermelon'}

```

##### .update(*others)

set에 여러 값 추가

```python
a = {'apple', 'banana', 'watermelon'}
a.update({'strawberry', 'banana', 'kiwi'})
print(a)
```



##### .remove(elem)

set에서 값을 삭제 (없다면 `KeyError`)

##### .discard(elem)

set에서 값을 삭제 (없으면 변동 없음)

```python
```



##### .pop()

임의의 원소를 제거해 반환 (list와 비슷하나, set는 non-sequencial이므로 indexing할 수 없고 임의로 뽑힘)

*set가 비었다면?* `KeyError`



# dictionary



##### .get(key[,default])

key에 대응하는 value를 get

*key가 dict에 없다면? default를 반환* (기본값: None)

```python
a = {'apple': '사과', 'banana': '바나나'}
print(a.get('pineapple', 0))
```



##### .pop(key[,default])

key가 dict에 있다면 제거하고 그 값을 반환

key가 dict에 없다면? 역시 default를 반환

default 값이 없고 key가 dict에 없다면 `KeyError`



##### .update()

키워드 인자를 받아 기존 dict에 갱신(덮어씀)

```python
```

### dict의 순회

기본적으로 key를 순회, key를 통해 값 활용

```python
for student in grades:
    print(student)
    
for student in grades:
    print(student[score])
```



추가 메서드를 활용하여 순회 가능

##### keys(), values(), items()

key로, value로, (key, value) tuple로 구성된 iterable한 결과

```python
```



### dictionary comprehension

```python
{key: value for }

scores = {'국': 80, '영': 62, '수': 79, '사':87, '과': 91}

result = {}
for key, value in scores.items():
    if value > 70:
        result[key] = value
print(result)
```

```python
{key: value for key, value in scores.items() if value > 70}
```



##### 참조: list comprehension과 map의 치환성

```python
a = ''.join([str(num) for num in numbers])

b = ''.join(map(str, numbers))
```

