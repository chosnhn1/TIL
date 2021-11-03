* 



# Intro

## Front-End Development

HTML, CSS and JavaScript >> User

* Front-end Frameworks
  * Vue.js
  * React
  * Angular



# What is Vue.js?

"Progressive JavaScript Framework for User Interface"

SPA(Single Page Application)

by Evan You (2014)



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

* ```javascript
  const app = new Vue({
      
  })
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
2. Raw HTML
3. Attributes
4. JS Expressions



### Directive

* `v-` 접두사가 있는 속성
* 속성값은 단일 JS 표현식이 됨
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
* XSS 공격에 취약
  * 사용자로부터 입력받은 내용을 v-html에는 절대 사용해서는 안 됨 (악성 사용자 공격)

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