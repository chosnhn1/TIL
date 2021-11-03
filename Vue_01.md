* Intro
* Why Vue.js?
* Concepts of Vue.js
* Quick Start
* Basic Syntax



# Intro

## Front-End Development

* HTML, CSS and JavaScript >> Visualize Data for User
  * View and communicate

* Front-end Frameworks
  * Vue.js
  * React
  * Angular



# What is Vue.js?

"Progressive JavaScript Framework for User Interface"

SPA(Single Page Application)

by Evan You (2014)



cf. Virtual DOM





## Single Page Application: SPA

* Communicate via Dynamic Web Page
* 단일 페이지 구성, 최초에만 페이지를 다운로드하고 그 이후에는 동적으로 DOM을 구성
* 연속되는 페이지 간의 UX를 향상
  * Less Traffic, More Usability & Responsiveness
* 동작 원리의 일부가 CSR의 구조를 따름
  * Client Side Rendering



### Rise of SPA

* Multi Page Application (MPA)
* Smartphones and "Mobile Optimization"
* CSR & SPA
* UX like mobile apps



## Client Side Rendering: CSR

* <-> SSR
* Construct Viewport by Client
* 최초 요청
  * 각종 리소스
* 이후 요청
  * 필요 데이터를 요청, JS로 DOM을 Render
* 뼈대를 서버로부터 받고 브라우저에서 동적으로 DOM을 그림



#### Pros & Cons

* Pros
  * Reduce Traffic
  * UX 향상
* Cons
  * Late total page render point
  * Hard to search engine optimization (SEO)



#### Server Side Rendering: SSR



* Pros
  * Fast initial time
  * Feasible to search engine optimization
* Cons
  * Construct new pages for every response
    * more traffic
    * more refreshes



### SSR & CSR

"Who renders this -- Server or Client?"

SSR and CSR can be mixed

>  i.e Django & JS Axios: SSR but CSR for some components



## Appendix: How to Response SEO?

SPA Framwork-included

or... Nuxt.js and Next.js



# Why Vue.js?

* Quantitative expansions of web app
* Heavier web pages and interactivity
  * Facebook >> React
* 



i.e 100만개의 글을 작성한 user가 닉네임을 바꾼다면



# Concepts of Vue.js

## MVVM Pattern

View - [ViewModel] - Model

HTML (DOM) / Vue/ Plain JS Obj



* Model
  * by JavaScript Object (Key & Value)
  * Data for Vue Instance
* View
  * DOM(HTML)
  * Changed by Data
* ViewModel
  * by All Vue Instance
  * Data Handling



# Quick Start of Vue.js

* Django
  * url > views > template
* Vue.js: "Data > DOM"
  * Data logic
  * DOM



# Basic Syntax of Vue.js

Vue instance

* Vue 앱: Vue 함수로 새 인스턴스 만들기로 시작

* ```html
  <div id="app">
      {{ message }}
  </div>
  ```

* 

* ```javascript
  // 인스턴스 -> 요소, 객체
  const app = new Vue({
  	el: '#app',
      data: {
          message: '안녕하세요 Vue!'
          
      }
  })
  
  // app이라는 scope 안에서
  // data의 변수들과
  // methods의 함수들을 사용
  // 한다고 생각하면...!
  ```

* Vue 인스턴스 생성 시 Options 객체를 전달해야 함

* 여러 Options로 원하는 동작 구현

* Vue Instance as Vue Component



## Options/DOM

* `el`
  * Vue Instance에 mount할 기존
* `data`
  * Vue instance의 데이터 객체
  * Vue instance의 상태 데이터를 정의
  * Vue template에서 interpolation으로 접근 가능
  * Directive(v-on, v-bind)에서도 사용 가능
* `methods`
  * Vue instance에 추가할 method
  * 역시 interpolation으로 접근 가능
  * directive에서도 사용 가능
  * 객체 내 다른 함수에서 this 키워드를 통해 접근 가능
* 주의: data, methods 메서드 정의에서 Arrow Function 사용 불가
  * 부모 컨텍스트 바인딩 문제



## `this` Keyword in Vue.js

* Vue 함수 내에서 인스턴스를 가리킴



## Template Syntax

Rendered DOM을 Vue와 Bind

* Interpolation
* Directive



### Interpolation

1. Text
2. Raw HTML (**쓰지 마세요**)
3. Attributes
4. JS Expressions

```html
<!-- 1. Text -->
<span>메시지: {{ msg }}</span>
```





### Directive

* `v-` 접두사가 있는 속성
* 속성값은 단일 JS 표현식이 됨 (v-for 제외)
* 표현식의 값이 변경될 때 반응적으로 DOM에 적용



* Arguments 전달인자
  * `:`을 통해 전달인자를 받을 수도
* Modifier 수식어
  * `.` 특수 접미사
  * directive를 특별한 방법으로 bind함을 나타냄



#### v-text

* 엘리먼트의 textContent를 업데이트
* 내부적으로 interpolation 문법이 v-text로 compile



#### v-html

* 엘리먼트 innerHTML을 업데이트
* **XSS 공격에 취약**
  * **사용자로부터 입력받은 내용을 v-html에는 절대 사용해서는 안 됨 (악성 사용자 공격)**

#### v-show

* 조건부 렌더링
* 일단 렌더링되나, 표현식 False인 경우 css display: none



#### v-if, v-else-if, v-else

* 조건부 렌더링
* 조건에 따라 블록 렌더링
* directive 표현식이 true일 때에만 렌더링



#### v-show vs. v-if

* v-show
  * expensive init load
  * cheap toggle
* v-if
  * cheap init load
  * expensive toggle



#### v-for

* 원본 data 기반으로 el 또는 template 블록을 여러 번 render
* `item in items` 구문 사용
* item 위치의 변수를 각 요소에서 사용할 수 있음
  * 객체의 경우 key
* v-if와 v-for가 같이 사용되는 경우 v-for가 우선순위가 더 높음
* **가능하면 v-if와 v-for를 함께 사용하지 말 것**

[공식문서 참고](https://vuejs.org/v2/style-guide/#Priority-A-Rules-Essential-Error-Prevention)



#### v-bind

* HTML 요소 속성에 Vue의 상태 데이터를 값으로 할당
* Object 형태로 사용하면 value가 true인 key가 class 바인딩 값으로 할당
* 단, 단방향으로
* Shorthand: `v-bind:`를 `:`로 생략할 수 있음
  * `:key`
  * `v-bind:href` = `:href`

#### v-model

* HTML 요소의 값과 data를 양방향 바인딩
* 수식어
  * `.lazy`
  * `.number`
  * `.trim`
* 



### `computed`

* Data based computed attribute
* 함수의 형태로 정의하나, 함수가 아니라
  함수의 반환값이 바인딩됨
* 종속된 데이터에 따라 저장(caching)됨
* **종속된 데이터가 변경될 때에만 함수를 실행**
  * 즉 어떤 데이터에도 의존하지 않는
* 반드시 return 값이 있어야 함



* vs. methods
* computed는 종속 대상을 따라 저장됨
* 즉, computed는 종속된 대상이 변경되지 않는 한 함수를 여러번 호출해도 계산을 다시 하지 않고 기계산된 결과만 반환
* 반면 methods는 다시 계산



### `watch`

* 데이터를 감시
* 데이터에 변화가 일어났을 때 실행되는 함수



#### watch vs. computed

* computed
  * 특정 데이터를 직접 사용/가공하여 다른 값으로 만들 때 사용
  * SW Engineering: 선언형 프로그래밍 방식
* watch
  * 변화 상황에 맞춰 다른 data 등이 바뀌어야 할 때 주로 사용
  * 그 데이터가 바뀌면 특정 함수를 실행하는 방식
  * SW Engineering: 명령형 프로그래밍 방식





# Lifecycle Hooks

각 Vue 인스턴스는 생성 시 일련의 초기화 단계 거침

그 과정에서 사용자 정의 로직을 실행할 수 있는 Lifecycle Hook



예시

* beforeCreate
* created
* beforeMount
* mounted
* beforeUpdate
* updated
* destroyed



# lodash Library

* 모듈성, 성능 및 추가 기능을 제공하는 JavaScript Utility Library
* 