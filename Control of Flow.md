# Control of Flow, 제어문

## Control Statement: 제어문

코드를 위에서 아래로 실행하는 것 대신....

### Conditional Statement 조건문

if 문은 참, 거짓을 판단할 수 있는 조건식과 함께 사용

else 문은 선택적으로 활용가능

들여쓰기 중요! (PEP8에서는 4space 권장)

* tab을 4space로 바꿔주는 것은 IDE가 컨트롤
* 원래 1tab != 4spaces

```python
a = int(input())

if a % 2 == 1:
    print('홀수입니다.')
else:
    print('짝수입니다.')
```

복수 조건식은 `elif <exp>:` 형태로 사용



#### Nested Conditional Statement: 중첩조건문

```python
a = 500

if a > 300:
    print('over 300')
    if a > 500:
        print('high')
else:
    print('under 300')
```



#### Conditional Expression: 조건 표현식

= Ternary Operator (삼항 연산자)

`값 = 참일 때 if <exp> else 거짓일 때`

`value = num if num >= 0 else -num`



`result = "홀수입니다" if num % 2 else "짝수입니다"`



### Loop Statement: 반복문

* while statement
  * 종료 조건이 주어짐
* for statement
  * 별도 종료 조건 없이 반복가능(iterable) 객체를 모두 순회하면 종료
* loop control: break, continue, for-else



#### while Statement

조건식이 참인 경우 반복실행, 즉 조건식이 거짓이 될 때까지 반복

조건이 참인 경우 코드블록 실행

실행 완료 시 다시 조건식 검사

while문은 **무한 루프**하지 않도록 주의

```python
a = 0
while a < 5:
    print(a)
    a += 1
print("End")
```

#### for Statement

시퀀스(string, tuple, list, range)를 포함한 iterable한 객체를 모두 순회

`for <var name> in <iterable obj>: `

```python
for a in ['a', 'b', 'c']:
    print(a)
print("End")
```

for 문에 들어가는 시퀀스에는 복수형 표현을 쓰는 것을 권장 (이해하기 쉬움)



### 리스트 순회하기: enumerate()

enumerate() 숫자와 값의 튜플 형태로: 인덱스값과 같이 쓸 때 유용



### Loop Control

* break: 반복문을 종료

```python
n = 0
while True:
    if n == 5:
        break
    print(n)
    n += 1
```



* continue: 이하 코드블록을 실행하지 않고 다음 순회로 진행
* for-else: 끝까지 반복문을 실행한 이후에 else문 실행

```python
for a in 'apple':
    if char == 'a':
        print('a!')
        break
else:
    print('b가 없습니다.')
```

break 등으로 구문이 도중에 중단되면 else문이 실행되지 않음



* pass: 아무것도 하지 없음 (자리를 채우는 용도), 반복문이 아니어도 사용 가능

