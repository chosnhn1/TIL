* SFC
* Vue CLI
* Pass Props & Emit Event
* Vue Router



# Single File Component: SFC

## Component

cf.

* "monolithic development"
* VueX



* Basic HTML Elements를 extend: capsulate reusable codes
* Vue Component === Vue Instance
* Easier maintenance, reusable codes



## SFC

Vue의 Component-based Dev의 핵심 특징

One component is a result of `.vue` file

화면 특정 영역에 대한 HTML, CSS, JavaScript 코드를 하나의 파일 .vue에서 관리

"Vue Component === Vue Instance === file.vue"

cf. "SRP" in SOLID



### Single File Dev vs. Multiple Components Vue

단일 파일 개발

* 쉬운 개발
* 커질수록 어려워지는 변수 관리 / 유지보수

기능별 컴포넌트

* 초기 비용(시간) 증가
* 이후 변수 관리 용이 / 기능별 유지보수 비용 감소
* 한 화면 내에서도 기능별로 각기 다른 component 존재
  * 꼭 파일별 구분이 필요하지는 않음
  * 단일 `.html`파일 안에서도 여러 개의 component를 만들어 개발 가능



* Vue Component is also Vue Instance
* `.vue` file management
* HTML CSS JavaScript >> `.vue`



# Vue CLI

* Standard Tools for Vue.js Development
* Provide extension plug-ins, GUI, ES2015 components, ...

```bash
$ vue create projectname
```





## NPM: Node Package Manage

Package manager for Node.js

```bash
$ npm install -g @vue/cli
$ vue --version
```



## Babel

JavaScript Compiler

ECMAScript 2015+ Code를 이전 버전으로 번역/변환





## Webpack

Static module bundler

Solve dependency between modules

map modules and build dependency graph internally



Module means a file

브라우저만 조작할 수 있었던 시기의 JavaScript: 모듈 관런 문법이 없었음

JavaScript w/ modular

Legacies: AMD, CommonJS, UMD



Too many modules, deeper dependencies => Webpack

Webpack as bundler

cf. 

Vue CLI already inits, sets Babel, Webpack







----

* Node.js
  * JavaScript Runtime Environment
* Babel
  * Compiler
* Webpack
  * Bundler



## Structure of Vue Project

* node_modules
* public/index.html
* src/
  * assets
    * Static files built by Webpack
  * components
    * Lower Components
  * App.vue
    * Highest Component
  * main.js
    * Webpack entry point
  * package.json
  * package-lock.json
    * Handle all dependencies on `node_modules`
  * 

### Pass Props & Emit Events

Parents > Pass Props

Emit Event < Child



### Template & Script & Style

* `template` (HTML)
* `script` (JavaScript)
* `style` (CSS)



1. 불러오기
2. 등록하기
3. 보여주기

```html
<template>
    <!-- 3. 보여주기 -->
</template>

<script>
    // 1. 불러오기 
    
    
    // 2. 등록하기
</script>

<style>
</style>
```



* Static Props
* Dynamic Props











**주의**

* declaration: camelCase
* in template: kebab-case
* data는 반드시 함수 형태로 객체를 반환하도록 해야 함
  * why? 각 컴포넌트가 데이터를 공유하지 않도록
* props시 자주 하는 실수
* JavaScript 숫자를 전달하려면 표현식으로 평가되도록 v-bind 형태로 전달해야 함



### 단방향 데이터 흐름

* 모든 props는 하위 속성과 상위 속성 사이의 단방향 bind를 형성
* parent에서 변경되면 child로 전달, but 반대로는 안 됨
  * 



### event Name Convention

event는 자동 대소문자 변환 미제공

이벤트 이름에서는 항상 kebab-case를 사용하는 것을 권장



# Vue Router

* Map components to route, and inform where it should be rendered
* SPA 상에서 routing을 쉽게 개발할 수 있는 기능 제공
* Official Vue.js Router

```bash
$ vue add router
```



1. Create and Move Project 

   * ```bash
     & npm i
     ```

     package-locked.js로부터 node_modules 작성

   * 

2. Install Vue Router Plugin

   * ```bash
     ```

   

Vue Router >>

1. App.vue
2. router/index.js
3. views/ 생성



* `router/index.js`





## "router-link"

```html
<router-link to=""> Home </router-link>
```

사용자 내비게이션을 가능하게 하는 컴포넌트

목표 경로는 'to' prop으로 지정

HTML5 History mode에서 router-link는 click prevented

get 요청을 보내지 않음



## "router-view"

주어진 라우트에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트

router-link를 클릭하면 



## History mode

HTML History API를 사용하여 router 구현

브라우저에 히스토리는 남김

URL은 변경하지만 여전히 SPA로 동작



## Routing Methods

### 1. Named Routes

Pass obj to vue-router: prop

```js
const routes = [
    ...
    {
        name: 'About',
    }
]
```

```vue

<router-link :to="{name: 'Home'}">Home</router-link>
```

### 2. Navigation by Programming

```javascript
methods: {
    moveToHome: function () {
        this.$router.push({ name: 'Home' })
    }
}
```



###  3. Dynamic Route Matching

동적 인자 전달 (~ variable routing in Django)

(cf. Redirecting)

```javascript
const routes = [
    {
        path: '/user/:userId',
        name: 'User',
    }
]
```

```html
<h2>
    {{ $route.params.userId }}
</h2>
<router-link :to="{ name: 'profile', params: { userId: ASDF }}">Profile</router-link>
```

동적 인자는 `:`으로 시작

Component에서 `this.$route.params`로 사용 가능

(router가 아닌 route임에 주의)





## `components` and `views`

정해진 것은 없으나 대개 router에 mapping되는 것들이 views,

router에 mapping된 component의 내부에 작성하는 components이 components



1. Before SPA
   * 서버가 모든 라우팅을 통제
   * 요청 경로에 맞는 HTML 제공
2. After SPA
3. 라우팅 처리 차이
   * SSR: 라우팅 결정권을 서버가 가짐
   * CSR: 라우팅 결정권을 클라이언트가 가짐





# Case Study: Youtube Project

TheSearchBar.vue

App.vue <> Youtube Data V3 API

* VideoList.vue <> VideoListItem.vue
* VideoDetail.vue

참고: Vue.js Name Conventions

* 단어 이어붙여서 하위 컴포넌트
* 하위 컴포넌트가 없는 단독 컴포넌트: `The~`

