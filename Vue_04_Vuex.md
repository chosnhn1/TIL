* Vuex
* Vuex Core Concepts
* Case Study: Todo app w/ Vuex



# Vuex

**"Statement management pattern"** & Library

[Vuex](https://vuex.vuejs.org)

cf. React - Redux

상태(state ~ 데이터)를 전역 저장소로 관리할 수 있도록 지원하는 라이브러리

상태가 예측가능한 방식으로만 변경될 수 있도록 보장하는 규칙 설정

애플리케이션의 모든 컴포넌트에 대한 중앙 집중식 저장소 역할

Vue의 공식 devtools와 통합되어 기타 고급기능을 제공



## State

State == Data, Core of the App

### State Management Pattern

* 컴포넌트의 공유된 상태 추출, 전역에서 관리
* 컴포넌트 as big view, all components 트리에 상관없이 상태에 access, 동작을 trigger할 수 있음
* 상태 관리 및 특정 규칙 적용과 관련된 개념을 정의하고 분리 >> 코드 구조, 유지관리기능 향상

cf. trigger >> 특정 동작에 반응해 자동으로 필요한 동작을 실행





* Centered store manages state
* Efficient in large projects

#### vs. 기존 Pass Props & Emit Event

* each component manage data independently
* data has one-way flow (subcomponent triggers events)
* Pros: Intuitive (부모에서 자식으로만 흐르므로)
* Cons: Deep components - inconvenience



# Vuex Core Concepts

![Vuex Core Concepts](https://vuex.vuejs.org/vuex.png)

* State
  * 중앙에서 관리하는 모든 상태 정보
  * Vuex uses single state tree
  * Single source of truth
  * "1 App = 1 Store"
  * Change in state => all DOM renders
* Mutations (~ORM)
  * The only way to change state
  * Handler functions must be sync
  * 1st args are always state
  * Actions call mutations via `commit()`
* Actions
  * data fetch and process
  * can have async works
  * receive contexts as args
  * Actions can manipulate all others, but state can only be accessed by mutations
* Getters (state >> getters >> Vue components)
  * does not change state, but uses state to compute
  * ~ computed
  * results of getters are cached
  * **getters does not change state**





# Todo App by Vuex

1. Set projects
2. create todo
3. delete todo
4. update todo
5. getters
6. vuex component binding helper
7. local storage







----



1. Component > (dispatch) > actions
2. Actions > (commit) > mutations
3. Mutations >> state



----

Spread Syntax





# Getters





# Component Binding Helper

* mapState
  * computed와 state mapping
* mapGetters
* mapActions
* mapMutations
* (createNamespaceHelpers)



## LocalStorage

`vuex-persistedstate`

Vuex state를 자동으로 LocalStorage에 저장해주는 라이브러리

