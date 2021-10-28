# ECMAScript 6

ECMA





# Introduction

## Semicolon: ASI

Selective use of semicolon

```javascript
// semicolon
const greeting = 'Hello, world!';
console.log(greeting);

// no semicolon
const greeting = 'Hello, world!'
console.log(greeting)

// Both works
```



## Coding Style Guide

[Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)



# Variables and Identifier

* 반드시 문자, $ 또는 _로 시작



## Identifier Style

* camelCase: 변수, 객체, 함수
* PascalCase: class, constructor(생성자)
* SNAKE_CASE: Constants
  * Dev 의도와 상관없이 변경될 가능성이 없는 값
* cf. kebab-case: - instead of _



```javascript
let dog
const userInfo = { name: 'juan', age: 28}

class User {
    
}

const API_KEY = 'ASDFG'
```



## Variable Declaration

JavaScript: Static Typing Language (cf. Python as Dynamic Typing Language)

Static / Dynamic Declaration

"Dynamic" (v. Static)

* let
  * dynamic
  * 재할당 가능 변수 선언
  * 재선언 불가
* const
  * static
  * 재할당 불가 변수 선언
  * 재선언 불가

```javascript
let number = 10
number = 50			// Ok

const number = 10
number = 10			// Error (cannot reassignment)

let number = 50     // Error
// Chrome DevTools can do this (let and class redeclaration)
```



### Block Scope

중괄호 내에서의 선언과 할당: 바깥에서 접근 불가

```javascript
let x = 1

if (x === 1) {
    let x = 2
    console.log(X)	// 2
}

console.log(x)		// 1
```



### var

var: 재선언, 재할당이 가능한 선언

ES6 이전에 사용됨

Hoisting 문제: "var 문이 제일 위로 뜸" > 개발자가 예상치 못한 문제 발생하는 경우 많음

현재는 쓰지 않는 것을 권장











cf.

* Declaration
* Assignment
* Initialization

```javascript
let foo				// Declaration
console.log(foo)

foo = 11			// Assignment
console.log(foo)

let bar = 0			// Declaration + Assignment
console.log(bar)
```



참조: var와 const/let은 if block scope에서 다른 결과가 나온다

```javascript
const codeEditor = 'vscode'

if (codeEditor === 'vscode') {
  var theme = 'dark+'
}
console.log(theme)

// ----------------------

let fullName = 'Brendan Eich'

if (fullName === 'Brendan Eich') {
  let fullName = 'Guido Van Rossum'
  const language = 'Python'
}

console.log(language)
```



# Types and Operators

All JS variables have values

* Data Type
  * Primitive Type: 원시 타입
    * 실제 값 자체를 들고 있음
      * 즉, 다른 변수에 복사할 때 실제 값이 복사됨
    * number
    * string
    * boolean
    * undefined
    * null
    * symbol
  * Reference Type: 참조 타입
    * 값이 위치한 주소를 들고 있음
    * objects
      * array
      * function
      * ...



## Primitive Types

* Number

  * 참조: Boolean 형변환 시 0, -0, NaN은 False

* String

  * text data
  * Template Literal
    * \` \`으로 표현

* Undefined

  * 변수의 값이 없음을 나타냄 (변수에 아무 값도 할당하지 않았다면 자동으로 삽입)

* Null

  * 변수의 값이 "없음"을 의도적으로 표현

  * 참조

    * ```javascript
      typeof null // object
      ```

    * 왜죠: null 타입은 원시 타입에 속하지만, `typeof` 연산자 결과는 객체로 나타남

* Boolean

  * 논리적 참/거짓
  * JS에서 참이란? 1; 거짓이란? 0
  * 자동 형변환
  * 



## Assignment Operators

"="

단축 연산자 ++, --, +=(사칙연산) 등 



### 동등 비교 연산자 `==`

비교 시 암묵적 형변환으로 타입을 일치시킨 다음 비교

예상치 못한 결과 많아 특별한 경우를 제외하고는 사용하지 않음



### 일치 비교 연산자 `===`

타입과 값 모두 같은지 비교

객체라면, 같은 주소를 바라보는지 비교



### 논리 연산자

and: &&

or: ||

not: !

단축 평가 지원



### Ternary Operator: 삼항 연산자







# Conditional Statement & Iteration Statement

## Conditional Statements

* if

  * ```java
    if (condition) {
        
    } else if (condition) {
        
    } else {
        
    }
    ```

  * 

* switch

  * 참조: Python 3.10에서 지원

  * 조건 표현식의 결과값이 어디에 속하는지

  * ```javascript
    switch (expression) {
        case 'first': {
            
        break
    }
        case 'second': {
            
        break
        }
            
        default: {
            
        }
    }
    ```

  * 

  * 

## Iteration

* while

  * 조건문이 true인 동안 실행

  * ```javascript
    while (condition) {
        // do sth
    }
    ```

  * 

* for

  * ```javascript
    for (initialization; condition; ) {
        // do sth
    }
    ```

  * ```javascript
    // i = 0
    // i < 6 ?
    // true면 실행하고 i++
    for (let i = 0; i < 6; i++) {
        console.log(i)
        // 0, 1, 2, 3, 4, 5
    }
    ```

  * 

* for ... in

  * object의 속성 순회 시

  * 배열도 순회 가능하나 권장하지 않음

  * 

  * ```javascript
    for (variable in object) {
        // do sth
    }
    ```

  * ```javascript
    const capitals = {
        Korea: 'Seoul',
        France: 'Paris'
    }
    for 
    ```

  * 

* for ... of

  * iterable 순회 시

  * ```javascript
    for (variable of iterables) {
        // do sth
    }
    ```

  * ```javascript
    const fruit = ['Apple', 'Banana']
    for (let fruit of fruits) {
        
    }
    ```

  * 

* for ... each



# Function

* 함수 선언식

* 함수 표현식

* JavaScript의 함수: first-class object*

  * 적용가능한 연산을 모두 지원하는 객체

  

* 



## Function Declaration

```javascript
function name(args) {
    // do sth
    
}
```

## Function Expression

```javascript
const myFunction = function (args) {
    
}
// 함수의 이름, 인자, 내용
// 표현식에서는 함수의 이름을 생략가능
```

|      | 함수 선언식                    | 함수 표현식                    |
| ---- | ------------------------------ | ------------------------------ |
| 공통 | 데이터타입                     |                                |
| 차이 | 익명 함수 불가<br />호이스팅 O | 익명 함수 가능<br />호이스팅 X |
|      |                                | (Airbnb Style Guide O)         |

둘 모두 타입은 function



## Arrow Function





# Arrays and Objects

## Arrays

* 키와 속성들을 담고 있는 참조 타입의 객체
* 순서를 보장
* 주로 대괄호를 사용하여 생성
* 0을 포함한 양의 정수 인덱스로 특정값 접근



### 배열 관련 주요 메서드

`reverse`

`push` `pop`

`unshift` `shift`

`includes`

`indexOf`

`join`

```javascript
const numbers = [1, 2, 3, 4, 5]
console.log(numbers)
```



### Array Helper Methods

배열을 순회하며 특정 로직을 수행하는 메서드들

메서드 호출 시 인자로 callback 함수를 받음

(cf. Python's `map()`)

* forEach

  * 배열 각 요소에 콜백 함수를 한번씩 실행하고 종료

* map

  * 배열 각 요소에 콜백 함수를 한번씩 실행하고,
    각 반환값을 요소로 하는 새로운 배열 반환

* filter

  * 배열 각 요소에 콜백 함수를 한번씩 실행하고,
    각 참인 반환값만을 요소로 하는 새로운 배열 반환

* reduce

  * 콜백 함수의 반환값들을 하나의 값에 누적하고 반환

  * ```javascript
    array.reduce((acc, element, index, array) => {
        // do sth
    }, initialValue)
    ```

  * ```javascript
    const arr = [1, 2, 3, 4, 5]
    const sums = arr.reduce((acc, num) => {
        return acc + num
    }, 0)
    
    console.log(sums)
    ```

  * 

* find

  * 콜백 함수의 반환값이 참이면 해당 요소를 반환
  * 빈번히 쓰임 (객체와 찾는 값을 직접 비교할 수는 없으므로)

* some

  * 배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환

* every

  * 배열의 모든 요소가 판별 함수를 통과하면 참을 반환



# Objects

객체 ~~ Python Dictionary

객체 관련 ES6 문법

* 속성명 축약
* 메서드명 축약
* Computed Property Name: 계산된 속성명 사용
  * 본래 문자열만 들어가던 속성명을 동적으로 연동해서 사용가능
* 구조 분해 할당



## JSON (JavaScript Object Notation)

JavaScript의 객체와 유사하게 생겼으나 실제로는 문자열 타입이므로 내장 메서드를 사용해야 함

* from JSON to JS Obj: `JSON.parse()`
* from JS to JSON: `Object.stringify()`

